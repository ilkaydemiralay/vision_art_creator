# Storyboard Artist — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

A skill that turns a written screenplay into **readable visual storytelling**. By
minimizing panel count, it ensures every panel exists for a dramatic reason.
It captures a scene's critical moments, preserves screen direction, tracks eyeline
continuity, and hands off cleanly to AI image/video prompts.

## Philosophy

A storyboard is not "scene drawing" — it is a **visual storytelling system**. This skill:

- **Panel economy**: few panels + sharp choices — not many panels + weak decisions
- **Screen direction (180°)** and **eyeline continuity**: spatial consistency across cuts
- **Graphic dynamics**: where does the eye land? what is the focus?
- **Continuity awareness**: costume, location, light direction, screen direction, movement
- **Locked anchors**: character DNA + location master reference in every panel
- **Producibility**: knows AI production constraints and flags risky scenes

## What it does

| Output | Content |
|--------|---------|
| **Per-scene storyboard** | Scene-by-scene panel list (all panel data) |
| **Per-panel sheets** | Detailed single-panel file for complex scenes |
| **AI image prompts** | Production-ready prompt per panel |
| **AI video prompts** | Video prompt for moving panels |
| **Continuity log** | Flags for costume/location/direction risks |
| **Animatic plan** | Plans the animatic ordering of all scenes |
| **Director / DOP notes** | Brief visual/technical notes for the director and DOP |
| **Handoff to shot-list** | Panel data in creator-shot-list-designer format |

## When it kicks in

- A screenplay is in hand and a visual breakdown is wanted
- When the director wants a scene visualized in advance
- When a visual concept is needed before the DOP's lens/light decisions
- When storyboard logic is wanted before AI prompt generation
- When `creator-pipeline-supervisor` delegates the storyboard stage

## Panel content (canonical fields)

Every panel records these fields:

```
Scene 04 — Panel 04.03
Shot type: medium close
Camera angle: eye level
Frame: Demir merkez-sağ; kettle ön plan-sol; arka plan
       dolap soft-focus; sağ kenar negatif alan açık
Lens feeling: 50mm (eye-equivalent, samimi)
Character position: Demir sandalyede, omuzlar düşmüş, eller masada
Character movement: yok — duraksama
Camera movement: static
Setting / dressing: kireçli mutfak — pencere doğu, kettle ateşte
Light / atmosphere: pencereden yumuşak gri sabah, mum yok
Emotional emphasis: bastırılmış yas; ilk gerçek duygu kırılması
Dialogue / action note: sessizlik; kettle ıslığı
Dramatic justification: Demir'in iç çatışmasını yüzeye getiren ilk an
Transition to next panel: J-cut — kettle sesi devam ederken Panel 4.04 başlar
AI image prompt: [tam prompt]
AI video prompt: [tam prompt, 6s]
Continuity note: palto sahne başında; ceket askıda; kettle aktif
```

## Where it writes its outputs

Under `project/storyboards/`:

| File | Content |
|------|---------|
| `scene-{NN}/storyboard.md` | Scene-based panel list (canonical) |
| `scene-{NN}/panel-{PP}.md` | Detailed single panel (in complex scenes) |
| `scene-{NN}/prompts.md` | Per-panel AI prompts (image + video) |
| `scene-{NN}/continuity.md` | Continuity flags |
| `animatic-plan.md` | Animatic ordering notes for the whole film |
| `notes-to-creator-director.md` | Questions/warnings for the director |
| `handoff-to-shot-list.md` | Formatted panel data for the shot-list designer |

## Shot type glossary (with dramatic equivalent)

| Type | Dramatic use |
|------|--------------|
| Establishing | Positions the viewer in the space |
| Master | Scene geometry, fallback |
| Wide/Full | Character–environment relationship |
| Medium | Neutral dialogue |
| Close | Inner conflict, intimate emotion |
| Extreme close | Subjective intensity |
| Insert | Object emphasis |
| Cutaway | Parallel/external information |
| Reaction | Reaction over action |
| OTS | Dialogue perspective |
| POV | Character subjectivity |
| 2-shot / group | Relationship geometry |
| Silhouette | Anonymity, mystery |
| Negative-space frame | Isolation, smallness |
| Symmetrical | Power, formality, unsettling stillness |
| Tracking | Continuous following |
| Static | Observation, the meaning of silence |

"Use a close-up" is not enough — **why** a close-up is needed is the question.

## Continuity audit

Tracking from panel to panel, scene to scene:

- Costume
- Hair/makeup/accessories
- Location identity (with locked anchor)
- Light direction
- Day/night
- Screen direction (180° rule)
- Spatial logic of the characters
- Action flow
- Prop position

When a risk is detected, it is written explicitly in the panel's `continuity note` field.

## Coordination with other skills

- **Reads**: screenplay, director's vision + direction sheets, DOP per-scene plan,
  character DNA + FACS, location anchors
- **Writes**: `project/storyboards/*`
- **Delegates**:
  - `creator-shot-list-designer` (panel → shot list)
  - `creator-prompt-engineer` (panel prompt → tool-specific optimization)
- **Receives feedback from**: Director, Pipeline Supervisor

## AI-production-focused solutions

- Breaks complex scenes into simple panels
- Clarifies visual focus in multi-character scenes
- Simplifies movements the AI would struggle with
- Uses fixed anchors for the same location/character
- Offers a safe static-shot alternative instead of camera movement
- Suggests selective framing in crowded scenes
- Suggests rhythmic cuts instead of fast action

## Behavior rules

| Does | Doesn't |
|------|---------|
| Writes a dramatic justification for every panel | Fills in "another panel" for its own sake |
| Few panels + sharp choices | Many panels + weak decisions |
| Unifies screenwriter + director + DOP + character + production | Silently overrides upstream |
| Preserves screen direction and eyeline | Mixes up direction across a cut |
| Puts locked anchors into every prompt | Re-describes from scratch in every panel |
| Breaks a complex scene into panels | Loads it onto a single overloaded frame |
| AI risk flag + safe alternative | Suggests an unproducible movement |
| Structured, downstream-readable output | Dumps a single block of text |
