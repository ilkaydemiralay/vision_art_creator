# Graph Engineering — ilk uygulama ve tek sahne pilotu

Tarih: 2026-10-03.

2026-10-04 güncellemesi: [bağımsız denetim bulgularının düzeltme raporu](review-fixes-2026-10-04.tr.md).
Eski v01/v02 onayları rol alanı içermediğinden artık yalnız açık
`--legacy-approvals` modunda denetlenir; bunlar yeni üretim onayı sayılmaz.
 Başlangıç commit'i: `c6b6473`.
Bu belge güncel uygulama sonucudur; `graph-engineering-plan.tr.md` başlangıç
incelemesini ve planı tarihsel kayıt olarak korur.

## Değişenler

- 11 creator skill korundu. Sekiz SKILL.md dosyasında sınırlı sözleşme düzeltmesi
  yapıldı; hiçbir skill kaldırılmadı veya yeniden adlandırılmadı.
- Storyboard ve görüntü yönetmeninin prompt taslakları kendi dizinlerinde kalır;
  `prompts/` nihai görüntü/video çıktılarının tek yazarı prompt engineer oldu.
- Supervisor'a ayrı referans belgesi üzerinden kayıtlı graf modu eklendi.
  Tasarımda ortak başlangıç snapshot'ı, taslaklar ve ortak onay ayrıldı.
- `workflows/single-scene.v1.json`: 12 düğümlü, tek sahnelik ön prodüksiyon DAG'ı.
  Mevcut kurgu skill'i korunur; medya ve kurgu bu profilin dışında kalır.
- `schemas/`: workflow, artifact, run, review, manifest ve revision sözleşmeleri.
- `scripts/validate_graph.py`: şema, çevrim, sahiplik, gerçek dosya SHA256,
  bağımlılıklar, onay kapsamı/zamanı, bağımsız reviewer kimliği ve revizyon etkisi.
  Yalnız okur; agent başlatmaz, dosya izinlerini yönetmez.
- Python bağımlılığı `requirements-graph.txt`; testler `tests/test_graph.py`.
  Normal skill kullanımı için Python ortamı gerekmez.

## Pilot kanıtı

Pilot metinleri bu oturumda tek yazar tarafından hazırlandı; yaratıcı roller
ayrı agent'lar gibi sunulmadı. Taslaklar sırayla üretildi, eşzamanlı çalışma
performansı sınanmadı. Ayrı `/root/independent_review` görevi içerik ve kodu denetledi.

| Kayıt | Ne oldu? | Anlamı |
|---|---|---|
| `examples/single-scene/v00-conflict/` | Erik moru hırka ile aynı renk duvar çatışması, başarısız tasarım kapısını temsil eden 7 düğümlü kayıt | Kısmi checkpoint geçerli; üretime hazır paket değil |
| `examples/single-scene/v01/` | Kırık beyaz duvarla çatışma çözüldü; 15 saniye, 3 plan, sabit kırmızı zarf | İlk tam metin paketi; bağımsız içerik denetimi mevcut |
| `examples/single-scene/v02/` | Zarf kırmızıdan kreme değişti; revizyon kaydı ve yeni denetim | Değişiklik etkisi ve çıktıların yeniden kullanımı sınandı |

Revizyonda yeniden çalışılan/kontrol edilen 7 düğüm:
`production`, `design`, `canon`, `storyboard`, `shots`, `prompts`, `sound`.
Değişmeden kullanılan 5 düğüm: `brief`, `script`, `direction`, `character`, `camera`.
Bunların artefakt ve run kayıtları birebir aynı kaldı.

Ses planının metni değişmedi, ancak tüm shot-list dosyasını tükettiği için yeni
sürüme göre yeniden kontrol edildi ve revizyon numarası arttı. Daha dar semantik
bağımlılık olmadığı için sesin güncel kaldığı varsayılmadı.

