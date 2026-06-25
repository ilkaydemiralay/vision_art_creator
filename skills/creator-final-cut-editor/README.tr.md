# Final Cut Editor — `creator-final-cut-editor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · **Türkçe** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

AI üretim çıktılarını **bitmiş filme** çeviren skill. Pre-production'ın
sonu / post-production'ın başı. Material üretildikten sonra rough cut → fine
cut → final cut → delivery akışını yönetir; AI generation hatalarını triage
eder, continuity'yi denetler, ses/müzik entegrasyonunu kontrol eder,
delivery-hazır master'lar üretir.

**Shot-list-designer'dan farkı**: shot-list editorial niyeti çekim ÖNCESİ
tasarlar; creator-final-cut-editor gerçek material üzerinde kesimi YÜRÜTÜR.

## Felsefe

Final cut **teknik sıralama değildir** — sinemasal bütünlük inşasıdır.
Bu skill:

- **Her kesimde dramatik gerekçe** — "iyi durur" yetmez
- **Çoklu ölçek ritim**: shot içi, sahne içi, film geneli
- **AI error triage**: hangi hata break, hangisi gizlenebilir, hangisi kalabilir
- **Audience experience design**: izleyici ne hisseder, neyi öğrenir, ne kalır
- **Delivery discipline**: YouTube ≠ festival ≠ Instagram ≠ arşiv
- **Versioning**: rough/fine/final + festival/social/trailer cut'larını ayrı yönetir

## Ne işe yarar

| Çıktı | İçerik |
|-------|--------|
| **Material evaluation** | Her shot için: usable / revize / re-generate / cut |
| **Rough cut plan** | İlk kaba sıralama, eksik material listesi |
| **Fine cut plan** | Kesme noktaları, shot süreleri, sessizlik |
| **Final cut plan** | Final readiness + delivery checklist |
| **Per-scene final-check** | Sahne bazlı detaylı audit |
| **Whole-film report** | Tüm film final cut raporu |
| **AI error report** | Generation hataları + severity sınıflama |
| **Audio integration audit** | Ses tasarımcısına geri bildirim |
| **Color grade notes** | Renk düzeltme direktifleri |
| **EDL** | NLE'de okunabilir Edit Decision List |
| **Version manifest** | Festival/social/trailer cut versiyonları |
| **Delivery specs** | Platform bazlı export ayarları |
| **Trailer plan** | Teaser/trailer cut planı |

## Ne zaman devreye girer

- AI video shot'ları üretildi, montaja geçiliyor
- Rough/fine/final cut planlaması gerekli
- AI hata audit'i isteniyor
- Çoklu cut (festival, social, trailer) üretilecek
- Delivery export hazırlığı
- `creator-pipeline-supervisor` post-production aşamasını delege ettiğinde

## Tipik akış

1. **Material evaluation** — her shot kategorize edilir (✅🟡🟠🔴)
2. **Rough cut v01** — hikâye sırası, temel dramatik sequence
3. **Fine cut v01** — kesme noktaları, ritim, sessizlik
4. **Sound integration audit** — creator-sound-music-designer'a feedback
5. **AI error report** — kritik/orta/küçük sınıflama
6. **Color grade notes** — gerekirse
7. **Subtitle / titles / graphics check**
8. **Final cut v01** — readiness checklist
9. **Delivery export** — platform bazlı versiyon

## AI error triage matrisi

| Severity | Tanım | Aksiyon |
|----------|-------|---------|
| 🔴 Kritik | Final cut'a giremez | Re-generate (creator-prompt-engineer'a flag) |
| 🟡 Orta | Hidden via trim/crop/color/sound | Editorial workaround |
| ✅ Küçük | Seyirciyi rahatsız etmiyor | Kalabilir |

Kontrol edilenler: yüz bozulması, el/parmak hatası, lip-sync, kostüm değişimi,
aksesuar kaybı, mekân kayması, ışık yönü tutarsızlığı, kamera yapay hareket,
flicker, warping, morphing, eriyen objeler, arka plan bozulması, anakronizm,
plastik görüntü.

## Per-scene final-check formatı

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

## Çıktıları nereye yazar

`project/cuts/` altına:

