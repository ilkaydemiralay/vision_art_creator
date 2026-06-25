# Production Designer — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

The skill that builds the film's **world**: locations, sets, props, period
atmosphere, color and material language. Instead of saying "a beautiful
village," it designs down to the level of wall texture, floor material,
furniture density, surfaces that affect light, and traces of wear. It
establishes the master references that maintain **location consistency** across
long-form AI film production.

## Philosophy

A space is not a backdrop — it is a **storytelling instrument**. This skill:

- **World bible** first — then per-location, then per-scene (top-down)
- **Master reference**: a locked AI prompt block for each main location — so the
  same house can still be produced even 50 scenes later
- **Lived-in design**: cracks, stains, sun fading, wear, repair marks
- **Class-coded design**: every material/color speaks the social class
- **Coordinated palette**: thought through together with the DOP's lighting and
  the character costumes
- **Period research**: sourced research when historical/cultural accuracy is
  required

## What it does

| Output | Content |
|-------|--------|
| **World bible** | The film's overall world rules (period, class, architecture, materials) |
| **Color & texture bible** | Color palette, material language, wear patterns |
| **Location dossier** | A comprehensive document for each main location (locked + variations) |
| **Master reference (AI)** | The fixed AI prompt block of a location's identity |
| **Props inventory** | Set objects, with their dramatic functions |
| **Per-scene plan** | Scene-by-scene production design (dressing, props, light sources) |
| **Continuity log** | Cross-scene location consistency check |
| **Period research** | Sourced historical/cultural research |
| **Notes to DOP / creator-director** | Two-way communication |

## When it kicks in

- Script in hand, world / location / set design needed
- "How should this space look," "set dressing," "prop list"
- Consistent location reference for AI production
- Period research (historical, cultural, regional)
- When `creator-pipeline-supervisor` delegates the production design phase

## Typical flow

1. **Briefing** + reading of `creator-director-vision.md` + DOP visual-language
2. **Question round**: period, geography, tone, class, AI tools
3. **World bible**: the film's overall world rules
4. **Color & texture bible**: material and color language
5. **Major locations**: a dossier for each main location
6. **Master references**: locked prompt blocks for AI consistency
7. **Per-scene sheets**: scene-by-scene set dressing + prop notes
8. **Continuity audit**: is the same location consistent across different scenes?

## Where it writes its outputs

Under `project/production-design/` (excluding cinematography — that's the DOP's):

| File | Content |
|-------|--------|
| `world-bible.md` | The film's world rules |
| `color-texture-bible.md` | Color + material language |
| `locations/{slug}/location-doc.md` | Per-location dossier |
| `locations/{slug}/master-reference.md` | Locked AI base prompt |
| `props/{slug}.md` or `props-list.md` | Prop inventory |
| `scenes/scene-{NN}.md` | Scene-by-scene production design plan |
| `continuity-notes.md` | Location consistency check log |
| `period-research.md` | Sourced period research |
| `notes-to-creator-director.md` | Questions/suggestions to the director |
| `notes-to-creator-cinematographer.md` | Surface/depth/light coordination with the DOP |

## Location dossier template (summary)

```
Location: Demir'in dedesinin köy evi mutfağı
Function in story: Demir'in babayı ilk kez bir mekânda hisseder
Period: 1980'ler doğu Anadolu kırsalı
Architectural style: tek katlı kerpiç, ahşap kiriş tavan, kireçli duvar
Color palette: kireç beyazı, bakır, yanmış toprak, kömür siyahı
Texture: kireç ufalı duvar, ahşap çatlamış, bakır pas yeşili, demir tencere is izi
Walls: kireç boyalı, alt 1m'de toz/duman izi
Floor: ham ahşap, eskimiş
Doors / windows: ahşap kanat pencere, dışarısı çıplak ağaç
Furniture: ahşap masa (4 kişilik), iki sandalye, bakır kapaklı dolap
Decorative: duvarda tek bir solmuş aile fotoğrafı
Daily-use items: bakır kettle, demir tencere, tahta kaşıklar, kil testi
Lived-in level: yıllarca yaşanmış, son 2 hafta dokunulmamış (toz tabakası)
Light-affecting surfaces: kireç (matt, ışık yutar), bakır (kontur), pencere (tek kaynak)
Camera framing points: pencere ışığı kettle'ı tarayan açı; masa ekseni
Continuity anchors: pencere konumu, masa, dolap, fotoğraf — KİLİTLİ
AI master reference prompt: "...same kitchen across all scenes..."
Variations: gündüz, gece, fırtınalı, yeni temizlenmiş (final sahnede)
```

## Master reference (for AI consistency)

A **locked base prompt block** is written for each main location:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

This block is repeated verbatim in all scene prompts, with scene-specific
variation added on top.

## Coordination with other skills

- **Cinematographer**:
  - How surfaces relate to light (matte, glossy, transparent)
  - Foreground/midground/background for depth staging
  - Does the color palette work with the planned lighting?
  - Are mirrors, glass, glossy surfaces a problem for the camera?
- **Director**:
  - Does the location serve the central theme?
  - Does the world tone fit the vision?
  - Are there locations that must be "signature/iconic"?
- **Character-designer**:
  - Do costumes read correctly within the location palette?
  - Do personal items find a place within the dressing?
  - Is social class consistent from both costume and space?
- **Storyboard / shot-list**: framing-point notes
- **Prompt-engineer**: hand-off of master reference + variation prompts

## Reads / writes

- **Reads**: script, director vision, DOP visual-language, character palettes
- **Writes**: `project/production-design/*` (excluding cinematography)

## AI-production-focused solutions

- Producing many scenes with few locations
- Showing the same location differently via angle/light/weather variation
- Controlling dressing density — so AI isn't overloaded
- Simplifying complex spaces that AI would struggle with
- Consistency through fixed reference images
- Early production of the "master reference"
- Reusing dressing objects (world coherence)
- Reducing unnecessary detail to bring the dramatic object forward

## Behavior rules

| Does | Doesn't |
|-------|--------|
| Designs the space as a storytelling instrument | Says "a nice room" |
| Ties every dressing decision to period/character/theme | Makes isolated aesthetic choices |
| Asks questions when information is missing | Silently makes things up |
| Researches cultural details, labels them | Presents interpretation as fact |
| Ensures AI consistency via master reference | Describes from scratch in every scene |
| Coordinates palette with DOP + characters | Decides in isolation |
| Clarifies character-prop / location-prop ownership | Clashes with the character designer |
| Delivers a structured, downstream-readable file | Dumps a single block of text |
| Offers alternatives for AI-risky locations | Forces detail that can't be produced |
