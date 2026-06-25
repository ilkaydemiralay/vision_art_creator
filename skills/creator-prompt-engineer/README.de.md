# Prompt-Engineer — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · **Deutsch** · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Die **Übersetzungsschicht** zwischen der kreativen Pipeline und den KI-Generatoren.
Sie verwandelt die Entscheidungen der Skills für Drehbuch, Regie, DOP, Charakter,
Production Design, Storyboard und Shotliste in **wirklich produzierbare,
konsistente** Prompts. Sie optimiert pro Tool (Midjourney ≠ Sora ≠
Stable Diffusion), bettet die gesperrten Anchors in jeden Prompt ein und erzeugt
sichere Alternativen für riskante Szenen.

## Philosophie

Der Prompt-Engineer **erfindet keine Bilder** — er kodiert die Entscheidungen
des Upstreams. Diese Skill:

- **Locked anchors**: character DNA + location master reference + style block —
  selbst nach 50 Prompts kommt derselbe Charakter mit demselben Gesicht heraus
- **Tool fitness**: jedes KI-Tool hat seine eigene Prompt-Sprache
- **Producibility audit**: diese Szene wird den Generator überfordern — schlage eine Alternative vor
- **Consistency discipline**: für einen Langfilm sind Prompts ein System, nichts Isoliertes
- **FACS expression coding**: AU1 + AU4 + AU15 statt „traurig" — konsistentere Ergebnisse
- **Überschreibt den Upstream niemals stillschweigend**: markiert ihn und fragt bei Bedarf zurück

## Wofür es gut ist

| Ausgabe | Inhalt |
|---------|--------|
| **Character prompts** | Gesperrte DNA + Szene-für-Szene-Variation |
| **Location prompts** | Master reference + Tag-/Nacht-/Wettervariation |
| **Style anchors** | Filmweiter visueller/technischer Block |
| **Negative prompts** | Kategoriebasierte Negativ-Prompt-Bank |
| **Panel prompts** | Bilderzeugungs-Prompt aus einem Storyboard-Panel |
| **Shot prompts** | KI-Videoerzeugungs-Prompt aus der Shotliste |
| **Character sheets** | Front-/Seiten-/Rück-/Close-Referenzerzeugung |
| **Producibility risk report** | Risiko auf Szenen-/Shot-Ebene + sichere Alternative |
| **Tool guide** | Tool-spezifische Hinweise für den Operator |

## Wann es einsetzt

- Vor der Produktion werden KI-Bild-/Video-Prompts benötigt
- Für die Charakter-/Location-Konsistenz muss ein Anchor-System aufgebaut werden
- Eine Storyboard- oder Shotlisten-Ausgabe soll in Tool-Prompts umgewandelt werden
- Ein vorhandener Prompt ist riskant — eine sichere Alternative wird gewünscht
- Wenn `creator-pipeline-supervisor` die Prompt-Phase delegiert

## Leitfaden zur Tool-Optimierung (Zusammenfassung)

### Midjourney
- Parameter `--ar`, `--style raw`, `--s`
- `--cref` und `--cw` für die Charakterreferenz
- `--sref` für die Stilreferenz
- Kompakte Formulierung — Adjektiv-Stapelung schwächt das Signal

### DALL·E
- Natürliche Sprache > Tag-Abladung
- Räumliche Beziehungen ausschreiben
- Texterzeugung im Bild vermeiden

### Stable Diffusion (SDXL / SD3)
- Positive + negative getrennt
- LoRA- / Reference- / Seed-Notizen für die Charakterkonsistenz
- Wichtige Begriffe nach vorn (token weight)

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- Eine einzige Hauptkamerabewegung
- Kontrollierte Anzahl an Charakteren
- Klares opening + closing frame
- Kurze Dauer (typisch 3–10 s)
- Tool-spezifische Limits:
  - Sora 2: ~20 s
  - Kling 3.0: subject binding für Konsistenz
  - Veo: starke motion fidelity
  - Runway Gen-3/4: Bewegung schlüssig, lip sync schwach

## System der gesperrten Anchors (für einen Langfilm)

### Character DNA block

Wird **wortwörtlich** aus `project/characters/{slug}/ai-prompts.md` kopiert:

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

Wortwörtlich aus `project/production-design/locations/{slug}/master-reference.md`:

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

Diese Blöcke werden in **jedem Prompt** dieser Szene/dieses Charakters/dieser
Location **wortwörtlich wiederholt**. Diese Disziplin ist der Motor der Konsistenz.

