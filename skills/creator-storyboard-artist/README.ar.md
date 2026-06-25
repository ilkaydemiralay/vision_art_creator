# فنان الـ Storyboard — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

مهارة تحوّل السيناريو المكتوب إلى **سرد بصري قابل للقراءة**. من خلال تقليل عدد
اللوحات إلى أدنى حد، تضمن أن كل لوحة موجودة لسبب درامي. تلتقط اللحظات الحاسمة في
المشهد، وتحافظ على screen direction، وتتابع eyeline continuity، وتسلّم بوضوح إلى
prompts الصور/الفيديو الخاصة بالذكاء الاصطناعي.

## الفلسفة

الـ storyboard ليس "رسم المشهد" — بل هو **نظام سرد بصري**. هذه المهارة:

- **Panel economy**: لوحات قليلة + اختيارات حادة — لا لوحات كثيرة + قرارات ضعيفة
- **Screen direction (180°)** و**eyeline continuity**: اتساق مكاني عبر القطعات
- **Graphic dynamics**: أين تقع العين؟ ما هو محور التركيز؟
- **Continuity awareness**: الأزياء، الموقع، اتجاه الضوء، اتجاه الشاشة، الحركة
- **Locked anchors**: character DNA + location master reference في كل لوحة
- **Producibility**: تعرف قيود الإنتاج بالذكاء الاصطناعي وتُعلّم المشاهد المحفوفة بالمخاطر

## ما الذي تقوم به

| المُخرَج | المحتوى |
|---------|---------|
| **Per-scene storyboard** | قائمة لوحات مشهداً بمشهد (كل بيانات اللوحة) |
| **Per-panel sheets** | ملف لوحة مفردة مفصّل للمشاهد المعقدة |
| **AI image prompts** | prompt جاهز للإنتاج لكل لوحة |
| **AI video prompts** | prompt فيديو للوحات المتحركة |
| **Continuity log** | إشارات لمخاطر الأزياء/الموقع/الاتجاه |
| **Animatic plan** | يخطط لترتيب الـ animatic لجميع المشاهد |
| **Director / DOP notes** | ملاحظات بصرية/تقنية موجزة للمخرج والـ DOP |
| **Handoff to shot-list** | بيانات اللوحة بصيغة creator-shot-list-designer |

## متى تتدخّل

- عند توفر سيناريو والرغبة في تقسيم بصري
- عندما يريد المخرج تصوّر المشهد بصرياً مسبقاً
- عند الحاجة إلى مفهوم بصري قبل قرارات العدسة/الإضاءة للـ DOP
- عند الرغبة في منطق الـ storyboard قبل توليد prompt للذكاء الاصطناعي
- عندما يفوّض `creator-pipeline-supervisor` مرحلة الـ storyboard

## Panel content (الحقول المعيارية)

تسجّل كل لوحة هذه الحقول:

```
Scene 04 — Panel 04.03
Shot type: medium close
Camera angle: eye level
Frame: Demir merkez-sağ; kettle ön plan-sol; arka plan
       dolap soft-focus; sağ kenar negatif alan açık
Lens feeling: 50mm (eye-equivalent, samimi)
Character position: Demir sandalyede, omuzlar düşmüş, eller masada
Character movement: yok — duraksama
Camera movement: static
Setting / dressing: kireçli mutfak — pencere doğu, kettle ateşte
Light / atmosphere: pencereden yumuşak gri sabah, mum yok
Emotional emphasis: bastırılmış yas; ilk gerçek duygu kırılması
Dialogue / action note: sessizlik; kettle ıslığı
Dramatic justification: Demir'in iç çatışmasını yüzeye getiren ilk an
Transition to next panel: J-cut — kettle sesi devam ederken Panel 4.04 başlar
AI image prompt: [tam prompt]
AI video prompt: [tam prompt, 6s]
Continuity note: palto sahne başında; ceket askıda; kettle aktif
```

## أين تكتب مخرجاتها

تحت `project/storyboards/`:

