# Graph Engineering — inceleme ve aşamalı plan

Tarih: 2026-10-03. Bu belge başlangıç incelemesi ve planının tarihsel kaydıdır.
Güncel uygulama ve pilot sonucu: [sonuç raporu](graph-engineering-results.tr.md).

## İnceleme temeli

- [kesin] Yerel HEAD ve GitHub `main`: `c6b6473e16c8191bacab2ab8815c18ece2a07977`.
- [kesin] 11 `skills/creator-*/SKILL.md` var; supervisor bu 11'e dahil.
- [kesin] İnceleme başlangıcında yalnız takipsiz `audit.md` vardı; korunmuştur.
- [kesin] Ortak vault'ta bu repoya ait proje kaydı bulunamadı.
- Yöntem: takipli dosya envanteri, 11 skill'in girdi/çıktı sözleşmeleri,
  supervisor akışı, kurulum ve katkı sözleşmelerinin statik incelemesi.
- Sınır: gerçek agent yürütümü, model çağrısı, medya üretimi ve kurgu denenmedi.

## Doğrulanan bulgular

| Bulgu | Kanıt (repo içi dosya ve satır) | Sonuç |
|---|---|---|
| Paralellik yazılı; kayıtlı yürütme grafı yok | `skills/creator-pipeline-supervisor/SKILL.md:129-135`; takipli dosya envanterinde workflow, schema, test yok | Düğümler, bağımlılıklar ve geçiş koşulları makinece doğrulanamıyor. GitHub issue/PR şablonları yürütme workflow'u değildir. |
| Tasarım departmanları karşılıklı çıktı okuyor | `skills/creator-character-designer/SKILL.md:296-301`, `skills/creator-production-designer/SKILL.md:240-244`, `skills/creator-cinematographer/SKILL.md:187-192` | Aynı turda hem paralel üretim hem tamamlanmış karşılıklı girdiler varsayılamaz. |
| Prompt yazma sahipliği çakışıyor | `skills/creator-storyboard-artist/SKILL.md:200-201` ile `skills/creator-prompt-engineer/SKILL.md:282-300` | Aynı `project/prompts/scene-{NN}/panel-{PP}.md` iki yazara açık. |
| Çakışmanın kapsamı daha geniş | `skills/creator-cinematographer/SKILL.md:154-155` | DOP da prompt engineer'ın `prompts/*` alanına yazabiliyor. |
| QC mevcut, bağımsızlık şartı eksik | `skills/creator-pipeline-supervisor/SKILL.md:170-171,319-330` | Supervisor hem kanonu derliyor hem ona göre denetliyor; ayrı reviewer kimliği ve onaylanan sürüm bağı yok. |
| Revizyon takibi mevcut, dosya düzeyinde izlenebilirlik eksik | `skills/creator-pipeline-supervisor/SKILL.md:272-300` | Durum tablosu ve revizyon isteği korunmalı; bunlar dosya hash'i, tüketilen sürüm ve otomatik stale hesabı içermiyor. |
| İlk üretim ile revizyon girdileri ayrılmamış | `skills/creator-screenwriter/SKILL.md:139-140`, `skills/creator-shot-list-designer/SKILL.md:54` | Opsiyonel geri beslemeler zorunlu başlangıç bağımlılığına çevrilirse yeni döngüler oluşur. |
| QC yolu tutarsız | `skills/creator-final-cut-editor/SKILL.md:61` ve supervisor `:163` | Editor supervisor raporlarını continuity altında bekliyor; asıl alan qc. |

Kök neden: uzmanlık talimatları güçlü; artefakt sözleşmeleri, sürüm bağımlılıkları
ve onay geçişleri aynı kesinlikte tanımlanmamış. Skill'leri yeniden yazmak gerekmez.

## Yaklaşım ve sınırlar

Graph Engineering burada: her düğümün girdisi, çıktısı, tek yazarı, bağımlılığı,
doğrulama koşulu ve revizyon etkisi açıkça kayıtlı bir üretim grafı anlamındadır.
İlk sürüm dosya tabanlı ve elle yürütülür. Yeni framework, servis veya otomatik
agent çağrı döngüsü gerektirmez. Graf, aynı skill'in farklı aşamalarda birden çok
düğüm olarak kullanılmasına izin verir; skill sayısı 11 kalır.