## Negativ-Prompt-Kategorien

| Problem | Negativbegriff |
|---------|----------------|
| Gesichtsverzerrung | distorted face, malformed face, asymmetric eyes, blurred features |
| Handfehler | extra fingers, missing fingers, fused fingers, deformed hand |
| Anachronismus | modern clothes, modern tech, plastic, neon, smartphone |
| KI-Artefakt | warping, morphing, flickering, jittery motion |
| Qualität | low quality, low resolution, jpeg artifacts, oversaturated |
| Text | unwanted text, watermark, signature, logo |
| Komposition | extra characters, cropped subject, duplicate subject |
| Kamera | unintended shake, fisheye distortion |

Manche Tools ignorieren den Negativ-Prompt — in dem Fall schreibe ihn als
*"avoid: ..."*-Hinweis in den positive prompt.

## KI-Video-Producibility-Audit

Prüfungen, bevor ein Video-Prompt ausgegeben wird:

- Zu viel Action in einem einzigen Shot?
- Zu viele Charaktere?
- Ist die Kamerabewegung komplex?
- Ist das Hand-/Finger-/Gesichtsdetail riskant?
- Lässt sich die Kostüm-/Requisitenkonsistenz halten?
- Ist die Location zu überfüllt?
- Sind Licht und Tageszeit konsistent?
- Sollte die Szene in Teile aufgeteilt statt in einen einzigen Prompt gepackt werden?
- Ist lip sync nötig? (markieren)
- Ist der Prompt unnötig abstrakt?

Bei Risiko liefert sie eine **sichere, vereinfachte Alternative**.

## Variantenerzeugung

Fokussierte Varianten für dieselbe Szene:

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

Der **Zweck jeder Variante wird notiert** — warum und in welchem Fall sie genutzt wird.

## Wohin sie ihre Ausgaben schreibt

Unter `project/prompts/`:

| Datei | Inhalt |
|-------|--------|
| `character-prompts/{slug}.md` | Gesperrte DNA + Szenenvarianten |
| `location-prompts/{slug}.md` | Master anchor + Varianten |
| `style-anchors.md` | Filmweite style block(s) |
| `negative-prompts.md` | Negativ-Prompt-Bank |
| `scene-{NN}/panel-{PP}.md` | Panel-Bild-Prompts |
| `scene-{NN}/shot-{SS}.md` | Shot-Video-Prompts |
| `character-sheets/{slug}.md` | Front-/Seiten-/Rück-/Close-Sheet-Erzeugungs-Prompts |
| `prompt-system.md` | Dokumentation des Anchor-Systems |
| `producibility-risk-report.md` | Risiko-Flags + sichere Alternative |
| `tool-guide.md` | Tool-spezifische Operator-Hinweise |

## Zweisprachiges Prompt-Format

Wenn der Nutzer eine Erläuterung in der Muttersprache + einen englischen Prompt möchte:

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

## Koordination mit anderen Skills

- **Liest**: alle kreativen Ausgaben des Upstreams
- **Schreibt**: `project/prompts/*`
- **Delegiert**:
  - an den menschlichen Operator, der die KI-Tools ausführen wird
  - Feedback an den **storyboard artist** oder den **shot-list designer**, wenn
    das Producibility-Audit eine Änderung des Upstreams erfordert
- **Erhält Feedback**: Pipeline Supervisor (Konsistenz-Drift)

## Verhaltensregeln

| Tut | Tut nicht |
|-----|-----------|
| Setzt die locked anchors bei Multi-Shot-Arbeit in jeden Prompt | Beschreibt jedes Mal von Grund auf neu |
| Schreibt tool-gerechte Prompts | Gibt jedem Tool denselben Prompt |
| Producibility-Audit + sichere Alternative | Übergeht das Risiko stillschweigend |
| Verwendet FACS-AU-Codes | Stapelt Adjektive wie „traurig" |
| Reduziert Adjektiv-Aufblähung | Füllt mit gestelzten Wörtern |
| Bewahrt die Upstream-Entscheidung, ohne stilles Überschreiben | Fügt kreative Erfindung hinzu |
| Respektiert die Epochenrecherche | Lässt Anachronismen stehen |
| Strukturierte, downstream-lesbare Ausgabe | Wirft einen Prompt im Einzelblock hin |
| Format Muttersprache-Erläuterung + englischer Prompt (auf Wunsch) | Erzwingt durchweg Englisch |
