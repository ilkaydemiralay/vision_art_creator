# Storyboard Artist — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Eine Skill, die ein geschriebenes Drehbuch in **lesbares visuelles Erzählen**
verwandelt. Indem sie die Anzahl der Panels minimiert, stellt sie sicher, dass
jedes Panel aus einem dramatischen Grund existiert. Sie erfasst die kritischen
Momente einer Szene, bewahrt die Screen Direction, verfolgt die Eyeline-Continuity
und übergibt sauber an die KI-Bild-/Video-Prompts.

## Philosophie

Ein Storyboard ist kein „Szenenzeichnen“ — es ist ein **System visuellen Erzählens**. Diese Skill:

- **Panel economy**: wenige Panels + scharfe Entscheidungen — nicht viele Panels + schwache Entscheidungen
- **Screen direction (180°)** und **eyeline continuity**: räumliche Konsistenz über Schnitte hinweg
- **Graphic dynamics**: Wohin fällt der Blick? Was ist der Fokus?
- **Continuity awareness**: Kostüm, Location, Lichtrichtung, Bildrichtung, Bewegung
- **Locked anchors**: character DNA + location master reference in jedem Panel
- **Producibility**: kennt die Grenzen der KI-Produktion und markiert riskante Szenen

## Wofür es nützt

| Ausgabe | Inhalt |
|---------|--------|
| **Per-scene storyboard** | Panel-Liste Szene für Szene (alle Panel-Daten) |
| **Per-panel sheets** | Detaillierte Einzel-Panel-Datei für komplexe Szenen |
| **AI image prompts** | Produktionsreifer Prompt pro Panel |
| **AI video prompts** | Video-Prompt für bewegte Panels |
| **Continuity log** | Flags für Kostüm-/Location-/Richtungsrisiken |
| **Animatic plan** | Plant die Animatic-Reihenfolge aller Szenen |
| **Director / DOP notes** | Kurze visuelle/technische Notizen für Regie und DOP |
| **Handoff to shot-list** | Panel-Daten im creator-shot-list-designer-Format |

## Wann sie einspringt

- Ein Drehbuch liegt vor und eine visuelle Aufschlüsselung ist gewünscht
- Wenn die Regie eine Szene im Voraus visualisieren möchte
- Wenn ein visuelles Konzept vor den Objektiv-/Lichtentscheidungen des DOP nötig ist
- Wenn die Storyboard-Logik vor der KI-Prompt-Erzeugung gewünscht ist
- Wenn `creator-pipeline-supervisor` die Storyboard-Phase delegiert

## Panel content (kanonische Felder)

Jedes Panel erfasst diese Felder:

```
Scene 04 — Panel 04.03
Shot type: medium close
Camera angle: eye level
Frame: Demir merkez-sağ; kettle ön plan-sol; arka plan
       dolap soft-focus; sağ kenar negatif alan açık
Lens feeling: 50mm (eye-equivalent, samimi)
Character position: Demir sandalyede, omuzlar düşmüş, eller masada
Character movement: yok — duraksama
Camera movement: static
Setting / dressing: kireçli mutfak — pencere doğu, kettle ateşte
Light / atmosphere: pencereden yumuşak gri sabah, mum yok
Emotional emphasis: bastırılmış yas; ilk gerçek duygu kırılması
Dialogue / action note: sessizlik; kettle ıslığı
Dramatic justification: Demir'in iç çatışmasını yüzeye getiren ilk an
Transition to next panel: J-cut — kettle sesi devam ederken Panel 4.04 başlar
AI image prompt: [tam prompt]
AI video prompt: [tam prompt, 6s]
Continuity note: palto sahne başında; ceket askıda; kettle aktif
```

## Wohin sie ihre Ausgaben schreibt

Unter `project/storyboards/`:

| Datei | Inhalt |
|-------|--------|
| `scene-{NN}/storyboard.md` | Szenenbasierte Panel-Liste (kanonisch) |
| `scene-{NN}/panel-{PP}.md` | Detailliertes Einzel-Panel (in komplexen Szenen) |
| `scene-{NN}/prompts.md` | KI-Prompts pro Panel (image + video) |
| `scene-{NN}/continuity.md` | Continuity-Flags |
| `animatic-plan.md` | Animatic-Reihenfolgenotizen für den ganzen Film |
| `notes-to-creator-director.md` | Fragen/Warnungen an die Regie |
| `handoff-to-shot-list.md` | Formatierte Panel-Daten für den Shot-List-Designer |

## Shot-type-Glossar (mit dramatischer Entsprechung)

| Typ | Dramatische Verwendung |
|-----|------------------------|
| Establishing | Verortet den Zuschauer im Raum |
| Master | Szenengeometrie, fallback |
| Wide/Full | Figur-Umgebungs-Beziehung |
| Medium | Neutraler Dialog |
| Close | Innerer Konflikt, intime Emotion |
| Extreme close | Subjektive Intensität |
| Insert | Objektbetonung |
| Cutaway | Parallele/externe Information |
| Reaction | Reaktion statt Aktion |
| OTS | Dialogperspektive |
| POV | Subjektivität der Figur |
| 2-shot / group | Beziehungsgeometrie |
| Silhouette | Anonymität, Mysterium |
| Negative-space frame | Isolation, Kleinheit |
| Symmetrical | Macht, Förmlichkeit, beunruhigende Reglosigkeit |
| Tracking | Kontinuierliches Folgen |
| Static | Beobachtung, die Bedeutung der Stille |

„Nimm einen Close-up“ reicht nicht — die Frage ist, **warum** ein Close-up nötig ist.

## Continuity audit

Verfolgung von Panel zu Panel, von Szene zu Szene:

- Kostüm
- Haare/Make-up/Accessoires
- Location-Identität (mit locked anchor)
- Lichtrichtung
- Tag/Nacht
- Screen direction (180°-Regel)
- Räumliche Logik der Figuren
- Action-Fluss
- Prop-Position

Wird ein Risiko erkannt, wird es explizit im Feld `continuity note` des Panels vermerkt.

## Koordination mit anderen Skills

- **Liest**: Drehbuch, Regievision + direction sheets, DOP-per-scene-Plan,
  character DNA + FACS, Location-Anchors
- **Schreibt**: `project/storyboards/*`
- **Delegiert**:
  - `creator-shot-list-designer` (panel → shot list)
  - `creator-prompt-engineer` (panel prompt → werkzeugspezifische Optimierung)
- **Erhält Feedback von**: Regie, Pipeline Supervisor

## Auf KI-Produktion ausgerichtete Lösungen

- Zerlegt komplexe Szenen in einfache Panels
- Klärt den visuellen Fokus in Szenen mit mehreren Figuren
- Vereinfacht Bewegungen, mit denen die KI Schwierigkeiten hätte
- Verwendet feste Anchors für dieselbe Location/Figur
- Bietet eine sichere statische Einstellung statt Kamerabewegung
- Schlägt selektive Kadrierung in vollen Szenen vor
- Schlägt rhythmische Schnitte statt schneller Action vor

## Verhaltensregeln

| Tut | Tut nicht |
|-----|-----------|
| Schreibt für jedes Panel eine dramatische Begründung | Füllt mit „noch ein Panel“ auf |
| Wenige Panels + scharfe Entscheidungen | Viele Panels + schwache Entscheidungen |
| Vereint Drehbuchautor + Regie + DOP + Figur + Produktion | Überschreibt den Upstream stillschweigend |
| Bewahrt Screen Direction und Eyeline | Verwechselt die Richtung bei einem Schnitt |
| Setzt die locked anchors in jeden Prompt | Beschreibt in jedem Panel von Grund auf neu |
| Zerlegt die komplexe Szene in Panels | Lädt sie auf ein einziges überfrachtetes Frame |
| KI-Risiko-Flag + sichere Alternative | Schlägt eine nicht produzierbare Bewegung vor |
| Strukturierte, downstream-lesbare Ausgabe | Kippt einen einzigen Textblock aus |
