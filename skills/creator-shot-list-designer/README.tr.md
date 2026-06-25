# Shot List Designer — `creator-shot-list-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · **Türkçe** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Sahneleri ve storyboard'ları **shot list + kurgu intent**'e çeviren skill.
Pre-production planlaması ile editorial intent'in birleştiği yer. Final-cut
editor değildir — material üretilmeden ÖNCE editorial niyeti tasarlar ki
çekim doğru parçaları üretsin.

## Felsefe

Shot list teknik envanter değil, **dramatik + editorial niyetin haritasıdır**.
Bu skill:

- **Shot economy**: her shot tek bir net aksiyon taşır
- **Edit rhythm awareness**: hangi shot uzun tutulur, hangisi hızla kesilir?
  shot süresi bir editorial karardır
- **Screen direction + continuity**: kesmelerde uzay/zaman tutarlılığı
- **Producibility for AI**: tek-shot karmaşıklığını AI tool kısıtlarına göre planlar
- **Editorial intent before production**: kurgu mantığı çekimden ÖNCE belirlenir
  ki gereksiz shot çekilmesin
- **Audience experience design**: izleyici ne hisseder, ne öğrenir, ne saklanır?

## Ne işe yarar

| Çıktı | İçerik |
|-------|--------|
| **Per-scene shot list** | Kanonik shot listesi, dramatik + editorial gerekçeli |
| **Edit plan** | Sahne içi tempo, kesme noktası, açılış/kapanış görüntüsü |
| **Transition design** | Sahneler arası geçiş kararları (hard cut, match, J/L, sound bridge) |
| **Continuity risk audit** | Shot'lar arası tutarlılık risklerinin raporu |
| **Sound edit notes** | Ses tasarımcısı için J-cut / L-cut / silence noktaları |
| **Film-wide shot list** | Tüm filmi kapsayan konsolide liste |
| **Rhythm map** | Sahne sahne tempo (shot süresi aralıkları) |
| **Redundancy report** | Kesilmesi/birleştirilmesi gereken shot'lar |
| **Final editor notes** | Final-cut-editor'a editorial intent hand-off |

## Ne zaman devreye girer

- Sahne ve storyboard elde, shot bazlı plana ihtiyaç var
- Edit-aware shot sıralama isteniyor
- Uzun sahneler AI üretilebilir parçalara bölünecek
- Yönetmen veya DOP yapısal çekim/üretim planı talep ettiğinde
- `creator-pipeline-supervisor` pre-edit planlamasını delege ettiğinde

## Tipik akış

1. **Brifing** + tüm upstream skill çıktılarını okuma
2. **Soru turu**: format, edit ritmi, ton, AI tool'lar
3. **Shot list (per scene)**: kanonik yapıda, dramatik + editorial gerekçeli
4. **Edit plan (per scene)**: tempo, açılış/kapanış, kesme noktası
5. **Transition design**: sahneler arası geçişler
6. **Continuity audit**: cross-shot riskler
7. **Rhythm map**: film geneli tempo haritası
8. **Redundancy report**: kesilebilir shot tespiti
9. **Hand-off**: creator-prompt-engineer için shot prompt verisi + creator-final-cut-editor için editorial intent

## Shot — kanonik yapı

```
Scene 04 — Shot 04.02
Shot name: "Kettle close, sessizlik"
Shot type: insert
Frame scale: extreme close
Camera angle: eye level (yan-üst)
Camera movement: static
Lens recommendation: 100mm macro feeling
Estimated duration: 4s
Location: Anatolian kitchen 1980s [anchor: kitchen-anatolian-1980s]
Time: gece
Characters in frame: yok (sadece kettle)
Character action: kettle ıslığı sönüyor (off-screen Demir ateşi kapatıyor)
Dialogue / silence note: SİLENCE (yalnızca kettle + saat tıkırtı)
Light / atmosphere: pencereden gri ay ışığı, bakır kettle highlight
Sound / music note: müzik YOK; saat tıkırtısı + kettle dying
Dramatic purpose: Demir'in iç dönüşümüne sembolik karşılık
Edit purpose: 4 saniye nefes — kesmeye gerek yok, hold it
Link to previous shot: 04.01 (Demir oturuyor wide) — match by sound
Link to next shot: 04.03 (Demir yüzü close, ilk göz kırpma) — hard cut
Continuity note: kettle = aynı bakır, aynı leke pattern
AI video production note: tek aksiyon (ıslığın sönmesi) + static camera = düşük risk
Safe alternative: 6s versiyon — daha yavaş ıslık fade, kamera çok yavaş push-in
```

## Editorial intent — sahne planı

Sahne bazlı editorial sorular:

- Hangi shot sahneyi açar?
- Hangi görüntü kapatır?
- Hangi shot uzun tutulur?
- Hangi shot kısa kesilir?
- Reaction shot'lar nereye yerleşir?
- Sessizlik nerede uzar?
- Sert kesme nerede gerekir?
- Yumuşak geçiş nerede?
- Hangi görüntü bir sonraki sahneye bağlanır?
- Hangi shot dramatik tepe noktayı taşır?
- Hangi shot gereksizdir?
- Hangi shot bilgi verir, hangisi duygu?

`project/shot-list/scene-{NN}/edit-plan.md` altına yazılır.

## Çıktıları nereye yazar

