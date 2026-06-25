# مصمّم الصوت والموسيقى — `creator-sound-music-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [**العربية**](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

المهارة التي تبني **العالم الحسّي** للفيلم. يجتمع هنا تخصّصان متكاملان:
- **مصمّم الصوت**: الواقع الحسّي للأماكن والشخصيات والأشياء والأحداث — ambience وfoley وتأثيرات وصوتيات ومنظور صوتي و**الصمت** (كأداة درامية فاعلة)
- **مؤلّف موسيقى الفيلم / مشرف الموسيقى**: الثيمة الرئيسية وleitmotifs الشخصيات وموسيقى المشاهد والإيقاع ونقاط دخول/خروج الموسيقى

## الفلسفة
الصوت والموسيقى **ليسا زينة**. كل قرار صوتي وموسيقي مرتبط بالغرض الدرامي للمشهد، وبنفسية الشخصية، وبالأجواء البصرية، وبإيقاع المونتاج، وبتأثيره في الجمهور. هذه المهارة:
- لا تقول "استخدم موسيقى حزينة" — بل تصمّم leitmotifs وتخطّط لتطوّرها
- **تصمّم الصمت بشكل فاعل** — ليس غياباً، بل قراراً درامياً
- **leitmotifs الشخصيات**: motif يبدأ على flute يتحوّل إلى عمل ملحمي مع الوتريات في الـ finale
- **منضبطة من حيث حقوق النشر**: لا تقلّد فنانين أحياء، "مشابه لكن ليس نفسه"
- **متزامنة مع إيقاع المونتاج**: دخول/خروج الموسيقى منسّق مع خطة مونتاج الـ shot-list
- **توليد prompts صوت/موسيقى بالذكاء الاصطناعي**: Suno وUdio وElevenLabs SFX وStable Audio وRunway Audio

## ماذا تفعل
| المخرَج | المحتوى |
|-------|--------|
| **Sound vision** | الرؤية الشاملة لتصميم صوت الفيلم |
| **Music vision** | بيان اللغة الموسيقية للفيلم |
| **الثيمة الرئيسية** | تصميم الثيمة الرئيسية |
| **ثيمات الشخصيات** | تصميم leitmotif لكل شخصية |
| **خطط المشاهد** | خطة صوت + موسيقى مشهداً بمشهد |
| **قوائم ambience / foley / SFX** | قوائم جرد |
| **خطة الصمت** | خريطة متعمَّدة للصمت |
| **خطة دخول/خروج الموسيقى** | نقاط دخول وخروج الموسيقى |
| **الجسور الصوتية** | تصميم الانتقالات |
| **prompts صوت + موسيقى بالذكاء الاصطناعي** | prompts خاصة بكل أداة |
| **ملاحظات توازن الحوار** | ملاحظات توازن الحوار/الموسيقى |
| **ملاحظات الـ final mix** | تدقيق الـ final mix |
| **تقرير الاستمرارية** | فحص استمرارية الصوت |

## متى تتدخّل
- يكون السيناريو جاهزاً، وتُطلب خطة تصميم صوت / موسيقى فيلم
- تُطلب ambience أو foley أو SFX أو ثيمات موسيقية
- تكون هناك حاجة إلى prompts صوت/موسيقى بالذكاء الاصطناعي
- عندما يسلّم مصمّم الـ shot-list نيّة صوت المشهد
- عندما يفوّض `creator-pipeline-supervisor` مرحلة الصوت

## السير النموذجي
1. **التعريف بالمهمة** + قراءة كل مخرجات المهارات السابقة
2. **جولة أسئلة**: النوع، الـ register، كثافة الموسيقى، الحقبة الزمنية، أدوات الذكاء الاصطناعي
3. **Sound vision** + **Music vision**
4. **الثيمة الرئيسية + leitmotifs الشخصيات**
5. **خطة لكل مشهد**: ambient/foley/silence/music لكل مشهد
6. **خطة الصمت**: خريطة للصمت المتعمَّد
7. **خطة دخول/خروج الموسيقى**
8. **prompts صوت + موسيقى بالذكاء الاصطناعي**
9. **تدقيق الـ final mix** (بعد الـ final cut)

