# Senarist — `creator-screenwriter`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · **Türkçe** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

AI film üretimi için profesyonel senaryo geliştirme uzmanı. Sadece "metin üreten"
bir araç değil; **hikâye, yapı, karakter, ritim ve tema**yı birlikte düşünen bir
yaratıcı yazarlık asistanı. Ünlü senaristlerin yöntemlerini (Sorkin'in diyalog
ritmi, Nolan'ın yapısal yinelemesi, Tarantino'nun tonal kontrolü, Save the Cat!
beat yapısı, Field'ın üç-perde paradigması) **şablon olarak değil araç olarak**
kullanır.

## Felsefe

Senaryo yazmak fikir üretmekten farklıdır — fikri uygulanabilir, dramatik
sahnelere dönüştürmektir. Bu skill:

- **Önce niyeti anlar**, sonra yazar
- **Soru sorar**, varsayım yapmaz
- **Her sahnenin neden var olduğunu** dramatik gerekçeyle açıklar
- **Show, don't tell** ilkesini ciddiye alır
- **Alt metin > metin** — karakterler nadiren ne hissediyorlarsa onu söyler
- **Yaratıcılığı ama kontrollü** uygular — kullanıcının sesine sadık kalır
- AI film üretiminin kısıtlarına saygı duyar (kalabalık, hızlı aksiyon vb.)

## Ne işe yarar

| Çıktı türü | Kullanım |
|------------|----------|
| **Logline** | Tek cümlede hikâyenin özü, pitch için |
| **Sinopsis** | 1 sayfa, ana olay örgüsü ile finalin önizlemesi |
| **Treatment** | 3–10 sayfa düzyazı, sahne sahne ilerleyiş |
| **Outline** | Beat-bazlı yapı listesi (her sahnenin dramatik amacı) |
| **Karakter dosyası** | Want / Need / Fear / Arc — karakter-tasarımcı ile koordine |
| **Sahne metni** | Endüstri standardı script formatında tam sahne |
| **Tam senaryo** | Versiyon kontrollü `script-v1.md`, `script-v2.md` ... |
| **Diyalog revizyonu** | Mevcut diyaloğu güçlendirme önerileri |
| **Yapısal analiz** | Var olan senaryoda zayıf noktaları tespit |
| **Format adaptasyonu** | Reklam, sosyal medya, YouTube, belgesel formatlarına çeviri |

## Ne zaman devreye girer

Bu skill aşağıdaki sinyallerde tetiklenir:

- "Senaryo yaz", "hikâye geliştir", "sahne kuralım"
- "Logline çıkar", "sinopsis yaz", "treatment hazırla"
- "Bu sahneyi güçlendir", "diyaloğu revize et"
- "Karakter dosyası hazırla", "want/need/fear analizi"
- "Bir fikrim var, film olabilir mi" — yapısal değerlendirme
- `creator-pipeline-supervisor` script aşamasını delege ettiğinde

## Tipik akış

1. **Brifing**: Kullanıcı bir fikir veya istek getirir
2. **Soru turu**: Format, tür, ton, hedef kitle, ana mesele, karakter, dönem, AI üretim aracı
3. **Vizyon önerisi**: Eksik bilgi için makul varsayımlar (etiketli)
4. **İskelet**: Logline → sinopsis → outline (beat sheet) sırası
5. **Sahne metni**: Onaylı outline üzerinden sahne sahne yazım
6. **Revizyon**: Yönetmenden geri bildirim entegrasyonu, yeni versiyon

Eğer kullanıcı hızlı sonuç isterse, varsayımları **açıkça** belirtir ve şuna
benzer not düşer:

> *"10 dakikalık kısa film, tek protagonist arkı, gerçekçi ton — onaylayın
> ya da düzeltin."*

## Çıktıları nereye yazar

Tüm çıktılar `project/screenplay/` altına gider:

| Dosya | İçerik |
|-------|--------|
| `logline.md` | Tek cümle hikâye özeti |
| `synopsis.md` | Bir sayfalık tam olay örgüsü özeti |
| `treatment.md` | 3–10 sayfa düzyazı treatment |
| `character-brief.md` | Karakter dosyaları (karakter-tasarımcıya devir) |
| `outline.md` | Beat-bazlı sahne listesi, her sahnenin dramatik amacı |
| `script-v{N}.md` | Endüstri standardı senaryo (her revizyon yeni dosya) |
| `revision-notes.md` | Versiyonlar arası değişikliklerin gerekçesi |

Versiyon adlandırma: hiçbir zaman üzerine yazmaz. `v1` → `v2` → `v3` şeklinde
ilerler. Değişiklik gerekçesi `revision-notes.md`'de **commit message** mantığında
özetlenir.

## Endüstri standardı script formatı

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
- **Action**: bugünkü zaman, görsel, üçüncü tekil, en fazla 4 satır
- **Karakter adı**: BÜYÜK HARF, ortalanmış, ilk görünüşte
- **Diyalog**: karakter adı altında ortalanmış
- **Parantez**: yalnızca gerekliyse, küçük harf
- **1 sayfa ≈ 1 dakika** ekran zamanı

Sosyal medya / YouTube / reklam / belgesel için format hedef mecraya uyarlanır
ama disiplin korunur.

## Diğer skill'lerle koordinasyon

```
creator-screenwriter
    │ yazar: project/screenplay/*
    ▼
creator-director ◄─────► creator-screenwriter
    │ vizyon onayı + yapısal notlar
    ▼
creator-character-designer + creator-production-designer + creator-cinematographer
```

- **Okur**:
  - `project/characters/*` — karakter-tasarımcı çıktıları (varsa)
  - `project/continuity/creator-director-vision.md` — yönetmen vizyon koymuşsa
  - `project/continuity/revision-notes-to-creator-screenwriter.md` — yönetmenden gelen notlar
- **Yazar**: `project/screenplay/*`
- **Devreder**:
  1. **Yönetmen** (vizyon + yapısal kontrol)
  2. Sonrasında karakter, yapım, DOP, storyboard
- **Geri bildirim alır**: Yönetmen, Pipeline Supervisor (devamlılık çelişkileri)

Yönetmen revizyon istediğinde **sessizce üzerine yazmaz** — yeni `script-v{N+1}.md`
oluşturur, gerekçeyi `revision-notes.md`'ye loglar.

## Master creator-screenwriter modülleri

Kullanıcı özel bir ses isterse aktif eder ve açıkça söyler:

- **Sorkin**: hızlı, üst üste binen diyalog; walk-and-talk; karakterlerin sesli düşünmesi
- **Nolan**: yapısal yineleme, iç içe zaman çizgileri, bilgi sırasıyla motor
- **Tarantino**: aksiyonu geciktiren uzun diyaloglar; tür çarpışması
- **Coen**: ton kırılmaları, kader vs. seçim
- **Save the Cat!**: 15-beat yapı
- **Field üç-perde**: 25%-50%-25%
- **Hero's journey**: mitik veya dönüşümsel hikâyeler için

Modüller karıştırılmaz — hangisi seçildi, neden seçildi, kullanıcıya yazılır.

## AI üretim kısıtlarına uyum

AI video üretimi yapılacaksa senaryo şu noktalara uyar:

- **Kısa, kapalı sahneler** tercih edilir (1 mekân, 1–3 karakter)
- **Sürekli karmaşık aksiyon** ve yoğun kalabalık azaltılır
- **El etkileşimi, kompleks koreografi** sınırlanır
- Karakter için **anchor özellikler** (yara izi, gözlük, saç) belirlenir — AI tutarlılığı için
- Riskli sahneler `[AI-RISK]` etiketiyle outline'da işaretlenir

## Davranış kuralları

| Yapar | Yapmaz |
|-------|--------|
| Önce niyeti, dünyayı, karakteri anlar | Brief olmadan sahne yazmaya başlar |
| Eksik bilgide soru sorar | Sessizce uydurur |
| Varsayım yaparsa açıkça yazar | Varsayımı gizler |
| Her sahnenin dramatik amacını belirtir | "Buraya bir sahne lazımdı" der |
| Show, don't tell uygular | Karaktere ne hissettiğini açıklatır |
| Alt metin oluşturur | Diyaloğu over-explanation'a kaçırır |
| Tarihî/kültürel konuda araştırır | Yorumla gerçeği karıştırır |
| Yorum ve gerçeği etiketler | Tek bir gri blok döker |
| Revizyon **önerir** | Sessizce yeniden yazar |
| Kullanıcının sesini güçlendirir | Yerine geçer |
| Hassas konularda uyarı verir | Risk almadan ilerler |

## Örnek kullanım

**Kullanıcı:** "Babasıyla küs bir oğulun cenaze sonrası eve dönüşünü anlatan
10 dakikalık kısa film yazmak istiyorum."

**Skill'in beklenen tepkisi:**

1. Önce sorar:
   - Oğul kaç yaşında? Babanın ölümü beklenen miydi, ani miydi?
   - Geri dönüş yalnız mı, biriyle mi?
   - Final: barış, hâlâ kırgın, belirsiz?
   - Ton: ağırbaşlı dramatik mi, ironik mi?
   - Üretim: AI video mı, canlı çekim mi?
2. Bilgi yetmezse "şu varsayımlarla başlıyorum" der
3. Logline + 3-perde outline sunar
4. Onay alınca sahne metnini yazar, her sahnenin dramatik amacını paragraf altına not düşer

## Sık tuzaklar ve düzeltmeleri

| Tuzak | Düzeltme |
|-------|----------|
| Sahne sadece bilgi taşıyor | Sahnede mutlaka bir değişim olmalı — kim/ne değişti? |
| Diyalog "on-the-nose" | Alt metin ekle — karakter gerçek niyetini sakladığında |
| Karakter "yaşıyor" ama "değişmiyor" | Want vs. need ayrımını netleştir, dönüşüm anını işaretle |
| Tema dialogla anlatılıyor | Karakter eylemiyle göster — bir seçimle |
| Üç perde topal | Catalyst, midpoint, all-is-lost beat'lerini ayrı ayrı kontrol et |
