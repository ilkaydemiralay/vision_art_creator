# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Changed

- Supervisor pipeline section is now a 10-row table; the ASCII diagram moved
  to `references/pipeline-diagram.md`. SKILL.md 423 → ~370 lines.
- Review fixes (independent audit, 2026-10-31): `media_registry.py` rejects
  directories, undecodable files, `take < 1` and missing prompt files, warns
  when no prompt is given, classifies still images (`kind: image`, no fake
  fps), requires `--note` on `select`, and `verify` catches hand-edited logs
  (duplicate `add`, decisions without `add`). `contact_sheet.py` samples by
  the clip's real fps, refuses cut times outside the clip and fails loudly
  when ffmpeg decodes no frame. Supervisor gained the evidence-table gate and
  the `--shots` example. `install.sh` warns when the plugin is already enabled.
  Turkish docs: em/en dashes and circumflexes removed.

## [1.3.1] - 2026-10-31

### Changed

- `creator-pipeline-supervisor/SKILL.md` trimmed from 545 to 423 lines: the
  continuity bible, project bible and locked prompt block templates moved to
  `references/*-template.md`; the media registry section now points to
  `--help`. Behaviour unchanged, less context per invocation.

## [1.3.0] - 2026-10-30

### Added

- **Claude Code plugin.** `.claude-plugin/plugin.json` + a single-plugin
  marketplace in this repo. Install in one step:
  `/plugin install vision-art-creator --marketplace ilkaydemiralay/vision_art_creator`.
  `install.sh` remains for Codex and manual symlink installs.
- **Media registry** (`creator-pipeline-supervisor/scripts/media_registry.py`,
  schema `schemas/media-registry.schema.json`): binds every generated file to
  its shot, take, model, prompt hash, file hash and probed duration/fps/size;
  `select`/`reject` with reasons; `verify` fails on missing or changed files,
  zero or duplicate selections, wrong durations; `report` sums recorded cost.
- **QC contact sheet and A/B comparison**
  (`creator-final-cut-editor/scripts/contact_sheet.py`): labelled frame grids
  with before/after-cut frames outlined, and a time-aligned side-by-side video
  of two takes with labels and a progress bar. No ffmpeg `drawtext` needed.
- **Historical evidence table**
  (`creator-production-designer/references/historical-evidence-table.md`):
  claim → source → certainty → decision → affected prompts, wired into the
  screenwriter, production-designer and supervisor skills.

### Changed

- Final-cut-editor, pipeline-supervisor, production-designer and screenwriter
  SKILL.md files reference the new scripts and table.
- Plugin icon added at `.claude-plugin/icon.png`.

## [1.2.0] - 2026-10-05

### Added

- **OpenAI Codex support.** The skills are plain `SKILL.md` folders and work in
  Codex as well as Claude Code. `./install.sh --codex` links them into
  `~/.agents/skills/`; `./uninstall.sh --codex` removes them.
- **Demo film.** *Before She Leaves*, a 26-second scene made with the pack and
  Higgsfield, plus a 30-second making-of showing the recorded graph. Both play
  inline in the READMEs; full-quality files are attached to the release. All
  footage is AI-generated.
- `docs/media/social-preview.png`: the repository's social preview image.

### Changed

- All 12 READMEs name both Claude Code and OpenAI Codex and include the demo.

## [1.1.0] - 2026-10-04

### Added

- **Recorded graph mode (optional, experimental).** `creator-pipeline-supervisor`
  can run pre-production for a single scene as a 12-node graph
  (`workflows/single-scene.v1.json`). The contract lives in
  `skills/creator-pipeline-supervisor/references/graph-workflow.md`.
- Six JSON Schemas (`schemas/`), a read-only validator
  (`scripts/validate_graph.py` with `workflow`, `validate`, `impact` and
  `revision` commands) and 44 tests (`tests/`). Tested on Python 3.10, 3.11 and 3.14.
- Hash-bound approval gates. An approval must cover the exact SHA-256 of the
  artifact and its direct inputs, pass every check, and come before the run
  that consumes it. Failed or partial runs cannot be recorded.
- Design approvals must declare `approver_role: director` or `user`. A
  coordinator approving its own design is rejected.
- Revision impact tracking. Only transitively affected nodes re-run; unaffected
  artifacts and runs must stay identical. `--allow-growth` validates the step
  from a partial checkpoint to a full package.
- Timestamps must be RFC 3339 with a timezone.
- A worked 15-second, three-shot text pilot in `examples/single-scene/`:
  v00 stops at a design conflict, v01 resolves it, v02 changes one prop colour
  and re-runs 7 of 12 nodes.
- Design and results notes in `docs/` (Turkish).
- `CHANGELOG.md` and `VERSION`.

### Changed

- `creator-cinematographer` and `creator-storyboard-artist` keep prompt drafts
  in their own folders. Only `creator-prompt-engineer` writes final prompts
  under `project/prompts/`.
- `creator-pipeline-supervisor` owns the QC layer except `qc/reviews/`, which
  is reserved for independent reviewers.
- `creator-final-cut-editor` reads supervisor reports from `project/qc/`
  (previously `project/continuity/`).
- Character, production, screenwriter and shot-list skills gained a short
  "Recorded graph mode" section on ownership and input snapshots.

### Fixed

- The output table in `creator-cinematographer` showed a doubled
  `cinematography/` path.

### Notes

- Without graph mode the skills are used exactly as before, and no Python is needed.
- The pilot's v01/v02 approvals predate approver roles. They validate only with
  `--legacy-approvals`, which reports "historical compatibility only; not
  production approval".
- Known limits: text-only pilot by a single author. Parallel department runs,
  media generation, editing and cost were not tested. Approver identity and
  timestamps are declared by the operator, not signed.

## [1.0.0] - 2026-06-25

First public release: 11 `creator-*` skills, `install.sh` / `uninstall.sh`,
READMEs in 12 languages, MIT license, contributing guide, issue and PR
templates.

[1.2.0]: https://github.com/ilkaydemiralay/vision_art_creator/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/ilkaydemiralay/vision_art_creator/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/ilkaydemiralay/vision_art_creator/releases/tag/v1.0.0
