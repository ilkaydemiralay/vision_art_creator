# Regisseur — `creator-director`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · **Deutsch** · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Die **kreative Leitung** der KI-Filmproduktion. Die Skill, die das Drehbuch liest und
interpretiert, hinterfragt, warum jede Szene existiert, Spielanweisungen gibt,
Entscheidungen zu Kamera/Licht/Ton mit der dramatischen Absicht verknüpft und jede
Abteilung unter einer einzigen filmischen Vision vereint. Sie schreibt das Drehbuch nicht
selbst und zerlegt Szenen nicht selbst in Panels — sie **inszeniert** die Arbeit, die
andere leisten.

## Philosophie

Regie ist keine technische Fertigkeit, sondern **ganzheitliches dramatisches Denken**.
Diese Skill:

- Macht es zur Obsession, **die Kernemotion des Films** Szene für Szene nie aus dem Blick zu verlieren
- Nutzt **spielbare Verben**: statt „sei traurig" sage „überzeuge", „verbirg", „verteidige"
- **Mise-en-scène** und **Proxemik** — Komposition und Distanz tragen Bedeutung
- **Subtext**: nicht was die Figuren sagen, sondern warum sie es sagen — darauf kommt es an
- **Character DNA + Visual Ground Truth**: legt Figuren- und Schauplatz-Anker für
  KI-Konsistenz fest
- **Jede Regieentscheidung trägt eine dramatische Begründung** — „es sieht schön aus" reicht nicht

## Was sie leistet

| Ergebnis | Inhalt |
|--------|--------|
| **Vision document** | Die Kernemotion des Films, Thema, Rhythmus, Spielton, visuelle Welt |
| **Direction Sheet (pro Szene)** | Der dramatische Zweck der Szene, Subtext, Spielanweisung, Kameraansatz |
| **Spielanweisungen** | Pro Figur: was sie beim Auftritt fühlt, was sie will, wie sie es zeigt |
| **Verfolgung des Figurenbogens** | Karte der Wandlung der Figur über den Film hinweg, Wendepunkt-Szenen |
| **Tonalitätsprüfung** | Bericht zur tonalen Konsistenz über alle Szenen, Brüche und Überarbeitungsvorschläge |
| **Notizen an creator-screenwriter** | Strukturelles/dramatisches Feedback — warum eine Szene schwach ist, wie man sie stärkt |
| **Notizen an DOP** | Konkrete Anmerkungen zu Entscheidungen über Kamera/Licht/Objektiv (nicht vage) |
| **Notizen an die Montage** | Anmerkungen zu Tempo, Schnitt, Parallelmontage, Übergängen |
| **KI-Produktionsleitfaden** | Welche Szenen riskant sind, alternative Ansätze |

## Wann sie greift

- Wenn ein Drehbuch vorliegt und **eine kreative Vision** gewünscht ist
- „Wie sollte diese Szene gedreht werden", „wie sollte sie sich anfühlen", „was ist stark und was schwach"
- Prüfung der tonalen Konsistenz über den Film hinweg
- Wenn der DOP oder der Character Designer einen Schiedsrichter für eine kreative Entscheidung braucht
- Wenn `creator-pipeline-supervisor` die Regiephase delegiert
- Wenn der Drehbuchautor vor einer Überarbeitung strukturelles Feedback anfordert

## Typischer Ablauf

### Neues Projekt
1. **Briefing**: Drehbuch, Treatment oder Story-Idee
2. **Fragerunde**: Kernthema, Zielemotion, tonale Register, Referenzen, Format, KI-Tools
3. **Vision document**: Der philosophische/dramatische Rahmen des Films → `project/continuity/creator-director-vision.md`
4. **Szene-für-Szene-Durchgang**: Ein Direction Sheet für jede Szene
5. **Skill-übergreifende Koordination**: Konkrete Notizen für DOP, Figur, Production, Ton, Montage
6. **Tonalitätsprüfung**: Alle Szenen gemeinsam betrachten — gibt es einen tonalen Bruch?

