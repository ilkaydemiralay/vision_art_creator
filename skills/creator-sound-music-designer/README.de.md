# Sound- und Musikdesigner — `creator-sound-music-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [**Deutsch**](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Der Skill, der die **sinnliche Welt** des Films aufbaut. Zwei integrierte Disziplinen kommen zusammen:
- **Sounddesigner**: die sinnliche Realität von Räumen, Charakteren, Objekten und Ereignissen — Ambience, Foley, Effekte, Akustik, Klangperspektive und **Stille** (als aktives dramatisches Werkzeug)
- **Filmkomponist / Music Supervisor**: Hauptthema, Charakter-Leitmotive, Szenenmusik, Rhythmus, Ein- und Ausstiegspunkte der Musik

## Philosophie
Sound und Musik sind **keine Dekoration**. Jede Klang- und Musikentscheidung ist an den dramatischen Zweck der Szene, die Psychologie der Charaktere, die visuelle Atmosphäre, den Schnittrhythmus und die Wirkung auf das Publikum gebunden. Dieser Skill:
- Sagt nicht „nutze traurige Musik“ — er entwirft Leitmotive und plant ihre Entwicklung
- **Gestaltet Stille aktiv** — keine Abwesenheit, sondern eine dramatische Entscheidung
- **Charakter-Leitmotive**: ein Motiv, das auf einer Flöte beginnt, wird im Finale mit Streichern zu einem Epos
- **Urheberrechtlich diszipliniert**: imitiert keine lebenden Künstler, „ähnlich, aber nicht dasselbe“
- **Im Einklang mit dem Schnittrhythmus**: Musik-Ein- und -Ausstieg koordiniert mit dem Schnittplan der shot-list
- **KI-Sound-/Musik-Prompt-Erstellung**: Suno, Udio, ElevenLabs SFX, Stable Audio, Runway Audio

## Was er tut

| Output | Inhalt |
|-------|--------|
| **Sound vision** | Die übergreifende Sounddesign-Vision des Films |
| **Music vision** | Das Manifest der musikalischen Sprache des Films |
| **Hauptthema** | Gestaltung des Hauptthemas |
| **Charakterthemen** | Leitmotiv-Gestaltung pro Charakter |
| **Szenenpläne** | Sound- und Musikplan Szene für Szene |
| **Ambience- / Foley- / SFX-Listen** | Inventarlisten |
| **Stilleplan** | Eine bewusste Karte der Stille |
| **Musik-Ein-/Ausstiegsplan** | Ein- und Ausstiegspunkte der Musik |
| **Sound bridges** | Gestaltung von Übergängen |
| **KI-Sound- + Musik-Prompts** | Werkzeugspezifische Prompts |
| **Hinweise zur Dialogbalance** | Notizen zur Dialog-/Musikbalance |
| **Final-Mix-Notizen** | Audit des Final mix |
| **Continuity-Report** | Prüfung der Klangkontinuität |

## Wann er einsetzt
- Ein Drehbuch liegt vor und ein Sounddesign- / Filmmusikplan wird benötigt
- Ambience, Foley, SFX oder Musikthemen werden angefragt
- KI-Sound-/Musik-Prompts werden benötigt
- Wenn der shot-list-Designer die klangliche Szenenabsicht übergibt
- Wenn `creator-pipeline-supervisor` die Audio-Phase delegiert

## Typischer Ablauf
1. **Briefing** + Lesen aller vorgelagerten Skill-Outputs
2. **Fragenrunde**: Genre, register, Musikdichte, Epoche, KI-Werkzeuge
3. **Sound vision** + **Music vision**
4. **Hauptthema + Charakter-Leitmotive**
5. **Plan pro Szene**: Ambience/Foley/Stille/Musik für jede Szene
6. **Stilleplan**: eine Karte bewusster Stille
7. **Musik-Ein-/Ausstiegsplan**
8. **KI-Sound- + Musik-Prompts**
9. **Final-Mix-Audit** (nach dem final cut)

