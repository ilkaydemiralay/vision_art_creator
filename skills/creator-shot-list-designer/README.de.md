# Shot-List-Designer — `creator-shot-list-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · **Deutsch** · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Die Skill, die Szenen und Storyboards in eine **Shot-List + Edit-Intent** verwandelt.
Der Ort, an dem die Planung der Vorproduktion und die editorische Intention zusammenkommen. Sie ist
nicht der Final-Cut-Editor — sie entwirft die editorische Intention, BEVOR irgendwelches Material
produziert wird, damit der Dreh die richtigen Teile erzeugt.

## Philosophie

Eine Shot-List ist kein technisches Inventar; sie ist eine **Karte der dramatischen +
editorischen Intention**. Diese Skill:

- **Shot-Ökonomie**: jeder Shot trägt eine einzige klare Aktion
- **Bewusstsein für den Schnittrhythmus**: welcher Shot wird lange gehalten, welcher wird
  schnell geschnitten? Die Shot-Dauer ist eine editorische Entscheidung
- **Bildrichtung + Continuity**: räumliche/zeitliche Konsistenz über Cuts hinweg
- **Produzierbarkeit für KI**: plant die Komplexität eines einzelnen Shots rund um die Beschränkungen der KI-Tools
- **Editorische Intention vor der Produktion**: die Schnittlogik wird VOR dem Dreh festgelegt,
  damit keine unnötigen Shots gedreht werden
- **Gestaltung des Publikumserlebnisses**: was fühlt, lernt der Zuschauer, und was wird vorenthalten?

## Was sie produziert

| Output | Inhalt |
|-------|---------|
| **Shot-List pro Szene** | Kanonische Shot-List, mit dramatischer + editorischer Begründung |
| **Edit-Plan** | Pacing innerhalb der Szene, Cut-Punkte, Eröffnungs-/Schlussbild |
| **Transition-Design** | Transition-Entscheidungen von Szene zu Szene (hard cut, match, J/L, sound bridge) |
| **Continuity-Risiko-Audit** | Bericht über Konsistenzrisiken zwischen Shots |
| **Sound-Edit-Notizen** | J-cut / L-cut / Stillepunkte für den Sound-Designer |
| **Filmweite Shot-List** | Konsolidierte Liste, die den gesamten Film abdeckt |
| **Rhythmuskarte** | Pacing Szene für Szene (Bereiche der Shot-Dauer) |
| **Redundanzbericht** | Shots, die geschnitten/zusammengeführt werden sollten |
| **Notizen für den Final-Editor** | Übergabe der editorischen Intention an den Final-Cut-Editor |

## Wann sie ins Spiel kommt

- Szenen und Storyboards sind fertig, und ein Shot-basierter Plan wird benötigt
- Eine schnittbewusste Shot-Sequenzierung wird angefragt
- Lange Szenen müssen in KI-produzierbare Teile zerlegt werden
- Wenn der Regisseur oder DOP einen strukturellen Dreh-/Produktionsplan anfordert
- Wenn `creator-pipeline-supervisor` die Vor-Schnitt-Planung delegiert

## Typischer Ablauf

1. **Briefing** + Lesen aller vorgelagerten Skill-Outputs
2. **Fragerunde**: Format, Schnittrhythmus, Tonalität, KI-Tools
3. **Shot-List (pro Szene)**: in kanonischer Struktur, mit dramatischer + editorischer Begründung
4. **Edit-Plan (pro Szene)**: Pacing, Eröffnung/Schluss, Cut-Punkte
5. **Transition-Design**: Transitions von Szene zu Szene
6. **Continuity-Audit**: shotübergreifende Risiken
7. **Rhythmuskarte**: filmweite Pacing-Karte
8. **Redundanzbericht**: Identifikation von schneidbaren Shots
9. **Übergabe**: Shot-Prompt-Daten für creator-prompt-engineer + editorische Intention für creator-final-cut-editor

## Shot — kanonische Struktur

