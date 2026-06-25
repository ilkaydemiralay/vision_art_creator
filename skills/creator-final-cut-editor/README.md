# Final Cut Editor — `creator-final-cut-editor`

**English** · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

The skill that turns AI production outputs into a **finished film**. The end of
pre-production / the start of post-production. Once material has been produced,
it manages the rough cut → fine cut → final cut → delivery flow; it triages AI
generation errors, audits continuity, checks audio/music integration, and
produces delivery-ready masters.

**Difference from shot-list-designer**: the shot list designs editorial intent
BEFORE the shoot; creator-final-cut-editor EXECUTES the cut on the actual
material.

## Philosophy

The final cut is **not a technical sequencing** — it is the construction of
cinematic wholeness. This skill:

- **A dramatic rationale for every cut** — "looks good" isn't enough
- **Multi-scale rhythm**: within a shot, within a scene, across the whole film
- **AI error triage**: which error breaks the cut, which can be hidden, which can stay
- **Audience experience design**: what the viewer feels, learns, and takes away
- **Delivery discipline**: YouTube ≠ festival ≠ Instagram ≠ archive
- **Versioning**: manages rough/fine/final + festival/social/trailer cuts separately

## What it does

| Output | Content |
|-------|---------|
| **Material evaluation** | Per shot: usable / revise / re-generate / cut |
| **Rough cut plan** | First rough sequencing, list of missing material |
| **Fine cut plan** | Cut points, shot durations, silence |
| **Final cut plan** | Final readiness + delivery checklist |
| **Per-scene final-check** | Detailed scene-by-scene audit |
| **Whole-film report** | Final cut report for the entire film |
| **AI error report** | Generation errors + severity classification |
| **Audio integration audit** | Feedback to the sound designer |
| **Color grade notes** | Color correction directives |
| **EDL** | NLE-readable Edit Decision List |
| **Version manifest** | Festival/social/trailer cut versions |
| **Delivery specs** | Platform-specific export settings |
| **Trailer plan** | Teaser/trailer cut plan |

## When it kicks in

- AI video shots have been produced, editing is starting
- Rough/fine/final cut planning is required
- An AI error audit is requested
- Multiple cuts (festival, social, trailer) will be produced
- Delivery export preparation
- When `creator-pipeline-supervisor` delegates the post-production phase

## Typical flow

1. **Material evaluation** — each shot is categorized (✅🟡🟠🔴)
2. **Rough cut v01** — story order, basic dramatic sequence
3. **Fine cut v01** — cut points, rhythm, silence
4. **Sound integration audit** — feedback to creator-sound-music-designer
5. **AI error report** — critical/medium/minor classification
6. **Color grade notes** — if needed
7. **Subtitle / titles / graphics check**
8. **Final cut v01** — readiness checklist
9. **Delivery export** — platform-specific version

## AI error triage matrix

| Severity | Definition | Action |
|----------|------------|--------|
| 🔴 Critical | Cannot make it into the final cut | Re-generate (flag to creator-prompt-engineer) |
| 🟡 Medium | Hidden via trim/crop/color/sound | Editorial workaround |
| ✅ Minor | Doesn't disturb the viewer | Can stay |

Checked: face distortion, hand/finger errors, lip-sync, costume changes,
loss of accessories, location drift, light-direction inconsistency, artificial
camera movement, flicker, warping, morphing, melting objects, background
breakdown, anachronism, plastic look.

## Per-scene final-check format

```
Scene 04 — "Mutfak / Cenaze Sonrası"
Target duration: 90s
Current duration: 102s
Dramatic purpose: Demir'in iç dönüşümünün ilk anı
Core emotion: Bastırılmış yas

Shots used: 04.01, 04.02, 04.03, 04.05, 04.06
Shots cut: 04.04 (gereksiz reaction, ritim düşürüyor)
Shots shortened: 04.05 (8s → 5s — wide hold gereksiz uzun)
Shots lengthened: 04.02 (4s → 6s — kettle hold dramatik nefes)
Cut points:
  - 04.01 → 04.02: sound bridge (kettle ıslığı önce)
  - 04.02 → 04.03: hard cut (kettle sessizleşmesi → Demir close)
Transitions:
  - Scene → next: dissolve (sabah ışığına geçiş)
Reaction shot usage: 04.03 (Demir close) — yas kırılma anı
Silence usage: 04.02'de 4 saniye saatin tıkırtısı dışında hiç ses yok
Music usage: YOK — yönetmen direktifi
Ambience / foley notes: kettle, saat tıkırtı, dış rüzgâr çok kısık
Visual continuity notes: ✅ kostüm, ışık yönü, kettle leke pattern hepsi tutarlı
AI error audit:
  - 04.02 kettle buharı warping (🟡 orta) — sound design ile maskelenecek
  - 04.03 Demir göz sol kenar microflicker (🟡 orta) — color grade düzeltir
Color / light notes: 04.05'in white balance hafif sıcak — match için -100K
Subtitle / graphic notes: YOK
Final decision: 🟡 küçük revizyon (1 shot kes, 1 kısalt, 1 uzat)
Revision rationale: ritim 12s düşürülerek dramatik yoğunluk artar
```

