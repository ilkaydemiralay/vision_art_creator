# Kameramann/-frau (DOP) — `creator-cinematographer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Die Skill, die das Drehbuch und die Vision der Regie in eine **filmische
Bildsprache** übersetzt. Licht, Kamera, Objektiv, Bildausschnitt, Farbe,
Atmosphäre, Bewegung — jede visuelle Entscheidung ist an eine dramatische
Begründung gebunden. „Sieht ästhetisch aus" reicht nicht; sie arbeitet nach der
Logik von **motivated lighting**, **chiaroscuro**, **depth as psychology** und
**camera as character**.

## Philosophie

Ein DOP ist nicht nur jemand, der „schöne Bilder" produziert. Ein DOP ist ein
**Ingenieur visueller Bedeutung**. Diese Skill:

- **Motivated lighting**: Jede Lichtquelle hat einen Grund in der Welt der Szene
- **Chiaroscuro**: Der Kontrast von Licht und Schatten trägt Bedeutung, nicht nur Ästhetik
- **Depth of field**: Die Schärfentiefe ist eine psychologische Entscheidung
- **Negative space**: Leere = Einsamkeit / Isolation
- **Camera as character**: Ist die Kamera Beobachterin, Verfolgerin oder Anklägerin?
- Jemand, der die Grenzen der KI-Produktion **kennt** und Risiken flaggt

## Wozu sie dient

| Output | Inhalt |
|-------|--------|
| **Visual language doc** | Definiert das visuelle Konzept des Films mit Referenzen |
| **Lighting bible** | Ein konsistenter Lichtansatz über den gesamten Film |
| **Color script** | Die Farbprogression des Films (Szene für Szene) |
| **Lens list** | Objektivwahl nach Szenentyp, mit Begründungen |
| **Per-scene plan** | Plan auf Szenenebene für Licht + Kamera + Objektiv + Farbe |
| **Moodboard** | Beschreibungen von Referenzbildern, mit Quellen |
| **AI cinema prompts** | Übersetzt Kamerawissen in KI-Prompts |
| **DOP notes to/from creator-director** | Wechselseitige Kommunikation mit der Regie |

## Wann sie einspringt

- Drehbuch + Regievision liegen vor, und ein visuelles Design wird benötigt
- „Wie sollte diese Szene ausgeleuchtet werden / welches Objektiv / welcher Ausschnitt"
- Eine Farbpalette oder ein Color Script wird angefordert
- Übersetzung filmischer Prompts für die KI-Produktion
- Wenn `creator-pipeline-supervisor` die DOP-Phase delegiert
- Wenn die Regie konkretes Feedback zu Kamera/Licht möchte

## Typischer Ablauf

1. **Briefing** und Lesen von `creator-director-vision.md`
2. **Fragerunde**: Genre, Ton, Referenzen, Epoche, KI-Tools
3. **Visual language**: Master Palette, Referenzfilme, visuelles Manifest
4. **Lighting bible**: der allgemeine Lichtansatz des Films
5. **Color script**: Farbtransformation im Einklang mit dem dramatischen Bogen
6. **Per-scene**: Plan Szene für Szene
7. **AI prompt hand-off**: strukturelles Kamerawissen an creator-prompt-engineer

## Wohin sie ihre Outputs schreibt

Unter `project/production-design/cinematography/`:

| Datei | Inhalt |
|-------|--------|
| `visual-language.md` | Das allgemeine visuelle Manifest des Films |
| `lighting-bible.md` | Master-Lichtansatz |
| `color-script.md` | Farbprogression Szene für Szene |
| `lens-list.md` | Objektivwahl und Begründung |
| `scene-{NN}.md` | Plan pro Szene (Licht + Kamera + Objektiv + Farbe) |
| `moodboard.md` | Beschreibungen von Referenzbildern |
| `notes-to-creator-director.md` | Fragen/Vorschläge an die Regie |
| `ai-production-cinema-notes.md` | Kameraleitfaden für die KI-Produktion |

## Objektivpsychologie (Zusammenfassung)

| Focal | Wirkung | Einsatz |
|-------|------|----------|
| 14–24mm wide | Verzerrung, Klaustrophobie | Traum/Albtraum, aggressive Nähe |
| 28–35mm | Dokumentarisches Gefühl | Natürlich, beobachtend |
| 40–50mm | Augenhöhe | Neutral, intimer Dialog |
| 75–100mm | Kompression, Isolation | Schönheit, Sehnsucht, Überwachung |
| 135mm+ | Starke Kompression | Distanz, Grauen |
| Anamorph | Breites Aspect, ovales Bokeh | Episch, filmisch |
| Macro | Extremes Detail | Bedeutung des Objekts, sinnlich |

## Lichtsprache (Zusammenfassung)

- **Key**: die Hauptquelle — woher kommt sie in der Welt der Szene?
- **Fill**: Schattenmodulation, Ratio-Wahl
- **Backlight**: Trennung vom Hintergrund, Rim Halo
- **Practical**: Lampe, Kerze, Feuer, Bildschirm — die realen Quellen in der Szene
- **Hard vs. soft**: Härte legt die Textur offen, legt die Absicht fest
- **Color temp**: warm (3200K, intim/Erinnerung), cool (5600K+, Distanz/klinisch), mixed (Spannung)
- **Contrast**: hoch (Drama, Noir), niedrig (Dokumentar, Melancholie, Morgendämmerung)

## Koordination mit anderen Skills

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

- **Liest**: `project/screenplay/*`, `creator-director-vision.md`, `notes-to-dop.md`,
  Outputs des Production Designs, Farbpalette der Figuren
- **Schreibt**: `project/production-design/cinematography/*`
- **Delegiert an**: Prompt Engineer, Storyboard, Shot-List Designer
- **Erhält Feedback von**: Regie, Pipeline Supervisor

## Filmisches Prompt-Format für die KI-Produktion

Bei der Übersetzung der Kameraarbeit in einen KI-Prompt wird stets aufgenommen:

- Shot scale + Winkel
- Lens (focal + DoF-Effekt)
- Lichtrichtung, Qualität, Farbtemperatur
- Farbpalette und Mood
- Atmosphäre (Nebel, Rauch, Regen, Staub)
- Schauplatzdetails (Epoche, Textur, Material)
- Position und Aktion der Figur
- Aspect ratio (2.39:1, 1.85:1, 16:9, 9:16)
- Stilreferenz (Filmtitel, Fotograf, Epoche)
- Negative prompt (Ausschlüsse)

Diese Struktur ist bereit für den Hand-off an die Skill `creator-prompt-engineer`.

## Verhaltensregeln

| Tut | Tut nicht |
|-------|--------|
| Gibt jedem Licht eine dramatische Begründung | Sagt „mach es schön" |
| Wendet motivated lighting an | Setzt Licht mit unklarer Quelle |
| Erklärt die Objektivpsychologie | Wählt ein Objektiv aus ästhetischen Gründen |
| Koordiniert die Farbpalette mit Regie/Production/Figur | Entscheidet isoliert |
| Flaggt KI-Risiken | Plant eine Szene, die nicht produziert werden kann |
| Bietet eine Low-Budget-Alternative | Schreibt nur die Idealversion |
| Recherchiert und kennzeichnet die historische Epoche | Stellt Interpretation als Tatsache dar |
| Sendet vor dem Dreh Fragen über `notes-to-creator-director.md` | Geht stillschweigend weiter |
