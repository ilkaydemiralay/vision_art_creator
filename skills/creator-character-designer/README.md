# Character Designer — `creator-character-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

A skill that lifts a character beyond the **name + age + appearance** triad and
designs them as a **coherent being**. It produces dramatic function, psychology,
biography, body language, costume, props, casting profile, and a **FACS Action
Unit-coded expression library**. It establishes the "Character DNA" anchors that
preserve character consistency across long-form AI film production.

## Philosophy

A character is not generated at random — they derive from the script's needs, the
director's vision, and the DOP's visual world. This skill:

- **Every character is an answer to a dramatic question** — otherwise it suggests cutting the character
- Mandatorily establishes the **Want / Need / Fear / Wound** quartet for every main character
- **FACS Action Units**: instead of saying "sad," it says AU1+AU4+AU15 —
  AI models and animators interpret anatomical code more consistently
- **Character DNA**: defines locked anchor traits for AI consistency
- **Visual distinction audit**: when there are multiple characters, it audits silhouette, color, and energy distinctions

## What it does

| Output | Content |
|--------|---------|
| **Character sheet** | Character file — psychology, costume, props, FACS, AI prompt |
| **Costume bible** | Costume variations and continuity across the whole film |
| **Props list** | The character's personal items and their dramatic uses |
| **FACS expression library** | 3–5 signature expressions per character, AU-coded |
| **Casting brief** | The profile sought in an actor (no names suggested, traits defined) |
| **AI prompts** | Base prompt + scene variations for a consistent character reference |
| **Arc tracker** | Character transformation coordinated with the director's arc tracking |
| **Continuity notes** | Scene-by-scene costume/prop continuity |

## When it kicks in

- The script is in hand and characters need to be developed
- "Prepare a character sheet," "design a costume," "draft a casting profile"
- A consistent character reference is needed for AI film
- When the director or `creator-pipeline-supervisor` delegates the character stage
- When the visual distinction of existing characters is in question

## Using FACS — why and how

**The Facial Action Coding System (Ekman & Friesen, 1978)** is the anatomical
coding of facial muscles. An Action Unit (AU) = a specific muscle movement.

### Why does this skill use it?

- **AI generators** interpret abstract inputs like "happy face" inconsistently;
  "AU6 + AU12 (Duchenne smile)" yields a more reliable result
- **Animator/VFX teams** share a single reference set via AU codes
- **A character's signature expression** can be filed — for example, "Demir
  carries his suppressed grief with AU4 + AU17 (brow furrowed, chin raised, no AU15)"

### Common AU combinations

| Expression | AUs |
|------------|-----|
| Duchenne smile (genuine happiness) | AU6 + AU12 |
| Polite smile (fake/social) | AU12 alone |
| Sadness | AU1 + AU4 + AU15 |
| Anger | AU4 + AU5 + AU7 + AU23 |
| Fear | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26 |
| Disgust | AU9 + AU15 + AU16 |
| Surprise | AU1 + AU2 + AU5B + AU26 |
| Contempt (asymmetric) | AU12 (one-sided) + AU14 |
| Suppressed grief | AU4 + AU17 (no AU15) |
| Tense calm | AU7 + AU23 + AU24 |

## Character sheet template (summary)

```
Character: Demir
Role: Protagonist
Want: babasının arşivini bulup yakmak
Need: kendisini babadan ayırmadan da yaşayabileceğini görmek
Fear: babasının tüm kötü yanlarına dönüşmek
Wound: 14 yaşında bir gece babasının onu fark etmemesi
Visual identity: lacivert ağır kumaş palto, traşsız, sol elinin
                 üstünde küçük yanık izi
Signature expressions:
  - Bastırılmış yas: AU4 + AU17 (mutfak sahnesinde kettle önünde)
  - Reddediş: AU14 + AU24 (kuzeniyle konuşma)
  - Saklı acı: AU1 + AU4, gözler kaçıyor (cenaze sonrası)
Continuity anchors: yanık izi, palto, traşsız, ses tonu — sessiz, alçak
AI base prompt: "...same character across all scenes..."
```

## Where it writes its outputs

Under `project/characters/{character-slug}/`:

| File | Content |
|------|---------|
| `character-sheet.md` | The canonical character file |
| `costume-bible.md` | All costume variations + continuity |
| `props.md` | The character's items, dramatic use |
| `facs-expressions.md` | Signature expression library, AU-coded |
| `casting-brief.md` | Actor profile / basis for an AI face prompt |
| `ai-prompts.md` | Base prompt + scene-by-scene variation |
| `arc-tracker.md` | Sync with the director's arc tracking |
| `continuity-notes.md` | Scene-by-scene costume/prop continuity |

There is also a `cast-list.md` in the parent directory — a list summarizing all characters.

## Visual distinction audit

When there is more than one character, the skill runs these checks:

- Silhouette distinction (height, posture, costume form)
- Color-world distinction (or deliberate contrast)
- Energy register distinction
- Speech pattern distinction
- Screen presence distinction (foreground / background type)

If two characters "blur together," it reports it and suggests a revision.

## AI consistency (Character DNA)

To generate the same character across 50 scenes with the same face/costume:

1. **Base prompt** — key traits (face shape, hair, distinguishing mark) held fixed
2. **Anchor descriptors** — 2–3 of them recur in every scene prompt
3. **Expression via FACS** — AU-coded, not adjectives
4. **Early character sheet production** — front/side/back/close reference images
5. **Reference in the scene prompt**: "consistent with `characters/demir/sheet.png`"

## Coordination with other skills

- **Reads**:
  - `project/screenplay/character-brief.md`
  - `project/continuity/creator-director-vision.md`
  - `project/continuity/performance-notes/*`
  - `project/production-design/cinematography/visual-language.md`
  - `project/production-design/world-bible.md`
- **Writes**: `project/characters/*`
- **Delegates to**: Prompt engineer, storyboard, DOP (palette coordination)
- **Receives feedback from**: Director, Pipeline Supervisor

## Costume design approach

Costume tells the character — it isn't merely "what they wear":

- Main piece + its function
- Fabric: heavy, soft, stiff, fibrous
- Color: harmony/contrast with the palette
- Wear / newness / damage / signs of repair
- Period accuracy
- Relationship to the character's state of mind
- Effect on mobility
- Interaction with light (matte, glossy, transparent, dust-catching)

For each main scene, a costume continuity note: does it change within the scene,
does it change between scenes, why?

## Props approach

Props are storytelling tools — not decorative:

- Name + function
- Relationship to the character
- Appearance, material, color, condition
- Meaning to the character (memento, identity, relationship)
- Dramatic use (foreshadowing, payoff, reveal)
- How the camera sees it (close, detail, passing)
- Continuity (where it is in each scene)

Character-prop / location-prop ownership is clarified and coordinated with
**creator-production-designer**.

## Rules of behavior

| Does | Doesn't |
|------|---------|
| Generates a character with a dramatic rationale | Says "we need one more character" |
| Ties every visual choice to arc / function / theme | Makes isolated aesthetic choices |
| Asks questions when information is missing | Quietly makes things up |
| Researches cultural detail | Presents a guess as fact |
| Defines expressions with FACS AU codes | Uses adjectives like "sad" |
| Runs a visual distinction audit | Lets two characters blur together |
| Embeds continuity anchors into AI prompts | Describes from scratch in every scene |
| Clarifies character-prop ownership | Overlaps with the production designer |
| Delivers structured, downstream-readable files | Dumps a single block of text |
