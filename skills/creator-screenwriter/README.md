# Screenwriter — `creator-screenwriter`

**English** · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

A professional script-development specialist for AI film production. Not just a tool that "generates text," but a creative-writing assistant that thinks about **story, structure, character, rhythm, and theme** together. It draws on the methods of renowned screenwriters (Sorkin's dialogue rhythm, Nolan's structural recursion, Tarantino's tonal control, the Save the Cat! beat structure, Field's three-act paradigm) **as tools, not as templates**.

## Philosophy

Writing a screenplay is different from generating ideas — it means turning an idea into producible, dramatic scenes. This skill:

- **Understands intent first**, then writes
- **Asks questions**, doesn't assume
- **Explains why every scene exists** with a dramatic rationale
- Takes the **show, don't tell** principle seriously
- **Subtext > text** — characters rarely say exactly what they feel
- Applies **creativity, but controlled** — staying faithful to the user's voice
- Respects the constraints of AI film production (crowds, fast action, etc.)

## What it does

| Output type | Use |
|------------|----------|
| **Logline** | The essence of the story in one sentence, for the pitch |
| **Synopsis** | 1 page, the main plot with a preview of the ending |
| **Treatment** | 3–10 pages of prose, scene-by-scene progression |
| **Outline** | A beat-based structural list (the dramatic purpose of every scene) |
| **Character brief** | Want / Need / Fear / Arc — coordinated with the character designer |
| **Scene text** | A full scene in industry-standard script format |
| **Full screenplay** | Version-controlled `script-v1.md`, `script-v2.md` ... |
| **Dialogue revision** | Suggestions for strengthening existing dialogue |
| **Structural analysis** | Identifying weak spots in an existing screenplay |
| **Format adaptation** | Conversion to ad, social media, YouTube, or documentary formats |

## When it kicks in

This skill is triggered by signals such as:

- "Write a screenplay," "develop a story," "let's build a scene"
- "Pull a logline," "write a synopsis," "prepare a treatment"
- "Strengthen this scene," "revise the dialogue"
- "Prepare a character brief," "want/need/fear analysis"
- "I have an idea — could it be a film?" — structural evaluation
- When `creator-pipeline-supervisor` delegates the script stage

## Typical flow

1. **Brief**: The user brings an idea or request
2. **Question round**: Format, genre, tone, target audience, central conflict, characters, period, AI production tool
3. **Vision proposal**: Reasonable assumptions for missing information (clearly labeled)
4. **Skeleton**: Logline → synopsis → outline (beat sheet) order
5. **Scene text**: Scene-by-scene writing from the approved outline
6. **Revision**: Integrating feedback from the director, a new version

If the user wants a quick result, it states the assumptions **explicitly** and adds a note like:

> *"10-minute short film, single protagonist arc, realistic tone — confirm or correct."*

## Where it writes its outputs

All outputs go under `project/screenplay/`:

| File | Content |
|-------|--------|
| `logline.md` | One-sentence story summary |
| `synopsis.md` | One-page full plot summary |
| `treatment.md` | 3–10 page prose treatment |
| `character-brief.md` | Character briefs (handoff to the character designer) |
| `outline.md` | Beat-based scene list, the dramatic purpose of every scene |
| `script-v{N}.md` | Industry-standard screenplay (a new file for each revision) |
| `revision-notes.md` | The rationale for changes between versions |

Version naming: it never overwrites. It progresses as `v1` → `v2` → `v3`. The rationale for each change is summarized in `revision-notes.md` in **commit message** style.

## Industry-standard script format

```
INT. KITCHEN - NIGHT

A worn brass kettle whistles. ELIF (40s, exhausted but composed)
stares at it without moving.

DEMIR (O.S.)
                Elif?

She turns off the burner. The whistle dies.

                              ELIF
                  (quiet)
                  I'm coming.
```

