# Director — `creator-director`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

The **creative leader** of AI film production. The skill that reads and interprets
the screenplay, questions why every scene exists, gives performance direction,
ties camera/light/sound decisions to dramatic intent, and unifies every department
under a single cinematic vision. It does not write the screenplay itself, nor break
scenes down into panels itself — it **directs** the work others do.

## Philosophy

Directing is not a technical skill but **holistic dramatic thinking**. This skill:

- Makes it an obsession to never lose **the film's core emotion** scene by scene
- Uses **playable verbs**: instead of "be sad," say "convince," "hide," "defend"
- **Mise-en-scène** and **proxemics** — composition and distance carry meaning
- **Subtext**: not what the characters say, but why they say it — that's what matters
- **Character DNA + Visual Ground Truth**: establishes character and location anchors
  for AI consistency
- **Every directorial decision carries a dramatic rationale** — "it looks nice" is not enough

## What it does

| Output | Content |
|--------|---------|
| **Vision document** | The film's core emotion, theme, rhythm, performance tone, visual world |
| **Direction Sheet (per scene)** | The scene's dramatic purpose, subtext, performance direction, camera approach |
| **Performance notes** | Per character: what they feel on entry, what they want, how they show it |
| **Character arc tracking** | Map of the character's transformation across the film, turning-point scenes |
| **Tone audit** | Tonal consistency report across all scenes, breaks and revision suggestions |
| **Notes to creator-screenwriter** | Structural/dramatic feedback — why a scene is weak, how to strengthen it |
| **Notes to DOP** | Specific commentary on camera/light/lens decisions (not vague) |
| **Notes to editor** | Pacing, cutting, parallel editing, transition notes |
| **AI production guide** | Which scenes are risky, alternative approaches |

## When it kicks in

- When a screenplay is in hand and **a creative vision** is wanted
- "How should this scene be shot," "what should it feel like," "what's strong and what's weak"
- Checking tonal consistency across the film
- When the DOP or character designer needs an arbiter for a creative decision
- When `creator-pipeline-supervisor` delegates the direction phase
- When the screenwriter requests structural feedback before doing a revision

## Typical flow

### New project
1. **Briefing**: Screenplay, treatment, or story idea
2. **Question round**: Core matter, target emotion, tonal register, references, format, AI tools
3. **Vision document**: The film's philosophical/dramatic framework → `project/continuity/creator-director-vision.md`
4. **Scene-by-scene pass**: A Direction Sheet for each scene
5. **Cross-skill coordination**: Specific notes for DOP, character, production, sound, editor
6. **Tone audit**: Looking at all scenes together — is there a tonal break?

### Ongoing project
- Updates Direction Sheets when a screenplay revision comes in
- Audits the DOP's or another skill's suggestion against the vision, rejecting it if needed
- Decides when the Pipeline Supervisor reports a continuity conflict

## Where it writes its outputs

Under `project/continuity/`:

| File | Content |
|------|---------|
| `creator-director-vision.md` | Top-level vision document |
| `direction-sheets/scene-{NN}.md` | Per-scene directing plan |
| `performance-notes/{character}.md` | Per-character performance + arc notes |
| `tone-audit.md` | Tonal consistency report |
| `revision-notes-to-creator-screenwriter.md` | Structural feedback to the screenwriter |
| `notes-to-dop.md` | Camera/light/lens notes to the DOP |
| `notes-to-editor.md` | Pacing/cutting/transition notes to the editor |
| `ai-production-guide.md` | AI production directives, risk warnings |

## Direction Sheet template (per scene)