| الملف | المحتوى |
|-------|---------|
| `scene-{NN}/storyboard.md` | قائمة لوحات قائمة على المشهد (معيارية) |
| `scene-{NN}/panel-{PP}.md` | لوحة مفردة مفصّلة (في المشاهد المعقدة) |
| `scene-{NN}/prompts.md` | prompts الذكاء الاصطناعي لكل لوحة (image + video) |
| `scene-{NN}/continuity.md` | إشارات الـ continuity |
| `animatic-plan.md` | ملاحظات ترتيب الـ animatic للفيلم بأكمله |
| `notes-to-creator-director.md` | أسئلة/تنبيهات للمخرج |
| `handoff-to-shot-list.md` | بيانات لوحة منسّقة للـ shot-list designer |

## معجم shot type (مع المقابل الدرامي)

| النوع | الاستخدام الدرامي |
|-------|-------------------|
| Establishing | يضع المشاهد داخل الفضاء |
| Master | هندسة المشهد، fallback |
| Wide/Full | علاقة الشخصية بالبيئة |
| Medium | حوار محايد |
| Close | صراع داخلي، عاطفة حميمة |
| Extreme close | كثافة ذاتية |
| Insert | تأكيد على غرض |
| Cutaway | معلومات موازية/خارجية |
| Reaction | رد الفعل أكثر من الفعل |
| OTS | منظور الحوار |
| POV | ذاتية الشخصية |
| 2-shot / group | هندسة العلاقة |
| Silhouette | الغفلية، الغموض |
| Negative-space frame | العزلة، الصِّغَر |
| Symmetrical | القوة، الرسمية، السكون المقلق |
| Tracking | متابعة مستمرة |
| Static | المراقبة، معنى الصمت |

"استخدم close-up" لا يكفي — السؤال هو **لماذا** يلزم الـ close-up.

## Continuity audit

المتابعة من لوحة إلى لوحة، ومن مشهد إلى مشهد:

- الأزياء
- الشعر/المكياج/الإكسسوارات
- هوية الموقع (مع locked anchor)
- اتجاه الضوء
- نهار/ليل
- Screen direction (قاعدة الـ 180°)
- المنطق المكاني للشخصيات
- تدفّق الحركة
- موضع الـ prop

عند اكتشاف خطر، يُكتب بوضوح في حقل `continuity note` الخاص باللوحة.

## التنسيق مع المهارات الأخرى

- **تقرأ**: السيناريو، رؤية المخرج + direction sheets، خطة الـ DOP per-scene،
  character DNA + FACS، anchors الموقع
- **تكتب**: `project/storyboards/*`
- **تفوّض**:
  - `creator-shot-list-designer` (panel → shot list)
  - `creator-prompt-engineer` (panel prompt → تحسين خاص بالأداة)
- **تتلقى ملاحظات من**: المخرج، Pipeline Supervisor

## حلول مركّزة على الإنتاج بالذكاء الاصطناعي

- تقسّم المشاهد المعقدة إلى لوحات بسيطة
- توضّح محور التركيز البصري في المشاهد متعددة الشخصيات
- تبسّط الحركات التي سيصعب على الذكاء الاصطناعي تنفيذها
- تستخدم anchor ثابتاً لنفس الموقع/الشخصية
- تقدّم بديلاً آمناً بلقطة ثابتة بدلاً من حركة الكاميرا
- تقترح تأطيراً انتقائياً في المشاهد المزدحمة
- تقترح قطعات إيقاعية بدلاً من الحركة السريعة

## قواعد السلوك

| تفعل | لا تفعل |
|------|---------|
| تكتب تبريراً درامياً لكل لوحة | تملأ بـ "لوحة أخرى" لمجرد الملء |
| لوحات قليلة + اختيارات حادة | لوحات كثيرة + قرارات ضعيفة |
| توحّد كاتب السيناريو + المخرج + DOP + الشخصية + الإنتاج | تتجاوز الـ upstream بصمت |
| تحافظ على screen direction والـ eyeline | تخلط الاتجاه عند القطع |
| تضع locked anchors في كل prompt | تعيد الوصف من الصفر في كل لوحة |
| تقسّم المشهد المعقد إلى لوحات | تحمّله على frame واحد مثقل |
| flag لمخاطر الذكاء الاصطناعي + بديل آمن | تقترح حركة غير قابلة للإنتاج |
| مخرَج منظّم وقابل للقراءة في المراحل اللاحقة | تسكب كتلة نصية واحدة |
