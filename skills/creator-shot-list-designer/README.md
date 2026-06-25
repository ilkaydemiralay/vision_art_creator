# Shot List Designer — `creator-shot-list-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

The skill that turns scenes and storyboards into a **shot list + edit intent**.
The place where pre-production planning and editorial intent come together. It is
not the final-cut editor — it designs editorial intent BEFORE any material is
produced, so that the shoot generates the right pieces.

## Philosophy

A shot list is not a technical inventory; it is a **map of dramatic + editorial
intent**. This skill:

- **Shot economy**: every shot carries a single clear action
- **Edit rhythm awareness**: which shot is held long, which is cut quickly?
  Shot duration is an editorial decision
- **Screen direction + continuity**: spatial/temporal consistency across cuts
- **Producibility for AI**: plans single-shot complexity around AI tool constraints
- **Editorial intent before production**: the edit logic is set BEFORE the shoot
  so that unnecessary shots are not filmed
- **Audience experience design**: what does the viewer feel, learn, and what is withheld?

## What it produces

| Output | Content |
|-------|---------|
| **Per-scene shot list** | Canonical shot list, with dramatic + editorial justification |
| **Edit plan** | Within-scene pacing, cut points, opening/closing image |
| **Transition design** | Scene-to-scene transition decisions (hard cut, match, J/L, sound bridge) |
| **Continuity risk audit** | Report of consistency risks across shots |
| **Sound edit notes** | J-cut / L-cut / silence points for the sound designer |
| **Film-wide shot list** | Consolidated list covering the whole film |
| **Rhythm map** | Scene-by-scene pacing (shot duration ranges) |
| **Redundancy report** | Shots that should be cut/merged |
| **Final editor notes** | Editorial intent hand-off to the final-cut editor |

## When it comes into play

- Scenes and storyboards are ready, and a shot-based plan is needed
- Edit-aware shot sequencing is requested
- Long scenes need to be broken into AI-producible pieces
- When the director or DOP requests a structural shooting/production plan
- When `creator-pipeline-supervisor` delegates pre-edit planning

## Typical flow

1. **Briefing** + reading all upstream skill outputs
2. **Question round**: format, edit rhythm, tone, AI tools
3. **Shot list (per scene)**: in canonical structure, with dramatic + editorial justification
4. **Edit plan (per scene)**: pacing, opening/closing, cut points
5. **Transition design**: scene-to-scene transitions
6. **Continuity audit**: cross-shot risks
7. **Rhythm map**: film-wide pacing map
8. **Redundancy report**: identification of cuttable shots
9. **Hand-off**: shot prompt data for creator-prompt-engineer + editorial intent for creator-final-cut-editor

## Shot — canonical structure

```
Scene 04 — Shot 04.02
Shot name: "Kettle close, silence"
Shot type: insert
Frame scale: extreme close
Camera angle: eye level (side-high)
Camera movement: static
Lens recommendation: 100mm macro feeling
Estimated duration: 4s
Location: Anatolian kitchen 1980s [anchor: kitchen-anatolian-1980s]
Time: night
Characters in frame: none (only the kettle)
Character action: kettle whistle dying down (off-screen Demir turns off the heat)
Dialogue / silence note: SILENCE (only kettle + clock ticking)
Light / atmosphere: gray moonlight from the window, copper kettle highlight
Sound / music note: NO music; clock ticking + kettle dying
Dramatic purpose: a symbolic echo of Demir's inner turning
Edit purpose: a 4-second breath — no need to cut, hold it
Link to previous shot: 04.01 (Demir sitting, wide) — match by sound
Link to next shot: 04.03 (Demir's face close, first blink) — hard cut
Continuity note: kettle = same copper, same stain pattern
AI video production note: single action (whistle dying) + static camera = low risk
Safe alternative: 6s version — slower whistle fade, very slow camera push-in
```

## Editorial intent — scene plan

Scene-level editorial questions:

- Which shot opens the scene?
- Which image closes it?
- Which shot is held long?
- Which shot is cut short?
- Where do the reaction shots go?
- Where does silence stretch?
- Where is a hard cut needed?
- Where is a soft transition?
- Which image links to the next scene?
- Which shot carries the dramatic peak?
- Which shot is unnecessary?
- Which shot delivers information, which delivers emotion?

Written under `project/shot-list/scene-{NN}/edit-plan.md`.

