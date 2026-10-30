#!/usr/bin/env python3
"""Contact sheet and A/B comparison for generated clips.

A static board does not prove motion quality, so this tool makes both:
  sheet  — one labelled frame grid per clip (start / evenly spaced / end, plus
           frames just before and after each cut time you pass), so a reviewer
           sees face, costume, light and prop drift without scrubbing.
  ab     — a side-by-side video of two takes, time-aligned, with labels, so
           motion, pacing and morphing errors can be compared in playback.

Usage:
  contact_sheet.py sheet  --out qc/S07.jpg  --label "S07 take2"  clip.mp4 [--frames 6] [--cuts 2.0 4.5]
  contact_sheet.py sheet  --out qc/all.jpg  --label-from-name  S07-t1.mp4 S07-t2.mp4 S08-t1.mp4
  contact_sheet.py ab     --out qc/S07-ab.mp4  a.mp4 b.mp4 [--labels "take 1" "take 2"] [--duration 5]

Requires ffmpeg/ffprobe on PATH and Pillow.
"""
from __future__ import annotations
import argparse, json, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

THUMB_W, THUMB_H, PAD, LABEL_H = 320, 180, 8, 22
BG, FG, ACCENT = (25, 22, 27), (238, 231, 221), (118, 81, 105)


def run(args: list[str]) -> str:
    p = subprocess.run(args, capture_output=True, text=True)
    if p.returncode:
        raise SystemExit(p.stderr[-2000:])
    return p.stdout


def duration(path: Path) -> float:
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)])
    return float(json.loads(out)["format"]["duration"])


def frame_at(path: Path, t: float, dest: Path) -> Image.Image:
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{t:.3f}", "-i", str(path),
         "-frames:v", "1", "-vf", f"scale={THUMB_W}:{THUMB_H}:force_original_aspect_ratio=decrease,"
         f"pad={THUMB_W}:{THUMB_H}:(ow-iw)/2:(oh-ih)/2:color=black", str(dest)])
    return Image.open(dest).convert("RGB")


def font(size: int):
    for cand in ("/System/Library/Fonts/Helvetica.ttc", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(cand, size)
        except OSError:
            continue
    return ImageFont.load_default()


def sample_times(dur: float, n: int, cuts: list[float]) -> list[tuple[str, float]]:
    eps = 1 / 24
    times = [("start", 0.0)]
    for i in range(1, n - 1):
        times.append((f"{dur * i / (n - 1):.2f}s", dur * i / (n - 1)))
    times.append(("end", max(dur - eps, 0)))
    for c in cuts:
        times += [(f"cut-{c:.2f}s", max(c - eps, 0)), (f"cut+{c:.2f}s", min(c + eps, dur - eps))]
    return sorted(times, key=lambda x: x[1])


def cmd_sheet(a) -> int:
    clips = [Path(c) for c in a.clips]
    labels = a.label or []
    if a.label_from_name or not labels:
        labels = [c.stem for c in clips]
    if len(labels) != len(clips):
        raise SystemExit("one --label per clip, or use --label-from-name")
    rows = []
    with tempfile.TemporaryDirectory() as td:
        for i, (clip, label) in enumerate(zip(clips, labels)):
            dur = duration(clip)
            times = sample_times(dur, a.frames, a.cuts or [])
            imgs = [(t_label, frame_at(clip, t, Path(td) / f"{i}-{j}.png")) for j, (t_label, t) in enumerate(times)]
            rows.append((label, dur, imgs))
        cols = max(len(r[2]) for r in rows)
        W = PAD + cols * (THUMB_W + PAD)
        H = PAD + sum(LABEL_H + THUMB_H + LABEL_H + PAD for _ in rows)
        board = Image.new("RGB", (W, H), BG)
        d = ImageDraw.Draw(board)
        f_big, f_small = font(16), font(13)
        y = PAD
        for label, dur, imgs in rows:
            d.text((PAD, y), f"{label}   {dur:.2f}s", font=f_big, fill=FG)
            y += LABEL_H
            for j, (t_label, im) in enumerate(imgs):
                x = PAD + j * (THUMB_W + PAD)
                board.paste(im, (x, y))
                if t_label.startswith("cut"):
                    d.rectangle((x, y, x + THUMB_W - 1, y + THUMB_H - 1), outline=ACCENT, width=3)
                d.text((x, y + THUMB_H + 3), t_label, font=f_small, fill=FG)
            y += THUMB_H + LABEL_H + PAD
        out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
        board.save(out, quality=85)
    print(f"wrote {out}  ({len(rows)} clips, {cols} frames each)")
    return 0


def label_png(text: str, dest: Path, width: int) -> None:
    im = Image.new("RGBA", (width, 44), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = font(26)
    tw = d.textlength(text, font=f)
    d.rectangle((8, 4, 8 + tw + 16, 40), fill=(0, 0, 0, 140))
    d.text((16, 8), text, font=f, fill=(255, 255, 255, 255))
    im.save(dest)


def cmd_ab(a) -> int:
    left, right = Path(a.clips[0]), Path(a.clips[1])
    la, lb = (a.labels or [left.stem, right.stem])
    dur = a.duration or min(duration(left), duration(right))
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    # Labels are rendered with Pillow and overlaid, so no drawtext/fontconfig build of ffmpeg is required.
    # A thin bar at the bottom moves with time so pacing differences stay readable in playback.
    with tempfile.TemporaryDirectory() as td:
        pa, pb = Path(td) / "a.png", Path(td) / "b.png"
        label_png(la, pa, 1280); label_png(lb, pb, 1280)
        fc = (f"[0:v]scale=-2:720,fps=24[l0];[1:v]scale=-2:720,fps=24[r0];"
              f"[l0][2:v]overlay=0:0[l];[r0][3:v]overlay=0:0[r];[l][r]hstack=inputs=2[s];"
              f"[s][4:v]overlay=x='-w+(main_w*t/{dur:.3f})':y=main_h-6:shortest=1[v]")
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(left), "-i", str(right),
             "-i", str(pa), "-i", str(pb), "-f", "lavfi", "-i", f"color=c=0xeee7dd:s=2560x6:r=24:d={dur:.3f}",
             "-filter_complex", fc, "-map", "[v]", "-t", f"{dur:.3f}", "-an", "-c:v", "libx264", "-crf", "20",
             "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)])
    print(f"wrote {out}  ({dur:.2f}s side by side)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sheet"); s.add_argument("clips", nargs="+"); s.add_argument("--out", required=True)
    s.add_argument("--label", action="append"); s.add_argument("--label-from-name", action="store_true")
    s.add_argument("--frames", type=int, default=5, help="evenly spaced frames per clip (default 5)")
    s.add_argument("--cuts", type=float, nargs="*", help="cut times in seconds; frames just before/after are added")
    b = sub.add_parser("ab"); b.add_argument("clips", nargs=2); b.add_argument("--out", required=True)
    b.add_argument("--labels", nargs=2); b.add_argument("--duration", type=float)
    a = ap.parse_args(argv)
    return {"sheet": cmd_sheet, "ab": cmd_ab}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