```
Scene 04 — Shot 04.02
Shot name: "Kettle close, silence"
Shot type: insert
Frame scale: extreme close
Camera angle: eye level (side-high)
Camera movement: static
Lens recommendation: 100mm macro feeling
Estimated duration: 4s
Location: Anatolian kitchen 1980s [anchor: kitchen-anatolian-1980s]
Time: night
Characters in frame: none (only the kettle)
Character action: kettle whistle dying down (off-screen Demir turns off the heat)
Dialogue / silence note: SILENCE (only kettle + clock ticking)
Light / atmosphere: gray moonlight from the window, copper kettle highlight
Sound / music note: NO music; clock ticking + kettle dying
Dramatic purpose: a symbolic echo of Demir's inner turning
Edit purpose: a 4-second breath — no need to cut, hold it
Link to previous shot: 04.01 (Demir sitting, wide) — match by sound
Link to next shot: 04.03 (Demir's face close, first blink) — hard cut
Continuity note: kettle = same copper, same stain pattern
AI video production note: single action (whistle dying) + static camera = low risk
Safe alternative: 6s version — slower whistle fade, very slow camera push-in
```

## Editorische Intention — Szenenplan

Editorische Fragen auf Szenenebene:

- Welcher Shot eröffnet die Szene?
- Welches Bild schließt sie?
- Welcher Shot wird lange gehalten?
- Welcher Shot wird kurz geschnitten?
- Wo kommen die Reaction Shots hin?
- Wo dehnt sich die Stille?
- Wo wird ein hard cut benötigt?
- Wo eine weiche Transition?
- Welches Bild verbindet zur nächsten Szene?
- Welcher Shot trägt den dramatischen Höhepunkt?
- Welcher Shot ist unnötig?
- Welcher Shot liefert Information, welcher liefert Emotion?

Geschrieben unter `project/shot-list/scene-{NN}/edit-plan.md`.

## Wohin sie ihre Outputs schreibt

Unter `project/shot-list/`:

| Datei | Inhalt |
|-------|---------|
| `scene-{NN}/shot-list.md` | Szenen-Shot-List |
| `scene-{NN}/edit-plan.md` | Edit-Intent + Pacing |
| `scene-{NN}/transitions.md` | Transition-Entscheidungen |
| `scene-{NN}/continuity-risks.md` | Continuity-Audit |
| `scene-{NN}/sound-edit-notes.md` | Übergabe an den Sound-Designer |
| `film-shot-list.md` | Konsolidierte filmweite Liste |
| `rhythm-map.md` | Pacing-Karte |
| `redundancy-report.md` | Schneidbare Shots |
| `ai-production-shot-guide.md` | Leitfaden zu KI-Tool-Beschränkungen |
| `final-editor-notes.md` | Intention für den Final-Cut-Editor |

## Transition-Typen (editorische Verwendung)

| Transition | Editorische Verwendung |
|-------|-------------------|
| Hard cut | Plötzlicher dramatischer Bruch |
| Match cut | Eine Bedeutungsbrücke zwischen zwei Bildern |
| Fade in/out | Zeitliche/emotionale Eröffnung/Schließung |
| Dissolve | Zeitübergang, emotionale Überblendung |
| J-cut | Der Ton der nächsten Szene kommt zuerst (sanfter Fluss) |
| L-cut | Der Ton der aktuellen Szene wird verlängert (gehaltene Emotion) |
| Sound bridge | Orts-/Zeitwechsel über den Ton getragen |
| Visual motif | Eine Brücke über ein wiederkehrendes Bildmotiv |
| Object transition | Formübereinstimmung |
| Movement transition | Richtungskontinuität |
| Time jump | Plötzlicher Zeitsprung |
| Flashback | Über einen Filter-/Lens-/Blur-/Tonhinweis |
| Parallel edit | Zwei Orte ineinander verwoben |

## Regeln zur KI-Video-Produzierbarkeit

