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
        run(REG, 'select', '--project', self.proj, '--shot', 'S07', '--take', 1)
        run(REG, 'select', '--project', self.proj, '--shot', 'S07', '--take', 2)  # demotes take 1
        ok = run(REG, 'verify', '--project', self.proj, '--require-selected', '--expect-duration', 2)
        self.assertIn('OK', ok.stdout)
        rep = run(REG, 'report', '--project', self.proj).stdout
        self.assertIn('superseded by take 2', rep); self.assertIn('total recorded cost: 3.0', rep)
        (self.proj / 'media/raw/S07-t2.mp4').write_bytes(b'corrupt')
        bad = run(REG, 'verify', '--project', self.proj, check=False)
        self.assertEqual(bad.returncode, 1); self.assertIn('sha256 changed', bad.stdout)

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
