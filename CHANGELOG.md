# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project uses [Semantic Versioning](https://semver.org/).

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