## Where it writes its outputs

Under `project/shot-list/`:

| File | Content |
|-------|---------|
| `scene-{NN}/shot-list.md` | Scene shot list |
| `scene-{NN}/edit-plan.md` | Edit intent + pacing |
| `scene-{NN}/transitions.md` | Transition decisions |
| `scene-{NN}/continuity-risks.md` | Continuity audit |
| `scene-{NN}/sound-edit-notes.md` | Sound designer hand-off |
| `film-shot-list.md` | Whole-film consolidated list |
| `rhythm-map.md` | Pacing map |
| `redundancy-report.md` | Cuttable shots |
| `ai-production-shot-guide.md` | AI tool constraint guide |
| `final-editor-notes.md` | Intent for the final-cut editor |

## Transition types (editorial use)

| Transition | Editorial use |
|-------|-------------------|
| Hard cut | Sudden dramatic break |
| Match cut | A bridge of meaning between two images |
| Fade in/out | Temporal/emotional opening/closing |
| Dissolve | Time transition, emotional blend |
| J-cut | The next scene's sound arrives first (smooth flow) |
| L-cut | The current scene's sound is extended (held emotion) |
| Sound bridge | Change of place/time carried over sound |
| Visual motif | A bridge via a recurring visual |
| Object transition | Shape match |
| Movement transition | Directional continuity |
| Time jump | Sudden time skip |
| Flashback | Via a filter/lens/blur/sound cue |
| Parallel edit | Two places interwoven |

## AI video producibility rules

- One clear action per shot
- One main camera movement (not chained)
- A controlled number of characters
- A clear visual target
- Break complex motion into multi-shot
- Flag risky hand/finger/lip sync
- Selective framing for crowds
- Locked location + character anchors in every prompt
- Shot duration typically 3–10s
- Each shot maps cleanly to a single video prompt

When a risk is detected, flag it:

> *"This shot is too complex for AI video — split it into two shots."*
> *"Lip sync may fail here; use a reaction shot instead of the speaker."*
> *"The hand movement is critical — use a wider frame instead of an insert."*
> *"Crowd action — build it with cuts, not a single shot."*

## Rhythm and pacing

Vague phrases like "make it fast" are not used. Pacing is:

- Expressed as a **shot duration range**
- Measured by **cut frequency**

Example:
> *"Scene 3 averages 4–6s/shot, scene 12 averages 1.5–3s/shot —
> the pace speeds up as the character conflict escalates."*

## Dialogue edit intent

For dialogue-heavy scenes:

- The speaker or the listener?
- Where do the reaction shots go?
- Where is silence stronger?
- Another image over the dialogue?
- Subtext through facial expression?
- Hard cut vs. natural overlap?
- Cut before the sentence ends?
- Redundant repetition of explanation?
- On whom is the emotion the viewer really needs to see?

J-cut / L-cut markers are set here.

## Coordination with other skills

- **Reads**: script, director's vision + direction sheets, DOP per-scene plan,
  storyboard panel data, character/location anchors
- **Writes**: `project/shot-list/*`
- **Hands off to**:
  - `creator-prompt-engineer` (shot-level video prompts)
  - `creator-final-cut-editor` (editorial intent files)
- **Receives feedback from**: Director, Pipeline Supervisor

## Redundancy detection

In a long AI film, flag:

- A shot that repeats the same information
- A shot that does not change the emotion
- A detail shot that drops the rhythm
- Excessive use of reaction shots
- An AI-hard shot with low dramatic contribution
- Late-in / early-out opportunities
- A moment that can be told visually instead of in dialogue

*"This shot can be cut"* or *"These two shots can be merged"* is written explicitly.

## Behavioral rules

| Does | Doesn't |
|-------|---------|
| Gives every shot a dramatic **and** editorial justification | Make a technical inventory |
| Coordinates with director's rhythm, DOP framing, storyboard | Decide in isolation |
| Flags unnecessary shots | Add filler |
| Checks continuity proactively | Wait for problems to surface after the shoot |
| Designs around AI tool constraints | Plan unproducible shots |
| A safe alternative for risky shots | Provide a single version |
| Considers the listener too in dialogue | Follow only the speaker |
| Coordinates sound and music editorial intent | Think only of the picture |
| Structured, downstream-readable output | Dump a single block of text |
