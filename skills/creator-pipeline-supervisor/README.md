# Pipeline & Continuity Supervisor — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

The **orchestrator** and **continuity supervisor** of an AI film project. Two
integrated disciplines come together:

- **Pipeline supervisor**: which skill runs when, where shared state lives,
  how revisions loop, how versions are tracked, how the project ships
- **Continuity supervisor**: audits the consistency of character, costume,
  location, prop, light, color, sound, time, and edit direction scene by
  scene and department by department — catches contradictions early, requests
  fixes

## Philosophy

The pipeline-supervisor is not a "checklist tool." It thinks like a combination
of a **unit production manager + script supervisor**. It holds the entire
project in its head and lets no department's work drift from the film's
coherent intent. This skill:

- **Keeps a single source of truth**: `bible/continuity-bible.md` governs
  everything
- **Production status table** always current — the answer to "what should I do
  now"
- **Locked-anchor discipline**: character DNA + location master reference +
  style block — enters every prompt verbatim
- **Cross-skill arbitration**: when two departments conflict, it relays both
  positions, presents options referenced against the director's vision, and
  escalates to the user
- **Revision-loop management**: when a downstream skill finds a problem
  upstream, it cascades in canonical order
- **Risk register**: proactive risk tracking, mitigation follow-up
- **Ship gate**: won't say "done" without a delivery-readiness audit

## What it produces

| Output | Content |
|--------|---------|
| **Project bible** | High-level project canon |
| **Style bible** | Cross-skill style canon |
| **Continuity bible** | Continuity single source of truth |
| **Prompt blocks** | Consolidated locked prompt blocks |
| **Production status table** | Skill × scene status matrix |
| **Risk register** | Risk + severity + mitigation log |
| **Continuity audit reports** | Domain-based audits |
| **Revision request manifests** | Cross-skill revision requests |
| **Prompt consistency report** | Pre-generation audit |
| **AI generation error summary** | Post-generation audit |
| **Final QC report** | Whole-project audit |
| **Delivery readiness** | Ship gate (pass/fail) |
| **Decisions log** | Dated decision history |

## When it engages

- A new AI film project is being started
- A cross-skill consistency audit is requested on an ongoing project
- On the question "what should I do now" (the answer comes from production
  status)
- When a continuity or pipeline question crosses a skill boundary
- A delivery-readiness audit is requested
- A folder-structure / file-organization question
- When a revision needs to cascade to dependent skills

## When it does NOT engage

- Single-skill creative work (let the specialist work on its own)
- Simple single-shot generation
- Purely technical questions outside film production

## Canonical pipeline

```
0. project bible & vision
1. creator-screenwriter
2. creator-director
3-4-5. character + production + DOP (parallel)
6. creator-storyboard-artist
7. creator-shot-list-designer
8. creator-prompt-engineer
   → [AI material generation — operator]
9. creator-sound-music-designer
10. creator-final-cut-editor

Throughout all stages: creator-pipeline-supervisor handles continuity, QC, revision, bible management
```

The order is **canonical but not rigid**:
- **Iterative loops**: creator-director feedback → creator-screenwriter new v
- **Parallel work**: after the director's vision, character/production/DOP run
  in parallel

## Continuity domains (audit areas)

1. Story / plot
2. Time / chronology
3. Character (physical)
4. Character arc (emotional)
5. Costume
6. Hair / makeup
7. Accessories / props
8. Location
9. Set dressing
10. Light direction
11. Color palette
12. Camera language
13. Sound / ambience
14. Music theme (leitmotif)
15. Emotional flow
16. Edit / screen direction
17. AI prompt consistency (locked anchors verbatim)
18. Reference image consistency
19. Scene / shot numbering

There is a risk log for each domain: `project/qc/continuity-reports/`.

## Continuity bible (single source of truth)

`project/bible/continuity-bible.md` — this file is the **authority**. If a
skill's output conflicts with the bible, the bible wins (or the bible is
updated).