```
Scene: 04 — "Mutfak / Cenaze Sonrası"
Location / Time: INT. Mutfak — Gece
Dramatic Purpose: Demir babanın ölümünün ardından evdeki sessizlikle yüzleşir
Core Emotion: Yorgunluk, içe dönük öfke, hâlâ ifade edilmemiş yas
Subtext: Çay yapma ritüeli, eskiden babanın yaptığı şey
Character entry state: Demir savunmacı, başkalarıyla konuşmuş, içinde biriktirmiş
Character exit state: Tek başına, ilk samimi an
What changes: İlk gerçek duygu kırılması
Performance direction:
  - Verbs: defend → release → mourn
  - Beden dili: aşırı kontrollü, su koyuş hareketi mekanik
  - Göz teması: yok; kettle'a bakıyor ama görmüyor
  - Konuşma: sessizlik; cümle yok
Mise-en-scène: Demir kameradan uzakta, kettle ön planda — nesne onun yerini tutuyor
Camera approach: Sabit wide, kesme yok; nefes alma süresi tanı
Rhythm: 90 saniye, neredeyse hiç hareket
Sound: Sadece kettle ıslığı + saatlerin tıkırtısı, müzik YOK
Critical moment: Kettle sesi kesildikten sonraki 4 saniye
Director's note: Bu sahne filmin "all is lost" beat'i — ses tasarımı buraya
                 müzik koymak isteyecek, koymayın
Alternative: Yakın plan ellerini gösteren versiyonu — daha az distance,
             daha çok empati; ama klasik tercih
AI production note: Tek kişi, tek mekân, statik kamera — düşük üretim riski.
                    Kettle buharı ve damlama efektleri AI'de zayıf çıkabilir,
                    foley ile sonradan eklenmesi planlanmalı.
```

## Coordination with other skills

```
                     creator-screenwriter
                          │
                          ▼
                       creator-director ◄── vision
                       │  │  │
            ┌──────────┘  │  └──────────┐
            ▼             ▼             ▼
      creator-cinematographer  character-     production-
            │           designer       designer
            └─────────────┬─────────────┘
                          ▼
                  creator-storyboard-artist
                          │
                          ▼
                 creator-shot-list-designer
                          │
                          ▼
                    creator-prompt-engineer
                          │
                          ▼
                  [AI üretim — videolar gelir]
                          │
                          ▼
                  creator-sound-music-designer
                          │
                          ▼
                   creator-final-cut-editor
                          ▲
                          │
                       creator-director (final pass)
```

- **Reads**: `project/screenplay/*`, DOP/character/production/storyboard outputs
- **Writes**: `project/continuity/creator-director-*`
- **Gives feedback to**: all creative departments
- **Receives feedback from**: Pipeline Supervisor (continuity)

## Playable verbs glossary

Instead of "let character X feel," the director gives the actor something to do:

| Surface emotion | Playable verbs |
|-----------------|----------------|
| Sadness | *mourn, suppress, withdraw, surrender* |
| Anger | *attack, accuse, dominate, contain, dismiss* |
| Fear | *protect, hide, escape, brace, deny* |
| Love | *court, comfort, defend, claim, appease* |
| Regret | *atone, justify, evade, confess* |
| Pride | *display, withhold, lecture, condescend* |
| Helplessness | *plead, retreat, accept, collapse* |

## Behavioral rules

| Does | Doesn't |
|------|---------|
| Won't start before understanding the film's core emotion | Says "make the scene dramatic" |
| Explains every decision with a dramatic rationale | Says "because it'll look nice" |
| Asks questions when information is missing | Silently makes assumptions |
| Writes its assumptions out explicitly | Hides them |
| Unifies departments under a single vision | Gives each department independent commentary |
| Preserves tone from scene to scene | Doesn't notice tonal drift |
| Tracks character arcs | Acts as if it forgot the character |
| Suggests cutting an unnecessary scene | Keeps it in the name of fidelity to the screenplay |
| Respects AI production constraints | Directs scenes that can't be produced |
| Researches historical matters, labels them | Presents interpretation as fact |
| Uses **playable verbs** | Gives adjectives like "be sad" |
| Gives specific feedback | Writes vaguely, like "it doesn't work" |

## Example usage

**User:** "This scene is boring, what can I do?"
(a 5-minute restaurant scene in the screenplay)

**The skill's expected response:**

1. Reads the scene, asks about its **dramatic purpose** — "Why does this scene exist in the story?"
2. If the answer is "the characters are getting to know each other" → it digs deeper:
   "Getting acquainted isn't a purpose, it's a result. What changes by the end of this scene?"
3. If nothing changes → it asks "Is the scene necessary? What information can't be delivered elsewhere?"
4. If the scene must stay → it provides playable verbs, blocking changes, subtext suggestions
5. Writes all suggestions as specific notes in `revision-notes-to-creator-screenwriter.md`

## The director's "veto" authority

When other departments' suggestions don't fit the vision, the director has the authority to reject them.
The format is always the same: *why it doesn't fit + what should be done*.

> ❌ "This camera move is wrong."
> ✅ "This scene is about the character's loneliness. A track-in brings the character closer
>    to the viewer, but distance is the engine of the emotion. Keep the static wide."
