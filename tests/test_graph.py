import copy
import json
from datetime import datetime, timezone
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_graph import (ROOT, read, digest, schema_check, validate_workflow,
                            validate_package, impact, validate_revision)


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / 'project'
        shutil.copytree(ROOT / 'examples/single-scene/v01/project', self.project)
        self.graph = read(ROOT / 'workflows/single-scene.v1.json')
        self.manifest = read(ROOT / 'examples/single-scene/v01/manifest.json')
        for review in self.manifest['reviews']:
            if review['gate'] == 'design':
                review['approver_role'] = 'director'  # Synthetic test role, not a historical approval.
        self.manifest['reviews'] = [r for r in self.manifest['reviews'] if r['gate'] != 'package']
        self.manifest['reviews'].append({
            'review_id': 'synthetic-test-review', 'gate': 'package',
            'reviewer_id': 'unit-test-reviewer', 'reviewed_at': datetime.now(timezone.utc).isoformat(),
            'subjects': [{'artifact_id': a['artifact_id'], 'sha256': a['sha256']}
                         for a in self.manifest['artifacts']],
            'checks': [{'name': 'fixture only', 'passed': True, 'evidence': 'synthetic unit-test data'}],
            'verdict': 'pass', 'notes': 'Synthetic test approval; never used as pilot evidence.'})

    def validate(self):
        return validate_package(self.graph, self.manifest, self.project)

    def fails(self, text):
        with self.assertRaisesRegex(ValueError, text):
            self.validate()

    def test_valid(self):
        self.assertEqual(self.validate()['nodes'], 12)

    def test_cycle(self):
        self.graph['nodes'][0]['needs'] = ['prompts']
        with self.assertRaisesRegex(ValueError, 'cycle'):
            validate_workflow(self.graph)

    def test_missing_dependency_node(self):
        self.graph['nodes'][-1]['needs'] = ['unknown']
        with self.assertRaisesRegex(ValueError, 'unknown dependency'):
            validate_workflow(self.graph)

    def test_two_writers_same_path(self):
        self.graph['nodes'][8]['output']['path'] = self.graph['nodes'][10]['output']['path']
        with self.assertRaisesRegex(ValueError, 'duplicate output path'):
            validate_workflow(self.graph)

    def test_storyboard_cannot_write_prompts(self):
        self.graph['nodes'][8]['output']['path'] = 'prompts/scene-01/panel-01.md'
        with self.assertRaisesRegex(ValueError, 'ownership violation'):
            validate_workflow(self.graph)

    def test_production_cannot_write_camera(self):
        self.graph['nodes'][4]['output']['path'] = 'production-design/cinematography/other.md'
        with self.assertRaisesRegex(ValueError, 'ownership violation'):
            validate_workflow(self.graph)

    def test_supervisor_cannot_write_review(self):
        self.graph['nodes'][6]['output']['path'] = 'qc/reviews/decision.md'
        with self.assertRaisesRegex(ValueError, 'ownership violation'):
            validate_workflow(self.graph)

    def test_unknown_skill(self):
        self.graph['nodes'][1]['owner'] = 'creator-absent'
        with self.assertRaisesRegex(ValueError, 'unknown skill'):
            validate_workflow(self.graph)

    def test_path_escape(self):
        self.manifest['artifacts'][0]['path'] = '../outside.md'
        self.fails('unsafe path')

    def test_symlink_escape(self):
        path = self.project / self.manifest['artifacts'][0]['path']
        outside = Path(self.temp.name) / 'outside.md'
        outside.write_bytes(path.read_bytes())
        path.unlink()
        path.symlink_to(outside)
        self.fails('escapes project')

    def test_unregistered_file(self):
        (self.project / 'unregistered.md').write_text('extra')
        self.fails('unregistered')

    def test_changed_file(self):
        (self.project / self.manifest['artifacts'][4]['path']).write_text('cream envelope')
        self.fails('changed file')

    def test_missing_file(self):
        (self.project / self.manifest['artifacts'][4]['path']).unlink()
        self.fails('missing file')

    def test_stale_dependency(self):
        self.manifest['artifacts'][8]['inputs'][0]['sha256'] = '0' * 64
        self.fails('stale/missing artifact inputs')

    def test_missing_input(self):
        self.manifest['runs'][8]['inputs'] = []
        self.fails('stale/missing run inputs')

    def test_failed_run_and_retry(self):
        failed = self.manifest['runs'][10]
        failed['status'], failed['error'] = 'failed', 'interrupted'
        self.fails('failed run')
        # Resume only this node; all other records stay unchanged.
        unchanged = copy.deepcopy(self.manifest['runs'][:10] + self.manifest['runs'][11:])
        failed.update(status='succeeded', error='', attempt=2, run_id='test-prompts-retry')
        self.assertEqual(self.validate()['result'], 'pass')
        self.assertEqual(unchanged, self.manifest['runs'][:10] + self.manifest['runs'][11:])

    def test_missing_gate(self):
        self.manifest['reviews'] = [r for r in self.manifest['reviews'] if r['gate'] != 'design']
        self.fails('missing approval')

    def test_failed_gate(self):
        self.manifest['reviews'][1]['verdict'] = 'fail'
        self.fails('failed approval')

    def test_false_check_in_pass_review(self):
        self.manifest['reviews'][-1]['checks'][0]['passed'] = False
        self.fails('failed approval')

    def test_stale_review_hash(self):
        self.manifest['reviews'][-1]['subjects'][0]['sha256'] = '0' * 64
        self.fails('stale/incomplete approval')

    def test_missing_final_review(self):
        self.manifest['reviews'].pop()
        self.fails('missing approval: package')

    def test_author_cannot_review_self(self):
        self.manifest['reviews'][-1]['reviewer_id'] = self.manifest['runs'][0]['actor_id']
        self.fails('reviewer is an author')

    def test_gate_approved_too_late(self):
        self.manifest['reviews'][1]['reviewed_at'] = '2099-01-01T00:00:00+00:00'
        self.fails('gate not approved before run')

    def test_incomplete_review_coverage(self):
        self.manifest['reviews'][-1]['subjects'].pop()
        self.fails('stale/incomplete approval')

    def test_impact_closure(self):
        self.assertEqual(impact(self.manifest, ['production']),
                         ['canon', 'design', 'production', 'prompts', 'shots', 'sound', 'storyboard'])

    def test_partial_failed_gate_is_a_checkpoint_not_release(self):
        m = read(ROOT / 'examples/single-scene/v00-conflict/manifest.json')
        p = ROOT / 'examples/single-scene/v00-conflict/project'
        self.assertTrue(validate_package(self.graph, m, p, partial=True)['partial'])
        with self.assertRaisesRegex(ValueError, 'missing node runs'):
            validate_package(self.graph, m, p)

    def test_revision_lineage(self):
        revised = read(ROOT / 'examples/single-scene/v02/manifest.json')
        record = read(ROOT / 'examples/single-scene/v02/revision.json')
        previous = ROOT / 'examples/single-scene/v01/manifest.json'
        self.assertEqual(validate_revision(self.graph, previous, revised, record)['result'], 'pass')
        record['affected'].remove('sound')
        with self.assertRaisesRegex(ValueError, 'incorrect revision impact'):
            validate_revision(self.graph, previous, revised, record)

    def test_unaffected_run_is_not_repeated(self):
        revised = read(ROOT / 'examples/single-scene/v02/manifest.json')
        record = read(ROOT / 'examples/single-scene/v02/revision.json')
        previous = ROOT / 'examples/single-scene/v01/manifest.json'
        revised['runs'][0]['run_id'] = 'unnecessary-repeat'
        with self.assertRaisesRegex(ValueError, 'unaffected output rerun'):
            validate_revision(self.graph, previous, revised, record)

    def test_failed_checkpoint_review_binding(self):
        for mutation in ['hash', 'subject', 'time']:
            with self.subTest(mutation=mutation):
                m = read(ROOT / 'examples/single-scene/v00-conflict/manifest.json')
                review = m['reviews'][-1]
                if mutation == 'hash':
                    review['subjects'][0]['sha256'] = '0' * 64
                elif mutation == 'subject':
                    review['subjects'][0]['artifact_id'] = 'nonexistent'
                else:
                    review['reviewed_at'] = '2000-01-01T00:00:00Z'
                with self.assertRaises(ValueError):
                    validate_package(self.graph, m, ROOT / 'examples/single-scene/v00-conflict/project', partial=True)

    def test_duplicate_revision_changed_ids(self):
        from jsonschema.exceptions import ValidationError
        revised = read(ROOT / 'examples/single-scene/v02/manifest.json')
        record = read(ROOT / 'examples/single-scene/v02/revision.json')
        previous = ROOT / 'examples/single-scene/v01/manifest.json'
        record['changed'].append('production')
        with self.assertRaises(ValidationError):
            validate_revision(self.graph, previous, revised, record)

    def test_duplicate_revision_artifact_ids(self):
        revised = read(ROOT / 'examples/single-scene/v02/manifest.json')
        record = read(ROOT / 'examples/single-scene/v02/revision.json')
        previous = ROOT / 'examples/single-scene/v01/manifest.json'
        revised['artifacts'].append(copy.deepcopy(revised['artifacts'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate current artifact'):
            validate_revision(self.graph, previous, revised, record)

    def test_utc_z_timestamps(self):
        for run in self.manifest['runs']:
            for field in ['started_at', 'finished_at']:
                run[field] = run[field].replace('+00:00', 'Z')
        for review in self.manifest['reviews']:
            review['reviewed_at'] = review['reviewed_at'].replace('+00:00', 'Z')
        self.assertEqual(self.validate()['result'], 'pass')

    def test_failed_design_cannot_be_consumed_in_partial_mode(self):
        m = read(ROOT / 'examples/single-scene/v00-conflict/manifest.json')
        p = Path(self.temp.name) / 'checkpoint'
        shutil.copytree(ROOT / 'examples/single-scene/v00-conflict/project', p)
        canon = copy.deepcopy(next(a for a in self.manifest['artifacts'] if a['artifact_id'] == 'canon'))
        run = copy.deepcopy(next(r for r in self.manifest['runs'] if r['node_id'] == 'canon'))
        design = next(a for a in m['artifacts'] if a['artifact_id'] == 'design')
        refs = [{'artifact_id': 'design', 'sha256': design['sha256']}]
        canon['inputs'] = refs
        run['inputs'] = refs
        shutil.copyfile(self.project / canon['path'], p / canon['path'])
        m['artifacts'].append(canon)
        m['runs'].append(run)
        with self.assertRaisesRegex(ValueError, 'failed approval: design'):
            validate_package(self.graph, m, p, partial=True)

    def test_missing_design_role_is_rejected_by_default(self):
        self.manifest['reviews'][1].pop('approver_role')
        self.fails('design approval requires director/user role')

    def test_coordinator_cannot_approve_design(self):
        self.manifest['reviews'][1]['approver_role'] = 'coordinator'
        for legacy in [False, True]:
            with self.assertRaisesRegex(ValueError, 'design approval requires director/user role'):
                validate_package(self.graph, self.manifest, self.project, legacy_approvals=legacy)

    def test_user_can_approve_design(self):
        self.manifest['reviews'][1]['approver_role'] = 'user'
        self.assertEqual(self.validate()['result'], 'pass')

    def test_historical_missing_role_requires_explicit_compatibility_mode(self):
        self.manifest['reviews'][1].pop('approver_role')
        result = validate_package(self.graph, self.manifest, self.project, legacy_approvals=True)
        self.assertEqual(result['result'], 'pass')
        self.assertIn('not production approval', result['scope'])

    def test_naive_timestamps_rejected_without_optional_format_packages(self):
        from jsonschema.exceptions import ValidationError
        for run in self.manifest['runs']:
            for field in ['started_at', 'finished_at']:
                run[field] = run[field].replace('+00:00', '')
        for review in self.manifest['reviews']:
            review['reviewed_at'] = review['reviewed_at'].replace('+00:00', '')
        with self.assertRaises(ValidationError):
            self.validate()

    def test_timestamp_syntax_is_explicit(self):
        from validate_graph import parse_time
        for value in ['2026-10-04', '2026-10-04 12:00:00+00:00', '2026-10-04T12:00:00',
                      '2026-10-04T12:00:00+99:00', '2026-10-04T12:00:00+03:99', '2026-02-30T12:00:00Z']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                parse_time(value)
        self.assertIsNotNone(parse_time('2026-10-04t12:00:00z').utcoffset())
        self.assertIsNotNone(parse_time('2026-10-04T12:00:00+03:00').utcoffset())

    def test_ds_store_is_ignored_but_other_hidden_files_are_not(self):
        (self.project / '.DS_Store').write_bytes(b'Finder metadata')
        (self.project / 'bible/.DS_Store').write_bytes(b'Finder metadata')
        self.assertEqual(self.validate()['result'], 'pass')
        (self.project / '.hidden-prompt.md').write_text('unregistered')
        self.fails('unregistered')

    def test_revision_api_checks_previous_file_hash(self):
        revised = read(ROOT / 'examples/single-scene/v02/manifest.json')
        record = read(ROOT / 'examples/single-scene/v02/revision.json')
        previous = Path(self.temp.name) / 'previous.json'
        previous.write_bytes((ROOT / 'examples/single-scene/v01/manifest.json').read_bytes() + b'\n')
        with self.assertRaisesRegex(ValueError, 'previous manifest changed'):
            validate_revision(self.graph, previous, revised, record)

    def test_partial_to_full_lineage_requires_growth_flag(self):
        previous = ROOT / 'examples/single-scene/v00-conflict/manifest.json'
        current = read(ROOT / 'examples/single-scene/v01/manifest.json')
        record = read(ROOT / 'examples/single-scene/lineage-v00-v01.json')
        with self.assertRaisesRegex(ValueError, 'preserve pilot artifact IDs'):
            validate_revision(self.graph, previous, current, record)
        self.assertEqual(validate_revision(self.graph, previous, current, record, allow_growth=True)['result'], 'pass')
        current['artifacts'][-1]['revision'] = 2
        with self.assertRaisesRegex(ValueError, 'start at revision 1'):
            validate_revision(self.graph, previous, current, record, allow_growth=True)

    def test_growth_cannot_remove_existing_artifacts(self):
        previous = ROOT / 'examples/single-scene/v00-conflict/manifest.json'
        current = read(ROOT / 'examples/single-scene/v01/manifest.json')
        record = read(ROOT / 'examples/single-scene/lineage-v00-v01.json')
        current['artifacts'] = current['artifacts'][1:]
        with self.assertRaisesRegex(ValueError, 'preserve pilot artifact IDs'):
            validate_revision(self.graph, previous, current, record, allow_growth=True)

    def test_all_schemas_are_valid(self):
        from jsonschema import Draft202012Validator
        for p in (ROOT / 'schemas').glob('*.schema.json'):
            Draft202012Validator.check_schema(read(p))


if __name__ == '__main__':
    unittest.main()