Sahne: Deniz masadaki kapalı zarfı fark eder, iki adım yaklaşır, dokunmadan durur.
Planlar 0–5, 5–10, 10–15 saniye; kamera ekseni, kostüm, mekân ve zarf sürekliliği
korunur. Bunlar metin sahne/prompt çıktılarıdır; render veya film değildir.

## Doğrulama

- 33 otomatik test: başarılı akış; çevrim, çift yazar, yanlış sahiplik, eksik
  girdi/dosya, hash değişimi, eski/eksik/başarısız onay, yazarın kendi review'u,
  yol/symlink kaçışı, kayıt dışı dosya ve yinelenen revizyon kayıtlarının reddi.
- Başarısız düğümün reddi ve ikinci denemede diğer kayıtların korunması birim
  testinde simüle edildi; gerçek üretim servisi kesintisi sınanmadı.
- Bağımsız denetimde bulunan başarısız checkpoint onay bağı sorunu ve yinelenen
  revizyon kimlikleri düzeltildi; regresyon testleri eklendi.
- 11 skill, skill-creator `quick_validate.py` kontrolünden geçti.
- Geçici hedefe kurulum: 11 symlink ve kurulu supervisor'dan ortak workflow
  kaynaklarının çözülmesi doğrulandı. Kullanıcının kurulum hedefi değiştirilmedi.
- Python 3.14.4 / jsonschema 4.26.0 ile çalıştırıldı. Z zaman damgası normalize
  edilir. 2026-10-04'te 44 test Python 3.10.20 ve 3.11.15 ile de geçti.

Bağımsız raporlar her tam snapshot'ın `review.md` dosyasında; JSON review'ları
manifest içindedir. `v02/revision.json` eski manifestin SHA256 değerine bağlanır.
Bu dosyalar tamamlanmış snapshot olarak korunmalı; revizyon yeni klasöre yazılmalı.

## Çalıştırma

Repo kökünde, Python 3.10+ ile:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-graph.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_graph.py workflow
.venv/bin/python scripts/validate_graph.py validate --manifest examples/single-scene/v00-conflict/manifest.json --partial
.venv/bin/python scripts/validate_graph.py validate --manifest examples/single-scene/v01/manifest.json --legacy-approvals
.venv/bin/python scripts/validate_graph.py validate --manifest examples/single-scene/v02/manifest.json --legacy-approvals
.venv/bin/python scripts/validate_graph.py revision --previous examples/single-scene/v01/manifest.json --manifest examples/single-scene/v02/manifest.json --record examples/single-scene/v02/revision.json
```

Yeni bir paket bağımsız denetim bekliyorsa `validate ... --pre-review` yalnız
teknik hazırlığı doğrular. Yeni paketlerde tam geçiş için `--pre-review` ve `--legacy-approvals`
kullanılmadan kontrol edilmelidir. `revision` komutu sadece geçmiş/etki bağını denetler; iki paketin
ayrı tam doğrulamasının yerine geçmez.

## Sınırlar ve sonraki adım

- Kimlikler/zamanlar operatör beyanıdır; imzalı kimlik doğrulaması değildir.
  Run zamanları kayıt/çıktı oluşturma anlarını gösterir, model düşünme süresini
  veya gerçek maliyeti ölçmez. Token, maliyet ve hız karşılaştırması yapılmadı.
- Dosya sahipliği doğrulanır; işletim sistemi düzeyinde yazma kilidi kurulmadı.
- Onaylar ve bağımlılıklar kayıtlıdır; otomatik scheduler veya agent döngüsü yoktur.
- Promptlar sağlayıcıdan bağımsızdır. Gerçek medya öncesinde araç seçimi,
  sağlayıcıya uyarlama, referans görseller ve üretim parametreleri gerekir.
- Sıradaki küçük adım: aynı sahnede seçilen tek görüntü/video aracıyla sınırlı
  üretim; gerçek referans tutarlılığı ve çıktı kalitesini ölçmek. Çok sahne ve
  tam otomatik yürütme bu pilotun kanıtlarıyla henüz doğrulanmış değildir.

Commit ve push yapılmadı. Önceden bulunan `audit.md` korundu.
