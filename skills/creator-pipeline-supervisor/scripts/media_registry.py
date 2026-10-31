#!/usr/bin/env python3
"""Media registry: bind generated media files to the shots they were made for.

Every generated clip or image is registered with its shot id, take number,
model, prompt hash, file hash and probed technical facts. Selection and
rejection are recorded with a reason, so a later cut never picks the wrong
file and every prompt → result pair stays traceable.

Registry file: <project>/media/registry.jsonl (one JSON object per line).

Usage:
  media_registry.py add     --project P --file clip.mp4 --shot S07 --take 2 \
                            --model seedance_2_0 [--prompt prompt.txt] [--job-id ID] [--cost 12.5]
  media_registry.py select  --project P --shot S07 --take 2 [--note "best motion"]
  media_registry.py reject  --project P --shot S07 --take 1 --reason "hand morphs at 3s"
  media_registry.py verify  --project P            # re-hash, missing files, duplicate takes
  media_registry.py report  --project P [--json]   # per-shot status table

Exit code 1 on verification failures. Requires ffprobe on PATH for video/audio.
"""
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

REGISTRY = "media/registry.jsonl"
STATUSES = ("registered", "selected", "rejected")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def probe(path: Path) -> dict:
    """Return duration/fps/width/height/has_audio via ffprobe; images fall back to Pillow."""
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
            capture_output=True, text=True, check=True).stdout
    except (FileNotFoundError, subprocess.CalledProcessError):
        return _probe_image(path)
    info = json.loads(out)
    v = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), None)
    if not v:
        return {}
    # Still images (png/jpeg/webp…) open fine in ffprobe but carry a fake demuxer fps; classify them separately.
    if v.get("codec_name") in ("png", "mjpeg", "webp", "bmp", "tiff", "gif") or path.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
        return {"width": v.get("width"), "height": v.get("height"), "fps": None, "duration_s": None,
                "frames": 1, "has_audio": False, "kind": "image"}
    fps = None
    if v.get("r_frame_rate") and "/" in v["r_frame_rate"]:
        n, d = v["r_frame_rate"].split("/")
        fps = round(int(n) / int(d), 3) if int(d) else None
    dur = info.get("format", {}).get("duration")
    return {
        "width": v.get("width"), "height": v.get("height"), "fps": fps,
        "duration_s": round(float(dur), 3) if dur else None,
        "frames": int(v["nb_frames"]) if str(v.get("nb_frames", "")).isdigit() else None,
        "has_audio": any(s.get("codec_type") == "audio" for s in info["streams"]),
        "kind": "video",
    }


def _probe_image(path: Path) -> dict:
    try:
        from PIL import Image
        with Image.open(path) as im:
            return {"width": im.width, "height": im.height, "duration_s": None, "fps": None,
                    "frames": 1, "has_audio": False, "kind": "image"}
    except Exception:
        return {}


def load(project: Path) -> list[dict]:
    p = project / REGISTRY
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]


def append(project: Path, rec: dict) -> None:
    p = project / REGISTRY
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def current_state(records: list[dict]) -> dict[tuple[str, int], dict]:
    """Fold the event log into the latest state per (shot, take)."""
    state: dict[tuple[str, int], dict] = {}
    for r in records:
        key = (r["shot_id"], r["take"])
        if r["event"] == "add":
            state[key] = {**r, "status": "registered"}
        elif key in state:
            state[key] = {**state[key], "status": "selected" if r["event"] == "select" else "rejected",
                          "decision_at": r["at"], "decision_note": r.get("note") or r.get("reason")}
    return state


def cmd_add(a) -> int:
    project = Path(a.project)
    f = Path(a.file)
    if not f.is_file():
        print(f"ERROR: not a file: {f}", file=sys.stderr); return 2
    if a.take < 1:
        print("ERROR: --take must be >= 1", file=sys.stderr); return 2
    if a.prompt and not Path(a.prompt).is_file():
        print(f"ERROR: prompt file not found: {a.prompt}", file=sys.stderr); return 2
    if not a.prompt:
        print("WARNING: no --prompt given; prompt → result traceability is lost for this take", file=sys.stderr)
    pr = probe(f)
    if not pr.get("width"):
        print(f"ERROR: not a decodable image or video (ffprobe/Pillow found no picture stream): {f}", file=sys.stderr); return 2
    state = current_state(load(project))
    if (a.shot, a.take) in state:
        print(f"ERROR: {a.shot} take {a.take} already registered; use a new take number", file=sys.stderr); return 2
    rec = {
        "event": "add", "at": now(), "shot_id": a.shot, "take": a.take,
        "file": str(f.resolve().relative_to(project.resolve())) if f.resolve().is_relative_to(project.resolve()) else str(f.resolve()),
        "sha256": sha256(f), "bytes": f.stat().st_size, "model": a.model,
        "job_id": a.job_id, "cost": a.cost, "tool": a.tool,
        "prompt_sha256": sha256(Path(a.prompt)) if a.prompt else None,
        "prompt_file": a.prompt, "probe": pr, "note": a.note,
    }
    dup = [k for k, v in state.items() if v["sha256"] == rec["sha256"]]
    if dup:
        print(f"WARNING: identical file already registered as {dup[0][0]} take {dup[0][1]}", file=sys.stderr)
    append(project, rec)
    print(f"registered {a.shot} take {a.take}  {rec['sha256'][:12]}  {rec['probe']}")
    return 0


