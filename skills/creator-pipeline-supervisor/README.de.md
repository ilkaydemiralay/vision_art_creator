# Pipeline- & Continuity-Supervisor — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Der **Orchestrator** und **Continuity-Supervisor** eines KI-Filmprojekts. Zwei
integrierte Disziplinen kommen zusammen:

- **Pipeline supervisor**: welcher Skill wann läuft, wo der gemeinsame State
  lebt, wie Revisionen in Schleifen laufen, wie Versionen getrackt werden, wie
  das Projekt geshippt wird
- **Continuity supervisor**: prüft die Konsistenz von Charakter, Kostüm,
  Location, Prop, Licht, Farbe, Ton, Zeit und Schnittrichtung Szene für Szene
  und Abteilung für Abteilung — erkennt Widersprüche früh, fordert Fixes an

## Philosophie

Der Pipeline-Supervisor ist kein „Checklist-Tool". Er denkt wie eine
Kombination aus **Unit Production Manager + Script Supervisor**. Er behält das
gesamte Projekt im Kopf und lässt die Arbeit keiner Abteilung von der
kohärenten Intention des Films abdriften. Dieser Skill:

- **Hält eine einzige Source of Truth**: `bible/continuity-bible.md` regiert
  alles
- **Production status table** stets aktuell — die Antwort auf „was soll ich
  jetzt tun"
- **Locked-Anchor-Disziplin**: Charakter-DNA + Location Master Reference +
  Style Block — geht verbatim in jeden Prompt ein
- **Cross-skill arbitration**: bei Konflikt zweier Abteilungen vermittelt er
  beide Positionen, präsentiert Optionen mit Bezug auf die Regie-Vision und
  eskaliert an den Nutzer
- **Revision-Loop-Management**: findet ein nachgelagerter Skill ein Problem
  upstream, kaskadiert er in kanonischer Reihenfolge
- **Risk register**: proaktives Risiko-Tracking, Mitigation-Verfolgung
- **Ship Gate**: sagt nicht „fertig" ohne ein Delivery-Readiness-Audit

## Was er produziert

| Output | Inhalt |
|--------|--------|
| **Project bible** | Projekt-Canon auf hoher Ebene |
| **Style bible** | Cross-skill Style-Canon |
| **Continuity bible** | Continuity Single Source of Truth |
| **Prompt blocks** | Konsolidierte Locked Prompt Blocks |
| **Production status table** | Skill-×-Szene-Statusmatrix |
| **Risk register** | Risiko- + Severity- + Mitigation-Log |
| **Continuity audit reports** | Domänenbasierte Audits |
| **Revision request manifests** | Cross-skill Revisionsanfragen |
| **Prompt consistency report** | Pre-Generation-Audit |
| **AI generation error summary** | Post-Generation-Audit |
| **Final QC report** | Gesamtprojekt-Audit |
| **Delivery readiness** | Ship Gate (pass/fail) |
| **Decisions log** | Datierte Entscheidungshistorie |

## Wann er einspringt

- Ein neues KI-Filmprojekt wird gestartet
- Ein Cross-skill-Konsistenz-Audit wird in einem laufenden Projekt angefordert
- Bei der Frage „was soll ich jetzt tun" (die Antwort kommt aus dem Production
  Status)
- Wenn eine Continuity- oder Pipeline-Frage eine Skill-Grenze überschreitet
- Ein Delivery-Readiness-Audit wird angefordert
- Frage zur Ordnerstruktur / File Organization
- Wenn eine Revision zu abhängigen Skills kaskadieren muss

## Wann er NICHT einspringt

- Kreativarbeit eines einzelnen Skills (der Specialist arbeitet allein)
- Einfache Single-Shot-Generierung
- Rein technische Fragen außerhalb der Filmproduktion

## Canonical pipeline

```
0. project bible & vision
1. creator-screenwriter
2. creator-director
3-4-5. character + production + DOP (parallel)
6. creator-storyboard-artist
7. creator-shot-list-designer
8. creator-prompt-engineer
   → [AI material generation — operator]
9. creator-sound-music-designer
10. creator-final-cut-editor

In allen Phasen: creator-pipeline-supervisor übernimmt Continuity, QC, Revision, Bible-Management
```