`project/shot-list/` altına:

| Dosya | İçerik |
|-------|--------|
| `scene-{NN}/shot-list.md` | Sahne shot listesi |
| `scene-{NN}/edit-plan.md` | Edit niyeti + tempo |
| `scene-{NN}/transitions.md` | Geçiş kararları |
| `scene-{NN}/continuity-risks.md` | Continuity audit |
| `scene-{NN}/sound-edit-notes.md` | Sound designer hand-off |
| `film-shot-list.md` | Tüm film konsolide liste |
| `rhythm-map.md` | Tempo haritası |
| `redundancy-report.md` | Kesilebilir shot'lar |
| `ai-production-shot-guide.md` | AI tool kısıt rehberi |
| `final-editor-notes.md` | Final-cut-editor için intent |

## Geçiş türleri (editorial kullanımı)

| Geçiş | Editorial kullanım |
|-------|-------------------|
| Hard cut | Ani dramatik kırılma |
| Match cut | İki görüntü arası anlam köprüsü |
| Fade in/out | Zamansal/duygusal açılış/kapanış |
| Dissolve | Zaman geçişi, duygu harmanı |
| J-cut | Sonraki sahnenin sesi önce gelir (yumuşak akış) |
| L-cut | Mevcut sahnenin sesi uzatılır (tutulan duygu) |
| Sound bridge | Ses üzerinden mekân/zaman değişimi |
| Visual motif | Tekrarlayan görsel ile köprü |
| Object transition | Şekil eşleşmesi |
| Movement transition | Yön süreklilik |
| Time jump | Ani zaman atlama |
| Flashback | Filtre/lens/blur/ses ipucuyla |
| Parallel edit | İki mekân iç içe |

## AI video producibility kuralları

- Tek shot'ta tek net aksiyon
- Tek ana kamera hareketi (zincirleme değil)
- Kontrollü karakter sayısı
- Net görsel hedef
- Karmaşık hareketi multi-shot'a böl
- Riskli el/parmak/dudak senkronu için flag
- Kalabalık için seçici kadraj
- Locked location + character anchor'ları her prompt'ta
- Shot süresi 3–10s typically
- Her shot tek bir video prompt'a temiz mapping

Risk tespit edildiğinde flag:

> *"Bu shot AI video için fazla karmaşık — iki shot'a böl."*
> *"Dudak senkronu burada fail edebilir; speaker yerine reaction shot kullan."*
> *"El hareketi kritik — insert yerine wider kadraj kullan."*
> *"Kalabalık aksiyon — tek shot değil kesmelerle kur."*

## Rhythm ve tempo

"Hızlı olsun" gibi belirsiz ifadeler kullanılmaz. Tempo:

- **Shot süresi aralığı** ile ifade edilir
- **Kesme sıklığı** ile ölçülür

Örnek:
> *"Sahne 3 ortalama 4–6s/shot, sahne 12 ortalama 1.5–3s/shot —
> tempo karakter çelişkisi yükselirken hızlanıyor."*

## Diyalog kurgu intent'i

Diyalog ağırlıklı sahneler için:

- Konuşan mı, dinleyen mi?
- Reaction shot nereye?
- Sessizlik nerede daha güçlü?
- Diyalog üstüne başka görüntü?
- Alt metin yüz ifadesiyle mi?
- Sert kesme vs. doğal overlap?
- Cümle bitmeden kesmek?
- Gereksiz açıklama tekrarı?
- İzleyicinin asıl görmesi gereken duygu kimde?

J-cut / L-cut işaretleri burada belirlenir.

## Diğer skill'lerle koordinasyon

- **Okur**: senaryo, yönetmen vizyonu + direction sheets, DOP per-scene plan,
  storyboard panel verisi, karakter/lokasyon anchor'ları
- **Yazar**: `project/shot-list/*`
- **Devreder**:
  - `creator-prompt-engineer` (shot-level video prompts)
  - `creator-final-cut-editor` (editorial intent dosyaları)
- **Geri bildirim alır**: Yönetmen, Pipeline Supervisor

## Redundancy detection

Uzun AI filmde flag:

- Aynı bilgiyi tekrarlayan shot
- Duygu değiştirmeyen shot
- Ritim düşüren detay shot
- Aşırı reaction kullanımı
- AI-hard ama dramatik katkısı düşük shot
- Geç gir / erken çık fırsatları
- Diyalog yerine görsel anlatılabilir an

*"Bu shot kesilebilir"* veya *"İki shot birleştirilebilir"* açıkça yazılır.

## Davranış kuralları

| Yapar | Yapmaz |
|-------|--------|
| Her shot'a dramatik **ve** editorial gerekçe | Teknik envanter yapar |
| Yönetmen ritim, DOP kadraj, storyboard ile koordine | İzole karar verir |
| Gereksiz shot flag'ler | Doldurma yapar |
| Continuity proaktif kontrol | Çekim sonrası sorun çıkmasını bekler |
| AI tool kısıtına göre tasarlar | Üretilemeyecek shot planlar |
| Riskli shot için safe alternatif | Tek versiyon koyar |
| Diyalogda dinleyeni de düşünür | Sadece konuşanı takip eder |
| Ses ve müzik editorial intent koordine | Sadece picture düşünür |
| Yapısal, downstream-readable çıktı | Tek blok metin döker |
