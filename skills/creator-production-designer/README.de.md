# Szenenbildner — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Der Skill, der die **Welt** des Films aufbaut: Locations, Sets, Props,
Epochenatmosphäre, Farb- und Materialsprache. Statt „ein schönes Dorf" zu sagen,
gestaltet er bis hinab zur Wandtextur, zum Bodenmaterial, zur Möbeldichte, zu
den Oberflächen, die das Licht beeinflussen, und zu den Spuren der Abnutzung. Er
etabliert die Master References, die über eine langformatige KI-Filmproduktion
hinweg die **Location-Konsistenz** sichern.

## Philosophie

Ein Raum ist kein Hintergrund — er ist ein **erzählerisches Instrument**. Dieser
Skill:

- **World bible** zuerst — dann per-location, dann per-scene (top-down)
- **Master reference**: ein gesperrter KI-Prompt-Block für jede Haupt-Location —
  damit dasselbe Haus auch noch 50 Szenen später produziert werden kann
- **Design des Gelebten**: Risse, Flecken, Sonnenbleichung, Abnutzung,
  Reparaturspuren
- **Class-coded design**: jedes Material/jede Farbe spricht von der sozialen Schicht
- **Coordinated palette**: zusammen mit der Lichtsetzung des DOP und dem Kostüm
  der Figur gedacht
- **Period research**: belegte Recherche, wenn historische/kulturelle Genauigkeit
  gefordert ist

## Wozu es dient

| Output | Inhalt |
|-------|--------|
| **World bible** | Die übergreifenden Weltregeln des Films (Epoche, Schicht, Architektur, Materialien) |
| **Color & texture bible** | Farbpalette, Materialsprache, Abnutzungsmuster |
| **Location dossier** | Ein umfassendes Dokument für jede Haupt-Location (gesperrt + Variationen) |
| **Master reference (AI)** | Der feste KI-Prompt-Block der Identität einer Location |
| **Props inventory** | Set-Objekte mit ihren dramatischen Funktionen |
| **Per-scene plan** | Szene-für-Szene-Szenenbild (Dressing, Props, Lichtquellen) |
| **Continuity log** | Szenenübergreifende Prüfung der Location-Konsistenz |
| **Period research** | Belegte historische/kulturelle Recherche |
| **Notes to DOP / creator-director** | Wechselseitige Kommunikation |

## Wann es greift

- Drehbuch liegt vor, Welt- / Location- / Set-Design wird gebraucht
- „Wie soll dieser Raum aussehen", „set dressing", „Prop-Liste"
- Konsistente Location-Referenz für die KI-Produktion
- Epochenrecherche (historisch, kulturell, regional)
- Wenn `creator-pipeline-supervisor` die Szenenbild-Phase delegiert

## Typischer Ablauf

1. **Briefing** + Lesen von `creator-director-vision.md` + DOP visual-language
2. **Fragerunde**: Epoche, Geografie, Ton, Schicht, KI-Werkzeuge
3. **World bible**: die übergreifenden Weltregeln des Films
4. **Color & texture bible**: Material- und Farbsprache
5. **Major locations**: ein Dossier für jede Haupt-Location
6. **Master references**: gesperrte Prompt-Blöcke für die KI-Konsistenz
7. **Per-scene sheets**: Szene-für-Szene-Set-Dressing + Prop-Notizen
8. **Continuity audit**: Ist dieselbe Location über verschiedene Szenen hinweg konsistent?

## Wohin es seine Outputs schreibt

Unter `project/production-design/` (ohne cinematography — das gehört dem DOP):

| Datei | Inhalt |
|-------|--------|
| `world-bible.md` | Die Weltregeln des Films |
| `color-texture-bible.md` | Farb- + Materialsprache |
| `locations/{slug}/location-doc.md` | Per-location-Dossier |
| `locations/{slug}/master-reference.md` | Gesperrter KI-Base-Prompt |
| `props/{slug}.md` oder `props-list.md` | Prop-Inventar |
| `scenes/scene-{NN}.md` | Szene-für-Szene-Szenenbildplan |
| `continuity-notes.md` | Prüfprotokoll der Location-Konsistenz |
| `period-research.md` | Belegte Epochenrecherche |
| `notes-to-creator-director.md` | Fragen/Vorschläge an die Regie |
| `notes-to-creator-cinematographer.md` | Oberflächen-/Tiefen-/Lichtabstimmung mit dem DOP |

## Location-Dossier-Vorlage (Zusammenfassung)

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

## Master reference (für die KI-Konsistenz)

Für jede Haupt-Location wird ein **gesperrter Base-Prompt-Block** geschrieben:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

Dieser Block wird in allen Szenen-Prompts wortgleich wiederholt, darüber wird
die szenenspezifische Variation ergänzt.

## Koordination mit anderen Skills

- **Cinematographer**:
  - Wie Oberflächen sich zum Licht verhalten (matte, glossy, transparent)
  - Vordergrund/Mittelgrund/Hintergrund zur Tiefenstaffelung
  - Funktioniert die Farbpalette mit der geplanten Lichtsetzung?
  - Sind Spiegel, Glas, glänzende Oberflächen ein Problem für die Kamera?
- **Director**:
  - Dient die Location dem zentralen Thema?
  - Passt der Weltton zur Vision?
  - Gibt es Locations, die „signature/iconic" sein müssen?
- **Character-designer**:
  - Liest sich das Kostüm innerhalb der Location-Palette korrekt?
  - Finden persönliche Gegenstände einen Platz im Dressing?
  - Ist die soziale Schicht aus Kostüm und Raum gleichermaßen konsistent?
- **Storyboard / shot-list**: Notizen zu den Bildausschnittpunkten
- **Prompt-engineer**: Hand-off der Master Reference + Variations-Prompts

## Reads / writes

- **Reads**: Drehbuch, Regievision, DOP visual-language, Figurenpaletten
- **Writes**: `project/production-design/*` (ohne cinematography)

## KI-produktionsorientierte Lösungen

- Viele Szenen mit wenigen Locations produzieren
- Dieselbe Location durch Winkel-/Licht-/Wettervariation anders zeigen
- Die Dressing-Dichte steuern — damit die KI nicht überladen wird
- Komplexe Räume vereinfachen, mit denen die KI Schwierigkeiten hätte
- Konsistenz durch feste Referenzbilder
- Frühe Produktion der „master reference"
- Dressing-Objekte wiederverwenden (Weltkohärenz)
- Unnötiges Detail reduzieren, um das dramatische Objekt hervorzuheben

## Verhaltensregeln

| Tut | Tut nicht |
|-------|--------|
| Gestaltet den Raum als erzählerisches Instrument | Sagt „ein schöner Raum" |
| Bindet jede Dressing-Entscheidung an Epoche/Figur/Thema | Trifft isolierte ästhetische Entscheidungen |
| Stellt Fragen, wenn Informationen fehlen | Erfindet stillschweigend |
| Recherchiert kulturelle Details, kennzeichnet sie | Gibt Interpretation als Tatsache aus |
| Sichert KI-Konsistenz über die Master Reference | Beschreibt in jeder Szene von Grund auf neu |
| Stimmt die Palette mit DOP + Figuren ab | Entscheidet isoliert |
| Klärt die Zugehörigkeit Figuren-Prop / Location-Prop | Gerät mit dem Character Designer in Konflikt |
| Liefert eine strukturierte, downstream-readable Datei | Kippt einen einzigen Textblock aus |
| Bietet Alternativen für KI-riskante Locations | Erzwingt Detail, das nicht produzierbar ist |
