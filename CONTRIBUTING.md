# Contributing to vision_art_creator

Thanks for your interest in improving this AI film-production skill pack for
[Claude Code](https://claude.com/claude-code). Contributions of all kinds are
welcome — fixing a skill, adding a new `creator-*` skill, improving docs, or
adding/correcting a translation.

By contributing you agree that your contributions are licensed under the
project's [MIT License](LICENSE).

---

## Repository layout

```
vision_art_creator/
├── install.sh / uninstall.sh   # symlink-based install into ~/.claude/skills/
├── README.md  + README.<lang>.md   # docs in 12 languages
└── skills/
    └── creator-<name>/
        ├── SKILL.md                # the skill instructions (English only)
        └── README.md + README.<lang>.md   # human-facing docs in 12 languages
```

Each `creator-*` skill is a self-contained directory. `install.sh` symlinks
each one into `~/.claude/skills/`, so editing a file in this repo takes effect
immediately in Claude Code — no reinstall needed.

---

## Local setup

```bash
git clone https://github.com/ilkaydemiralay/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

Restart Claude Code and confirm all 11 `creator-*` skills appear (e.g. type
`/creator-pipeline-supervisor`). Because the skills are symlinked, your edits
are picked up after a restart.

---

## Conventions

### SKILL.md is English-only

`SKILL.md` files are **instructions to the model**, not end-user docs. Keep them
in English:

- Claude already responds in the user's language at runtime.
- A single canonical instruction set avoids duplicate skill names and drift.

Every `SKILL.md` must start with valid frontmatter:

```markdown
---
name: creator-<name>
description: One clear sentence on what the skill does and when to use it.
---
```

The `name` must match the directory name exactly and stay in the `creator-*`
namespace.

### READMEs are translated; English is canonical

Human-facing docs live in 12 languages:

`README.md` (English, **canonical**) · `README.zh.md` · `README.es.md` ·
`README.hi.md` · `README.ar.md` · `README.pt-BR.md` · `README.tr.md` ·
`README.fr.md` · `README.de.md` · `README.ru.md` · `README.ja.md` ·
`README.ko.md`

Every README begins with an H1 title, then the language-selector line (the
current language shown in **bold** without a link, all others linked), e.g.:

```markdown
# Screenwriter — `creator-screenwriter`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)
```

When translating, keep verbatim: skill identifiers (`creator-*`), file/dir
paths, code blocks, ASCII diagrams, CLI commands, tool/model names, and any
table structure (same columns and rows).

---

## Changing an existing skill

1. Edit `skills/creator-<name>/SKILL.md` (and/or its READMEs).
2. Restart Claude Code and test the behavior in a real session.
3. If you changed the **English** `README.md`, update the 11 translations to
   match. If you can't translate them all, say so in the PR — a maintainer or
   another contributor can fill the gaps.

---

## Adding a new skill

```bash
mkdir -p skills/creator-<name>
# write SKILL.md (English) and README.md (English, canonical)
./install.sh   # create the symlink for the new skill
```

Then:

- Add the language-selector header to the README and provide translations
  (or open the PR noting which languages are still missing).
- Add a row for the skill in the **root** README table (and ideally the
  translated root READMEs).
- If the skill participates in the pipeline, wire it into
  `creator-pipeline-supervisor` (sequence, shared-state directories, continuity
  domains) so it stays consistent with the rest of the pack.

---

## Adding or fixing a translation

Translations are very welcome — including new languages.

- Translate from the **English** canonical file.
- Match the markdown structure exactly; only translate prose, headings, and
  table cell text.
- Keep identifiers, paths, code, and tool names untouched.
- Adding a brand-new language? Update the language-selector line in **every**
  existing README so the new file is linked everywhere, and mention it in the
  PR description.

---

## Commit & pull-request guidelines

- Keep commits focused; use clear, present-tense messages
  (e.g. `docs: fix shot-list table in README.ja.md`).
- One logical change per PR where practical.
- In the PR description, note what you changed and — for doc changes — which
  languages are in sync vs. still pending.
- Open an issue first for larger changes (new skills, structural reworks) so we
  can align on direction.

---

## Questions

Open a [GitHub issue](https://github.com/ilkaydemiralay/vision_art_creator/issues)
for bugs, ideas, or questions. Thanks for contributing!
