# Historical evidence table

Use this whenever the film touches real history, a real place, a real person,
a period costume, a uniform, a flag, a vehicle, a document, or a dated event.
"Research first" is already a rule in the screenwriter, production-designer and
cinematographer skills; this table turns that rule into an auditable record so
a wrong detail can be traced to every prompt it reached.

File: `project/bible/evidence-table.md` (owner: creator-production-designer;
screenwriter adds story claims; pipeline-supervisor checks it before prompts
are consolidated).

## Table

| ID | Claim or object | Scene(s) | Date / place | Source (title, page or URL, accessed) | Certainty | Decision | Affected prompts |
|----|-----------------|----------|--------------|----------------------------------------|-----------|----------|------------------|
| E01 | Infantry uniform colour, 1922 | S03, S07 | Western Anatolia, Aug 1922 | Museum catalogue X, p. 41, accessed 2026-10-30 | verified | as documented | P-S03-02, P-S07-01 |
| E02 | Radio in village coffeehouse | S05 | Edirne, 1935 | Oral account only | plausible | dramatised, kept | P-S05-03 |
| E03 | Street lamp type | S01 | Istanbul, 1920 | none found | unknown | neutral choice, no close-up | P-S01-01 |

**Certainty**: `verified` (two independent sources or a primary source) ·
`plausible` (one secondary source or expert memory) · `unknown` (no source).

**Decision**: `as documented` · `dramatised, kept` (knowingly inaccurate for
story reasons, say why in a note) · `neutral choice` (avoid the detail or keep it
out of focus) · `cut`.

## Rules

- Every `unknown` row must either get a source or a `neutral choice` /
  `cut` decision before the prompt-engineer consolidates prompts. Prompts do
  not ship with unverified period claims in close-up.
- `dramatised, kept` rows are listed in the project bible under "Known
  departures from record" so credits or captions can acknowledge them.
- When a row changes, re-open every prompt listed in "Affected prompts" and
  bump their revision. The pipeline-supervisor logs the cascade.
- Dates: write the calendar in force at the time if it matters to the story,
  and the Gregorian date in brackets.
- Named real people: record the source of any quoted words. Invented dialogue
  for a real person is a `dramatised, kept` row.
- Flags, insignia, scripts and alphabets are high-risk anchors: an AI model
  will invent plausible-looking ones. Always provide a reference image and
  mark the row `verified` only after the generated frame is checked against it.
