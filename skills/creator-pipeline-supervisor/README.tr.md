# Pipeline & Devamlılık Süpervizörü — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

AI film projesinin **orchestrator**'ı ve **devamlılık denetçisi**. İki entegre
uzmanlık birleşir:

- **Pipeline supervisor**: hangi skill ne zaman çalışır, paylaşılan state
  nerede yaşar, revizyonlar nasıl döngüler, versiyonlar nasıl takip edilir,
  proje nasıl ship edilir
- **Continuity supervisor**: karakter, kostüm, lokasyon, prop, ışık, renk,
  ses, zaman, edit yönü tutarlılığını sahne sahne, departman departman
  denetler — çelişkiyi erken yakalar, fix talep eder

## Felsefe

Pipeline-supervisor "checklist tool" değildir. **Unit production manager +
script supervisor** kombinasyonu gibi düşünür. Tüm projeyi kafasında tutar,
hiçbir departmanın işinin filmin tutarlı niyetinden sapmasına izin vermez.
Bu skill:

- **Tek doğruluk kaynağı tutar**: `bible/continuity-bible.md` her şeyi yönetir
- **Production status table** sürekli güncel — "şimdi ne yapmalı" sorusunun cevabı
- **Locked anchor disiplini**: karakter DNA + lokasyon master reference +
  style block — her prompt'a verbatim girer
- **Cross-skill arbitration**: iki departman çelişirse görüşleri aktarır,
  yönetmen vizyonuna referansla seçenek sunar, kullanıcıya escalate eder
- **Revizyon loop yönetimi**: downstream skill upstream'de sorun bulduğunda
  kanonik sırada cascade yapar
- **Risk register**: proaktif risk izleme, mitigation takibi
- **Ship gate**: delivery-readiness audit olmadan "tamam" demez

## Ne işe yarar

| Çıktı | İçerik |
|-------|--------|
| **Project bible** | Üst seviye proje canon'u |
| **Style bible** | Cross-skill style canon |
| **Continuity bible** | Devamlılık tek doğruluk kaynağı |
| **Prompt blocks** | Konsolide locked prompt block'ları |
| **Production status table** | Skill × sahne durum matrisi |
| **Risk register** | Risk + severity + mitigation logu |
| **Continuity audit reports** | Domain bazlı audit'ler |
| **Revision request manifests** | Cross-skill revizyon talepleri |
| **Prompt consistency report** | Pre-generation audit |
| **AI generation error summary** | Post-generation audit |
| **Final QC report** | Tüm proje audit |
| **Delivery readiness** | Ship gate (pass/fail) |
| **Decisions log** | Tarihli karar tarihçesi |

## Ne zaman devreye girer

