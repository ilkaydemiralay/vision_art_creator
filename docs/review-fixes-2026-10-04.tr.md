# Bağımsız denetim bulguları — düzeltme kaydı

Tarih: 2026-10-04. Kapsam: 2026-10-03 bağımsız salt-okunur denetimindeki 10 bulgu.
11 skill korundu. Önceki pilot ve onay kayıtları değiştirilmedi.

| # | Düzeltme | Doğrulama |
|---|---|---|
| 1 | Başarılı tasarım review'u `approver_role: director|user` gerektirir. Coordinator reddedilir. | Eksik rol ve coordinator ret, director/user kabul testleri. Rol beyanı kimlik doğrulaması değildir. |
| 2 | Başarısız v00 design kapısını tüketen canon run'ı için doğrudan partial-mode regresyonu eklendi. | `failed approval: design` beklenir. |
| 3 | `qc/reviews/` bu profil için ayrılmış ama kullanılmayan alan olarak belgelendi; supervisor istisnası açıklandı. | Workflow sahiplik testi korunuyor; review kanıtları manifest yanında kalır. |
| 4 | Açık `--allow-growth` ile kısmi kayıttan büyüme doğrulanır; mevcut artefaktlar silinemez, yeni artefakt revizyonu 1 olmalıdır. | v00→v01 soy kaydı geçti; bayraksız büyüme, silme ve yanlış yeni revizyon reddedilir. |
| 5 | Pilot kaydının bir duruşu temsil ettiği açıklandı. Zamanlar dosya kaydı zamanıdır, gerçek bekleme/üretim süresi değildir. | Sonuç raporu ve workflow referansı güncellendi; eski zamanlar değiştirilmedi. |
| 6 | RFC3339 ve saat dilimi zorunluluğu doğrudan uygulanır; opsiyonel format paketine bağlı değildir. | Tümü saat dilimsiz manifest, yanlış tarih, yanlış offset ve eksik sözdizimi reddedilir; Z ve offset kabul edilir. |
| 7 | `validate_revision()` artık önceki manifestin yolunu alıp tek okumada ham byte hash'ini kendisi doğrular. CLI da aynı API'yi kullanır. | İçeriği aynı JSON'a fazladan newline eklenmesi bile eski hash ile reddedilir. |
| 8 | v1 kapsam daraltmaları belgelendi: artefakt status türetilir; scheduler yok; skill node owner'dan bulunur; scene-level dokümanlarda shot_id yok. | Workflow referansının kapsam bölümü. |
| 9 | DOP çıktı tablosundaki çift `cinematography/` kaldırıldı: göreli `scene-{NN}.md`. | SKILL.md format doğrulaması ve mevcut workflow yolu. |
| 10 | Yalnız `.DS_Store` adlı normal metadata dosyaları envanterden hariç tutulur. Diğer gizli dosyalar kayıtsızsa reddedilir. | Kökte ve alt dizinde Finder dosyaları geçer, `.hidden-prompt.md` reddedilir. |

## Eski onayların uyumluluğu

Review şemasındaki yeni rol alanı, eski belgeler okunabilsin diye opsiyoneldir;
başarılı tasarım onayında validator tarafından zorunlu tutulur. Eski v01/v02
manifestlerine sonradan rol/onay eklenmedi. Varsayılan tam doğrulama bunları
`design approval requires director/user role` ile reddeder.

Tarihsel denetim için `--legacy-approvals` açıkça seçilir. Sonuç scope alanında
“historical compatibility only; not production approval” yazar. Bu mod bile
beyan edilmiş coordinator rolünü kabul etmez. Yeni üretimde kullanılmamalıdır.
Yeni rolle geçerli akış test verisinde sınandı; gerçek yeni yönetmen/kullanıcı
onayı alınmış gibi raporlanmadı. Eski bağımsız reviewer raporları tarihsel kalır.

v00→v01 kaydı `examples/single-scene/lineage-v00-v01.json` dosyasındadır;
2026-10-04'te mevcut kayıtlardan geriye dönük çıkarıldığı açıkça belirtilmiştir.
`affected`/`rerun_nodes` büyüme modunda ilk kez üretilen düğümleri de içerir.
Soy doğrulaması, iki paketin içerik doğrulamasının yerine geçmez.

## Doğrulama ve kalan sınırlar

44 test, workflow CLI, v00 partial, v01/v02 tarihsel uyumluluk kontrolleri,
v00→v01 büyüme ve v01→v02 revizyon kontrolleri geçti. Eski üç snapshot'ın bütün
kaynak dosyaları kapanış SHA256 envanteriyle karşılaştırıldı. Sonuçlar:
`examples/single-scene/verification-20261004.json`.

11 skill format doğrulaması ve `git diff --check` geçti. Python 3.14 ortamı
kullanıldı; testler ayrıca Python 3.10.20 ve 3.11.15 ile geçti. Gerçek medya ve eşzamanlı agent yürütümü sınanmadı.
Düzeltmeler 2026-10-04'te ayrı bir oturumda yeniden çalıştırıldı: 44 test ve yukarıdaki tüm CLI kontrolleri aynı sonucu verdi.

```sh
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_graph.py validate --manifest examples/single-scene/v01/manifest.json --legacy-approvals
.venv/bin/python scripts/validate_graph.py validate --manifest examples/single-scene/v02/manifest.json --legacy-approvals
.venv/bin/python scripts/validate_graph.py revision --previous examples/single-scene/v00-conflict/manifest.json --manifest examples/single-scene/v01/manifest.json --record examples/single-scene/lineage-v00-v01.json --allow-growth
.venv/bin/python scripts/validate_graph.py revision --previous examples/single-scene/v01/manifest.json --manifest examples/single-scene/v02/manifest.json --record examples/single-scene/v02/revision.json
```
