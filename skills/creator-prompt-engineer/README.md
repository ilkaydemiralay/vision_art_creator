# Prompt Engineer — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

The **translation layer** between the creative pipeline and the AI generators.
It turns the decisions produced by the screenwriter, director, DOP, character,
production, storyboard, and shot-list skills into **truly producible, consistent**
prompts. It optimizes per tool (Midjourney ≠ Sora ≠ Stable Diffusion), embeds
locked anchors into every prompt, and produces safe alternatives for risky scenes.

## Philosophy

The prompt engineer **does not invent visuals** — it encodes upstream decisions.
This skill:

- **Locked anchors**: character DNA + location master reference + style block —
  even after 50 prompts the same character comes out with the same face
- **Tool fitness**: every AI tool has its own prompt language
- **Producibility audit**: this scene will defeat the generator — propose an alternative
- **Consistency discipline**: for a long film, prompts are a system, not isolated
- **FACS expression coding**: AU1 + AU4 + AU15 instead of "sad" — more consistent results
- **Never silently overrides upstream**: flags it and asks back when needed

## What it produces

| Output | Content |
|--------|---------|
| **Character prompts** | Locked DNA + scene-by-scene variation |
| **Location prompts** | Master reference + day/night/weather variation |
| **Style anchors** | Film-wide visual/technical block |
| **Negative prompts** | Category-based negative prompt bank |
| **Panel prompts** | Image-generation prompt from a storyboard panel |
| **Shot prompts** | AI video-generation prompt from the shot list |
| **Character sheets** | Front/side/back/close reference generation |
| **Producibility risk report** | Scene/shot-level risk + safe alternative |
| **Tool guide** | Tool-specific notes for the operator |

## When it kicks in

- AI image/video prompts are needed before production
- An anchor system must be set up for character/location consistency
- A storyboard or shot-list output is to be turned into tool prompts
- An existing prompt is risky — a safe alternative is wanted
- When `creator-pipeline-supervisor` delegates the prompt stage

## Tool optimization guide (summary)

### Midjourney
- `--ar`, `--style raw`, `--s` parameters
- `--cref` and `--cw` for character reference
- `--sref` for style reference
- Compact phrasing — adjective stacking weakens the signal

### DALL·E
- Natural language > tag dump
- Spell out spatial relationships
- Avoid generating in-image text

### Stable Diffusion (SDXL / SD3)
- Positive + negative separated
- LoRA / reference / seed notes for character consistency
- Important terms up front (token weight)

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- A single main camera move
- Controlled number of characters
- Clear opening + closing frame
- Short duration (3–10s typical)
- Tool-specific limits:
  - Sora 2: ~20s
  - Kling 3.0: subject binding for consistency
  - Veo: strong motion fidelity
  - Runway Gen-3/4: motion makes sense, lip sync weak

## Locked anchor system (for a long film)

### Character DNA block

Copied **verbatim** from `project/characters/{slug}/ai-prompts.md`:

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

Verbatim from `project/production-design/locations/{slug}/master-reference.md`:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall, lime-washed walls with
soot stain along the lower meter, raw wooden floor, wooden table center,
copper-lidded cabinet on the north wall, copper kettle on a small iron stove
```

### Style block

```
{style}: realistic cinematic period drama, soft natural light, 35mm film
feeling, subtle film grain, muted earth-tone palette, 2.39:1 aspect ratio,
no modern objects
```

These blocks are **repeated verbatim in every prompt** of that scene/character/location.
This discipline is the engine of consistency.

## Negative prompt categories

| Problem | Negative term |
|---------|--------------|
| Face distortion | distorted face, malformed face, asymmetric eyes, blurred features |
| Hand error | extra fingers, missing fingers, fused fingers, deformed hand |
| Anachronism | modern clothes, modern tech, plastic, neon, smartphone |
| AI artifact | warping, morphing, flickering, jittery motion |
| Quality | low quality, low resolution, jpeg artifacts, oversaturated |
| Text | unwanted text, watermark, signature, logo |
| Composition | extra characters, cropped subject, duplicate subject |
| Camera | unintended shake, fisheye distortion |

Some tools ignore the negative prompt — in that case write it inside the
positive prompt as an *"avoid: ..."* hint.

## AI video producibility audit

Checks before a video prompt is issued:

- Too much action in a single shot?
- Too many characters?
- Is the camera move complex?
- Is hand/finger/face detail risky?
- Can costume/prop consistency be maintained?
- Is the location too crowded?
- Are light and time consistent?
- Should the scene be split into parts instead of a single prompt?
- Is lip sync needed? (flag it)
- Is the prompt needlessly abstract?

If there is risk it gives a **safe simplified alternative**.

## Variation generation

Focused variations for the same scene:

- Realistic
- More cinematic
- Darker
- Low-budget / simpler
- Wide alt.
- Close alt.
- Night
- Daylight
- AI-safe
- Poster / key art

The **purpose of each variation is written down** — why and when it is used.

## Where it writes its outputs

Under `project/prompts/`:

| File | Content |
|------|---------|
| `character-prompts/{slug}.md` | Locked DNA + scene variations |
| `location-prompts/{slug}.md` | Master anchor + variations |
| `style-anchors.md` | Film-wide style block(s) |
| `negative-prompts.md` | Negative prompt bank |
| `scene-{NN}/panel-{PP}.md` | Panel image prompts |
| `scene-{NN}/shot-{SS}.md` | Shot video prompts |
| `character-sheets/{slug}.md` | Front/side/back/close sheet generation prompts |
| `prompt-system.md` | Anchor system documentation |
| `producibility-risk-report.md` | Risk flags + safe alternative |
| `tool-guide.md` | Tool-specific operator notes |

## Bilingual prompt format

When the user wants a native-language explanation + an English prompt:

```
Türkçe Açıklama:
Bu prompt karakterin yalnızlığını vurgulayan geniş bir dış mekân planı
üretmek için hazırlanmıştır.

English Prompt:
A lonely middle-aged man standing at the edge of a foggy rural road at
dawn, wide cinematic shot, 35mm lens feeling, cold blue morning light,
worn dark traditional clothing, quiet melancholic mood, realistic period
drama, subtle film grain, 16:9 aspect ratio.
```

## Coordination with other skills

- **Reads**: all upstream creative outputs
- **Writes**: `project/prompts/*`
- **Delegates**:
  - to the human operator who will run the AI tools
  - feedback to the **storyboard artist** or **shot-list designer** if the
    producibility audit requires changing upstream
- **Receives feedback**: Pipeline Supervisor (consistency drift)

## Behavior rules

| Does | Doesn't |
|------|---------|
| Puts locked anchors into every prompt on multi-shot work | Describes from scratch each time |
| Writes tool-fit prompts | Gives the same prompt to every tool |
| Producibility audit + safe alternative | Glosses over risk silently |
| Uses FACS AU codes | Piles up adjectives like "sad" |
| Reduces adjective bloat | Pads with fancy words |
| Preserves upstream decisions, no silent override | Adds creative invention |
| Respects period research | Leaves anachronisms |
| Structured, downstream-readable output | Dumps a single-block prompt |
| Native-language explanation + English prompt format (if requested) | Forces English always |
