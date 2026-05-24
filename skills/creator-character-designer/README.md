# Karakter Tasarımcısı & Casting Skill

Karakteri **isim + yaş + dış görünüş** üçlüsünden çıkarıp **bütünlüklü bir
yaratık** olarak tasarlayan skill. Dramatik işlev, psikoloji, biyografi,
beden dili, kostüm, prop'lar, oyuncu profili ve **FACS Action Unit kodlu
ifade kütüphanesi** üretir. Uzun AI film üretiminde karakter tutarlılığını
sağlayan "Character DNA" anchor'larını kurar.

## Felsefe

Karakter rastgele üretilmez — senaryonun ihtiyacından, yönetmenin vizyonundan
ve DOP'un görsel dünyasından türer. Bu skill:

- **Her karakter bir dramatik soruya cevaptır** — yoksa karakteri kesilmesini önerir
- **Want / Need / Fear / Wound** dörtlüsünü her ana karakter için zorunlu kurar
- **FACS Action Units**: "üzgün" demek yerine AU1+AU4+AU15 der —
  AI modelleri ve animatörler anatomik kodu daha tutarlı yorumlar
- **Character DNA**: AI tutarlılığı için kilitli anchor özellikler tanımlar
- **Visual distinction audit**: birden çok karakter varsa silüet, renk, enerji
  ayrımlarını denetler

## Ne işe yarar

| Çıktı | İçerik |
|-------|--------|
| **Character sheet** | Karakter dosyası — psikoloji, kostüm, prop, FACS, AI prompt |
| **Costume bible** | Tüm filmdeki kostüm varyasyonları ve devamlılık |
| **Props list** | Karaktere ait kişisel eşyalar ve dramatik kullanımları |
| **FACS expression library** | Karakter bazlı 3–5 imza ifade, AU kodlu |
| **Casting brief** | Oyuncuda aranan profil (isim önermez, özellik tanımlar) |
| **AI prompts** | Tutarlı karakter referansı için base prompt + sahne varyasyonları |
| **Arc tracker** | Yönetmenin arc tracking'i ile koordineli karakter dönüşümü |
| **Continuity notes** | Sahne sahne kostüm/prop devamlılığı |

## Ne zaman devreye girer

- Senaryo elde, karakterler geliştirilmek isteniyor
- "Karakter sheet hazırla", "kostüm tasarla", "casting profili çıkar"
- AI film için tutarlı karakter referansı gerekiyor
- Yönetmen veya `creator-pipeline-supervisor` karakter aşamasını delege ettiğinde
- Mevcut karakterlerin görsel ayrımı sorgulanıyor

## FACS kullanımı — neden ve nasıl

**Facial Action Coding System (Ekman & Friesen, 1978)** yüz kaslarının
anatomik kodlamasıdır. Action Unit (AU) = belirli bir kas hareketi.

### Neden bu skill kullanıyor?

- **AI generator'lar** "happy face" gibi soyut girdileri tutarsız yorumlar;
  "AU6 + AU12 (Duchenne smile)" daha güvenilir sonuç verir
- **Animator/VFX ekipleri** AU kodlarıyla tek bir referans kümesini paylaşır
- **Karakterin imza ifadesi** dosyalanabilir — örneğin "Demir bastırılmış
  yası AU4 + AU17 (alın çatık, çene kalkık, AU15 yok) ile taşır"

### Yaygın AU kombinasyonları

| İfade | AU'lar |
|-------|--------|
| Duchenne smile (gerçek mutluluk) | AU6 + AU12 |
| Polite smile (sahte/sosyal) | AU12 tek |
| Hüzün | AU1 + AU4 + AU15 |
| Öfke | AU4 + AU5 + AU7 + AU23 |
| Korku | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26 |
| Tiksinti | AU9 + AU15 + AU16 |
| Sürpriz | AU1 + AU2 + AU5B + AU26 |
| Aşağılama (asimetrik) | AU12 (tek taraflı) + AU14 |
| Bastırılmış yas | AU4 + AU17 (AU15 yok) |
| Gergin sükûnet | AU7 + AU23 + AU24 |

## Karakter sheet şablonu (özet)

```
Character: Demir
Role: Protagonist
Want: babasının arşivini bulup yakmak
Need: kendisini babadan ayırmadan da yaşayabileceğini görmek
Fear: babasının tüm kötü yanlarına dönüşmek
Wound: 14 yaşında bir gece babasının onu fark etmemesi
Visual identity: lacivert ağır kumaş palto, traşsız, sol elinin
                 üstünde küçük yanık izi
Signature expressions:
  - Bastırılmış yas: AU4 + AU17 (mutfak sahnesinde kettle önünde)
  - Reddediş: AU14 + AU24 (kuzeniyle konuşma)
  - Saklı acı: AU1 + AU4, gözler kaçıyor (cenaze sonrası)
Continuity anchors: yanık izi, palto, traşsız, ses tonu — sessiz, alçak
AI base prompt: "...same character across all scenes..."
```

