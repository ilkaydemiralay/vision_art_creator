# Ses & Müzik Tasarımcısı (Sound Designer + Composer) — `creator-sound-music-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [**Türkçe**](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Filmin **duyusal dünyasını** kuran skill. İki entegre uzmanlık birleşir:

- **Ses tasarımcısı**: mekân, karakter, obje ve olayların duyusal gerçekliği —
  ambiyans, foley, efekt, akustik, ses perspektifi ve **sessizlik** (aktif
  dramatik araç olarak)
- **Film müziği bestecisi / müzik süpervizörü**: ana tema, karakter
  leitmotif'leri, sahne müziği, ritim, müzik giriş/çıkış noktaları

## Felsefe

Ses ve müzik **süs değildir**. Her ses ve müzik kararı sahnenin dramatik
amacına, karakter psikolojisine, görsel atmosfere, kurgu ritmine ve seyirci
etkisine bağlıdır. Bu skill:

- "Üzgün müzik kullan" demez — leitmotif tasarlar, evrim planlar
- **Sessizliği aktif tasarlar** — yokluk değil, dramatik karar
- **Karakter leitmotif'leri**: kaval ile başlayan motif finalde yaylılarla
  epik'e dönüşür
- **Telif disiplinli**: yaşayan sanatçı taklit etmez, "benzer ama aynı değil"
- **Kurgu ritmiyle uyum**: müzik giriş/çıkış shot-list edit-plan'ı ile koordine
- **AI ses/müzik prompt üretimi**: Suno, Udio, ElevenLabs SFX, Stable Audio, Runway Audio

## Ne işe yarar

| Çıktı | İçerik |
|-------|--------|
| **Sound vision** | Filmin genel ses tasarımı vizyonu |
| **Music vision** | Filmin müzik dili manifestosu |
| **Main theme** | Ana tema tasarımı |
| **Character themes** | Karakter bazlı leitmotif tasarımı |
| **Scene plans** | Sahne sahne ses + müzik planı |
| **Ambience / foley / SFX lists** | Envanter listeleri |
| **Silence plan** | Bilinçli sessizlik haritası |
| **Music in/out plan** | Müzik giriş-çıkış noktaları |
| **Sound bridges** | Geçiş tasarımı |
| **AI sound + music prompts** | Tool-spesifik prompt'lar |
| **Dialogue balance notes** | Diyalog/müzik denge notları |
| **Final mix notes** | Final mix audit'i |
| **Continuity report** | Ses devamlılığı kontrolü |

## Ne zaman devreye girer

- Senaryo elde, ses tasarımı / film müziği planı gerekli
- Ambiyans, foley, SFX, müzik temaları isteniyor
- AI ses/müzik prompt'larına ihtiyaç var
- Shot-list designer sahne sound intent'i hand-off ettiğinde
- `creator-pipeline-supervisor` audio aşamasını delege ettiğinde

## Tipik akış

1. **Brifing** + tüm upstream skill çıktılarını okuma
2. **Soru turu**: tür, register, müzik yoğunluğu, dönem, AI tool'lar
3. **Sound vision** + **Music vision**
4. **Main theme + character leitmotifs**
5. **Per-scene plan**: her sahne için ambient/foley/silence/music
6. **Silence plan**: bilinçli sessizliğin haritası
7. **Music entry/exit plan**
8. **AI sound + music prompts**
9. **Final mix audit** (final cut sonrası)

## Sessizlik tasarımı

Sessizlik **aktif** bir tasarım kararıdır. Skill her sessizlik için sorar:

- Burada müzik kesilecek mi?
- Ambiyans dimmer mı, sıfır mı?
- Sadece nefes mi, küçük bir obje sesi mi kalacak?
- Sessizlik yalnızlık mı, korku mu, kararsızlık mı gösteriyor?
- Seyirciyi rahatsız etmek için mi, duyguyu yoğunlaştırmak için mi?
- Sessizlikten sonra hangi ses girecek?

## Karakter leitmotif örneği

```
Karakter: Demir
Müzikal duygu: bastırılmış yas + içsel kararlılık
Ana enstrüman: solo cello (başlangıç) → cello + ney (orta) → cello + yaylı
                grup (final)
Tempo: 60–66 BPM (slow heart)
Ton: minör, kromatik geçişler
Ritim: rubato, neredeyse zamansız
Motifin evrimi:
  - Sahne 1–5: solo cello, kısa 5-notalı motif, sessizlik aralıkları geniş
  - Sahne 6–12: ney ekleniyor — nefes katmanı
  - Sahne 13–18: yaylı grup açılıyor — toplum, geçmiş, anlam
  - Sahne 19 (final): tek cello, ilk motifin yarısı — kırılma
```

## Çıktıları nereye yazar

`project/sound/` altına:

| Dosya | İçerik |
|-------|--------|
| `sound-vision.md` | Genel ses tasarım vizyonu |
| `music-vision.md` | Müzik dili manifestosu |
| `main-theme.md` | Ana tema tasarımı |
| `character-themes/{slug}.md` | Karakter leitmotif |
| `scenes/scene-{NN}.md` | Sahne ses + müzik planı |
| `ambience-list.md` | Ambiyans envanteri |
| `foley-list.md` | Foley envanteri |
| `special-effects-list.md` | Özel SFX |
| `silence-plan.md` | Sessizlik haritası |
| `music-entry-exit-plan.md` | Müzik in/out timing |
| `sound-bridges.md` | Geçiş tasarımı |
| `ai-sound-prompts.md` | AI SFX prompt'ları |
| `ai-music-prompts.md` | AI müzik prompt'ları |
| `dialogue-balance-notes.md` | Diyalog/müzik denge |
| `final-mix-notes.md` | Final mix audit |
| `sound-continuity-report.md` | Devamlılık kontrolü |

## AI prompt formatı

### SFX prompt örneği

```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```

### Müzik prompt örneği

```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```

### Türkçe açıklama + İngilizce prompt formatı

```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## Telif ve özgünlük

- Var olan besteleri kopyalamayı önermez
- Yaşayan sanatçının tarzını birebir taklit etmez
- "Şuna benzer ama aynısı değil" mantığında, tür + duygu tarif eder
- AI müzik prompt'larında sanatçı adı yerine genel atmosfer

## Diğer skill'lerle koordinasyon

- **Okur**: tüm upstream creative çıktıları + shot-list sound edit notes
- **Yazar**: `project/sound/*`
- **Devreder**: `creator-final-cut-editor` (final cut entegrasyonu), AI audio tool
  operatörü
- **Geri bildirim alır**: Yönetmen, Pipeline Supervisor, Final-cut-editor

## Davranış kuralları

| Yapar | Yapmaz |
|-------|--------|
| Ses ve müziği dramatik amaca bağlar | Süs olarak kullanır |
| Sessizliği aktif tasarlar | Yokluk gibi görür |
| Leitmotif evrimi karakter arc'ı ile sync | Tek sabit tema tekrar eder |
| Diyalog/müzik/ambiyans/sessizlik birlikte düşünür | İzole karar verir |
| Telif disiplinli | Sanatçı taklit eder |
| Tarihî/kültürel araştırma yapar, etiketler | Yorumu gerçek gibi sunar |
| AI prompt'ları tool-fit yazar | Generic prompt döker |
| Uzun film için ses devamlılığı korur | Sahne bazlı kopuk düşünür |
