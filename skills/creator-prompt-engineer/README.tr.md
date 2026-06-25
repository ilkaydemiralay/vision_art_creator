# Prompt Mühendisi — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · **Türkçe** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Yaratıcı pipeline ile AI generator'lar arasında **çeviri katmanı**.
Senarist, yönetmen, DOP, karakter, yapım, storyboard, shot-list skill'lerinin
ürettiği kararları **gerçekten üretilebilir, tutarlı** prompt'lara dönüştürür.
Tool-spesifik optimize eder (Midjourney ≠ Sora ≠ Stable Diffusion), locked
anchor'ları her prompt'a gömer, riskli sahneler için safe alternative üretir.

## Felsefe

Prompt mühendisi **görsel icat etmez** — upstream kararlarını encode eder.
Bu skill:

- **Locked anchors**: character DNA + location master reference + style block —
  50 prompt sonra bile aynı karakter aynı yüzle çıkar
- **Tool fitness**: her AI tool'un kendi prompt dili var
- **Producibility audit**: bu sahne generator'ı yenecek — alternatif öner
- **Consistency discipline**: uzun film için prompt'lar bir sistemdir, izole değil
- **FACS expression coding**: "üzgün" yerine AU1 + AU4 + AU15 — daha tutarlı sonuç
- **Asla upstream'i sessizce ezmez**: gerekirse flag eder, geri sorar

## Ne işe yarar

| Çıktı | İçerik |
|-------|--------|
| **Character prompts** | Locked DNA + sahne sahne varyasyon |
| **Location prompts** | Master reference + day/night/weather varyasyonu |
| **Style anchors** | Film geneli görsel/teknik blok |
| **Negative prompts** | Kategori bazlı negatif prompt bankası |
| **Panel prompts** | Storyboard panelden görsel üretim prompt'u |
| **Shot prompts** | Shot-list'ten AI video üretim prompt'u |
| **Character sheets** | Front/side/back/close referans üretimi |
| **Producibility risk report** | Sahne/shot bazlı risk + safe alternative |
| **Tool guide** | Operatör için tool-spesifik notlar |

## Ne zaman devreye girer

- Üretim öncesi AI image/video prompt'a ihtiyaç var
- Karakter/mekân tutarlılığı için anchor sistemi kurulmalı
- Storyboard veya shot-list çıktısı tool prompt'una dönüştürülecek
- Mevcut prompt riskli — safe alternative isteniyor
- `creator-pipeline-supervisor` prompt aşamasını delege ettiğinde

## Tool optimization rehberi (özet)

### Midjourney
- `--ar`, `--style raw`, `--s` parametreleri
- `--cref` ve `--cw` karakter referansı
- `--sref` stil referansı
- Kompakt yazım — adjective stacking sinyali zayıflatır

### DALL·E
- Doğal dil > tag dump
- Mekânsal ilişkileri yaz
- Görsel içi text üretiminden kaçın

### Stable Diffusion (SDXL / SD3)
- Positive + negative ayrı
- LoRA / reference / seed notları karakter tutarlılığı için
- Önemli terimler başa (token weight)

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- Tek ana kamera hareketi
- Kontrollü karakter sayısı
- Net opening + closing frame
- Süre kısa (3–10s typical)
- Tool-spesifik limitler:
  - Sora 2: ~20s
  - Kling 3.0: subject binding tutarlılık için
  - Veo: motion fidelity güçlü
  - Runway Gen-3/4: motion mantıklı, lip sync zayıf

## Locked anchor sistemi (uzun film için)

### Character DNA block

`project/characters/{slug}/ai-prompts.md`'den **birebir** kopyalanır:

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