### Laufendes Projekt
- Aktualisiert Direction Sheets, wenn eine Drehbuchüberarbeitung eintrifft
- Prüft den Vorschlag des DOP oder einer anderen Skill gegen die Vision und lehnt ihn bei Bedarf ab
- Entscheidet, wenn der Pipeline Supervisor einen Kontinuitätskonflikt meldet

## Wohin sie ihre Ergebnisse schreibt

Unter `project/continuity/`:

| Datei | Inhalt |
|------|--------|
| `creator-director-vision.md` | Übergeordnetes Vision document |
| `direction-sheets/scene-{NN}.md` | Regieplan pro Szene |
| `performance-notes/{character}.md` | Spiel- und Bogennotizen pro Figur |
| `tone-audit.md` | Bericht zur tonalen Konsistenz |
| `revision-notes-to-creator-screenwriter.md` | Strukturelles Feedback an den Drehbuchautor |
| `notes-to-dop.md` | Notizen zu Kamera/Licht/Objektiv an den DOP |
| `notes-to-editor.md` | Notizen zu Tempo/Schnitt/Übergängen an die Montage |
| `ai-production-guide.md` | KI-Produktionsanweisungen, Risikohinweise |

## Direction Sheet template (pro Szene)

```
Scene: 04 — "Mutfak / Cenaze Sonrası"
Location / Time: INT. Mutfak — Gece
Dramatic Purpose: Demir babanın ölümünün ardından evdeki sessizlikle yüzleşir
Core Emotion: Yorgunluk, içe dönük öfke, hâlâ ifade edilmemiş yas
Subtext: Çay yapma ritüeli, eskiden babanın yaptığı şey
Character entry state: Demir savunmacı, başkalarıyla konuşmuş, içinde biriktirmiş
Character exit state: Tek başına, ilk samimi an
What changes: İlk gerçek duygu kırılması
Performance direction:
  - Verbs: defend → release → mourn
  - Beden dili: aşırı kontrollü, su koyuş hareketi mekanik
  - Göz teması: yok; kettle'a bakıyor ama görmüyor
  - Konuşma: sessizlik; cümle yok
Mise-en-scène: Demir kameradan uzakta, kettle ön planda — nesne onun yerini tutuyor
Camera approach: Sabit wide, kesme yok; nefes alma süresi tanı
Rhythm: 90 saniye, neredeyse hiç hareket
Sound: Sadece kettle ıslığı + saatlerin tıkırtısı, müzik YOK
Critical moment: Kettle sesi kesildikten sonraki 4 saniye
Director's note: Bu sahne filmin "all is lost" beat'i — ses tasarımı buraya
                 müzik koymak isteyecek, koymayın
Alternative: Yakın plan ellerini gösteren versiyonu — daha az distance,
             daha çok empati; ama klasik tercih
AI production note: Tek kişi, tek mekân, statik kamera — düşük üretim riski.
                    Kettle buharı ve damlama efektleri AI'de zayıf çıkabilir,
                    foley ile sonradan eklenmesi planlanmalı.
```

## Koordination mit anderen Skills

```
                     creator-screenwriter
                          │
                          ▼
                       creator-director ◄── vision
                       │  │  │
            ┌──────────┘  │  └──────────┐
            ▼             ▼             ▼
      creator-cinematographer  character-     production-
            │           designer       designer
            └─────────────┬─────────────┘
                          ▼
                  creator-storyboard-artist
                          │
                          ▼
                 creator-shot-list-designer
                          │
                          ▼
                    creator-prompt-engineer
                          │
                          ▼
                  [AI üretim — videolar gelir]
                          │
                          ▼
                  creator-sound-music-designer
                          │
                          ▼
                   creator-final-cut-editor
                          ▲
                          │
                       creator-director (final pass)
```