Its contents:
- Locked character anchors (DNA verbatim)
- Locked location anchors (master reference verbatim)
- Costume continuity table (scene × character)
- Time / weather table
- Prop continuity table
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction (screen direction × scene)
- Open continuity questions (awaiting a director's decision)
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`:

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

Updated after every skill run. The source of the answer to "what should I do now?"

## Revision-loop management

When a downstream skill finds a problem upstream:

1. **Origin detection**: which skill's output is faulty?
2. **Blast radius**: how does the fix affect dependent skills?
3. **Change request**: `qc/revision-notes/req-{NN}.md`
4. **Decision**: fix at origin (deep, slow) vs. workaround (shallow, fast)
5. **Origin fix**: skill is re-triggered, dependents go 🟡, cascade in canonical order
6. **Workaround**: where, why, and who applied it is recorded
7. **Resolution log**: appended to the continuity bible's "Resolved decisions"

## Cross-skill arbitration

When two skills conflict (e.g. DOP warm light vs. character cool palette):

1. Quote both proposals **verbatim**
2. State the conflict in plain language
3. Reference the director's vision
4. Present 2–3 solutions + trade-offs
5. Escalate to the user / director
6. The decision is written into the continuity bible

**It does not choose silently** — it makes the conflict visible.

## Risk register

`project/qc/risk-register.md`:

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| Lip-sync fail risk in scene 7 | medium | high | creator-shot-list-designer | use reaction shot | mitigating |
| Hand insert AI risk in scene 12 | medium | medium | creator-prompt-engineer | wider framing backup | mitigated |
| "Navy coat" hue drift | low | high | creator-character-designer | hex locked in DNA | mitigated |

## Folder structure (two options)

### Default (named — simple)

`project/screenplay/`, `project/characters/`, `project/cuts/` ...

### Alternate (numbered — for large projects)

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

Same content, numbered and friendly for visual scanning. Default is named; it
offers a migration on request.

## Where it writes its outputs

Under `project/bible/` and `project/qc/` (it does NOT write DIRECTLY to other
skills' directories — it sends them revision requests):

| File | Content |
|------|---------|
| `bible/project-bible.md` | High-level project canon |
| `bible/style-bible.md` | Cross-skill style canon |
| `bible/continuity-bible.md` | Continuity single source of truth |
| `bible/prompt-blocks.md` | Locked prompt blocks |
| `qc/production-status.md` | Skill × scene status matrix |
| `qc/risk-register.md` | Risk log |
| `qc/continuity-reports/{topic}.md` | Domain audits |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | Pre-generation audit |
| `qc/ai-generation-error-summary.md` | Post-generation audit |
| `qc/final-qc-report.md` | Whole-project audit |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | Dated decision history |

## Typical flow (new project)

1. User briefing
2. Write `bible/project-bible.md`
3. → Trigger **creator-screenwriter**
4. Script v1 → trigger **creator-director**
5. Vision → parallel: **character + production + DOP**
6. Cross-palette audit; flag conflicts
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. Build/update `bible/prompt-blocks.md`
10. → **creator-prompt-engineer**
11. Pre-generation audit
12. [AI material — operator runs it]
13. Post-generation audit
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit (ship gate)

Before it's called done:

- ✅ All scenes are in production-status
- ✅ Continuity audit is clean (or only minor flags)
- ✅ Final cut is director-approved
- ✅ Audio integration audit is clean
- ✅ AI errors triaged (no critical 🔴)
- ✅ Color grade applied or intentionally flagged
- ✅ Subtitles complete and timed
- ✅ Title cards / credits in place
- ✅ Master for all deliverable platforms under `project/delivery/`
- ✅ Trailer cut produced (if requested)
- ✅ Archive master stored
- ✅ Documentation current (bible, continuity, prompt-blocks)

## Coordination with other skills

- **Reads**: all skill outputs (everything in `project/`)
- **Writes**: `project/bible/*`, `project/qc/*` — does NOT write DIRECTLY to
  other directories
- **Triggers**: all specialist skills
- **Arbitrates**: cross-skill conflicts

## Behavior rules

| Does | Doesn't |
|------|---------|
| Enforces fidelity to the director's vision in every department | Allows silent drift |
| On cross-skill conflict, quotes both sides **verbatim** | Picks a side silently |
| Documents every decision with date + rationale | Acts without a record |
| Protects the continuity bible as the authority | Lets output that conflicts with the bible pass |
| Updates production-status after every skill run | Leaves a stale table |
| Cascades revisions in canonical order | Skips a dependent skill |
| Escalates creative disputes to the user / director | Arbitrates on its own |
| Continuity audit at every act break on a long film | Audits only at the end |
| Proactive risk register | Holds a critical 🔴 |
| Won't say "ship" until delivery-readiness.md is green | Calls it complete early |
| Structured, machine-readable output | Dumps a single block of text |