def _decide(a, event: str) -> int:
    project = Path(a.project)
    state = current_state(load(project))
    if (a.shot, a.take) not in state:
        print(f"ERROR: {a.shot} take {a.take} not registered", file=sys.stderr); return 2
    rec = {"event": event, "at": now(), "shot_id": a.shot, "take": a.take}
    if event == "select":
        rec["note"] = a.note
        prev = [k for k, v in state.items() if k[0] == a.shot and v["status"] == "selected" and k[1] != a.take]
        for k in prev:  # one selected take per shot: demote the old one explicitly
            append(project, {"event": "reject", "at": now(), "shot_id": k[0], "take": k[1],
                             "reason": f"superseded by take {a.take}"})
    else:
        rec["reason"] = a.reason
    append(project, rec)
    print(f"{event}ed {a.shot} take {a.take}")
    return 0


def cmd_verify(a) -> int:
    project = Path(a.project)
    records = load(project)
    state = current_state(records)
    problems: list[str] = []
    seen_add: set[tuple[str, int]] = set()
    for r in records:
        key = (r.get("shot_id"), r.get("take"))
        if r.get("event") == "add":
            if key in seen_add:
                problems.append(f"{key[0]} take {key[1]}: duplicate add event in registry (log edited by hand?)")
            seen_add.add(key)
        elif key not in seen_add:
            problems.append(f"{key[0]} take {key[1]}: {r.get('event')} event without a prior add")
        if r.get("event") == "add" and (not isinstance(r.get("take"), int) or r["take"] < 1):
            problems.append(f"{key[0]}: invalid take {r.get('take')!r}")
    for (shot, take), v in state.items():
        f = project / v["file"] if not Path(v["file"]).is_absolute() else Path(v["file"])
        if not f.exists():
            problems.append(f"{shot} take {take}: file missing: {v['file']}")
            continue
        if sha256(f) != v["sha256"]:
            problems.append(f"{shot} take {take}: sha256 changed since registration")
    shots: dict[str, list] = {}
    for (shot, take), v in state.items():
        shots.setdefault(shot, []).append(v)
    for shot, takes in shots.items():
        sel = [t for t in takes if t["status"] == "selected"]
        if len(sel) > 1:
            problems.append(f"{shot}: {len(sel)} takes selected, expected 1")
        if not sel and a.require_selected:
            problems.append(f"{shot}: no selected take")
        if a.expect_duration and sel:
            d = sel[0]["probe"].get("duration_s")
            if d is None or abs(d - a.expect_duration) > a.tolerance:
                problems.append(f"{shot}: selected duration {d}s, expected {a.expect_duration}±{a.tolerance}s")
    for shot in (a.shots or []):
        if shot not in shots:
            problems.append(f"{shot}: no media registered")
    if problems:
        print("\n".join("FAIL " + p for p in problems)); return 1
    print(f"OK  {len(state)} takes across {len(shots)} shots, all files present and unchanged")
    return 0


def cmd_report(a) -> int:
    state = current_state(load(Path(a.project)))
    shots: dict[str, list] = {}
    for (shot, take), v in sorted(state.items()):
        shots.setdefault(shot, []).append(v)
    if a.json:
        print(json.dumps(shots, indent=2, ensure_ascii=False)); return 0
    print(f"{'shot':8} {'take':4} {'status':10} {'model':16} {'dur':>6} {'size':>9}  {'sha256':12}  note")
    for shot, takes in shots.items():
        for v in takes:
            pr = v.get("probe") or {}
            dur = f"{pr['duration_s']:.2f}" if pr.get("duration_s") else "-"
            size = f"{pr['width']}x{pr['height']}" if pr.get("width") else "-"
            note = v.get("decision_note") or v.get("note") or ""
            print(f"{shot:8} {v['take']:<4} {v['status']:10} {str(v.get('model') or '')[:16]:16} "
                  f"{dur:>6} {size:>9}  {v['sha256'][:12]}  {note}")
    cost = sum((v.get("cost") or 0) for t in shots.values() for v in t)
    if cost:
        print(f"\ntotal recorded cost: {cost}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("add", "select", "reject", "verify", "report"):
        s = sub.add_parser(name); s.add_argument("--project", required=True)
        if name in ("add", "select", "reject"):
            s.add_argument("--shot", required=True); s.add_argument("--take", type=int, required=True)
        if name == "add":
            s.add_argument("--file", required=True); s.add_argument("--model", required=True)
            s.add_argument("--prompt"); s.add_argument("--job-id"); s.add_argument("--cost", type=float)
            s.add_argument("--tool", help="provider, e.g. higgsfield, fal"); s.add_argument("--note")
        if name == "select":
            s.add_argument("--note", required=True, help="why this take wins (required, it is the audit trail)")
        if name == "reject":
            s.add_argument("--reason", required=True)
        if name == "verify":
            s.add_argument("--require-selected", action="store_true")
            s.add_argument("--shots", nargs="*", help="shot ids that must have media")
            s.add_argument("--expect-duration", type=float); s.add_argument("--tolerance", type=float, default=0.25)
        if name == "report":
            s.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    return {"add": cmd_add, "select": lambda x: _decide(x, "select"), "reject": lambda x: _decide(x, "reject"),
            "verify": cmd_verify, "report": cmd_report}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
