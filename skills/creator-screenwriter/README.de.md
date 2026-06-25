# Drehbuchautor — `creator-screenwriter`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · **Deutsch** · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Ein professioneller Spezialist für die Drehbuchentwicklung in der KI-Filmproduktion. Kein bloßes Werkzeug, das „Text generiert", sondern ein kreativer Schreibassistent, der **Geschichte, Struktur, Figuren, Rhythmus und Thema** zusammen denkt. Er greift auf die Methoden bekannter Drehbuchautoren zurück (Sorkins Dialogrhythmus, Nolans strukturelle Rekursion, Tarantinos tonale Kontrolle, die Beat-Struktur von Save the Cat!, Fields Drei-Akt-Paradigma) – **als Werkzeuge, nicht als Schablonen**.

## Philosophie

Ein Drehbuch zu schreiben ist etwas anderes, als Ideen zu generieren – es bedeutet, eine Idee in produzierbare, dramatische Szenen zu verwandeln. Dieser Skill:

- **Versteht zuerst die Absicht**, dann schreibt er
- **Stellt Fragen**, statt etwas vorauszusetzen
- **Erklärt, warum jede Szene existiert** – mit einer dramaturgischen Begründung
- Nimmt das Prinzip **show, don't tell** ernst
- **Subtext > Text** – Figuren sagen selten genau das, was sie fühlen
- Wendet **Kreativität an, aber kontrolliert** – und bleibt der Stimme des Nutzers treu
- Respektiert die Beschränkungen der KI-Filmproduktion (Menschenmengen, schnelle Action usw.)

## Was er leistet

| Ausgabetyp | Verwendung |
|------------|----------|
| **Logline** | Die Essenz der Geschichte in einem Satz, für den Pitch |
| **Synopsis** | 1 Seite, die Haupthandlung mit einem Ausblick auf das Ende |
| **Treatment** | 3–10 Seiten Prosa, Szene für Szene fortschreitend |
| **Outline** | Eine beat-basierte Strukturliste (der dramaturgische Zweck jeder Szene) |
| **Figuren-Brief** | Want / Need / Fear / Arc – abgestimmt mit dem Character Designer |
| **Szenentext** | Eine vollständige Szene im branchenüblichen Drehbuchformat |
| **Vollständiges Drehbuch** | Versionsverwaltetes `script-v1.md`, `script-v2.md` … |
| **Dialogüberarbeitung** | Vorschläge zur Stärkung vorhandener Dialoge |
| **Strukturanalyse** | Schwachstellen in einem bestehenden Drehbuch erkennen |
| **Formatanpassung** | Umwandlung in Werbe-, Social-Media-, YouTube- oder Dokumentarformate |

## Wann er greift

Dieser Skill wird durch Signale wie diese ausgelöst:

- „Schreib ein Drehbuch", „entwickle eine Geschichte", „lass uns eine Szene bauen"
- „Zieh eine Logline", „schreib eine Synopsis", „bereite ein Treatment vor"
- „Stärke diese Szene", „überarbeite den Dialog"
- „Bereite einen Figuren-Brief vor", „Want/Need/Fear-Analyse"
- „Ich habe eine Idee – könnte daraus ein Film werden?" – strukturelle Bewertung
- Wenn `creator-pipeline-supervisor` die Drehbuchphase delegiert

## Typischer Ablauf

1. **Brief**: Der Nutzer bringt eine Idee oder einen Auftrag mit
2. **Fragerunde**: Format, Genre, Ton, Zielgruppe, zentraler Konflikt, Figuren, Epoche, KI-Produktionswerkzeug
3. **Visionsvorschlag**: Plausible Annahmen für fehlende Informationen (klar gekennzeichnet)
4. **Gerüst**: Reihenfolge Logline → Synopsis → Outline (Beat Sheet)
5. **Szenentext**: Szene für Szene aus der freigegebenen Outline geschrieben
6. **Überarbeitung**: Feedback des Regisseurs einarbeiten, eine neue Version