Her tur bir DAG'dır. Geri besleme aynı tur içinde çevrim oluşturmaz; yeni revizyon
turu açar. Tasarım taslakları aynı onaylı senaryo/yönetmenlik snapshot'ını okur;
birbirlerinin henüz bitmemiş çıktılarını okumaz. Ortak inceleme tüm taslaklar
bittikten sonra yapılır. Departmanlar kendi düzeltmelerini yazar; supervisor
onaylı sürümlerden kanonu derler. Çözülemeyen yaratıcı karar kullanıcıya gider.

## Aşamalar ve geçiş ölçütleri

| Aşama | Somut değişiklik | Tamamlanma ölçütü |
|---|---|---|
| 1 — Sözleşme | `workflows/single-scene.v1.json`, sahiplik tablosu, artefakt/run/review/revision JSON Schema'ları | Tüm düğüm ve skill referansları çözülür; zorunlu graf çevrimsizdir; aynı dosyanın iki yazarı yoktur. |
| 2 — Küçük skill uyarlamaları | Supervisor'a graf kapıları; üç tasarım skill'ine taslak/ortak inceleme ayrımı; storyboard ve DOP'a kendi alanında prompt taslağı; editor QC yolu düzeltmesi | Mevcut adlar, uzmanlık içeriği ve çıktı alanları korunur; çelişkili doğrudan yazım cümleleri giderilir. |
| 3 — Doğrulama | Küçük yerel validator; şema, sahiplik, bağımlılık/hash, onay ve stale kontrolleri | Geçerli örnek geçer; çift yazar, eksik girdi, eski onay, çevrim ve başarısız QC örnekleri reddedilir. |
| 4 — Tek sahne pilotu | İzole `examples/single-scene/` altında gerçek metin çıktıları ve yürütme kayıtları | İki koşu: ilk üretim ve kontrollü revizyon. Ayrı reviewer, ilgili dosya sürümlerini denetler; kanıt raporu çıkar. |
| 5 — Değerlendirme | Sonuçlar, maliyet, yeniden yapılan işler ve eksik sözleşmeler | Pilot kabul ölçütleri sağlanınca medya ve çok sahne kapsamı ayrıca genişletilir. |

Bu yollar öneridir; bu incelemede workflow veya validator oluşturulmadı.
Kurulum symlink tabanlı olduğundan ortak şemaların kurulu skill'den nasıl
bulunacağı 1. aşamada açıkça tanımlanıp geçici bir kurulum hedefinde denenmelidir.
Skill talimatları İngilizce kalır. README değişirse çeviri senkronu ayrıca izlenir.

## Dosya sahipliği

- Screenwriter: `screenplay/`; director: `continuity/`.
- Character designer: `characters/`.
- Production designer: `production-design/`, `cinematography/` alt ağacı hariç.
- Cinematographer: `production-design/cinematography/`; prompt taslakları da burada.
- Storyboard artist: `storyboards/`; mevcut `scene-{NN}/prompts.md` taslak alanı kalır.
- Shot-list designer: `shot-list/`.
- Prompt engineer: `prompts/` altında nihai görüntü/video promptlarının tek yazarı.
- Sound/music designer: `sound/`; ses promptları kendi alanında kalır.
- Final-cut editor: `cuts/`; medya teslim alanı genişleme aşamasında ayrıca sözleşmeye bağlanır.
- Supervisor: `bible/` ve koordinasyon kayıtları; bağımsız review raporları hariç `qc/`.
- Ayrı reviewer: yalnız ayrılmış review rapor alanı; incelenen içerikleri değiştiremez.
- Operatör: `generated-assets/`; pilotta gerçek medya yoksa bu adım beklemede kalır.

Sahiplik yalnız geniş glob karşılaştırmasıyla değil, alt ağaç istisnaları ve
gerçek çıktı yollarıyla doğrulanmalı. Tek başına skill metni yazmayı engellemez;
elle yürütülen pilotta önce/sonra dosya farkları da incelenir.

## Kayıt sözleşmesi

Markdown yaratıcı içerik korunur; yanına JSON kayıtları eklenir:

