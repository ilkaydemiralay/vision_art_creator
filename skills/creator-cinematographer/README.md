# Cinematographer — `creator-cinematographer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

The skill that translates the screenplay and the director's vision into a
**cinematic visual language**. Light, camera, lens, framing, color, atmosphere,
movement — every visual decision is tied to a dramatic justification. "It looks
good" is not enough; it works in the logic of **motivated lighting**,
**chiaroscuro**, **depth as psychology**, and **camera as character**.

## Philosophy

A DOP is not just someone who produces "nice images." A DOP is an **engineer of
visual meaning**. This skill:

- **Motivated lighting**: every light source has a reason in the world of the scene
- **Chiaroscuro**: the contrast of light and shadow carries meaning, not just aesthetics
- **Depth of field**: depth of field is a psychological choice
- **Negative space**: emptiness = loneliness / isolation
- **Camera as character**: is the camera an observer, a follower, or an accuser?
- Someone who **knows** the constraints of AI production and flags risks

## What it does

| Output | Content |
|-------|--------|
| **Visual language doc** | Defines the film's visual concept with references |
| **Lighting bible** | A consistent lighting approach across the whole film |
| **Color script** | The film's color progression (scene by scene) |
| **Lens list** | Lens choices by scene type, with justifications |
| **Per-scene plan** | Scene-level light + camera + lens + color plan |
| **Moodboard** | Reference image descriptions, with sources |
| **AI cinema prompts** | Translates cinematography knowledge into AI prompts |
| **DOP notes to/from creator-director** | Two-way communication with the director |

## When it kicks in

- The screenplay + director's vision exist, and visual design is needed
- "How should this scene be lit / which lens / which framing"
- A color palette or color script is requested
- Cinematic prompt translation for AI production
- When `creator-pipeline-supervisor` delegates the DOP phase
- When the director wants specific feedback on camera/lighting

## Typical flow

1. **Briefing** and reading of `creator-director-vision.md`
2. **Question round**: genre, tone, references, period, AI tools
3. **Visual language**: master palette, reference films, visual manifesto
4. **Lighting bible**: the film's overall lighting approach
5. **Color script**: color transformation aligned with the dramatic arc
6. **Per-scene**: scene-by-scene plan
7. **AI prompt hand-off**: structural cinema knowledge to creator-prompt-engineer

## Where it writes its outputs

Under `project/production-design/cinematography/`:

| File | Content |
|-------|--------|
| `visual-language.md` | The film's overall visual manifesto |
| `lighting-bible.md` | Master lighting approach |
| `color-script.md` | Scene-by-scene color progression |
| `lens-list.md` | Lens choices and justification |
| `scene-{NN}.md` | Per-scene plan (light + camera + lens + color) |
| `moodboard.md` | Reference image descriptions |
| `notes-to-creator-director.md` | Questions/suggestions to the director |
| `ai-production-cinema-notes.md` | Cinema guide for AI production |

## Lens psychology (summary)

| Focal | Effect | Use |
|-------|------|----------|
| 14–24mm wide | Distortion, claustrophobia | Dream/nightmare, aggressive proximity |
| 28–35mm | Documentary feel | Natural, observational |
| 40–50mm | Eye level | Neutral, intimate dialogue |
| 75–100mm | Compression, isolation | Beauty, longing, surveillance |
| 135mm+ | Strong compression | Distance, dread |
| Anamorphic | Wide aspect, oval bokeh | Epic, cinematic |
| Macro | Extreme detail | Object meaning, sensory |

## Lighting language (summary)

- **Key**: the main source — where does it come from in the world of the scene?
- **Fill**: shadow modulation, ratio choice
- **Backlight**: separation from the background, rim halo
- **Practical**: lamp, candle, fire, screen — the real sources in the scene
- **Hard vs. soft**: hardness reveals texture, sets intent
- **Color temp**: warm (3200K, intimate/memory), cool (5600K+, distance/clinical), mixed (tension)
- **Contrast**: high (drama, noir), low (documentary, melancholy, dawn)

## Coordination with other skills

```
creator-director-vision ──► creator-cinematographer
                         │
                         ├── coordinate ─► creator-production-designer
                         ├── coordinate ─► creator-character-designer
                         │
                         ▼
                  creator-prompt-engineer
                  creator-storyboard-artist
                  creator-shot-list-designer
```

- **Reads**: `project/screenplay/*`, `creator-director-vision.md`, `notes-to-dop.md`,
  production-design outputs, character color palette
- **Writes**: `project/production-design/cinematography/*`
- **Hands off to**: Prompt engineer, storyboard, shot-list designer
- **Receives feedback from**: Director, Pipeline Supervisor

## Cinematic prompt format for AI production

When translating cinematography into an AI prompt, the following are always included:

- Shot scale + angle
- Lens (focal + DoF effect)
- Light direction, quality, color temperature
- Color palette and mood
- Atmosphere (fog, smoke, rain, dust)
- Location details (period, texture, material)
- Character position and action
- Aspect ratio (2.39:1, 1.85:1, 16:9, 9:16)
- Style reference (film title, photographer, period)
- Negative prompt (exclusions)

This structure is ready for hand-off to the `creator-prompt-engineer` skill.

## Rules of behavior

| Does | Doesn't |
|-------|--------|
| Gives every light a dramatic justification | Says "make it look good" |
| Applies motivated lighting | Places light with an unclear source |
| Explains lens psychology | Picks a lens for aesthetic reasons |
| Coordinates the color palette with director/production/character | Decides in isolation |
| Flags AI risks | Plans a scene that can't be produced |
| Offers a low-budget alternative | Only writes the ideal version |
| Researches and labels the historical period | Presents interpretation as fact |
| Sends questions via `notes-to-creator-director.md` before the shoot | Proceeds silently |
