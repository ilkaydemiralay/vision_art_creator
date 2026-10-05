# vision_art_creator

**English** · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

> An AI film‑production skill pack for [Claude Code](https://claude.com/claude-code) and [OpenAI Codex](https://github.com/openai/codex).

`vision_art_creator` bundles **11 `creator-*` skills** that cover every
department of a film production — from the screenplay all the way to the final
cut — in a single repository. Install it on any machine with `git clone` +
`./install.sh`.

> The skills are designed to reference one another
> (`creator-pipeline-supervisor` orchestrates the rest). Installing them all
> together is recommended.

---

## Demo: *Before She Leaves*

A 26-second scene produced with this pack and Higgsfield (Nano Banana Pro references, Seedance 2.0 clips), plus a 30-second making-of that shows the recorded graph: owners, hashes and approvals. Two agents, Claude Code and OpenAI Codex, worked from the same skill files. All footage is AI-generated.

**Film (26 s)**

https://github.com/user-attachments/assets/1af79d83-494b-403b-96df-cfdf44dabbf1

**Making-of (30 s)**

https://github.com/user-attachments/assets/5db19cde-1c08-42f1-a48a-cd3a4a0a28d8

Full-quality files: [release v1.2.0](https://github.com/ilkaydemiralay/vision_art_creator/releases/tag/v1.2.0)

---

## Installation

```bash
git clone https://github.com/ilkaydemiralay/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

Using OpenAI Codex? Install into its skills directory instead, then restart Codex:

```bash
./install.sh --codex   # ~/.agents/skills/
```

`install.sh` creates a **symlink** for each skill under
`~/.claude/skills/<skill-name>` that points back into this repo. The benefit:
to update, a simple `git pull` is enough — no reinstall required.

### Options

```bash
./install.sh --target /path/to/skills   # install into a different skills dir
./install.sh --force                    # overwrite existing names
./uninstall.sh                          # remove the symlinks
```

`uninstall.sh` only removes symlinks that point into this repo — it leaves
foreign links and real directories untouched (unless `--force`).

### Verify

After installing, restart Claude Code and type:

```
/creator-pipeline-supervisor
```

Check that all 11 `creator-*` skills appear in the skill list.

---

## What's in the pack

| Skill | Summary |
|---|---|
| `creator-pipeline-supervisor` | Orchestrates the whole production, sequences the departments, enforces continuity, runs QC, and produces the delivery‑readiness report. |
| `creator-director` | Translates the screenplay into a unified directorial vision: scene direction, performance, blocking, tonal control. |
| `creator-screenwriter` | Writing and revising screenplays, treatments, loglines, scene outlines, and dialogue. |
| `creator-character-designer` | Designs the character as an integrated whole: psychology, biography, visual identity, costume, props, FACS‑coded expressions. |
| `creator-production-designer` | Builds the world of the film: locations, sets, props, period atmosphere, color/material language, continuity anchors. |
| `creator-cinematographer` | Designs the visual language: light, camera, lens, framing, color, atmosphere, movement. |
| `creator-storyboard-artist` | Visualizes scenes panel by panel: shot scales, angles, blocking, composition, AI prompts. |
| `creator-shot-list-designer` | Turns scenes and storyboards into a technical shot list, broken into AI‑producible chunks. |
| `creator-sound-music-designer` | The sonic world of the film: atmosphere, foley, SFX, score, leitmotifs, scene‑by‑scene music plan, AI audio prompts. |
| `creator-prompt-engineer` | Converts every department's output into consistent prompts for GPT Image 2.0, Nano Banana, Sora, Veo, Runway, Kling, Higgsfield, and more. |
| `creator-final-cut-editor` | Assembles AI‑generated shots/audio/music/graphics into a finished film: rough/fine/final cut, AI‑error triage, delivery formats. |

The full definition of each skill lives in its own `SKILL.md` file.

---

## How it works

The pack runs on **filesystem‑based shared state**. All skills read from and
write to a common `project/` tree (`bible/`, `screenplay/`, `characters/`,
`storyboards/`, `prompts/`, `cuts/`, `qc/`, …). `creator-pipeline-supervisor`
maintains the canonical files (the project & continuity "bibles") and audits
every department's output against them.

The canonical pipeline:

```
0. project bible & vision
1. creator-screenwriter        → screenplay
2. creator-director            → vision, direction sheets, arcs
3-4-5. creator-character-designer + creator-production-designer
        + creator-cinematographer        (run in parallel)
6. creator-storyboard-artist   → panels with prompts
7. creator-shot-list-designer  → shot list + edit plan
8. creator-prompt-engineer     → tool-fit image + video prompts
   → [AI material generation — operator]
9. creator-sound-music-designer → sound + score plan
10. creator-final-cut-editor   → rough → fine → final cut → delivery

Throughout: creator-pipeline-supervisor enforces continuity, runs QC,
manages revision loops, and holds the bibles.
```

The sequence is canonical but not rigid: director feedback can re‑trigger the
screenwriter, and character/production/cinematography typically run in parallel
once the directorial vision is set.

---

## Recorded graph mode (optional, experimental)

Since v1.1.0 the pack includes an optional, machine-checkable workflow for a single scene. `creator-pipeline-supervisor` can run pre-production as a 12-node graph: every artifact is recorded with its SHA-256 hash, every approval is bound to the exact inputs it reviewed, and a revision re-runs only the nodes it affects.

- Workflow: `workflows/single-scene.v1.json`. Contract: `skills/creator-pipeline-supervisor/references/graph-workflow.md`.
- JSON Schemas in `schemas/`, a read-only validator in `scripts/validate_graph.py`, tests in `tests/`.
- A worked 15-second, three-shot text pilot in `examples/single-scene/`: v00 stops at a design conflict, v01 resolves it, v02 changes one prop colour.

Normal skill use needs no Python. To run the validator (Python 3.10+):

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-graph.txt
.venv/bin/python -m unittest discover -s tests
.venv/bin/python scripts/validate_graph.py validate --manifest path/to/manifest.json
```

Limits: this is a text-only pilot written by a single author. Parallel department runs, media generation, editing and cost were not tested. Approver identity and timestamps are declared by the operator, not signed. Design and results notes are in `docs/` (Turkish).

---

## Updating

```bash
cd ~/projects/vision_art_creator
git pull
```

Because the skills are symlinked, no extra step is needed.

See [CHANGELOG.md](CHANGELOG.md) for what changed in each release. **v1.1.0:** `creator-cinematographer` and `creator-storyboard-artist` now keep prompt drafts in their own folders; only `creator-prompt-engineer` writes final prompts under `project/prompts/`.

---

## Development

1. Edit a skill in the repo (`skills/creator-*/SKILL.md`).
2. Test the change in Claude Code — since it's a symlink, it takes effect
   immediately.
3. Commit + push.

To add a new creator skill:

```bash
mkdir -p skills/creator-new-skill
# write SKILL.md and README.md
./install.sh   # create the symlink for the new skill
```

---

## Translations

This README and each skill's `README.md` are available in 12 languages (see the
language selector at the top). The `SKILL.md` instruction files are kept in
English on purpose — Claude responds in the user's language at runtime, and a
single canonical instruction set avoids duplicate skill names.

---

## License

[MIT](LICENSE) © 2026 İlkay Demiralay.
