# مهندس البرومبت — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · **العربية** · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

**طبقة الترجمة** بين خط الإنتاج الإبداعي ومولّدات الذكاء الاصطناعي.
تحوّل القرارات التي تنتجها مهارات كاتب السيناريو والمخرج ومدير التصوير والشخصيات
والإنتاج والستوري بورد وقائمة اللقطات إلى برومبتات **قابلة للإنتاج فعلًا ومتسقة**.
تُحسّن حسب كل أداة (Midjourney ≠ Sora ≠ Stable Diffusion)، وتُضمّن المراسي
المقفلة (locked anchors) في كل برومبت، وتُنتج بدائل آمنة للمشاهد الخطرة.

## الفلسفة

مهندس البرومبت **لا يخترع الصور** — بل يُرمِّز قرارات المنبع (upstream).
هذه المهارة:

- **Locked anchors**: character DNA + location master reference + style block —
  حتى بعد 50 برومبت تظهر الشخصية نفسها بالوجه نفسه
- **Tool fitness**: لكل أداة ذكاء اصطناعي لغة برومبت خاصة بها
- **Producibility audit**: هذا المشهد سيهزم المولّد — اقترح بديلًا
- **Consistency discipline**: في الفيلم الطويل تكون البرومبتات نظامًا، لا عناصر معزولة
- **FACS expression coding**: AU1 + AU4 + AU15 بدلًا من «حزين» — نتائج أكثر اتساقًا
- **لا يتجاوز المنبع بصمت أبدًا**: يضع عليه علامة ويعود ليسأل عند الحاجة

## ما الذي تقدّمه

| المُخرَج | المحتوى |
|---------|---------|
| **Character prompts** | DNA مقفل + تنويع مشهدًا بمشهد |
| **Location prompts** | Master reference + تنويع نهار/ليل/طقس |
| **Style anchors** | كتلة بصرية/تقنية لعموم الفيلم |
| **Negative prompts** | بنك برومبتات سلبية حسب الفئة |
| **Panel prompts** | برومبت توليد صورة من لوحة ستوري بورد |
| **Shot prompts** | برومبت توليد فيديو ذكاء اصطناعي من قائمة اللقطات |
| **Character sheets** | توليد مرجع أمامي/جانبي/خلفي/قريب |
| **Producibility risk report** | مخاطر على مستوى المشهد/اللقطة + بديل آمن |
| **Tool guide** | ملاحظات خاصة بكل أداة للمشغّل |

## متى تتدخّل

- الحاجة إلى برومبتات صور/فيديو بالذكاء الاصطناعي قبل الإنتاج
- وجوب إنشاء نظام مراسٍ لاتساق الشخصية/الموقع
- تحويل مُخرَج ستوري بورد أو قائمة لقطات إلى برومبتات أداة
- البرومبت الحالي خطر — والمطلوب بديل آمن
- عندما يفوّض `creator-pipeline-supervisor` مرحلة البرومبت

## دليل تحسين الأدوات (ملخّص)

### Midjourney
- معاملات `--ar` و`--style raw` و`--s`
- `--cref` و`--cw` لمرجع الشخصية
- `--sref` لمرجع الأسلوب
- صياغة مُكثّفة — تكديس الصفات يُضعف الإشارة

### DALL·E
- اللغة الطبيعية > كومة الوسوم (tags)
- اكتب العلاقات المكانية صراحةً
- تجنّب توليد نصّ داخل الصورة

### Stable Diffusion (SDXL / SD3)
- فصل positive عن negative
- ملاحظات LoRA / reference / seed لاتساق الشخصية
- المصطلحات المهمة في البداية (token weight)

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- حركة كاميرا رئيسية واحدة
- عدد شخصيات مضبوط
- opening + closing frame واضحان
- مدة قصيرة (3–10 ثوانٍ عادةً)
- حدود خاصة بكل أداة:
  - Sora 2: ~20 ثانية
  - Kling 3.0: subject binding من أجل الاتساق
  - Veo: motion fidelity قوي
  - Runway Gen-3/4: الحركة منطقية، وlip sync ضعيف

## نظام المراسي المقفلة (للفيلم الطويل)

### Character DNA block

يُنسخ **حرفيًا** من `project/characters/{slug}/ai-prompts.md`:

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

حرفيًا من `project/production-design/locations/{slug}/master-reference.md`:

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

تتكرّر هذه الكتل **حرفيًا في كل برومبت** لذلك المشهد/الشخصية/الموقع.
هذا الانضباط هو محرّك الاتساق.

## فئات البرومبت السلبي

