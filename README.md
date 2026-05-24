# vision_art_creator

AI film production skill paketi (Claude Code). Senaryodan final cut'a kadar
bir prodüksiyonun her departmanını kapsayan **11 creator skill**'i tek bir
repo'da toplar; başka bir makineye `git clone` + `./install.sh` ile kurulur.

> Bu skill'ler birbirine referans verecek şekilde tasarlanmıştır
> (`creator-pipeline-supervisor` diğerlerini orkestre eder). Hepsini birlikte
> kurmak önerilir.

---

## Kurulum

```bash
git clone git@github.com:<kullanıcı>/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

`install.sh` her skill için `~/.claude/skills/<skill-adı>` altında bu repo'ya
işaret eden bir **symlink** oluşturur. Avantajı: güncelleme için sadece
`git pull` yeterli — yeniden kurulum gerekmez.

### Seçenekler

```bash
./install.sh --target /path/to/skills   # farklı bir skills dizinine kur
./install.sh --force                    # mevcut isimleri üzerine yaz
./uninstall.sh                          # symlink'leri kaldır
```

`uninstall.sh` sadece bu repo'ya işaret eden symlink'leri siler — yabancı
linkleri veya gerçek dizinleri (`--force` olmadıkça) dokunmaz.

### Doğrulama

Kurulumdan sonra Claude Code'u yeniden başlat ve şunu yaz:

```
/creator-pipeline-supervisor
```

Skill listesinde 11 `creator-*` skill'in göründüğünü kontrol et.

---

## Paketin içeriği

| Skill | Açıklama (özet) |
|---|---|
| `creator-pipeline-supervisor` | Tüm prodüksiyonu orkestre eder, departmanları sıralar, sürekliliği denetler, QC ve teslim hazırlık raporu üretir. |
| `creator-director` | Senaryoyu birleşik yönetmen vizyonuna çevirir: sahne yönetimi, oyunculuk, blocking, tonal kontrol. |
| `creator-screenwriter` | Senaryo, treatment, logline, sahne outline ve diyalog yazımı/revizyonu. |
| `creator-character-designer` | Karakteri bütün olarak tasarlar: psikoloji, biyografi, görsel kimlik, kostüm, prop, FACS-kodlu ifadeler. |
| `creator-production-designer` | Filmin dünyasını kurar: mekan, set, prop, dönem atmosferi, renk/malzeme dili, süreklilik anchor'ları. |
| `creator-cinematographer` | Görsel dili tasarlar: ışık, kamera, lens, çerçeveleme, renk, atmosfer, hareket. |
| `creator-storyboard-artist` | Sahneleri panel panel görselleştirir: shot ölçekleri, açılar, blocking, kompozisyon, AI prompt'ları. |
| `creator-shot-list-designer` | Sahne ve storyboard'ları teknik shot listesine çevirir, AI-üretilebilir parçalara böler. |
| `creator-sound-music-designer` | Filmin sonik dünyası: atmosfer, foley, SFX, score, leitmotif, sahne bazlı müzik planı, AI ses prompt'ları. |
| `creator-prompt-engineer` | Tüm departman çıktılarını GPT Image 2.0, Nano Banana, Sora, Veo, Runway, Kling, Higgsfield vb. için tutarlı prompt'lara çevirir. |
| `creator-final-cut-editor` | AI'la üretilmiş shot/ses/müzik/grafiği bütün bir filme dönüştürür: rough/fine/final cut, AI hata triyajı, teslim formatları. |

Her skill'in tam tanımı kendi `SKILL.md` dosyasında yer alır.

---

## Güncelleme

```bash
cd ~/projects/vision_art_creator
git pull
```

Symlink olduğu için ekstra adım gerekmez.

---

## Geliştirme

1. Repo içindeki bir skill'i düzenle (`skills/creator-*/SKILL.md`).
2. Claude Code'da değişikliği test et — symlink olduğu için anında geçerli.
3. Commit + push.

Yeni bir creator skill eklemek için:

```bash
mkdir -p skills/creator-yeni-skill
# SKILL.md ve README.md yaz
./install.sh   # yeni skill için symlink oluştur
```

---

## Lisans

Proprietary. Bkz. [LICENSE](LICENSE). İzinsiz kullanım yasaktır.
