#!/usr/bin/env python3
"""Read-only contract validator. Does not launch agents or grant filesystem access."""
import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path, PurePosixPath

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(Path(path).read_text())


def parse_time(value):
    require(isinstance(value, str) and re.fullmatch(
        r'\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[Zz]|[+-](?:[01]\d|2[0-3]):[0-5]\d)', value),
        'timestamp must be RFC3339 with timezone')
    parsed = datetime.fromisoformat(value.upper().replace('Z', '+00:00'))
    require(parsed.utcoffset() is not None, 'timestamp requires timezone')
    return parsed


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def schema_check(name, data):
    schemas = [read(p) for p in (ROOT / 'schemas').glob('*.schema.json')]
    registry = Registry().with_resources((s['$id'], Resource.from_contents(s)) for s in schemas)
    schema = read(ROOT / 'schemas' / f'{name}.schema.json')
    Draft202012Validator.check_schema(schema)
    checker = FormatChecker()

    @checker.checks('date-time', raises=ValueError)
    def check_time(value):
        if isinstance(value, str):
            parse_time(value)
        return True

    Draft202012Validator(schema, registry=registry, format_checker=checker).validate(data)


def safe_path(value):
    p = PurePosixPath(value)
    require(not p.is_absolute() and '..' not in p.parts and str(p) == value
            and '\\' not in value and value != '.', f'unsafe path: {value}')
    return p


def owner_for(graph, path):
    safe_path(path)
    matches = [r for r in graph['ownership']
               if path == r['prefix'] or path.startswith(r['prefix'] + '/')]
    require(matches, f'no owner: {path}')
    return max(matches, key=lambda r: len(r['prefix']))['owner']


def unique(items, key, label):
    result = {x[key]: x for x in items}
    require(len(result) == len(items), f'duplicate {label}')
    return result


def validate_workflow(graph):
    schema_check('workflow', graph)
    nodes = unique(graph['nodes'], 'id', 'node')
    unique(graph['ownership'], 'prefix', 'ownership prefix')
    unique([n['output'] for n in nodes.values()], 'artifact_id', 'artifact output')
    unique([n['output'] for n in nodes.values()], 'path', 'output path')
    for rule in graph['ownership']:
        safe_path(rule['prefix'])
    visiting, visited = set(), set()

    def visit(node_id):
        require(node_id in nodes, f'unknown dependency: {node_id}')
        require(node_id not in visiting, f'cycle: {node_id}')
        if node_id in visited:
            return
        visiting.add(node_id)
        n = nodes[node_id]
        require((ROOT / 'skills' / n['owner'] / 'SKILL.md').is_file(), f'unknown skill: {n["owner"]}')
        require(owner_for(graph, n['output']['path']) == n['owner'], f'ownership violation: {node_id}')
        require(len(set(n['needs'])) == len(n['needs']), f'duplicate dependency: {node_id}')
        for dep in n['needs']:
            visit(dep)
        visiting.remove(node_id)
        visited.add(node_id)

    for node_id in nodes:
        visit(node_id)
    return nodes


def ref_map(refs):
    return {k: v['sha256'] for k, v in unique(refs, 'artifact_id', 'input/output reference').items()}


def impact(manifest, changed):
    artifacts = unique(manifest['artifacts'], 'artifact_id', 'artifact')
    require(set(changed) <= artifacts.keys(), 'unknown changed artifact')
    affected = set(changed)
    while True:
        next_set = affected | {a['artifact_id'] for a in artifacts.values()
                               if any(r['artifact_id'] in affected for r in a['inputs'])}
        if next_set == affected:
            break
        affected = next_set
    return sorted(affected)