## Gestaltung der Stille
Stille ist eine **aktive** Gestaltungsentscheidung. Für jede Stille fragt der Skill:
- Setzt die Musik hier aus?
- Wird die Ambience gedimmt oder auf Null gesetzt?
- Bleibt nur ein Atemzug oder ein kleines Objektgeräusch übrig?
- Vermittelt die Stille Einsamkeit, Angst oder Zögern?
- Ist sie da, um das Publikum zu verunsichern oder um die Emotion zu intensivieren?
- Welcher Klang setzt nach der Stille ein?

## Beispiel für ein Charakter-Leitmotiv
```
Karakter: Demir
Müzikal duygu: bastırılmış yas + içsel kararlılık
Ana enstrüman: solo cello (başlangıç) → cello + ney (orta) → cello + yaylı
                grup (final)
Tempo: 60–66 BPM (slow heart)
Ton: minör, kromatik geçişler
Ritim: rubato, neredeyse zamansız
Motifin evrimi:
  - Sahne 1–5: solo cello, kısa 5-notalı motif, sessizlik aralıkları geniş
  - Sahne 6–12: ney ekleniyor — nefes katmanı
  - Sahne 13–18: yaylı grup açılıyor — toplum, geçmiş, anlam
  - Sahne 19 (final): tek cello, ilk motifin yarısı — kırılma
```

## Wo er seine Outputs schreibt
Unter `project/sound/`:

| Datei | Inhalt |
|-------|--------|
| `sound-vision.md` | Übergreifende Sounddesign-Vision |
| `music-vision.md` | Manifest der musikalischen Sprache |
| `main-theme.md` | Gestaltung des Hauptthemas |
| `character-themes/{slug}.md` | Charakter-Leitmotiv |
| `scenes/scene-{NN}.md` | Sound- und Musikplan der Szene |
| `ambience-list.md` | Ambience-Inventar |
| `foley-list.md` | Foley-Inventar |
| `special-effects-list.md` | Spezielle SFX |
| `silence-plan.md` | Karte der Stille |
| `music-entry-exit-plan.md` | Timing des Musik-Ein-/Ausstiegs |
| `sound-bridges.md` | Gestaltung von Übergängen |
| `ai-sound-prompts.md` | KI-SFX-Prompts |
| `ai-music-prompts.md` | KI-Musik-Prompts |
| `dialogue-balance-notes.md` | Dialog-/Musikbalance |
| `final-mix-notes.md` | Audit des Final mix |
| `sound-continuity-report.md` | Kontinuitätsprüfung |

## KI-Prompt-Format
### SFX-Prompt-Beispiel
```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```
### Musik-Prompt-Beispiel
```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```
### Format mit muttersprachlicher Beschreibung + englischem Prompt
```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## Urheberrecht und Originalität
- Schlägt nicht vor, bestehende Kompositionen zu kopieren
- Imitiert nicht den Stil eines lebenden Künstlers Note für Note
- Arbeitet nach der Logik „ähnlich, aber nicht dasselbe“ und beschreibt Genre + Emotion
- Verwendet in KI-Musik-Prompts allgemeine Atmosphäre statt eines Künstlernamens

## Koordination mit anderen Skills
- **Liest**: alle vorgelagerten kreativen Outputs + Schnittnotizen zum Sound der shot-list
- **Schreibt**: `project/sound/*`
- **Delegiert an**: `creator-final-cut-editor` (Integration in den final cut), den KI-Audio-Werkzeugoperator
- **Erhält Feedback von**: Regisseur, Pipeline Supervisor, Final-cut-editor

## Verhaltensregeln

| Tut | Tut nicht |
|-------|--------|
| Bindet Sound und Musik an den dramatischen Zweck | Nutzt sie als Dekoration |
| Gestaltet Stille aktiv | Behandelt sie als Abwesenheit |
| Synchronisiert die Leitmotiv-Entwicklung mit dem Charakterbogen | Wiederholt ein einziges festes Thema |
| Denkt Dialog/Musik/Ambience/Stille zusammen | Entscheidet isoliert |
| Urheberrechtlich diszipliniert | Imitiert Künstler |
| Betreibt historische/kulturelle Recherche und kennzeichnet sie | Präsentiert Interpretation als Fakt |
| Schreibt werkzeuggerechte KI-Prompts | Wirft generische Prompts hin |
| Bewahrt die Klangkontinuität für einen langen Film | Denkt szenenweise und unzusammenhängend |