- **Slugline**: `INT./EXT. LOCATION - TIME`
- **Action**: present tense, visual, third person, at most 4 lines
- **Character name**: ALL CAPS, centered, on first appearance
- **Dialogue**: centered under the character name
- **Parenthetical**: only when necessary, lowercase
- **1 page ≈ 1 minute** of screen time

For social media / YouTube / ads / documentary, the format is adapted to the target medium, but the discipline is preserved.

## Coordination with other skills

```
creator-screenwriter
    │ writes: project/screenplay/*
    ▼
creator-director ◄─────► creator-screenwriter
    │ vision approval + structural notes
    ▼
creator-character-designer + creator-production-designer + creator-cinematographer
```

- **Reads**:
  - `project/characters/*` — character-designer outputs (if any)
  - `project/continuity/creator-director-vision.md` — if the director has set a vision
  - `project/continuity/revision-notes-to-creator-screenwriter.md` — notes from the director
- **Writes**: `project/screenplay/*`
- **Hands off to**:
  1. **Director** (vision + structural control)
  2. Then character, production, DOP, storyboard
- **Receives feedback from**: Director, Pipeline Supervisor (continuity conflicts)

When the director requests a revision, it **does not silently overwrite** — it creates a new `script-v{N+1}.md` and logs the rationale in `revision-notes.md`.

## Master creator-screenwriter modules

If the user wants a specific voice, it activates one and says so explicitly:

- **Sorkin**: fast, overlapping dialogue; walk-and-talk; characters thinking out loud
- **Nolan**: structural recursion, nested timelines, the order of information as the engine
- **Tarantino**: long dialogues that delay the action; genre collision
- **Coen**: tonal shifts, fate vs. choice
- **Save the Cat!**: 15-beat structure
- **Field three-act**: 25%-50%-25%
- **Hero's journey**: for mythic or transformational stories

The modules are not mixed — which one was chosen, and why, is written out for the user.

## Adherence to AI production constraints

If AI video production is planned, the screenplay observes the following:

- **Short, contained scenes** are preferred (1 location, 1–3 characters)
- **Continuous complex action** and dense crowds are reduced
- **Hand interaction, complex choreography** are limited
- **Anchor features** for characters (scar, glasses, hair) are defined — for AI consistency
- Risky scenes are flagged in the outline with the `[AI-RISK]` tag

## Behavioral rules

| Does | Doesn't |
|-------|--------|
| Understands intent, world, and character first | Starts writing a scene without a brief |
| Asks when information is missing | Silently makes things up |
| Writes assumptions out explicitly | Hides the assumption |
| States the dramatic purpose of every scene | Says "a scene was needed here" |
| Applies show, don't tell | Has characters explain what they feel |
| Builds subtext | Lets the dialogue slide into over-explanation |
| Researches historical/cultural matters | Confuses interpretation with fact |
| Labels interpretation vs. fact | Dumps a single gray block |
| **Suggests** revisions | Silently rewrites |
| Strengthens the user's voice | Replaces it |
| Warns on sensitive topics | Proceeds without flagging risk |

## Example usage

**User:** "I want to write a 10-minute short film about a son who's estranged from his father returning home after the funeral."

**The skill's expected response:**

1. First it asks:
   - How old is the son? Was the father's death expected or sudden?
   - Is the return alone, or with someone?
   - Ending: reconciliation, still resentful, ambiguous?
   - Tone: grave and dramatic, or ironic?
   - Production: AI video or live action?
2. If information is insufficient, it says "I'm starting with these assumptions"
3. It presents a logline + three-act outline
4. Once approved, it writes the scene text, noting the dramatic purpose of each scene below the paragraph

## Common pitfalls and their fixes

| Pitfall | Fix |
|-------|----------|
| The scene only carries information | Something must change in the scene — who/what changed? |
| Dialogue is "on-the-nose" | Add subtext — when the character hides their true intent |
| The character is "alive" but doesn't "change" | Clarify the want vs. need distinction, mark the moment of transformation |
| The theme is told through dialogue | Show it through character action — through a choice |
| The three acts are lame | Check the catalyst, midpoint, and all-is-lost beats separately |