def validate_package(graph, manifest, project, partial=False, require_review=True, legacy_approvals=False):
    nodes = validate_workflow(graph)
    schema_check('manifest', manifest)
    require(manifest['workflow_id'] == graph['workflow_id'], 'workflow mismatch')
    arts = unique(manifest['artifacts'], 'artifact_id', 'artifact')
    runs = unique(manifest['runs'], 'node_id', 'run node')
    unique(manifest['runs'], 'run_id', 'run id')
    unique(manifest['reviews'], 'review_id', 'review id')
    unique(manifest['reviews'], 'gate', 'review gate')
    unique(manifest['artifacts'], 'path', 'artifact path')
    require(set(runs) <= set(nodes), 'unknown run node')
    require(set(arts) <= {n['output']['artifact_id'] for n in nodes.values()}, 'unknown artifact')
    if not partial:
        require(set(runs) == set(nodes), 'missing node runs')
    project = Path(project).resolve()
    for a in arts.values():
        safe_path(a['path'])
        p = (project / a['path']).resolve()
        require(p.is_relative_to(project), 'artifact escapes project')
        require(p.is_file(), f'missing file: {a["path"]}')
        require(digest(p) == a['sha256'], f'changed file: {a["artifact_id"]}')
        require(a['scene_id'] == manifest['scene_id'], 'scene mismatch')
        require(owner_for(graph, a['path']) == a['owner'], f'ownership violation: {a["path"]}')
    gate_reviews = {r['gate']: r for r in manifest['reviews']}
    require(set(gate_reviews) <= {n['id'] for n in nodes.values() if n['gate']} | {'package'}, 'unknown review gate')

    def check_review(gate, expected, independent=False, must_pass=True):
        require(gate in gate_reviews, f'missing approval: {gate}')
        r = gate_reviews[gate]
        require(ref_map(r['subjects']) == expected, f'stale/incomplete approval: {gate}')
        if must_pass:
            require(r['verdict'] == 'pass' and all(c['passed'] for c in r['checks']), f'failed approval: {gate}')
        if gate == 'design' and r['verdict'] == 'pass':
            role = r.get('approver_role')
            require(role in {'director', 'user'} or (legacy_approvals and role is None),
                    'design approval requires director/user role')
        reviewed = parse_time(r['reviewed_at'])
        relevant = [run for run in runs.values() if set(ref_map(run['outputs'])) & set(expected)]
        require(all(reviewed >= parse_time(run['finished_at']) for run in relevant), f'approval predates output: {gate}')
        if independent:
            require(all(r['reviewer_id'] != run['actor_id'] for run in relevant), 'reviewer is an author')
        return r

    consumed_outputs = set()
    for node_id, run in runs.items():
        n = nodes[node_id]
        require(run['status'] == 'succeeded' and not run['error'], f'failed run: {node_id}')
        started, finished = parse_time(run['started_at']), parse_time(run['finished_at'])
        require(started <= finished, f'invalid run time: {node_id}')
        expected_inputs = {}
        for dep in n['needs']:
            require(dep in runs and runs[dep]['status'] == 'succeeded', f'missing/failed dependency: {dep}')
            require(parse_time(runs[dep]['finished_at']) <= started, f'dependency not finished: {dep}')
            aid = nodes[dep]['output']['artifact_id']
            require(aid in arts, f'missing input artifact: {aid}')
            expected_inputs[aid] = arts[aid]['sha256']
            if nodes[dep]['gate']:
                approval = check_review(dep, {**ref_map(arts[aid]['inputs']), aid: arts[aid]['sha256']})
                require(parse_time(approval['reviewed_at']) <= started, f'gate not approved before run: {dep}')
        require(ref_map(run['inputs']) == expected_inputs, f'stale/missing run inputs: {node_id}')
        aid = n['output']['artifact_id']
        require(aid in arts, f'missing output: {aid}')
        a = arts[aid]
        require(a['path'] == n['output']['path'] and a['owner'] == n['owner'], f'output contract: {node_id}')
        require(ref_map(a['inputs']) == expected_inputs, f'stale/missing artifact inputs: {node_id}')
        require(ref_map(run['outputs']) == {aid: a['sha256']}, f'output hash mismatch: {node_id}')
        consumed_outputs.add(aid)
    require(consumed_outputs == set(arts), 'artifact without producer run')
    for gate, review in gate_reviews.items():
        if gate == 'package':
            check_review(gate, {k: a['sha256'] for k, a in arts.items()}, True)
        else:
            aid = nodes[gate]['output']['artifact_id']
            require(aid in arts, 'approval without artifact')
            # Failed gate may be stored in a partial checkpoint, never consumed.
            check_review(gate, {**ref_map(arts[aid]['inputs']), aid: arts[aid]['sha256']},
                         must_pass=review['verdict'] == 'pass' or not partial)
    if require_review and not partial:
        check_review('package', {k: a['sha256'] for k, a in arts.items()}, True)
    actual = {p.relative_to(project).as_posix() for p in project.rglob('*') if p.is_file() and (p.name != '.DS_Store' or p.is_symlink())}
    require(actual == {a['path'] for a in arts.values()}, 'unregistered project files')
    return {'result': 'pass', 'nodes': len(runs), 'artifacts': len(arts),
            'independent_review': 'package' in gate_reviews, 'partial': partial,
            'scope': 'historical compatibility only; not production approval' if legacy_approvals
                     else 'partial checkpoint' if partial else 'validated package' if require_review
                     else 'structural only; not production approval'}