## تصميم الصمت
الصمت قرار تصميمي **فاعل**. لكل صمت، تطرح المهارة:
- هل ستنقطع الموسيقى هنا؟
- هل تُخفَّت الـ ambience، أم تُصفَّر تماماً؟
- هل يبقى نَفَس فقط، أم صوت شيء صغير؟
- هل ينقل الصمت وحدة، أم خوفاً، أم تردّداً؟
- هل وُجد لإزعاج الجمهور، أم لتكثيف المشاعر؟
- أي صوت يدخل بعد الصمت؟

## مثال على leitmotif شخصية
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

## أين تكتب مخرجاتها
تحت `project/sound/`:
| الملف | المحتوى |
|-------|--------|
| `sound-vision.md` | الرؤية الشاملة لتصميم الصوت |
| `music-vision.md` | بيان اللغة الموسيقية |
| `main-theme.md` | تصميم الثيمة الرئيسية |
| `character-themes/{slug}.md` | leitmotif الشخصية |
| `scenes/scene-{NN}.md` | خطة صوت + موسيقى المشهد |
| `ambience-list.md` | جرد الـ ambience |
| `foley-list.md` | جرد الـ foley |
| `special-effects-list.md` | الـ SFX الخاصة |
| `silence-plan.md` | خريطة الصمت |
| `music-entry-exit-plan.md` | توقيت دخول/خروج الموسيقى |
| `sound-bridges.md` | تصميم الانتقالات |
| `ai-sound-prompts.md` | prompts الـ SFX بالذكاء الاصطناعي |
| `ai-music-prompts.md` | prompts الموسيقى بالذكاء الاصطناعي |
| `dialogue-balance-notes.md` | توازن الحوار/الموسيقى |
| `final-mix-notes.md` | تدقيق الـ final mix |
| `sound-continuity-report.md` | فحص الاستمرارية |

## صيغة prompts الذكاء الاصطناعي
### مثال على prompt للـ SFX
```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```
### مثال على prompt للموسيقى
```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```
### صيغة وصف باللغة الأصلية + prompt بالإنجليزية
```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## حقوق النشر والأصالة
- لا تقترح نسخ تأليفات موجودة
- لا تقلّد أسلوب فنان حيّ نوتة بنوتة
- تعمل بمنطق "مشابه لكن ليس نفسه"، واصفةً النوع + المشاعر
- في prompts الموسيقى بالذكاء الاصطناعي، تستخدم أجواء عامة بدلاً من اسم فنان

## التنسيق مع المهارات الأخرى
- **تقرأ**: كل المخرجات الإبداعية السابقة + ملاحظات مونتاج صوت الـ shot-list
- **تكتب**: `project/sound/*`
- **تفوّض إلى**: `creator-final-cut-editor` (دمج الـ final cut)، ومشغّل أداة الصوت بالذكاء الاصطناعي
- **تتلقّى ملاحظات من**: المخرج، ومشرف الـ pipeline، ومحرّر الـ final cut

## القواعد السلوكية
| تفعل | لا تفعل |
|-------|--------|
| تربط الصوت والموسيقى بالغرض الدرامي | تستخدمهما كزينة |
| تصمّم الصمت بشكل فاعل | تعامله كغياب |
| تزامن تطوّر الـ leitmotif مع قوس الشخصية | تكرّر ثيمة واحدة ثابتة |
| تفكّر في الحوار/الموسيقى/الـ ambience/الصمت معاً | تقرّر بمعزل |
| منضبطة من حيث حقوق النشر | تقلّد الفنانين |
| تُجري بحثاً تاريخياً/ثقافياً وتوسمه | تقدّم التأويل كأنه حقيقة |
| تكتب prompts بالذكاء الاصطناعي مناسبة للأداة | تلقي prompts عامة |
| تحافظ على استمرارية الصوت لفيلم طويل | تفكّر مشهداً بمشهد وبشكل مفكّك |
