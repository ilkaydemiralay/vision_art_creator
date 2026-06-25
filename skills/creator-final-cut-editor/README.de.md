# Final Cut Editor — `creator-final-cut-editor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · **Deutsch** · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Der Skill, der KI-Produktionsergebnisse in einen **fertigen Film** verwandelt. Das
Ende der Vorproduktion / der Beginn der Postproduktion. Sobald das Material
produziert wurde, steuert er den Ablauf Rough Cut → Fine Cut → Final Cut →
Auslieferung; er sortiert KI-Generierungsfehler, prüft die Continuity, kontrolliert
die Audio-/Musikintegration und erstellt auslieferungsfertige Master.

**Unterschied zum shot-list-designer**: Der Shot List Designer entwirft die
Schnittabsicht VOR dem Dreh; creator-final-cut-editor FÜHRT den Schnitt am
tatsächlichen Material AUS.

## Philosophie

Der Final Cut ist **keine technische Aneinanderreihung** — er ist die Konstruktion
filmischer Ganzheit. Dieser Skill:

- **Eine dramaturgische Begründung für jeden Schnitt** — „sieht gut aus" reicht nicht
- **Rhythmus auf mehreren Ebenen**: innerhalb einer Einstellung, innerhalb einer Szene, über den ganzen Film hinweg
- **Triage von KI-Fehlern**: welcher Fehler den Schnitt zerstört, welcher kaschiert werden kann, welcher bleiben darf
- **Gestaltung des Zuschauererlebnisses**: was der Zuschauer fühlt, lernt und mitnimmt
- **Auslieferungsdisziplin**: YouTube ≠ Festival ≠ Instagram ≠ Archiv
- **Versionierung**: verwaltet Rough/Fine/Final + Festival-/Social-/Trailer-Cuts getrennt

## Was er leistet

| Ergebnis | Inhalt |
|-------|---------|
| **Materialbewertung** | Pro Einstellung: verwendbar / überarbeiten / neu generieren / streichen |
| **Rough-Cut-Plan** | Erste grobe Anordnung, Liste des fehlenden Materials |
| **Fine-Cut-Plan** | Schnittpunkte, Einstellungsdauern, Stille |
| **Final-Cut-Plan** | Endgültige Freigabe + Auslieferungs-Checkliste |
| **Final-Check pro Szene** | Detaillierte Szene-für-Szene-Prüfung |
| **Gesamtfilm-Bericht** | Final-Cut-Bericht für den gesamten Film |
| **KI-Fehlerbericht** | Generierungsfehler + Schweregrad-Klassifizierung |
| **Audio-Integrationsprüfung** | Rückmeldung an den Sound Designer |
| **Color-Grade-Notizen** | Anweisungen zur Farbkorrektur |
| **EDL** | NLE-lesbare Edit Decision List |
| **Versionsmanifest** | Festival-/Social-/Trailer-Cut-Versionen |
| **Auslieferungsspezifikationen** | Plattformspezifische Exporteinstellungen |
| **Trailer-Plan** | Teaser-/Trailer-Cut-Plan |

## Wann er greift

- KI-Videoeinstellungen wurden produziert, der Schnitt beginnt
- Eine Rough-/Fine-/Final-Cut-Planung ist erforderlich
- Eine KI-Fehlerprüfung wird angefordert
- Mehrere Cuts (Festival, Social, Trailer) sollen erstellt werden
- Vorbereitung des Auslieferungs-Exports
- Wenn `creator-pipeline-supervisor` die Postproduktionsphase delegiert

## Typischer Ablauf

1. **Materialbewertung** — jede Einstellung wird kategorisiert (✅🟡🟠🔴)
2. **Rough Cut v01** — Erzählreihenfolge, grundlegende dramaturgische Sequenz
3. **Fine Cut v01** — Schnittpunkte, Rhythmus, Stille
4. **Audio-Integrationsprüfung** — Rückmeldung an creator-sound-music-designer
5. **KI-Fehlerbericht** — Klassifizierung kritisch/mittel/gering
6. **Color-Grade-Notizen** — falls erforderlich
7. **Untertitel-/Titel-/Grafik-Prüfung**
8. **Final Cut v01** — Freigabe-Checkliste
9. **Auslieferungs-Export** — plattformspezifische Version