| Dosya | İçerik |
|-------|--------|
| `material-evaluation.md` | Her shot kategorisi |
| `rough-cut/v{NN}.md` | Rough cut planı |
| `fine-cut/v{NN}.md` | Fine cut planı |
| `final-cut/v{NN}.md` | Final cut planı + readiness |
| `scene-{NN}/final-check.md` | Sahne bazlı detay |
| `final-cut-report.md` | Tüm film audit |
| `ai-error-report.md` | AI hata raporu |
| `audio-integration-report.md` | Ses entegrasyon audit |
| `color-grade-notes.md` | Renk düzeltme |
| `subtitle-titles-graphics.md` | Altyazı/jenerik |
| `transitions.md` | Geçiş kararları |
| `edit-decision-list.md` | EDL |
| `versions/{cut-name}.md` | Versiyon manifest |
| `delivery/{platform}.md` | Platform export specs |
| `trailer-plan.md` | Trailer/teaser planı |

## Version management

| Versiyon | Süre | Hedef |
|----------|------|-------|
| Rough Cut v01 | ~115% target | İlk hikâye akışı testi |
| Rough Cut v02 | ~108% | Eksiklerin entegrasyonu |
| Fine Cut | ~102% | Ritim ve duygu lock |
| Director's Cut | %100 hedef | Yönetmen tam onay |
| Final Cut | %100 | Delivery-ready |
| Festival Cut | %100 | Festival format |
| YouTube Cut | %100 veya kısaltılmış | YouTube algoritma |
| Trailer Cut | 30s–2dk | Pazarlama |
| Social Cut | 9:16 short | Reels, TikTok |

Her versiyon için: name, duration, changes, removed/added scenes, audio
changes, revision rationale, approval status.

## Delivery örnek specs

| Platform | Aspect | Çözünürlük | FPS | Audio |
|----------|--------|------------|-----|-------|
| YouTube 16:9 master | 16:9 | 3840×2160 (4K) veya 1920×1080 | 24/25 | AAC 320kbps stereo |
| Festival master | 2.39:1 veya 16:9 | 4K | 24 | WAV 48kHz 24-bit stereo + 5.1 |
| Instagram Reels | 9:16 | 1080×1920 | 30 | AAC stereo |
| TikTok | 9:16 | 1080×1920 | 30 | AAC stereo |
| Web compressed | 16:9 | 1920×1080 | 24/25 | AAC 192kbps |
| Archive master | original | en yüksek | original | WAV master |

## Trailer kurgu mantığı

Trailer **filmin küçültülmüş hali değildir** — ayrı bir editorial mantık:

- En güçlü 6–10 görsel
- Spoiler exclusion list
- Hook → arka plan → tehdit/çatışma → climax teaser → karanlık → tagline
- Müzik yükselişi (filmden farklı, daha doğrudan)
- Hızlı kesme ritmi (filmden farklı)
- Karakter tanıtımı sıkıştırılmış
- Son vurucu image — film bağlamı **dışında**
- Social media 9:16 kısa versiyon

## Diğer skill'lerle koordinasyon

- **Okur**: tüm upstream creative çıktıları + shot-list `final-editor-notes.md`
- **Yazar**: `project/cuts/*`
- **Geri bildirim verir**:
  - **creator-sound-music-designer**: audio fix talepleri
  - **creator-prompt-engineer**: regeneration talepleri
  - **creator-pipeline-supervisor**: continuity escalation
- **Onay alır**: Yönetmen (final approval), Pipeline Supervisor

## Davranış kuralları

| Yapar | Yapmaz |
|-------|--------|
| Her kesim için dramatik gerekçe | Teknik sıralama yapar |
| Gereksiz sahne/shot açıkça flag | Sadakat adına korur |
| AI error'ı viewer experience'tan değerlendirir | Soyut/teknik perfectionism |
| Dialogue + music + ambience + silence beraber düşünür | İzole audit yapar |
| Yönetmen vizyonuna sadık | Editorial ego ile çakışır |
| Target süre disiplinli | Sınırı aşar |
| Büyük değişiklik öncesi kullanıcıya sorar | Sessizce keser |
| Multi-version takibi yapar | Tek dosyada karıştırır |
| Platform-fit delivery sunar | Tek master verir |
| Delivery readiness checklist olmadan "tamam" demez | Erken complete der |