- Artefakt: `artifact_id`, `scene_id`, `shot_id` (gerekiyorsa), `path`, `owner`,
  `revision`, `sha256`, `inputs` (artefakt kimliği + hash), `status`.
- Koşu: `run_id`, `node_id`, `skill`, `actor_id`, `attempt`, başlangıç/bitiş,
  girdi snapshot'ı, çıktı referansları, sonuç ve hata nedeni.
- İnceleme: `reviewer_id`, incelenen tam hash'ler, kontroller, bulgular,
  `pass/fail`, onaylayan ve tarih. Yazarın kendi kontrolü bağımsız review sayılmaz.
- Revizyon: sebep, değişen artefaktlar, etkilenen dosyalar, yeniden çalışacak
  düğümler ve kapanış kanıtı. Eski kayıtlar üzerine yazılmaz.

Durumlar: `pending → ready → running → produced → validated → approved`;
ayrıca `blocked`, `failed`, `stale`. Dosyanın var olması tamamlanma değildir.
Girdi değişirse tüketiciler geçişli olarak stale olur; eski hash'e verilen onay
yeni sürüm için geçersizdir. Bilinmeyen bağımlılıkta güvenli tarafta kalıp kapsam
genişletilir. Supervisor koordinasyon durumunun tek yazarıdır; çalışanlar kendi
run sonuçlarını ayrı dosyalarda teslim eder.

## Tek sahnelik ilk deneme

Öneri/varsayım: `scene-01`, 15 saniye, 3 plan, tek yetişkin karakter, tek oda,
tek ana nesne, diyalogsuz. Karakter masadaki kapalı mektubu fark eder, yaklaşır,
almadan durur. Bu bir teknik test brief'idir; gerçek filmin konusu olarak kabul
edilmiş değildir. İlk pilot metin ve kayıt üretir; görsel/video kalitesi ölçmez.

Akış:

```text
brief → screenplay → direction → başlangıç onayı
    → [character draft | production draft | cinematography draft]
    → ortak inceleme → sahiplerinin düzeltmeleri → tasarım onayı
    → supervisor: kilitli kanon
    → storyboard → shot list
    → [image/video prompts | sound plan]
    → bağımsız review → üretime hazır paket
    → operatör medya üretimi [ilk pilot dışında]
    → kurgu / son QC / teslim [ilk pilot dışında]
```

Reviewer ayrı bir yürütücü/oturum olmalı; aynı oturumun rol değiştirerek verdiği
onay bağımsızlık kanıtı sayılmamalı. Bu inceleme sırasında reviewer çağrılmadı.

Pilot sınamaları:

1. Üç taslak aynı girdi snapshot'ından çıkar; birbirlerinin dosyalarını yazmaz.
2. Kostüm–dekor renk çatışması kontrollü eklenir; ortak onay kapanmadan sonraki
   düğüm başlayamaz. Karar ve sahiplerin düzeltmeleri kayda girer.
3. Üç planın karakter, mekân, ekran yönü, süre ve kilitli prompt blokları denetlenir.
4. Storyboard'un nihai prompt yoluna yazma girişimi kontrol tarafından reddedilir.
5. Onaydan sonra mektup kırmızı zarftan krem zarfa değiştirilir. Gerçek girdi
   kenarlarına göre kanon, storyboard, shot list, prompt ve review kayıtlarının
   hangilerinin stale olduğu dosya listesiyle gösterilir. Renge bağımlı olmayan
   ses planı ancak kaydı bunu kanıtlıyorsa güncel kalır.
6. Bir düğümün başarısızlığı/kesintisi simüle edilir; kısmi çıktı onaylanamaz,
   tekrar başlatma onaylı ilgisiz çıktıları yeniden üretmez.
7. Son rapor: üretilen/değişen dosyalar, geçen/kalan kontroller, yeniden koşulan
   düğümler ve gerçek harcama/süre (ölçüldüyse). Medya ve teslim tamamlandı denmez.

## Karar önerisi

Önce 1–3. aşamayı küçük bir yerel değişiklik olarak uygula; ardından tek sahnede
4. aşamayı çalıştır. Pilot kanıtı olmadan 11 skill'in tamamına geniş yeniden
yazım veya tam otomatik orkestrasyon ekleme. Mevcut QC ve revizyon bilgisini
silmek yerine somut kayıtlarla güçlendir.