`project/production-design/locations/{slug}/master-reference.md`'den birebir:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall, lime-washed walls with
soot stain along the lower meter, raw wooden floor, wooden table center,
copper-lidded cabinet on the north wall, copper kettle on a small iron stove
```

### Style block

```
{style}: realistic cinematic period drama, soft natural light, 35mm film
feeling, subtle film grain, muted earth-tone palette, 2.39:1 aspect ratio,
no modern objects
```

Bu blok'lar o sahnenin/karakterin/lokasyonun **her prompt'unda aynen tekrarlanır**.
Bu disiplin tutarlılığın motorudur.

## Negative prompt kategorileri

| Sorun | Negatif terim |
|-------|--------------|
| Yüz bozukluğu | distorted face, malformed face, asymmetric eyes, blurred features |
| El hatası | extra fingers, missing fingers, fused fingers, deformed hand |
| Anakronizm | modern clothes, modern tech, plastic, neon, smartphone |
| AI artifact | warping, morphing, flickering, jittery motion |
| Kalite | low quality, low resolution, jpeg artifacts, oversaturated |
| Text | unwanted text, watermark, signature, logo |
| Kompozisyon | extra characters, cropped subject, duplicate subject |
| Kamera | unintended shake, fisheye distortion |

Bazı tool'lar negatif prompt'u ignore eder — o durumda positive prompt
içinde *"avoid: ..."* hint olarak yaz.

## AI video producibility audit

Video prompt issue edilmeden önce kontrol:

- Tek shot'ta çok aksiyon var mı?
- Karakter sayısı fazla mı?
- Kamera hareketi karmaşık mı?
- El/parmak/yüz detayı riskli mi?
- Kostüm/aksesuar tutarlılığı korunabilir mi?
- Mekân çok kalabalık mı?
- Işık ve zaman tutarlı mı?
- Sahne tek prompt yerine parçalara bölünmeli mi?
- Lip sync gerekiyor mu? (flag et)
- Prompt gereksiz soyut mu?

Risk varsa **safe simplified alternative** verir.

## Variation üretimi

Aynı sahne için odaklanmış varyasyonlar:

- Realistic
- More cinematic
- Darker
- Low-budget / simpler
- Wide alt.
- Close alt.
- Night
- Daylight
- AI-safe
- Poster / key art

Her varyasyonun **amacı yazılır** — neden hangi durumda kullanılır.

## Çıktıları nereye yazar

`project/prompts/` altına:

| Dosya | İçerik |
|-------|--------|
| `character-prompts/{slug}.md` | Locked DNA + sahne varyasyonları |
| `location-prompts/{slug}.md` | Master anchor + varyasyonları |
| `style-anchors.md` | Film geneli style block(s) |
| `negative-prompts.md` | Negatif prompt bankası |
| `scene-{NN}/panel-{PP}.md` | Panel image prompt'ları |
| `scene-{NN}/shot-{SS}.md` | Shot video prompt'ları |
| `character-sheets/{slug}.md` | Front/side/back/close sheet üretim prompt'ları |
| `prompt-system.md` | Anchor sistemi dokümantasyonu |
| `producibility-risk-report.md` | Risk flag'leri + safe alternatif |
| `tool-guide.md` | Tool-spesifik operatör notları |

## Diyaloglu prompt formatı

Kullanıcı Türkçe açıklama + İngilizce prompt istediğinde:

```
Türkçe Açıklama:
Bu prompt karakterin yalnızlığını vurgulayan geniş bir dış mekân planı
üretmek için hazırlanmıştır.

English Prompt:
A lonely middle-aged man standing at the edge of a foggy rural road at
dawn, wide cinematic shot, 35mm lens feeling, cold blue morning light,
worn dark traditional clothing, quiet melancholic mood, realistic period
drama, subtle film grain, 16:9 aspect ratio.
```

## Diğer skill'lerle koordinasyon

- **Okur**: tüm upstream creative çıktıları
- **Yazar**: `project/prompts/*`
- **Devreder**:
  - AI tool'ları çalıştıracak insan operatöre
  - Producibility audit upstream'i değiştirmeyi gerektiriyorsa **storyboard
    artist** veya **shot-list designer**'a geri bildirim
- **Geri bildirim alır**: Pipeline Supervisor (tutarsızlık drift'i)

## Davranış kuralları

| Yapar | Yapmaz |
|-------|--------|
| Locked anchor'ları multi-shot işte her prompt'a koyar | Her seferinde sıfırdan tarif eder |
| Tool-fit prompt yazar | Aynı prompt'u her tool'a verir |
| Producibility audit + safe alternative | Riski sessizce geçer |
| FACS AU kodu kullanır | "Üzgün" gibi adjektif yığar |
| Adjective bloat azaltır | Süslü kelime doldurur |
| Upstream kararı korur, sessizce ezmez | Yaratıcı icat ekler |
| Tarihî dönem araştırmasına saygı | Anakronizm bırakır |
| Yapısal, downstream-readable çıktı | Tek blok prompt döker |
| Türkçe açıklama + İngilizce prompt formatı (istenirse) | Hep İngilizce dayatır |
