# vision_art_creator

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · **Türkçe** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

AI film prodüksiyon skill paketi ([Claude Code](https://claude.com/claude-code)). Senaryodan final cut'a kadar
bir prodüksiyonun her departmanını kapsayan **11 creator skill**'i tek bir
repo'da toplar; başka bir makineye `git clone` + `./install.sh` ile kurulur.

> Bu skill'ler birbirine referans verecek şekilde tasarlanmıştır
> (`creator-pipeline-supervisor` diğerlerini orkestre eder). Hepsini birlikte
> kurmak önerilir.

---

## Kurulum

```bash
git clone https://github.com/<kullanıcı>/vision_art_creator.git ~/projects/vision_art_creator
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

## Nasıl çalışır

Paket **filesystem tabanlı paylaşılan state** üzerinde çalışır. Tüm skill'ler
ortak bir `project/` ağacını (`bible/`, `screenplay/`, `characters/`,
`storyboards/`, `prompts/`, `cuts/`, `qc/`, …) okur ve yazar.
`creator-pipeline-supervisor` canonical dosyaları (proje ve süreklilik
"bible"'larını) tutar ve her departmanın çıktısını bunlara karşı denetler.

Canonical pipeline:

```
0. proje bible & vizyon
1. creator-screenwriter        → senaryo
2. creator-director            → vizyon, yönetmen notları, arklar
3-4-5. creator-character-designer + creator-production-designer
        + creator-cinematographer        (paralel çalışır)
6. creator-storyboard-artist   → prompt'lu paneller
7. creator-shot-list-designer  → shot listesi + edit planı
8. creator-prompt-engineer     → araç-uyumlu görsel + video prompt'ları
   → [AI materyal üretimi — operatör]
9. creator-sound-music-designer → ses + score planı
10. creator-final-cut-editor   → rough → fine → final cut → teslim

Tüm aşamalarda: creator-pipeline-supervisor sürekliliği zorlar, QC yapar,
revizyon döngülerini yönetir ve bible'ları tutar.
```

Sıralama canonical ama rigid değil: yönetmen geri bildirimi senaristi yeniden
tetikleyebilir; yönetmen vizyonu belirlendikten sonra karakter/yapım/görüntü
yönetmenliği genellikle paralel çalışır.

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

## Çeviriler

Bu README ve her skill'in `README.md` dosyası 12 dilde mevcut (üstteki dil
seçicisine bak). `SKILL.md` talimat dosyaları bilinçli olarak İngilizce
tutulur — Claude çalışma anında kullanıcının dilinde yanıt verir ve tek bir
canonical talimat seti, çakışan skill adlarını önler.

---

## Lisans

[MIT](LICENSE) © 2026 İlkay Demiralay.
