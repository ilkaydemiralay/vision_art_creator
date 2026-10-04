# vision_art_creator

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · **Deutsch** · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

> Ein KI-Filmproduktions-Skill-Paket für [Claude Code](https://claude.com/claude-code).

`vision_art_creator` bündelt **11 `creator-*`-Skills**, die jede Abteilung
einer Filmproduktion abdecken — vom Drehbuch bis hin zum finalen Schnitt — in
einem einzigen Repository. Installiere es auf jedem Rechner mit `git clone` +
`./install.sh`.

> Die Skills sind so konzipiert, dass sie aufeinander verweisen
> (`creator-pipeline-supervisor` orchestriert die übrigen). Es wird empfohlen,
> sie alle gemeinsam zu installieren.

---

## Installation

```bash
git clone https://github.com/ilkaydemiralay/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

`install.sh` erstellt für jeden Skill einen **Symlink** unter
`~/.claude/skills/<skill-name>`, der in dieses Repo zurückverweist. Der Vorteil:
Für ein Update genügt ein einfaches `git pull` — keine Neuinstallation
erforderlich.

### Optionen

```bash
./install.sh --target /path/to/skills   # in ein anderes Skills-Verzeichnis installieren
./install.sh --force                    # bestehende Namen überschreiben
./uninstall.sh                          # die Symlinks entfernen
```

`uninstall.sh` entfernt nur Symlinks, die in dieses Repo verweisen — fremde
Links und echte Verzeichnisse bleiben unangetastet (sofern nicht `--force`).

### Überprüfen

Starte nach der Installation Claude Code neu und gib ein:

```
/creator-pipeline-supervisor
```

Prüfe, ob alle 11 `creator-*`-Skills in der Skill-Liste erscheinen.

---

## Was im Paket steckt

| Skill | Zusammenfassung |
|---|---|
| `creator-pipeline-supervisor` | Orchestriert die gesamte Produktion, taktet die Abteilungen, sorgt für Kontinuität, führt die QC durch und erstellt den Bericht zur Auslieferungsbereitschaft. |
| `creator-director` | Übersetzt das Drehbuch in eine einheitliche Regievision: Szenenführung, schauspielerische Leistung, Blocking, tonale Kontrolle. |
| `creator-screenwriter` | Verfassen und Überarbeiten von Drehbüchern, Treatments, Loglines, Szenengliederungen und Dialogen. |
| `creator-character-designer` | Entwirft die Figur als integriertes Ganzes: Psychologie, Biografie, visuelle Identität, Kostüm, Requisiten, FACS-codierte Mimik. |
| `creator-production-designer` | Baut die Welt des Films: Drehorte, Sets, Requisiten, Epochenatmosphäre, Farb- und Materialsprache, Kontinuitätsanker. |
| `creator-cinematographer` | Gestaltet die visuelle Sprache: Licht, Kamera, Objektiv, Bildausschnitt, Farbe, Atmosphäre, Bewegung. |
| `creator-storyboard-artist` | Visualisiert Szenen Panel für Panel: Einstellungsgrößen, Winkel, Blocking, Komposition, KI-Prompts. |
| `creator-shot-list-designer` | Verwandelt Szenen und Storyboards in eine technische Shot-Liste, aufgeteilt in KI-produzierbare Häppchen. |
| `creator-sound-music-designer` | Die klangliche Welt des Films: Atmosphäre, Foley, SFX, Score, Leitmotive, szenenweiser Musikplan, KI-Audio-Prompts. |
| `creator-prompt-engineer` | Wandelt die Ergebnisse jeder Abteilung in konsistente Prompts für GPT Image 2.0, Nano Banana, Sora, Veo, Runway, Kling, Higgsfield und mehr um. |
| `creator-final-cut-editor` | Fügt KI-generierte Shots/Audio/Musik/Grafiken zu einem fertigen Film zusammen: Rough/Fine/Final Cut, KI-Fehler-Triage, Auslieferungsformate. |

Die vollständige Definition jedes Skills befindet sich in seiner eigenen
`SKILL.md`-Datei.

---

## So funktioniert es

Das Paket läuft auf **dateisystembasiertem gemeinsamem Zustand**. Alle Skills
lesen aus einem gemeinsamen `project/`-Baum und schreiben in ihn (`bible/`,
`screenplay/`, `characters/`, `storyboards/`, `prompts/`, `cuts/`, `qc/`, …).
`creator-pipeline-supervisor` pflegt die kanonischen Dateien (die Projekt- und
Kontinuitäts-„Bibeln“) und prüft die Ergebnisse jeder Abteilung daran ab.

Die kanonische Pipeline:

```
0. project bible & vision
1. creator-screenwriter        → screenplay
2. creator-director            → vision, direction sheets, arcs
3-4-5. creator-character-designer + creator-production-designer
        + creator-cinematographer        (run in parallel)
6. creator-storyboard-artist   → panels with prompts
7. creator-shot-list-designer  → shot list + edit plan
8. creator-prompt-engineer     → tool-fit image + video prompts
   → [AI material generation — operator]
9. creator-sound-music-designer → sound + score plan
10. creator-final-cut-editor   → rough → fine → final cut → delivery

Throughout: creator-pipeline-supervisor enforces continuity, runs QC,
manages revision loops, and holds the bibles.
```

Die Reihenfolge ist kanonisch, aber nicht starr: Regie-Feedback kann die
Drehbuchautoren erneut auslösen, und Figuren-, Produktions- und Kameraarbeit
laufen typischerweise parallel, sobald die Regievision feststeht.

---

## Aufgezeichneter Graph-Modus (optional, experimentell)

Seit v1.1.0 enthält das Paket einen optionalen, maschinell prüfbaren Workflow für eine einzelne Szene. `creator-pipeline-supervisor` kann die Vorproduktion als Graph mit 12 Knoten ausführen: Jedes Artefakt wird mit seinem SHA-256-Hash erfasst, jede Freigabe ist an genau die geprüften Eingaben gebunden, und eine Revision führt nur die betroffenen Knoten erneut aus.

- Workflow: `workflows/single-scene.v1.json`. Vertrag: `skills/creator-pipeline-supervisor/references/graph-workflow.md`.
- JSON-Schemas in `schemas/`, ein schreibgeschützter Validator in `scripts/validate_graph.py`, Tests in `tests/`.
- Ein ausgearbeiteter Textpilot mit 15 Sekunden und drei Einstellungen in `examples/single-scene/`: v00 stoppt an einem Designkonflikt, v01 löst ihn, v02 ändert die Farbe eines Requisits.

Für die normale Nutzung der Skills ist kein Python nötig. Validator ausführen (Python 3.10+):

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-graph.txt
.venv/bin/python -m unittest discover -s tests
.venv/bin/python scripts/validate_graph.py validate --manifest path/to/manifest.json
```

Grenzen: ein reiner Textpilot eines einzelnen Autors. Parallele Abteilungsläufe, Mediengenerierung, Schnitt und Kosten wurden nicht getestet. Identität der Freigebenden und Zeitstempel werden vom Operator angegeben, nicht signiert. Design- und Ergebnisnotizen liegen in `docs/` (auf Türkisch).

---

## Aktualisieren

```bash
cd ~/projects/vision_art_creator
git pull
```

Da die Skills per Symlink eingebunden sind, ist kein weiterer Schritt nötig.

Was sich in jeder Version geändert hat, steht in [CHANGELOG.md](CHANGELOG.md). **v1.1.0:** `creator-cinematographer` und `creator-storyboard-artist` legen Prompt-Entwürfe jetzt in ihren eigenen Ordnern ab; nur `creator-prompt-engineer` schreibt finale Prompts nach `project/prompts/`.

---

## Entwicklung

1. Bearbeite einen Skill im Repo (`skills/creator-*/SKILL.md`).
2. Teste die Änderung in Claude Code — da es sich um einen Symlink handelt,
   wird sie sofort wirksam.
3. Committe + pushe.

So fügst du einen neuen Creator-Skill hinzu:

```bash
mkdir -p skills/creator-new-skill
# write SKILL.md and README.md
./install.sh   # create the symlink for the new skill
```

---

## Übersetzungen

Diese README sowie die `README.md` jedes Skills sind in 12 Sprachen verfügbar
(siehe die Sprachauswahl oben). Die `SKILL.md`-Anweisungsdateien werden bewusst
auf Englisch gehalten — Claude antwortet zur Laufzeit in der Sprache des
Nutzers, und ein einziger kanonischer Anweisungssatz vermeidet doppelte
Skill-Namen.

---

## Lizenz

[MIT](LICENSE) © 2026 İlkay Demiralay.