## Çıktıları nereye yazar

`project/characters/{karakter-slug}/` altına:

| Dosya | İçerik |
|-------|--------|
| `character-sheet.md` | Kanonik karakter dosyası |
| `costume-bible.md` | Tüm kostüm varyasyonları + devamlılık |
| `props.md` | Karaktere ait eşyalar, dramatik kullanım |
| `facs-expressions.md` | İmza ifade kütüphanesi, AU kodlu |
| `casting-brief.md` | Oyuncu profili / AI yüz prompt'u için temel |
| `ai-prompts.md` | Base prompt + sahne sahne varyasyon |
| `arc-tracker.md` | Yönetmenin arc tracking'i ile sync |
| `continuity-notes.md` | Sahne sahne kostüm/prop devamlılık |

Ayrıca üst dizinde `cast-list.md` — tüm karakterleri özetleyen liste.

## Visual distinction audit

Birden fazla karakter varsa skill şu kontrolleri yapar:

- Silüet ayrımı (boy, duruş, kostüm formu)
- Renk dünyası ayrımı (veya bilinçli zıtlık)
- Enerji register'ı ayrımı
- Konuşma deseni ayrımı
- Ekran varlığı ayrımı (foreground / background tipi)

İki karakter birbirine "karışıyorsa" rapor verir ve revizyon önerir.

## AI tutarlılığı (Character DNA)

Aynı karakteri 50 sahnede aynı yüz/kostümle üretmek için:

1. **Base prompt** — kilit özellikler (yüz şekli, saç, ayırt edici işaret) sabit
2. **Anchor descriptors** — her sahne prompt'unda 2–3 tanesi tekrar geçer
3. **FACS ile ifade** — adjektif değil, AU kodlu
4. **Erken karakter sheet üretimi** — front/side/back/close referans görseller
5. **Scene prompt'unda referans**: "consistent with `characters/demir/sheet.png`"

## Diğer skill'lerle koordinasyon

- **Okur**:
  - `project/screenplay/character-brief.md`
  - `project/continuity/creator-director-vision.md`
  - `project/continuity/performance-notes/*`
  - `project/production-design/cinematography/visual-language.md`
  - `project/production-design/world-bible.md`
- **Yazar**: `project/characters/*`
- **Devreder**: Prompt mühendisi, storyboard, DOP (palet koordinasyonu)
- **Geri bildirim alır**: Yönetmen, Pipeline Supervisor

## Kostüm tasarımı yaklaşımı

Kostüm karakteri anlatır — sadece "giyiyor" değil:

- Ana parça + işlevi
- Kumaş: ağır, yumuşak, sert, lifli
- Renk: paletle uyum/zıtlık
- Eskimişlik / yenilik / hasar / onarım izi
- Dönem doğruluğu
- Karakterin ruh hâli ile ilişki
- Hareket kabiliyetine etki
- Işıkla etkileşim (mat, parlak, transparan, toz tutan)

Her ana sahne için kostüm continuity not'u: sahne içinde değişiyor mu, sahneler
arası değişiyor mu, neden?

## Props yaklaşımı

Prop'lar hikâye aracıdır — dekoratif değil:

- Adı + işlevi
- Karakterle ilişkisi
- Görünüm, malzeme, renk, kondisyon
- Karakter için anlam (hatıra, kimlik, ilişki)
- Dramatik kullanım (önceleme, ödeme, ifşa)
- Kamera nasıl görür (yakın, detay, geçer)
- Devamlılık (her sahnede nerede)

Karakter-prop / mekân-prop sahipliği netleştirilir, **creator-production-designer**
ile koordine edilir.

## Davranış kuralları

| Yapar | Yapmaz |
|-------|--------|
| Karakteri dramatik gerekçe ile üretir | "Bir karakter daha lazım" der |
| Her görsel seçimi arc / fonksiyon / temaya bağlar | İzole estetik seçim yapar |
| Eksik bilgide soru sorar | Sessizce uydurur |
| Kültürel detayda araştırma yapar | Yorumu gerçek gibi sunar |
| FACS AU kodlarıyla ifade tanımlar | "Üzgün" gibi adjektif kullanır |
| Visual distinction audit yapar | İki karakteri birbirine karıştırır |
| Continuity anchor'ları AI prompt'larına gömer | Her sahnede sıfırdan tarif eder |
| Karakter-prop sahipliğini netleştirir | Yapım tasarımcı ile çakıştırır |
| Yapısal, downstream-readable dosyalar verir | Tek blok metin döker |

## Kaynak

NotebookLM — **Creator_SKILLs** notebook'u, kaynak: *Karakter Tasarımcısı ve
Casting AI Skill* (ID: `dab6c1d2`) + FACS eklemesi (kullanıcı talebi)