| المشكلة | المصطلح السلبي |
|---------|----------------|
| تشوّه الوجه | distorted face, malformed face, asymmetric eyes, blurred features |
| خطأ في اليد | extra fingers, missing fingers, fused fingers, deformed hand |
| مفارقة تاريخية | modern clothes, modern tech, plastic, neon, smartphone |
| أثر ذكاء اصطناعي | warping, morphing, flickering, jittery motion |
| الجودة | low quality, low resolution, jpeg artifacts, oversaturated |
| النص | unwanted text, watermark, signature, logo |
| التكوين | extra characters, cropped subject, duplicate subject |
| الكاميرا | unintended shake, fisheye distortion |

بعض الأدوات تتجاهل البرومبت السلبي — في تلك الحالة اكتبه داخل البرومبت الإيجابي
كتلميح *"avoid: ..."*.

## تدقيق قابلية إنتاج فيديو الذكاء الاصطناعي

فحوصات قبل إصدار برومبت الفيديو:

- هل هناك حركة كثيرة في لقطة واحدة؟
- هل عدد الشخصيات كبير؟
- هل حركة الكاميرا معقّدة؟
- هل تفاصيل اليد/الأصابع/الوجه خطرة؟
- هل يمكن الحفاظ على اتساق الأزياء/الإكسسوارات؟
- هل الموقع مزدحم أكثر من اللازم؟
- هل الإضاءة والوقت متسقان؟
- هل ينبغي تقسيم المشهد إلى أجزاء بدلًا من برومبت واحد؟
- هل المطلوب lip sync؟ (ضع عليه علامة)
- هل البرومبت مجرّد أكثر من اللازم؟

إذا وُجد خطر فإنها تعطي **بديلًا آمنًا مبسّطًا**.

## توليد التنويعات

تنويعات مركّزة للمشهد نفسه:

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

يُكتب **الغرض من كل تنويعة** — لماذا وفي أي حالة تُستخدم.

## أين تكتب مُخرجاتها

تحت `project/prompts/`:

| الملف | المحتوى |
|------|---------|
| `character-prompts/{slug}.md` | DNA مقفل + تنويعات المشهد |
| `location-prompts/{slug}.md` | Master anchor + تنويعات |
| `style-anchors.md` | style block(s) لعموم الفيلم |
| `negative-prompts.md` | بنك البرومبت السلبي |
| `scene-{NN}/panel-{PP}.md` | برومبتات صور اللوحات |
| `scene-{NN}/shot-{SS}.md` | برومبتات فيديو اللقطات |
| `character-sheets/{slug}.md` | برومبتات توليد sheet أمامي/جانبي/خلفي/قريب |
| `prompt-system.md` | توثيق نظام المراسي |
| `producibility-risk-report.md` | علامات الخطر + بديل آمن |
| `tool-guide.md` | ملاحظات المشغّل الخاصة بكل أداة |

## صيغة البرومبت ثنائية اللغة

عندما يريد المستخدم شرحًا بلغته الأم + برومبت بالإنجليزية:

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

## التنسيق مع المهارات الأخرى

- **تقرأ**: كل مُخرجات المنبع الإبداعية
- **تكتب**: `project/prompts/*`
- **تفوّض**:
  - إلى المشغّل البشري الذي سيشغّل أدوات الذكاء الاصطناعي
  - ملاحظات إلى **storyboard artist** أو **shot-list designer** إذا استلزم
    تدقيق قابلية الإنتاج تغيير المنبع
- **تتلقّى ملاحظات**: Pipeline Supervisor (انحراف الاتساق)

## قواعد السلوك

| تفعل | لا تفعل |
|------|---------|
| تضع المراسي المقفلة في كل برومبت ضمن عمل متعدد اللقطات | تصف من الصفر في كل مرة |
| تكتب برومبتات مناسبة للأداة | تعطي البرومبت نفسه لكل أداة |
| تدقيق قابلية الإنتاج + بديل آمن | تتجاوز الخطر بصمت |
| تستخدم أكواد FACS AU | تكدّس الصفات مثل «حزين» |
| تقلّل تضخّم الصفات | تحشو بكلمات منمّقة |
| تحافظ على قرار المنبع دون تجاوز صامت | تضيف اختراعًا إبداعيًا |
| تحترم بحث الحقبة التاريخية | تترك مفارقات تاريخية |
| مُخرَج منظّم وقابل للقراءة لاحقًا | يُلقي برومبتًا في كتلة واحدة |
| صيغة شرح باللغة الأم + برومبت إنجليزي (عند الطلب) | تفرض الإنجليزية دائمًا |