## KI-Fehler-Triage-Matrix

| Schweregrad | Definition | Maßnahme |
|----------|------------|--------|
| 🔴 Kritisch | Kann nicht in den Final Cut aufgenommen werden | Neu generieren (an creator-prompt-engineer melden) |
| 🟡 Mittel | Durch Trim/Crop/Color/Sound kaschiert | Schnitttechnischer Workaround |
| ✅ Gering | Stört den Zuschauer nicht | Darf bleiben |

Geprüft werden: Gesichtsverzerrung, Hand-/Fingerfehler, Lip-Sync,
Kostümwechsel, Verlust von Accessoires, Location-Drift, Inkonsistenz der
Lichtrichtung, künstliche Kamerabewegung, Flicker, Warping, Morphing,
schmelzende Objekte, Zerfall des Hintergrunds, Anachronismus, Plastik-Look.

## Format des Final-Checks pro Szene

```
Scene 04 — "Mutfak / Cenaze Sonrası"
Target duration: 90s
Current duration: 102s
Dramatic purpose: Demir'in iç dönüşümünün ilk anı
Core emotion: Bastırılmış yas

Shots used: 04.01, 04.02, 04.03, 04.05, 04.06
Shots cut: 04.04 (gereksiz reaction, ritim düşürüyor)
Shots shortened: 04.05 (8s → 5s — wide hold gereksiz uzun)
Shots lengthened: 04.02 (4s → 6s — kettle hold dramatik nefes)
Cut points:
  - 04.01 → 04.02: sound bridge (kettle ıslığı önce)
  - 04.02 → 04.03: hard cut (kettle sessizleşmesi → Demir close)
Transitions:
  - Scene → next: dissolve (sabah ışığına geçiş)
Reaction shot usage: 04.03 (Demir close) — yas kırılma anı
Silence usage: 04.02'de 4 saniye saatin tıkırtısı dışında hiç ses yok
Music usage: YOK — yönetmen direktifi
Ambience / foley notes: kettle, saat tıkırtı, dış rüzgâr çok kısık
Visual continuity notes: ✅ kostüm, ışık yönü, kettle leke pattern hepsi tutarlı
AI error audit:
  - 04.02 kettle buharı warping (🟡 orta) — sound design ile maskelenecek
  - 04.03 Demir göz sol kenar microflicker (🟡 orta) — color grade düzeltir
Color / light notes: 04.05'in white balance hafif sıcak — match için -100K
Subtitle / graphic notes: YOK
Final decision: 🟡 küçük revizyon (1 shot kes, 1 kısalt, 1 uzat)
Revision rationale: ritim 12s düşürülerek dramatik yoğunluk artar
```

## Wohin er seine Ergebnisse schreibt

Unter `project/cuts/`:

| Datei | Inhalt |
|-------|---------|
| `material-evaluation.md` | Kategorie jeder Einstellung |
| `rough-cut/v{NN}.md` | Rough-Cut-Plan |
| `fine-cut/v{NN}.md` | Fine-Cut-Plan |
| `final-cut/v{NN}.md` | Final-Cut-Plan + Freigabe |
| `scene-{NN}/final-check.md` | Szene-für-Szene-Detail |
| `final-cut-report.md` | Gesamtfilm-Prüfung |
| `ai-error-report.md` | KI-Fehlerbericht |
| `audio-integration-report.md` | Audio-Integrationsprüfung |
| `color-grade-notes.md` | Farbkorrektur |
| `subtitle-titles-graphics.md` | Untertitel/Titel |
| `transitions.md` | Übergangsentscheidungen |
| `edit-decision-list.md` | EDL |
| `versions/{cut-name}.md` | Versionsmanifest |
| `delivery/{platform}.md` | Plattform-Exportspezifikationen |
| `trailer-plan.md` | Trailer-/Teaser-Plan |