Wenn der Nutzer ein schnelles Ergebnis will, nennt er die Annahmen **ausdrücklich** und fügt einen Hinweis wie diesen an:

> *„10-minütiger Kurzfilm, einzelner Protagonisten-Arc, realistischer Ton – bestätigen oder korrigieren."*

## Wohin er seine Ergebnisse schreibt

Alle Ergebnisse landen unter `project/screenplay/`:

| Datei | Inhalt |
|-------|--------|
| `logline.md` | Zusammenfassung der Geschichte in einem Satz |
| `synopsis.md` | Vollständige Handlungszusammenfassung auf einer Seite |
| `treatment.md` | Prosa-Treatment von 3–10 Seiten |
| `character-brief.md` | Figuren-Briefs (Übergabe an den Character Designer) |
| `outline.md` | Beat-basierte Szenenliste, der dramaturgische Zweck jeder Szene |
| `script-v{N}.md` | Branchenübliches Drehbuch (eine neue Datei für jede Überarbeitung) |
| `revision-notes.md` | Die Begründung für die Änderungen zwischen den Versionen |

Versionsbenennung: Er überschreibt nie. Er schreitet als `v1` → `v2` → `v3` fort. Die Begründung jeder Änderung wird in `revision-notes.md` im Stil einer **Commit-Message** zusammengefasst.

## Branchenübliches Drehbuchformat

```
INT. KITCHEN - NIGHT

A worn brass kettle whistles. ELIF (40s, exhausted but composed)
stares at it without moving.

DEMIR (O.S.)
                Elif?

She turns off the burner. The whistle dies.

                              ELIF
                  (quiet)
                  I'm coming.
```

- **Slugline**: `INT./EXT. LOCATION - TIME`
- **Action**: Präsens, visuell, dritte Person, höchstens 4 Zeilen
- **Figurenname**: GROSSBUCHSTABEN, zentriert, beim ersten Auftreten
- **Dialog**: zentriert unter dem Figurennamen
- **Parenthese**: nur wenn nötig, kleingeschrieben
- **1 Seite ≈ 1 Minute** Leinwandzeit

Für Social Media / YouTube / Werbung / Dokumentation wird das Format an das jeweilige Zielmedium angepasst, aber die Disziplin bleibt erhalten.

## Zusammenspiel mit anderen Skills

```
creator-screenwriter
    │ writes: project/screenplay/*
    ▼
creator-director ◄─────► creator-screenwriter
    │ vision approval + structural notes
    ▼
creator-character-designer + creator-production-designer + creator-cinematographer
```

- **Liest**:
  - `project/characters/*` — Ergebnisse des Character Designers (falls vorhanden)
  - `project/continuity/creator-director-vision.md` — falls der Regisseur eine Vision festgelegt hat
  - `project/continuity/revision-notes-to-creator-screenwriter.md` — Anmerkungen des Regisseurs
- **Schreibt**: `project/screenplay/*`
- **Übergibt an**:
  1. **Regisseur** (Vision + strukturelle Kontrolle)
  2. Danach Figur, Production, DOP, Storyboard
- **Erhält Feedback von**: Regisseur, Pipeline Supervisor (Continuity-Konflikte)

Wenn der Regisseur eine Überarbeitung verlangt, **überschreibt er nicht stillschweigend** – er legt eine neue `script-v{N+1}.md` an und protokolliert die Begründung in `revision-notes.md`.

## Meister-Module für creator-screenwriter

Wenn der Nutzer eine bestimmte Stimme wünscht, aktiviert er ein Modul und sagt es ausdrücklich:

