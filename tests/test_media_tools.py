"""Smoke tests for media_registry.py and contact_sheet.py (need ffmpeg + Pillow)."""
import shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / 'skills/creator-pipeline-supervisor/scripts/media_registry.py'
CS = ROOT / 'skills/creator-final-cut-editor/scripts/contact_sheet.py'


def run(*args, check=True):
    return subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, check=check)


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'ffmpeg not installed')
class MediaToolTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.proj = Path(self.tmp.name) / 'project'
        (self.proj / 'media/raw').mkdir(parents=True)
        for i in (1, 2):
            subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'lavfi',
                            '-i', f'testsrc2=size=320x180:rate=24:duration=2', '-f', 'lavfi',
                            '-i', f'sine=frequency={300*i}:duration=2', '-c:v', 'libx264',
                            '-pix_fmt', 'yuv420p', '-c:a', 'aac', str(self.proj / f'media/raw/S07-t{i}.mp4')],
                           check=True)

    def test_registry_lifecycle(self):
        for i in (1, 2):
            run(REG, 'add', '--project', self.proj, '--file', self.proj / f'media/raw/S07-t{i}.mp4',
                '--shot', 'S07', '--take', i, '--model', 'test', '--cost', 1.5)
        dup = run(REG, 'add', '--project', self.proj, '--file', self.proj / 'media/raw/S07-t1.mp4',
                  '--shot', 'S07', '--take', 1, '--model', 'test', check=False)
        self.assertEqual(dup.returncode, 2)
        run(REG, 'select', '--project', self.proj, '--shot', 'S07', '--take', 1, '--note', 'first pick')
        no_note = run(REG, 'select', '--project', self.proj, '--shot', 'S07', '--take', 2, check=False)
        self.assertNotEqual(no_note.returncode, 0)  # a selection without a reason is refused
        run(REG, 'select', '--project', self.proj, '--shot', 'S07', '--take', 2, '--note', 'better')  # demotes take 1
        ok = run(REG, 'verify', '--project', self.proj, '--require-selected', '--expect-duration', 2)
        self.assertIn('OK', ok.stdout)
        rep = run(REG, 'report', '--project', self.proj).stdout
        self.assertIn('superseded by take 2', rep); self.assertIn('total recorded cost: 3.0', rep)
        (self.proj / 'media/raw/S07-t2.mp4').write_bytes(b'corrupt')
        bad = run(REG, 'verify', '--project', self.proj, check=False)
        self.assertEqual(bad.returncode, 1); self.assertIn('sha256 changed', bad.stdout)

    def test_registry_rejects_bad_input(self):
        base = [REG, 'add', '--project', self.proj, '--model', 'test']
        self.assertEqual(run(*base, '--file', self.proj / 'media', '--shot', 'S1', '--take', 1, check=False).returncode, 2)      # directory
        self.assertEqual(run(*base, '--file', self.proj / 'media/raw/S07-t1.mp4', '--shot', 'S1', '--take', 0, check=False).returncode, 2)  # take 0
        (self.proj / 'notes.txt').write_text('not media')
        self.assertEqual(run(*base, '--file', self.proj / 'notes.txt', '--shot', 'S1', '--take', 1, check=False).returncode, 2)  # undecodable
        self.assertEqual(run(*base, '--file', self.proj / 'media/raw/S07-t1.mp4', '--shot', 'S1', '--take', 1,
                             '--prompt', self.proj / 'missing.txt', check=False).returncode, 2)  # missing prompt
        png = self.proj / 'media/raw/ref 1.png'   # space in the name on purpose
        subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i', 'color=c=red:s=64x64',
                        '-frames:v', '1', str(png)], check=True)
        run(*base, '--file', png, '--shot', 'S1', '--take', 1)
        rep = run(REG, 'report', '--project', self.proj, '--json').stdout
        self.assertIn('"kind": "image"', rep); self.assertIn('"fps": null', rep)
        # hand-edited log: duplicate add and a select without add must fail verify
        with (self.proj / 'media/registry.jsonl').open('a') as f:
            f.write('{"event": "select", "at": "x", "shot_id": "S9", "take": 1, "note": "n"}\n')
        bad = run(REG, 'verify', '--project', self.proj, check=False)
        self.assertEqual(bad.returncode, 1); self.assertIn('without a prior add', bad.stdout)

    def test_contact_sheet_low_fps_and_bad_cut(self):
        slow = self.proj / 'media/raw/slow.mp4'
        subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i',
                        'testsrc2=size=320x180:rate=10:duration=2', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', str(slow)], check=True)
        run(CS, 'sheet', '--out', self.proj / 'qc/slow.jpg', slow)   # last frame of a 10 fps clip must decode
        self.assertTrue((self.proj / 'qc/slow.jpg').exists())
        out = run(CS, 'sheet', '--out', self.proj / 'qc/x.jpg', slow, '--cuts', '5', check=False)
        self.assertNotEqual(out.returncode, 0); self.assertIn('outside the clip', out.stderr)

    def test_contact_sheet_and_ab(self):
        a, b = self.proj / 'media/raw/S07-t1.mp4', self.proj / 'media/raw/S07-t2.mp4'
        run(CS, 'sheet', '--out', self.proj / 'qc/sheet.jpg', '--label-from-name', a, b, '--cuts', '1.0')
        self.assertTrue((self.proj / 'qc/sheet.jpg').stat().st_size > 1000)
        run(CS, 'ab', '--out', self.proj / 'qc/ab.mp4', a, b, '--labels', 't1', 't2')
        probe = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width', '-of', 'csv=p=0',
                                str(self.proj / 'qc/ab.mp4')], capture_output=True, text=True).stdout.strip()
        self.assertEqual(probe, '2560')


if __name__ == '__main__':
    unittest.main()
