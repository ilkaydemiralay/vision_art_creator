# Sound & Music Designer — `creator-sound-music-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

The skill that builds the film's **sensory world**. Two integrated disciplines come together:

- **Sound designer**: the sensory reality of spaces, characters, objects, and events —
  ambience, foley, effects, acoustics, sound perspective, and **silence** (as an active
  dramatic tool)
- **Film composer / music supervisor**: main theme, character
  leitmotifs, scene music, rhythm, music entry/exit points

## Philosophy

Sound and music are **not decoration**. Every sound and music decision is tied to the scene's
dramatic purpose, character psychology, visual atmosphere, edit rhythm, and audience
impact. This skill:

- Doesn't say "use sad music" — it designs leitmotifs and plans their evolution
- **Designs silence actively** — not absence, but a dramatic decision
- **Character leitmotifs**: a motif that begins on a flute turns into an epic with strings
  in the finale
- **Copyright-disciplined**: doesn't imitate living artists, "similar but not the same"
- **In sync with edit rhythm**: music entry/exit coordinated with the shot-list edit plan
- **AI sound/music prompt generation**: Suno, Udio, ElevenLabs SFX, Stable Audio, Runway Audio

## What it does

| Output | Content |
|-------|--------|
| **Sound vision** | The film's overall sound-design vision |
| **Music vision** | The film's musical-language manifesto |
| **Main theme** | Main theme design |
| **Character themes** | Per-character leitmotif design |
| **Scene plans** | Scene-by-scene sound + music plan |
| **Ambience / foley / SFX lists** | Inventory lists |
| **Silence plan** | A deliberate map of silence |
| **Music in/out plan** | Music entry and exit points |
| **Sound bridges** | Transition design |
| **AI sound + music prompts** | Tool-specific prompts |
| **Dialogue balance notes** | Dialogue/music balance notes |
| **Final mix notes** | Final mix audit |
| **Continuity report** | Sound continuity check |

## When it kicks in

- A script is in hand, and a sound-design / film-music plan is needed
- Ambience, foley, SFX, or music themes are requested
- AI sound/music prompts are needed
- When the shot-list designer hands off scene sound intent
- When `creator-pipeline-supervisor` delegates the audio stage

## Typical flow

1. **Briefing** + reading all upstream skill outputs
2. **Question round**: genre, register, music density, period, AI tools
3. **Sound vision** + **Music vision**
4. **Main theme + character leitmotifs**
5. **Per-scene plan**: ambient/foley/silence/music for every scene
6. **Silence plan**: a map of deliberate silence
7. **Music entry/exit plan**
8. **AI sound + music prompts**
9. **Final mix audit** (after final cut)

## Silence design

Silence is an **active** design decision. For each silence, the skill asks:

- Will the music cut out here?
- Is the ambience dimmed, or zeroed?
- Will only a breath remain, or a small object sound?
- Does the silence convey loneliness, fear, or hesitation?
- Is it there to unsettle the audience, or to intensify the emotion?
- Which sound enters after the silence?

## Character leitmotif example

```
Karakter: Demir
Müzikal duygu: bastırılmış yas + içsel kararlılık
Ana enstrüman: solo cello (başlangıç) → cello + ney (orta) → cello + yaylı
                grup (final)
Tempo: 60–66 BPM (slow heart)
Ton: minör, kromatik geçişler
Ritim: rubato, neredeyse zamansız
Motifin evrimi:
  - Sahne 1–5: solo cello, kısa 5-notalı motif, sessizlik aralıkları geniş
  - Sahne 6–12: ney ekleniyor — nefes katmanı
  - Sahne 13–18: yaylı grup açılıyor — toplum, geçmiş, anlam
  - Sahne 19 (final): tek cello, ilk motifin yarısı — kırılma
```

## Where it writes its outputs

Under `project/sound/`:

| File | Content |
|-------|--------|
| `sound-vision.md` | Overall sound-design vision |
| `music-vision.md` | Musical-language manifesto |
| `main-theme.md` | Main theme design |
| `character-themes/{slug}.md` | Character leitmotif |
| `scenes/scene-{NN}.md` | Scene sound + music plan |
| `ambience-list.md` | Ambience inventory |
| `foley-list.md` | Foley inventory |
| `special-effects-list.md` | Special SFX |
| `silence-plan.md` | Map of silence |
| `music-entry-exit-plan.md` | Music in/out timing |
| `sound-bridges.md` | Transition design |
| `ai-sound-prompts.md` | AI SFX prompts |
| `ai-music-prompts.md` | AI music prompts |
| `dialogue-balance-notes.md` | Dialogue/music balance |
| `final-mix-notes.md` | Final mix audit |
| `sound-continuity-report.md` | Continuity check |

## AI prompt format

### SFX prompt example

```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```

### Music prompt example

```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```

### Native-language description + English prompt format

```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## Copyright and originality

- Doesn't suggest copying existing compositions
- Doesn't imitate a living artist's style note-for-note
- Works on a "similar but not the same" logic, describing genre + emotion
- In AI music prompts, uses general atmosphere instead of an artist's name

## Coordination with other skills

- **Reads**: all upstream creative outputs + shot-list sound edit notes
- **Writes**: `project/sound/*`
- **Delegates to**: `creator-final-cut-editor` (final cut integration), the AI audio tool
  operator
- **Receives feedback from**: Director, Pipeline Supervisor, Final-cut-editor

## Behavioral rules

| Does | Doesn't |
|-------|--------|
| Ties sound and music to dramatic purpose | Uses them as decoration |
| Designs silence actively | Treats it as absence |
| Syncs leitmotif evolution with the character arc | Repeats one fixed theme |
| Thinks dialogue/music/ambience/silence together | Decides in isolation |
| Copyright-disciplined | Imitates artists |
| Does historical/cultural research and labels it | Presents interpretation as fact |
| Writes tool-fit AI prompts | Dumps generic prompts |
| Preserves sound continuity for a long film | Thinks scene-by-scene and disjointed |