## Versionsverwaltung

| Version | Dauer | Ziel |
|----------|----------|------|
| Rough Cut v01 | ~115 % Zielwert | Erster Test des Erzählflusses |
| Rough Cut v02 | ~108 % | Integration fehlender Teile |
| Fine Cut | ~102 % | Rhythmus und Emotion festlegen |
| Director's Cut | 100 % Zielwert | Vollständige Regiefreigabe |
| Final Cut | 100 % | Auslieferungsfertig |
| Festival Cut | 100 % | Festivalformat |
| YouTube Cut | 100 % oder gekürzt | YouTube-Algorithmus |
| Trailer Cut | 30s–2 Min | Marketing |
| Social Cut | 9:16 kurz | Reels, TikTok |

Für jede Version: Name, Dauer, Änderungen, entfernte/hinzugefügte Szenen,
Audio-Änderungen, Begründung der Überarbeitung, Freigabestatus.

## Beispiel-Auslieferungsspezifikationen

| Plattform | Seitenverhältnis | Auflösung | FPS | Audio |
|----------|--------|------------|-----|-------|
| YouTube 16:9 Master | 16:9 | 3840×2160 (4K) oder 1920×1080 | 24/25 | AAC 320kbps Stereo |
| Festival-Master | 2.39:1 oder 16:9 | 4K | 24 | WAV 48kHz 24-bit Stereo + 5.1 |
| Instagram Reels | 9:16 | 1080×1920 | 30 | AAC Stereo |
| TikTok | 9:16 | 1080×1920 | 30 | AAC Stereo |
| Web komprimiert | 16:9 | 1920×1080 | 24/25 | AAC 192kbps |
| Archiv-Master | original | höchste | original | WAV-Master |

## Logik des Trailer-Cuts

Ein Trailer ist **keine Miniaturausgabe des Films** — er hat seine eigene
Schnittlogik:

- Die 6–10 stärksten Bilder
- Spoiler-Ausschlussliste
- Hook → Hintergrund → Bedrohung/Konflikt → Höhepunkt-Teaser → Dunkelheit → Tagline
- Musikaufbau (anders als im Film, direkter)
- Schneller Schnittrhythmus (anders als im Film)
- Verdichtete Figureneinführungen
- Ein abschließendes Punch-Bild — **außerhalb** des Filmkontexts
- Kurze Social-Media-Version im Format 9:16

## Koordination mit anderen Skills

- **Liest**: alle vorgelagerten kreativen Ergebnisse + die `final-editor-notes.md` der Shot List
- **Schreibt**: `project/cuts/*`
- **Gibt Rückmeldung an**:
  - **creator-sound-music-designer**: Audio-Korrekturanfragen
  - **creator-prompt-engineer**: Neugenerierungsanfragen
  - **creator-pipeline-supervisor**: Continuity-Eskalation
- **Holt Freigabe ein von**: Regie (finale Freigabe), Pipeline Supervisor

## Verhaltensregeln

| Tut | Tut nicht |
|-------|---------|
| Eine dramaturgische Begründung für jeden Schnitt | Bloß technisch aneinanderreihen |
| Markiert unnötige Szenen/Einstellungen klar | Sie aus falscher Treue behalten |
| Bewertet KI-Fehler aus Sicht des Zuschauererlebnisses | Abstrakter/technischer Perfektionismus |
| Berücksichtigt Dialog + Musik + Ambience + Stille gemeinsam | Isoliert prüfen |
| Treu zur Vision der Regie | Mit dem Schnitt-Ego kollidieren |
| Diszipliniert bei der Zieldauer | Das Limit überschreiten |
| Fragt den Nutzer vor einer größeren Änderung | Stillschweigend schneiden |
| Verfolgt mehrere Versionen | Sie in einer einzigen Datei vermischen |
| Liefert plattformgerechte Auslieferung | Ein einziges Master übergeben |
| Sagt ohne Auslieferungs-Checkliste nicht „fertig" | Es zu früh für abgeschlossen erklären |