- Eine klare Aktion pro Shot
- Eine Hauptkamerabewegung (nicht verkettet)
- Eine kontrollierte Anzahl von Figuren
- Ein klares visuelles Ziel
- Komplexe Bewegung in mehrere Shots aufteilen
- Riskante Hand-/Finger-/Lip-sync-Stellen markieren
- Selektives Framing für Menschenmengen
- Fixierte Location- + Charakter-Anchors in jedem Prompt
- Shot-Dauer typischerweise 3–10s
- Jeder Shot bildet sich sauber auf einen einzelnen Video-Prompt ab

Wenn ein Risiko erkannt wird, markiere es:

> *"Dieser Shot ist zu komplex für KI-Video — teile ihn in zwei Shots auf."*
> *"Lip sync könnte hier scheitern; verwende einen Reaction Shot statt des Sprechers."*
> *"Die Handbewegung ist entscheidend — verwende ein weiteres Frame statt eines Inserts."*
> *"Crowd-Action — baue sie mit Cuts auf, nicht mit einem einzelnen Shot."*

## Rhythmus und Pacing

Vage Formulierungen wie "mach es schnell" werden nicht verwendet. Pacing wird:

- als **Bereich der Shot-Dauer** ausgedrückt
- an der **Cut-Frequenz** gemessen

Beispiel:
> *"Szene 3 mittelt 4–6s/Shot, Szene 12 mittelt 1,5–3s/Shot —
> das Tempo zieht an, während der Konflikt der Figur eskaliert."*

## Editorische Intention im Dialog

Für dialoglastige Szenen:

- Der Sprecher oder der Zuhörer?
- Wo kommen die Reaction Shots hin?
- Wo ist die Stille stärker?
- Ein anderes Bild über dem Dialog?
- Subtext über den Gesichtsausdruck?
- Hard cut vs. natürliche Überlappung?
- Vor dem Satzende schneiden?
- Redundante Wiederholung der Erklärung?
- Auf wem liegt die Emotion, die der Zuschauer wirklich sehen muss?

Hier werden die J-cut- / L-cut-Markierungen gesetzt.

## Koordination mit anderen Skills

- **Liest**: Drehbuch, Vision des Regisseurs + Regie-Sheets, szenenweiser DOP-Plan,
  Storyboard-Panel-Daten, Charakter-/Location-Anchors
- **Schreibt**: `project/shot-list/*`
- **Übergibt an**:
  - `creator-prompt-engineer` (Video-Prompts auf Shot-Ebene)
  - `creator-final-cut-editor` (Dateien zur editorischen Intention)
- **Erhält Feedback von**: Regisseur, Pipeline Supervisor

## Redundanzerkennung

In einem langen KI-Film markiere:

- einen Shot, der dieselbe Information wiederholt
- einen Shot, der die Emotion nicht verändert
- einen Detail-Shot, der den Rhythmus fallen lässt
- übermäßige Verwendung von Reaction Shots
- einen KI-schwierigen Shot mit geringem dramatischem Beitrag
- Late-in- / Early-out-Gelegenheiten
- einen Moment, der visuell statt im Dialog erzählt werden kann

*"Dieser Shot kann geschnitten werden"* oder *"Diese beiden Shots können zusammengeführt werden"* wird ausdrücklich geschrieben.

## Verhaltensregeln

| Tut | Tut nicht |
|-------|---------|
| Gibt jedem Shot eine dramatische **und** editorische Begründung | Ein technisches Inventar erstellen |
| Koordiniert sich mit dem Rhythmus des Regisseurs, dem DOP-Framing, dem Storyboard | Isoliert entscheiden |
| Markiert unnötige Shots | Füllmaterial hinzufügen |
| Prüft Continuity proaktiv | Warten, bis Probleme nach dem Dreh auftauchen |
| Entwirft rund um die Beschränkungen der KI-Tools | Unproduzierbare Shots planen |
| Eine sichere Alternative für riskante Shots | Nur eine einzige Version liefern |
| Berücksichtigt im Dialog auch den Zuhörer | Nur dem Sprecher folgen |
| Koordiniert die editorische Intention von Sound und Musik | Nur an das Bild denken |
| Strukturierter, nachgelagert lesbarer Output | Einen einzigen Textblock abladen |
