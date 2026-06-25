# Charakterdesigner — `creator-character-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Eine Skill, die eine Figur über die Trias **Name + Alter + Erscheinungsbild**
hinaushebt und sie als **kohärentes Wesen** gestaltet. Sie erzeugt dramatische
Funktion, Psychologie, Biografie, Körpersprache, Kostüm, Props, Casting-Profil und
eine **mit FACS Action Units codierte Ausdrucksbibliothek**. Sie etabliert die
„Character DNA"-Anker, die die Figurenkonsistenz über eine langformatige
KI-Filmproduktion hinweg bewahren.

## Philosophie

Eine Figur wird nicht zufällig erzeugt — sie leitet sich aus dem Bedarf des Drehbuchs,
der Vision des Regisseurs und der visuellen Welt des DOP ab. Diese Skill:

- **Jede Figur ist die Antwort auf eine dramatische Frage** — andernfalls schlägt sie vor, die Figur zu streichen
- Etabliert für jede Hauptfigur verbindlich das Quartett **Want / Need / Fear / Wound**
- **FACS Action Units**: statt „traurig" zu sagen, sagt sie AU1+AU4+AU15 —
  KI-Modelle und Animatoren interpretieren anatomischen Code konsistenter
- **Character DNA**: definiert gesperrte Anker-Merkmale für KI-Konsistenz
- **Visual distinction audit**: bei mehreren Figuren prüft sie die Unterschiede in Silhouette, Farbe und Energie

## Wozu sie dient

| Ausgabe | Inhalt |
|---------|--------|
| **Character sheet** | Figurendatei — Psychologie, Kostüm, Prop, FACS, AI prompt |
| **Costume bible** | Kostümvariationen und Kontinuität über den ganzen Film |
| **Props list** | Die persönlichen Gegenstände der Figur und ihre dramatischen Verwendungen |
| **FACS expression library** | 3–5 Signatur-Ausdrücke pro Figur, AU-codiert |
| **Casting brief** | Das im Schauspieler gesuchte Profil (schlägt keine Namen vor, definiert Merkmale) |
| **AI prompts** | Base prompt + Szenenvariationen für eine konsistente Figurenreferenz |
| **Arc tracker** | Mit dem Arc-Tracking des Regisseurs koordinierte Figurenwandlung |
| **Continuity notes** | Szene-für-Szene-Kontinuität von Kostüm/Props |

## Wann sie greift

- Das Drehbuch liegt vor und die Figuren sollen entwickelt werden
- „Erstelle ein character sheet", „entwirf ein Kostüm", „verfasse ein Casting-Profil"
- Eine konsistente Figurenreferenz für einen KI-Film wird benötigt
- Wenn der Regisseur oder `creator-pipeline-supervisor` die Figurenphase delegiert
- Wenn die visuelle Unterscheidung bestehender Figuren infrage steht

## FACS-Einsatz — warum und wie

Das **Facial Action Coding System (Ekman & Friesen, 1978)** ist die anatomische
Codierung der Gesichtsmuskeln. Eine Action Unit (AU) = eine bestimmte
Muskelbewegung.

### Warum verwendet diese Skill es?

- **KI-Generatoren** interpretieren abstrakte Eingaben wie „happy face" inkonsistent;
  „AU6 + AU12 (Duchenne smile)" liefert ein verlässlicheres Ergebnis
- **Animations-/VFX-Teams** teilen über AU-Codes einen einzigen Referenzsatz
- **Der Signatur-Ausdruck einer Figur** lässt sich ablegen — zum Beispiel „Demir
  trägt seine unterdrückte Trauer mit AU4 + AU17 (Stirn gerunzelt, Kinn angehoben, ohne AU15)"

### Häufige AU-Kombinationen

| Ausdruck | AU |
|----------|-----|
| Duchenne smile (echtes Glück) | AU6 + AU12 |
| Polite smile (falsch/sozial) | AU12 allein |
| Traurigkeit | AU1 + AU4 + AU15 |
| Wut | AU4 + AU5 + AU7 + AU23 |
| Angst | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26 |
| Ekel | AU9 + AU15 + AU16 |
| Überraschung | AU1 + AU2 + AU5B + AU26 |
| Verachtung (asymmetrisch) | AU12 (einseitig) + AU14 |
| Unterdrückte Trauer | AU4 + AU17 (ohne AU15) |
| Angespannte Ruhe | AU7 + AU23 + AU24 |

## Character-sheet-Vorlage (Zusammenfassung)

```
Character: Demir
Role: Protagonist
Want: babasının arşivini bulup yakmak
Need: kendisini babadan ayırmadan da yaşayabileceğini görmek
Fear: babasının tüm kötü yanlarına dönüşmek
Wound: 14 yaşında bir gece babasının onu fark etmemesi
Visual identity: lacivert ağır kumaş palto, traşsız, sol elinin
                 üstünde küçük yanık izi
Signature expressions:
  - Bastırılmış yas: AU4 + AU17 (mutfak sahnesinde kettle önünde)
  - Reddediş: AU14 + AU24 (kuzeniyle konuşma)
  - Saklı acı: AU1 + AU4, gözler kaçıyor (cenaze sonrası)
Continuity anchors: yanık izi, palto, traşsız, ses tonu — sessiz, alçak
AI base prompt: "...same character across all scenes..."
```