## Where it writes its outputs

Under `project/cuts/`:

| File | Content |
|-------|---------|
| `material-evaluation.md` | Each shot's category |
| `rough-cut/v{NN}.md` | Rough cut plan |
| `fine-cut/v{NN}.md` | Fine cut plan |
| `final-cut/v{NN}.md` | Final cut plan + readiness |
| `scene-{NN}/final-check.md` | Scene-by-scene detail |
| `final-cut-report.md` | Whole-film audit |
| `ai-error-report.md` | AI error report |
| `audio-integration-report.md` | Audio integration audit |
| `color-grade-notes.md` | Color correction |
| `subtitle-titles-graphics.md` | Subtitles/titles |
| `transitions.md` | Transition decisions |
| `edit-decision-list.md` | EDL |
| `versions/{cut-name}.md` | Version manifest |
| `delivery/{platform}.md` | Platform export specs |
| `trailer-plan.md` | Trailer/teaser plan |

## Version management

| Version | Duration | Goal |
|----------|----------|------|
| Rough Cut v01 | ~115% target | First story-flow test |
| Rough Cut v02 | ~108% | Integration of missing pieces |
| Fine Cut | ~102% | Lock rhythm and emotion |
| Director's Cut | 100% target | Full director approval |
| Final Cut | 100% | Delivery-ready |
| Festival Cut | 100% | Festival format |
| YouTube Cut | 100% or shortened | YouTube algorithm |
| Trailer Cut | 30s–2 min | Marketing |
| Social Cut | 9:16 short | Reels, TikTok |

For each version: name, duration, changes, removed/added scenes, audio
changes, revision rationale, approval status.

## Example delivery specs

| Platform | Aspect | Resolution | FPS | Audio |
|----------|--------|------------|-----|-------|
| YouTube 16:9 master | 16:9 | 3840×2160 (4K) or 1920×1080 | 24/25 | AAC 320kbps stereo |
| Festival master | 2.39:1 or 16:9 | 4K | 24 | WAV 48kHz 24-bit stereo + 5.1 |
| Instagram Reels | 9:16 | 1080×1920 | 30 | AAC stereo |
| TikTok | 9:16 | 1080×1920 | 30 | AAC stereo |
| Web compressed | 16:9 | 1920×1080 | 24/25 | AAC 192kbps |
| Archive master | original | highest | original | WAV master |

## Trailer cut logic

A trailer is **not a miniature of the film** — it has its own editorial logic:

- The 6–10 strongest visuals
- Spoiler exclusion list
- Hook → background → threat/conflict → climax teaser → darkness → tagline
- Music build (different from the film, more direct)
- Fast cutting rhythm (different from the film)
- Compressed character introductions
- A final punch image — **outside** the film's context
- Short social media 9:16 version

## Coordination with other skills

- **Reads**: all upstream creative outputs + shot-list `final-editor-notes.md`
- **Writes**: `project/cuts/*`
- **Gives feedback to**:
  - **creator-sound-music-designer**: audio fix requests
  - **creator-prompt-engineer**: regeneration requests
  - **creator-pipeline-supervisor**: continuity escalation
- **Gets approval from**: Director (final approval), Pipeline Supervisor

## Behavior rules

| Does | Doesn't |
|-------|---------|
| A dramatic rationale for every cut | Do mere technical sequencing |
| Clearly flags unnecessary scenes/shots | Keep them for the sake of loyalty |
| Evaluates AI errors from viewer experience | Abstract/technical perfectionism |
| Considers dialogue + music + ambience + silence together | Audit in isolation |
| Faithful to the director's vision | Clash with editorial ego |
| Disciplined about target duration | Overrun the limit |
| Asks the user before a major change | Cut silently |
| Tracks multiple versions | Mix them in a single file |
| Delivers platform-fit delivery | Hand over a single master |
| Won't say "done" without a delivery readiness checklist | Declare it complete early |