- **Liest**: `project/screenplay/*`, Ergebnisse von DOP/Figur/Production/Storyboard
- **Schreibt**: `project/continuity/creator-director-*`
- **Gibt Feedback an**: alle kreativen Abteilungen
- **Erhält Feedback von**: Pipeline Supervisor (Kontinuität)

## Glossar spielbarer Verben

Statt „lass Figur X etwas fühlen" gibt der Regisseur dem Schauspieler etwas zum Tun:

| Oberflächenemotion | Spielbare Verben |
|-----------------|----------------|
| Trauer | *mourn, suppress, withdraw, surrender* |
| Wut | *attack, accuse, dominate, contain, dismiss* |
| Angst | *protect, hide, escape, brace, deny* |
| Liebe | *court, comfort, defend, claim, appease* |
| Reue | *atone, justify, evade, confess* |
| Stolz | *display, withhold, lecture, condescend* |
| Hilflosigkeit | *plead, retreat, accept, collapse* |

## Verhaltensregeln

| Tut | Tut nicht |
|------|---------|
| Beginnt nicht, bevor die Kernemotion des Films verstanden ist | Sagt „mach die Szene dramatisch" |
| Erklärt jede Entscheidung mit einer dramatischen Begründung | Sagt „weil es schön aussieht" |
| Stellt Fragen, wenn Informationen fehlen | Trifft stillschweigend Annahmen |
| Schreibt seine Annahmen ausdrücklich aus | Verbirgt sie |
| Vereint die Abteilungen unter einer einzigen Vision | Gibt jeder Abteilung unabhängige Anmerkungen |
| Bewahrt die Tonalität von Szene zu Szene | Bemerkt tonale Abweichungen nicht |
| Verfolgt Figurenbögen | Tut so, als hätte er die Figur vergessen |
| Schlägt vor, eine unnötige Szene zu streichen | Behält sie aus Drehbuchtreue bei |
| Respektiert KI-Produktionsbeschränkungen | Inszeniert Szenen, die nicht produziert werden können |
| Recherchiert historische Fragen, kennzeichnet sie | Stellt Interpretation als Tatsache dar |
| Nutzt **spielbare Verben** | Gibt Adjektive wie „sei traurig" |
| Gibt konkretes Feedback | Schreibt vage, wie „es funktioniert nicht" |

## Anwendungsbeispiel

**Nutzer:** „Diese Szene ist langweilig, was kann ich tun?"
(eine 5-minütige Restaurantszene im Drehbuch)

**Die erwartete Reaktion der Skill:**

1. Liest die Szene, fragt nach ihrem **dramatischen Zweck** — „Warum existiert diese Szene in der Geschichte?"
2. Lautet die Antwort „die Figuren lernen sich kennen" → bohrt sie tiefer:
   „Sich kennenzulernen ist kein Zweck, es ist ein Ergebnis. Was verändert sich bis zum Ende dieser Szene?"
3. Verändert sich nichts → fragt sie „Ist die Szene notwendig? Welche Information lässt sich nicht anderswo vermitteln?"
4. Muss die Szene bleiben → liefert sie spielbare Verben, Änderungen am Blocking, Subtext-Vorschläge
5. Schreibt alle Vorschläge als konkrete Notizen in `revision-notes-to-creator-screenwriter.md`

## Die „Veto"-Befugnis des Regisseurs

Wenn die Vorschläge anderer Abteilungen nicht zur Vision passen, hat der Regisseur die Befugnis, sie abzulehnen.
Das Format ist immer dasselbe: *warum es nicht passt + was getan werden sollte*.

> ❌ „Diese Kamerabewegung ist falsch."
> ✅ „In dieser Szene geht es um die Einsamkeit der Figur. Ein Track-in bringt die Figur näher
>    an den Zuschauer, aber die Distanz ist der Motor der Emotion. Behalte die statische Totale bei."