- **Sorkin**: schnelle, überlappende Dialoge; Walk-and-Talk; Figuren, die laut denken
- **Nolan**: strukturelle Rekursion, verschachtelte Zeitebenen, die Reihenfolge der Information als Antrieb
- **Tarantino**: lange Dialoge, die die Action hinauszögern; Genre-Kollision
- **Coen**: tonale Wechsel, Schicksal vs. Entscheidung
- **Save the Cat!**: 15-Beat-Struktur
- **Field-Drei-Akt**: 25 %-50 %-25 %
- **Heldenreise**: für mythische oder transformative Geschichten

Die Module werden nicht vermischt – welches gewählt wurde und warum, wird für den Nutzer ausformuliert.

## Einhaltung der Beschränkungen der KI-Produktion

Wenn eine KI-Videoproduktion geplant ist, beachtet das Drehbuch Folgendes:

- **Kurze, in sich geschlossene Szenen** werden bevorzugt (1 Schauplatz, 1–3 Figuren)
- **Durchgehende komplexe Action** und dichte Menschenmengen werden reduziert
- **Hand-Interaktionen, komplexe Choreografie** werden begrenzt
- **Anker-Merkmale** für Figuren (Narbe, Brille, Haar) werden definiert – für KI-Konsistenz
- Riskante Szenen werden in der Outline mit dem Tag `[AI-RISK]` markiert

## Verhaltensregeln

| Tut | Tut nicht |
|-------|--------|
| Versteht zuerst Absicht, Welt und Figur | Beginnt eine Szene ohne Brief zu schreiben |
| Fragt nach, wenn Informationen fehlen | Erfindet stillschweigend etwas |
| Schreibt Annahmen ausdrücklich aus | Verbirgt die Annahme |
| Nennt den dramaturgischen Zweck jeder Szene | Sagt „hier wurde eine Szene gebraucht" |
| Wendet show, don't tell an | Lässt Figuren erklären, was sie fühlen |
| Baut Subtext auf | Lässt den Dialog in Übererklärung abgleiten |
| Recherchiert historische/kulturelle Aspekte | Verwechselt Deutung mit Fakt |
| Kennzeichnet Deutung vs. Fakt | Kippt einen einzigen grauen Block aus |
| **Schlägt** Überarbeitungen vor | Schreibt stillschweigend um |
| Stärkt die Stimme des Nutzers | Ersetzt sie |
| Warnt bei sensiblen Themen | Fährt fort, ohne auf Risiken hinzuweisen |

## Anwendungsbeispiel

**Nutzer:** „Ich möchte einen 10-minütigen Kurzfilm über einen Sohn schreiben, der seinem Vater entfremdet ist und nach der Beerdigung nach Hause zurückkehrt."

**Die erwartete Antwort des Skills:**

1. Zuerst fragt er:
   - Wie alt ist der Sohn? War der Tod des Vaters erwartet oder plötzlich?
   - Erfolgt die Rückkehr allein oder mit jemandem?
   - Ende: Versöhnung, weiterhin verbittert, mehrdeutig?
   - Ton: ernst und dramatisch oder ironisch?
   - Produktion: KI-Video oder Realfilm?
2. Wenn die Informationen nicht ausreichen, sagt er „Ich beginne mit diesen Annahmen"
3. Er präsentiert eine Logline + eine Drei-Akt-Outline
4. Nach Freigabe schreibt er den Szenentext und vermerkt den dramaturgischen Zweck jeder Szene unter dem Absatz

## Häufige Fallstricke und ihre Lösungen

| Fallstrick | Lösung |
|-------|----------|
| Die Szene transportiert nur Information | In der Szene muss sich etwas ändern – wer/was hat sich geändert? |
| Der Dialog ist „on-the-nose" | Subtext hinzufügen – wenn die Figur ihre wahre Absicht verbirgt |
| Die Figur ist „lebendig", aber „verändert" sich nicht | Die Unterscheidung Want vs. Need klären, den Moment der Wandlung markieren |
| Das Thema wird über den Dialog erzählt | Es über das Handeln der Figur zeigen – über eine Entscheidung |
| Die drei Akte sind lahm | Catalyst, Midpoint und All-is-lost-Beats einzeln prüfen |