## Wohin sie ihre Ausgaben schreibt

Unter `project/characters/{character-slug}/`:

| Datei | Inhalt |
|-------|--------|
| `character-sheet.md` | Die kanonische Figurendatei |
| `costume-bible.md` | Alle Kostümvariationen + Kontinuität |
| `props.md` | Die Gegenstände der Figur, dramatische Verwendung |
| `facs-expressions.md` | Signatur-Ausdrucksbibliothek, AU-codiert |
| `casting-brief.md` | Schauspielerprofil / Grundlage für einen AI face prompt |
| `ai-prompts.md` | Base prompt + Szene-für-Szene-Variation |
| `arc-tracker.md` | Sync mit dem Arc-Tracking des Regisseurs |
| `continuity-notes.md` | Szene-für-Szene-Kontinuität von Kostüm/Props |

Außerdem gibt es im übergeordneten Verzeichnis eine `cast-list.md` — eine Liste, die alle Figuren zusammenfasst.

## Visual distinction audit

Bei mehr als einer Figur führt die Skill diese Prüfungen durch:

- Silhouetten-Unterscheidung (Größe, Haltung, Kostümform)
- Farbwelt-Unterscheidung (oder bewusster Kontrast)
- Energie-Register-Unterscheidung
- Sprechmuster-Unterscheidung
- Leinwand-Präsenz-Unterscheidung (Typ foreground / background)

Wenn zwei Figuren „ineinander verschwimmen", meldet sie das und schlägt eine Überarbeitung vor.

## KI-Konsistenz (Character DNA)

Um dieselbe Figur über 50 Szenen hinweg mit demselben Gesicht/Kostüm zu erzeugen:

1. **Base prompt** — Schlüsselmerkmale (Gesichtsform, Haar, Erkennungsmerkmal) festgehalten
2. **Anchor descriptors** — 2–3 davon wiederholen sich in jedem Szenen-Prompt
3. **Ausdruck via FACS** — AU-codiert, keine Adjektive
4. **Frühe Erstellung des character sheets** — front/side/back/close Referenzbilder
5. **Referenz im Szenen-Prompt**: „consistent with `characters/demir/sheet.png`"

## Koordination mit anderen Skills

- **Liest**:
  - `project/screenplay/character-brief.md`
  - `project/continuity/creator-director-vision.md`
  - `project/continuity/performance-notes/*`
  - `project/production-design/cinematography/visual-language.md`
  - `project/production-design/world-bible.md`
- **Schreibt**: `project/characters/*`
- **Delegiert an**: Prompt-Engineer, Storyboard, DOP (Palettenkoordination)
- **Erhält Feedback von**: Regisseur, Pipeline Supervisor

## Ansatz beim Kostümdesign

Das Kostüm erzählt die Figur — es ist nicht nur „was sie trägt":

- Hauptteil + seine Funktion
- Stoff: schwer, weich, steif, faserig
- Farbe: Harmonie/Kontrast mit der Palette
- Abnutzung / Neuwertigkeit / Beschädigung / Spuren von Reparatur
- Epochengenauigkeit
- Beziehung zur Gemütslage der Figur
- Wirkung auf die Beweglichkeit
- Interaktion mit Licht (matt, glänzend, transparent, staubfangend)

Für jede Hauptszene eine Kostüm-Kontinuitätsnotiz: ändert es sich innerhalb der
Szene, ändert es sich zwischen den Szenen, warum?

## Ansatz bei den Props

Props sind erzählerische Werkzeuge — nicht dekorativ:

- Name + Funktion
- Beziehung zur Figur
- Aussehen, Material, Farbe, Zustand
- Bedeutung für die Figur (Andenken, Identität, Beziehung)
- Dramatische Verwendung (Vorausdeutung, Payoff, Enthüllung)
- Wie die Kamera es sieht (nah, Detail, im Vorbeigehen)
- Kontinuität (wo es in jeder Szene ist)

Figur-Prop- / Schauplatz-Prop-Zugehörigkeit wird geklärt und mit
**creator-production-designer** koordiniert.

## Verhaltensregeln

| Tut | Tut nicht |
|-----|-----------|
| Erzeugt eine Figur mit dramatischer Begründung | Sagt „wir brauchen noch eine Figur" |
| Bindet jede visuelle Entscheidung an Arc / Funktion / Thema | Trifft isolierte ästhetische Entscheidungen |
| Stellt Fragen, wenn Informationen fehlen | Erfindet stillschweigend etwas |
| Recherchiert kulturelle Details | Stellt eine Vermutung als Tatsache dar |
| Definiert Ausdrücke mit FACS-AU-Codes | Verwendet Adjektive wie „traurig" |
| Führt ein visual distinction audit durch | Lässt zwei Figuren ineinander verschwimmen |
| Bettet continuity anchors in die AI prompts ein | Beschreibt in jeder Szene von Grund auf neu |
| Klärt die Figur-Prop-Zugehörigkeit | Überschneidet sich mit dem Szenenbildner |
| Liefert strukturierte, downstream-readable Dateien | Schüttet einen einzigen Textblock aus |