Die Reihenfolge ist **kanonisch, aber nicht starr**:
- **Iterative Loops**: creator-director-Feedback → neue v von creator-screenwriter
- **Parallelarbeit**: nach der Regie-Vision laufen character/production/DOP
  parallel

## Continuity domains (Audit-Bereiche)

1. Story / plot
2. Time / chronology
3. Character (physical)
4. Character arc (emotional)
5. Costume
6. Hair / makeup
7. Accessories / props
8. Location
9. Set dressing
10. Light direction
11. Color palette
12. Camera language
13. Sound / ambience
14. Music theme (leitmotif)
15. Emotional flow
16. Edit / screen direction
17. AI prompt consistency (locked anchors verbatim)
18. Reference image consistency
19. Scene / shot numbering

Für jede Domäne gibt es ein Risiko-Log: `project/qc/continuity-reports/`.

## Continuity bible (Single Source of Truth)

`project/bible/continuity-bible.md` — diese Datei ist die **Autorität**. Steht
der Output eines Skills im Konflikt mit der Bible, gewinnt die Bible (oder die
Bible wird aktualisiert).

Ihr Inhalt:
- Locked character anchors (DNA verbatim)
- Locked location anchors (master reference verbatim)
- Costume-Continuity-Tabelle (Szene × Charakter)
- Time-/Weather-Tabelle
- Prop-Continuity-Tabelle
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction (screen direction × scene)
- Offene Continuity-Fragen (warten auf eine Regie-Entscheidung)
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`:

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

Nach jedem Skill-Run aktualisiert. Die Quelle der Antwort auf „was soll ich jetzt tun?".

## Revision-Loop-Management

Findet ein nachgelagerter Skill ein Problem upstream:

1. **Origin-Erkennung**: welcher Skill-Output ist fehlerhaft?
2. **Blast radius**: wie wirkt sich der Fix auf abhängige Skills aus?
3. **Change request**: `qc/revision-notes/req-{NN}.md`
4. **Entscheidung**: Fix am Origin (tief, langsam) vs. Workaround (oberflächlich, schnell)
5. **Origin fix**: Skill wird neu getriggert, Abhängige gehen auf 🟡, Cascade in kanonischer Reihenfolge
6. **Workaround**: wo, warum und wer ihn angewandt hat, wird festgehalten
7. **Resolution log**: angehängt an „Resolved decisions" der Continuity Bible

## Cross-skill arbitration

Bei Konflikt zweier Skills (z. B. warmes Licht des DOP vs. kühle Charakter-Palette):

1. Beide Vorschläge **verbatim** zitieren
2. Den Konflikt in klarer Sprache benennen
3. Bezug auf die Director Vision
4. 2–3 Lösungen + Trade-offs präsentieren
5. An Nutzer / Regie eskalieren
6. Die Entscheidung wird in die Continuity Bible geschrieben

**Er wählt nicht stillschweigend** — er macht den Konflikt sichtbar.

## Risk register

`project/qc/risk-register.md`:

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| Lip-Sync-Fehlerrisiko in Szene 7 | medium | high | creator-shot-list-designer | Reaction Shot nutzen | mitigating |
| KI-Risiko beim Hand-Insert in Szene 12 | medium | medium | creator-prompt-engineer | Backup mit Wider Framing | mitigated |
| „Navy coat"-Hue-Drift | low | high | creator-character-designer | Hex in DNA gesperrt | mitigated |

## Ordnerstruktur (zwei Optionen)

### Default (named — einfach)

`project/screenplay/`, `project/characters/`, `project/cuts/` ...

### Alternate (numbered — für große Projekte)

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

Gleicher Inhalt, nummeriert und für visuelles Scannen geeignet. Default ist
named; bietet bei Bedarf eine Migration an.

## Wohin er seine Outputs schreibt

Unter `project/bible/` und `project/qc/` (er schreibt NICHT DIREKT in die
Verzeichnisse anderer Skills — er sendet ihnen Revision Requests):

| Datei | Inhalt |
|-------|--------|
| `bible/project-bible.md` | Projekt-Canon auf hoher Ebene |
| `bible/style-bible.md` | Cross-skill Style-Canon |
| `bible/continuity-bible.md` | Continuity Single Source of Truth |
| `bible/prompt-blocks.md` | Locked Prompt Blocks |
| `qc/production-status.md` | Skill-×-Szene-Statusmatrix |
| `qc/risk-register.md` | Risiko-Log |
| `qc/continuity-reports/{topic}.md` | Domänen-Audits |
| `qc/revision-notes/req-{NN}.md` | Revision Request |
| `qc/prompt-consistency-report.md` | Pre-Generation-Audit |
| `qc/ai-generation-error-summary.md` | Post-Generation-Audit |
| `qc/final-qc-report.md` | Gesamtprojekt-Audit |
| `qc/delivery-readiness.md` | Ship Gate |
| `qc/decisions-log.md` | Datierte Entscheidungshistorie |

## Typischer Ablauf (neues Projekt)

1. Nutzer-Briefing
2. `bible/project-bible.md` schreiben
3. → **creator-screenwriter** triggern
4. Script v1 → **creator-director** triggern
5. Vision → parallel: **character + production + DOP**
6. Cross-Palette-Audit; Konflikte flaggen
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. `bible/prompt-blocks.md` build/update
10. → **creator-prompt-engineer**
11. Pre-Generation-Audit
12. [AI material — der Operator führt es aus]
13. Post-Generation-Audit
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision Loops
17. Final QC + Delivery Readiness
18. Ship

## Delivery readiness audit (Ship Gate)

Bevor es als fertig gilt:

- ✅ Alle Szenen sind im Production-Status
- ✅ Continuity-Audit sauber (oder nur Minor Flags)
- ✅ Final Cut regie-abgenommen
- ✅ Audio-Integration-Audit sauber
- ✅ KI-Fehler triagiert (kein kritisches 🔴)
- ✅ Color Grade angewandt oder absichtlich geflaggt
- ✅ Subtitles vollständig und timed
- ✅ Title Cards / Credits an Ort und Stelle
- ✅ Master für alle Deliverable-Plattformen unter `project/delivery/`
- ✅ Trailer Cut produziert (falls angefordert)
- ✅ Archive Master gespeichert
- ✅ Dokumentation aktuell (Bible, Continuity, Prompt-Blocks)

## Koordination mit anderen Skills

- **Liest**: alle Skill-Outputs (alles in `project/`)
- **Schreibt**: `project/bible/*`, `project/qc/*` — schreibt NICHT DIREKT in
  andere Verzeichnisse
- **Triggert**: alle Specialist-Skills
- **Arbitriert**: Cross-skill-Konflikte

## Verhaltensregeln

| Tut | Tut nicht |
|-----|-----------|
| Erzwingt die Treue zur Director Vision in jeder Abteilung | Lässt stilles Abdriften zu |
| Bei Cross-skill-Konflikt zitiert er beide Seiten **verbatim** | Wählt stillschweigend eine Seite |
| Dokumentiert jede Entscheidung mit Datum + Begründung | Handelt ohne Protokoll |
| Schützt die Continuity Bible als Autorität | Lässt Output durch, der mit der Bible kollidiert |
| Aktualisiert Production-Status nach jedem Skill-Run | Lässt eine stale Tabelle zurück |
| Kaskadiert Revisionen in kanonischer Reihenfolge | Überspringt einen abhängigen Skill |
| Eskaliert kreative Disputes an Nutzer / Regie | Arbitriert im Alleingang |
| Continuity-Audit an jedem Act Break eines langen Films | Auditiert nur am Ende |
| Proaktives Risk Register | Hält ein kritisches 🔴 zurück |
| Sagt kein „Ship", solange delivery-readiness.md nicht green ist | Erklärt es zu früh als complete |
| Strukturierter, machine-readable Output | Kippt einen einzigen Textblock aus |