def validate_revision(graph, previous_path, current, record, allow_growth=False):
    """Read and authenticate the previous snapshot in this API, not only in the CLI."""
    previous_bytes = Path(previous_path).read_bytes()
    previous = json.loads(previous_bytes)
    schema_check('revision', record)
    require(record['previous_manifest_sha256'] == hashlib.sha256(previous_bytes).hexdigest(),
            'previous manifest changed')
    validate_workflow(graph)
    schema_check('manifest', previous)
    schema_check('manifest', current)
    require(previous['workflow_id'] == current['workflow_id'] == graph['workflow_id'], 'workflow mismatch')
    require(previous['scene_id'] == current['scene_id'], 'scene mismatch')
    old = unique(previous['artifacts'], 'artifact_id', 'previous artifact')
    new = unique(current['artifacts'], 'artifact_id', 'current artifact')
    require(set(old) <= set(new) if allow_growth else set(old) == set(new),
            'revision must preserve pilot artifact IDs')
    added = set(new) - set(old)
    affected = sorted(set(impact(previous, record['changed'])) | added)
    require(record['affected'] == affected, 'incorrect revision impact')
    node_for = {n['output']['artifact_id']: n['id'] for n in graph['nodes']}
    require(record['rerun_nodes'] == sorted(node_for[a] for a in affected), 'incorrect rerun list')
    old_runs = unique(previous['runs'], 'node_id', 'previous run node')
    new_runs = unique(current['runs'], 'node_id', 'current run node')
    require(set(new) <= set(node_for), 'unknown revision artifact')
    require(set(new_runs) == {node_for[a] for a in new}, 'current run coverage mismatch')
    require(set(old_runs) == {node_for[a] for a in old}, 'previous run coverage mismatch')
    for aid in added:
        require(new[aid]['revision'] == 1, f'new artifact must start at revision 1: {aid}')
        require(new_runs[node_for[aid]]['run_id'] not in {r['run_id'] for r in old_runs.values()},
                f'new artifact reuses previous run: {aid}')
    for aid in old:
        nid = node_for[aid]
        if aid in affected:
            require(new[aid]['revision'] > old[aid]['revision'], f'revision not incremented: {aid}')
            require(new_runs[nid]['run_id'] != old_runs[nid]['run_id'], f'run not replaced: {nid}')
        else:
            require(new[aid] == old[aid] and new_runs[nid] == old_runs[nid], f'unaffected output rerun: {aid}')
    require(all(old[a]['sha256'] != new[a]['sha256'] for a in record['changed']), 'declared source did not change')
    return {'result': 'pass', 'affected': affected}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['workflow', 'validate', 'impact', 'revision'])
    parser.add_argument('--workflow', type=Path, default=ROOT / 'workflows/single-scene.v1.json')
    parser.add_argument('--manifest', type=Path)
    parser.add_argument('--project', type=Path)
    parser.add_argument('--partial', action='store_true')
    parser.add_argument('--legacy-approvals', action='store_true', help='historical audit only; allows missing design approver role')
    parser.add_argument('--allow-growth', action='store_true', help='revision may add first-run artifacts after a partial checkpoint')
    parser.add_argument('--pre-review', action='store_true', help='validate structure only, not production readiness')
    parser.add_argument('--changed', nargs='+')
    parser.add_argument('--previous', type=Path)
    parser.add_argument('--record', type=Path)
    args = parser.parse_args()
    try:
        graph = read(args.workflow)
        validate_workflow(graph)
        if args.command == 'workflow':
            result = {'result': 'pass', 'nodes': len(graph['nodes'])}
        else:
            require(args.manifest is not None, '--manifest required')
            manifest = read(args.manifest)
            if args.command == 'impact':
                require(args.changed, '--changed required')
                schema_check('manifest', manifest)
                result = {'affected': impact(manifest, args.changed)}
            elif args.command == 'revision':
                require(args.previous and args.record, '--previous and --record required')
                record = read(args.record)
                result = validate_revision(graph, args.previous, manifest, record, args.allow_growth)
            else:
                result = validate_package(graph, manifest, args.project or args.manifest.parent / 'project',
                                          args.partial, not args.pre_review, args.legacy_approvals)
                if args.pre_review:
                    result['scope'] = 'structural only; not production approval'
        print(json.dumps(result, indent=2))
    except Exception as exc:
        # CLI reports schema and filesystem errors uniformly with a failing exit code.
        print(json.dumps({'result': 'fail', 'error': str(exc)}, indent=2))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