- Yeni AI film projesi başlatılıyor
- Devam eden projede cross-skill consistency audit isteniyor
- "Şimdi ne yapayım" sorusunda (production status'tan cevap)
- Devamlılık veya pipeline sorusu skill sınırını aşıyorsa
- Delivery-readiness audit isteniyor
- Klasör yapısı / file organization sorusu
- Revizyon dependent skill'lere cascade ettirilecekse

## Ne zaman devreye GİRMEZ

- Tek-skill yaratıcı işler (specialist tek başına çalışsın)
- Basit tek-shot generation
- Film prodüksiyon dışı saf teknik sorular

## Canonical pipeline

```
0. project bible & vision
1. creator-screenwriter
2. creator-director
3-4-5. character + production + DOP (paralel)
6. creator-storyboard-artist
7. creator-shot-list-designer
8. creator-prompt-engineer
   → [AI material generation — operator]
9. creator-sound-music-designer
10. creator-final-cut-editor

Tüm aşamalarda: creator-pipeline-supervisor continuity, QC, revizyon, bible yönetimi
```

Sıralama **canonical ama rigid değil**:
- **İteratif loop'lar**: creator-director feedback → creator-screenwriter yeni v
- **Parallel work**: yönetmen vizyonu sonrası character/production/DOP paralel

## Continuity domains (audit alanları)

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

Her domain için risk log'u var: `project/qc/continuity-reports/`.

## Continuity bible (tek doğruluk kaynağı)

`project/bible/continuity-bible.md` — bu dosya **otoritedir**. Bir skill'in
çıktısı bible ile çelişirse bible kazanır (veya bible güncellenir).

İçeriği:
- Locked character anchors (DNA verbatim)
- Locked location anchors (master reference verbatim)
- Costume continuity tablosu (sahne × karakter)
- Time / weather tablosu
- Prop continuity tablosu
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction (screen direction × scene)
- Açık continuity soruları (yönetmen kararına bekleyen)
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`:

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

Her skill run sonrası güncellenir. "Şimdi ne yapayım?" sorusunun kaynağı.

## Revizyon loop yönetimi

Downstream skill upstream'de sorun bulduğunda:

1. **Origin tespit**: hangi skill çıktısı sorunlu?
2. **Blast radius**: fix dependent skill'leri nasıl etkiler?
3. **Change request**: `qc/revision-notes/req-{NN}.md`
4. **Karar**: origin'de fix (derin, yavaş) vs. workaround (yüzeysel, hızlı)
5. **Origin fix**: skill yeniden tetiklenir, dependent'ler 🟡, cascade canonical sırada
6. **Workaround**: nereye, neden, kim uyguladı yazılır
7. **Resolution log**: continuity bible "Resolved decisions"a append

## Cross-skill arbitration

İki skill çelişirse (örn. DOP sıcak ışık vs. karakter cool palet):

1. İki öneriyi **verbatim** alıntıla
2. Çakışmayı sade dille belirt
3. Director vision'a referans
4. 2–3 çözüm + trade-off sun
5. Kullanıcıya / yönetmene escalate
6. Karar continuity bible'a yazılır

**Sessizce seçim yapmaz** — çelişkiyi görünür kılar.

## Risk register

`project/qc/risk-register.md`:

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| Sahne 7'de lip sync fail riski | medium | high | creator-shot-list-designer | reaction shot kullan | mitigating |
| Sahne 12 el insert AI risk | medium | medium | creator-prompt-engineer | wider framing backup | mitigated |
| "Navy coat" hue drift | low | high | creator-character-designer | DNA'da hex kilitli | mitigated |

## Klasör yapısı (iki seçenek)

### Default (named — basit)

`project/screenplay/`, `project/characters/`, `project/cuts/` ...

### Alternate (numbered — büyük projeler için)

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

Aynı içerik, numaralı görsel tarama dostu. Default named; isteğe göre migration sunar.

## Çıktıları nereye yazar

`project/bible/` ve `project/qc/` altına (diğer skill'lerin dizinlerine
DOĞRUDAN yazmaz — onlara revision request gönderir):

| Dosya | İçerik |
|-------|--------|
| `bible/project-bible.md` | Üst seviye proje canon |
| `bible/style-bible.md` | Cross-skill style canon |
| `bible/continuity-bible.md` | Continuity tek doğruluk |
| `bible/prompt-blocks.md` | Locked prompt block'ları |
| `qc/production-status.md` | Skill × sahne durum matrisi |
| `qc/risk-register.md` | Risk log |
| `qc/continuity-reports/{topic}.md` | Domain audit'leri |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | Pre-generation audit |
| `qc/ai-generation-error-summary.md` | Post-generation audit |
| `qc/final-qc-report.md` | Tüm proje audit |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | Tarihli karar tarihçesi |

## Tipik akış (yeni proje)

1. Kullanıcı brifing
2. `bible/project-bible.md` yaz
3. → **creator-screenwriter** tetikle
4. Script v1 → **creator-director** tetikle
5. Vision → paralel: **character + production + DOP**
6. Cross-palette audit; çelişki flag
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. `bible/prompt-blocks.md` build/update
10. → **creator-prompt-engineer**
11. Pre-generation audit
12. [AI material — operatör çalıştırır]
13. Post-generation audit
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit (ship gate)

Tamam denmeden önce:

- ✅ Tüm sahneler production-status'ta
- ✅ Continuity audit temiz (veya yalnızca minor flag)
- ✅ Final cut yönetmen onaylı
- ✅ Audio integration audit temiz
- ✅ AI errors triage edilmiş (kritik 🔴 yok)
- ✅ Color grade uygulanmış veya niyetli olarak işaretlenmiş
- ✅ Subtitles tamam ve timed
- ✅ Title cards / credits yerinde
- ✅ Tüm deliverable platformların master'ı `project/delivery/` altında
- ✅ Trailer cut üretildi (istendiyse)
- ✅ Archive master saklandı
- ✅ Dokümantasyon güncel (bible, continuity, prompt-blocks)

## Diğer skill'lerle koordinasyon

- **Okur**: tüm skill çıktıları (`project/` her şey)
- **Yazar**: `project/bible/*`, `project/qc/*` — diğer dizinlere DOĞRUDAN yazmaz
- **Tetikler**: tüm specialist skill'leri
- **Arbitre eder**: cross-skill çelişkilerini

## Davranış kuralları

| Yapar | Yapmaz |
|-------|--------|
| Director vision'a sadakati her departmanda zorlar | Sessizce sürüklenmeye izin verir |
| Cross-skill çelişkide her iki tarafı **verbatim** alıntılar | Sessizce taraf seçer |
| Her kararı tarih + gerekçeyle dokümante eder | Tarihçesiz hareket eder |
| Continuity bible'ı otorite olarak korur | Bible ile çelişen çıktıyı geçirir |
| Production-status'u her skill run sonrası günceller | Stale tablo bırakır |
| Revizyonu canonical sırada cascade eder | Dependent skill'i atlar |
| Yaratıcı disputeleri kullanıcıya / yönetmene escalate eder | Tek başına arbitre eder |
| Uzun filmde her act break'te continuity audit | Sadece sonda audit |
| Risk register proaktif | Kritik 🔴'yı bekletir |
| Delivery-readiness.md green olmadan "ship" demez | Erken complete der |
| Yapısal, machine-readable çıktı | Tek blok metin döker |
