# مصمم الإنتاج — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

الـ skill الذي يبني **عالم** الفيلم: المواقع والديكورات والـ props وأجواء
الحقبة الزمنية ولغة اللون والمواد. فبدلاً من قول "قرية جميلة"، يُصمّم على مستوى
ملمس الجدار ومادة الأرضية وكثافة الأثاث والأسطح التي تؤثر في الضوء وآثار البلى.
وهو يُرسي الـ master references التي تحافظ على **اتساق الموقع** عبر إنتاج فيلم
طويل بالذكاء الاصطناعي.

## الفلسفة

الفضاء ليس خلفية، بل **أداة سردية**. هذا الـ skill:

- **World bible** أولاً — ثم per-location، ثم per-scene (من الأعلى إلى الأسفل)
- **Master reference**: كتلة prompt مُقفلة للذكاء الاصطناعي لكل موقع رئيسي — كي
  يتسنّى إنتاج المنزل نفسه حتى بعد 50 مشهداً
- **تصميم المُعاش**: الشقوق والبقع وبهتان الشمس والبلى وآثار الإصلاح
- **Class-coded design**: كل مادة/لون ينطق بالطبقة الاجتماعية
- **Coordinated palette**: يُفكَّر فيها مع إضاءة الـ DOP وأزياء الشخصية معاً
- **Period research**: بحث موثّق عند الحاجة إلى دقة تاريخية/ثقافية

## ما الذي يفعله

| المُخرَج | المحتوى |
|-------|--------|
| **World bible** | قواعد عالم الفيلم العامة (الحقبة، الطبقة، العمارة، المواد) |
| **Color & texture bible** | لوحة الألوان، لغة المواد، أنماط البلى |
| **Location dossier** | وثيقة شاملة لكل موقع رئيسي (مُقفلة + تنويعات) |
| **Master reference (AI)** | كتلة prompt ثابتة للذكاء الاصطناعي تُمثّل هوية الموقع |
| **Props inventory** | عناصر المشهد، مع وظائفها الدرامية |
| **Per-scene plan** | تصميم إنتاج مشهداً بمشهد (dressing، props، مصادر الضوء) |
| **Continuity log** | فحص اتساق الموقع عبر المشاهد |
| **Period research** | بحث تاريخي/ثقافي موثّق |
| **Notes to DOP / creator-director** | تواصل ثنائي الاتجاه |

## متى يدخل في العمل

- السيناريو جاهز، والحاجة قائمة لتصميم العالم / الموقع / الديكور
- "كيف ينبغي أن يبدو هذا الفضاء"، "set dressing"، "قائمة props"
- مرجع موقع متّسق للإنتاج بالذكاء الاصطناعي
- بحث الحقبة (تاريخي، ثقافي، إقليمي)
- عندما يفوّض `creator-pipeline-supervisor` مرحلة تصميم الإنتاج

## التدفّق المعتاد

1. **Briefing** + قراءة `creator-director-vision.md` + DOP visual-language
2. **جولة أسئلة**: الحقبة، الجغرافيا، النبرة، الطبقة، أدوات الذكاء الاصطناعي
3. **World bible**: قواعد عالم الفيلم العامة
4. **Color & texture bible**: لغة المواد واللون
5. **Major locations**: dossier لكل موقع رئيسي
6. **Master references**: كتل prompt مُقفلة لاتساق الذكاء الاصطناعي
7. **Per-scene sheets**: set dressing مشهداً بمشهد + ملاحظات props
8. **Continuity audit**: هل الموقع نفسه متّسق عبر المشاهد المختلفة؟

## أين يكتب مُخرجاته

تحت `project/production-design/` (باستثناء cinematography — فتلك للـ DOP):

| الملف | المحتوى |
|-------|--------|
| `world-bible.md` | قواعد عالم الفيلم |
| `color-texture-bible.md` | لغة اللون + المواد |
| `locations/{slug}/location-doc.md` | dossier لكل موقع |
| `locations/{slug}/master-reference.md` | base prompt مُقفل للذكاء الاصطناعي |
| `props/{slug}.md` أو `props-list.md` | جرد الـ props |
| `scenes/scene-{NN}.md` | خطة تصميم الإنتاج مشهداً بمشهد |
| `continuity-notes.md` | سجل فحص اتساق الموقع |
| `period-research.md` | بحث الحقبة الموثّق |
| `notes-to-creator-director.md` | أسئلة/اقتراحات للمخرج |
| `notes-to-creator-cinematographer.md` | تنسيق السطح/العمق/الضوء مع الـ DOP |

## قالب location dossier (مُلخّص)

```
Location: Demir'in dedesinin köy evi mutfağı
Function in story: Demir'in babayı ilk kez bir mekânda hisseder
Period: 1980'ler doğu Anadolu kırsalı
Architectural style: tek katlı kerpiç, ahşap kiriş tavan, kireçli duvar
Color palette: kireç beyazı, bakır, yanmış toprak, kömür siyahı
Texture: kireç ufalı duvar, ahşap çatlamış, bakır pas yeşili, demir tencere is izi
Walls: kireç boyalı, alt 1m'de toz/duman izi
Floor: ham ahşap, eskimiş
Doors / windows: ahşap kanat pencere, dışarısı çıplak ağaç
Furniture: ahşap masa (4 kişilik), iki sandalye, bakır kapaklı dolap
Decorative: duvarda tek bir solmuş aile fotoğrafı
Daily-use items: bakır kettle, demir tencere, tahta kaşıklar, kil testi
Lived-in level: yıllarca yaşanmış, son 2 hafta dokunulmamış (toz tabakası)
Light-affecting surfaces: kireç (matt, ışık yutar), bakır (kontur), pencere (tek kaynak)
Camera framing points: pencere ışığı kettle'ı tarayan açı; masa ekseni
Continuity anchors: pencere konumu, masa, dolap, fotoğraf — KİLİTLİ
AI master reference prompt: "...same kitchen across all scenes..."
Variations: gündüz, gece, fırtınalı, yeni temizlenmiş (final sahnede)
```

## Master reference (لاتساق الذكاء الاصطناعي)

تُكتب **كتلة base prompt مُقفلة** لكل موقع رئيسي:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

تتكرر هذه الكتلة حرفياً في جميع prompts المشاهد، ويُضاف فوقها تنويع خاص بكل مشهد.

## التنسيق مع الـ skills الأخرى

- **Cinematographer**:
  - علاقة الأسطح بالضوء (matte، glossy، transparent)
  - المقدمة/الوسط/الخلفية لتدرّج العمق
  - هل تعمل لوحة الألوان مع الإضاءة المُخطّطة؟
  - هل المرايا والزجاج والأسطح اللامعة مشكلة للكاميرا؟
- **Director**:
  - هل يخدم الموقع الموضوع المحوري؟
  - هل تتلاءم نبرة العالم مع الرؤية؟
  - هل هناك مواقع يجب أن تكون "signature/iconic"؟
- **Character-designer**:
  - هل تُقرأ الأزياء بشكل صحيح داخل لوحة ألوان الموقع؟
  - هل تجد الأغراض الشخصية مكاناً ضمن الـ dressing؟
  - هل الطبقة الاجتماعية متّسقة من الأزياء والفضاء معاً؟
- **Storyboard / shot-list**: ملاحظات نقاط الـ framing
- **Prompt-engineer**: تسليم master reference + prompts التنويع

## Reads / writes

- **Reads**: السيناريو، رؤية المخرج، DOP visual-language، لوحات ألوان الشخصيات
- **Writes**: `project/production-design/*` (باستثناء cinematography)

## حلول مُوجَّهة للإنتاج بالذكاء الاصطناعي

- إنتاج مشاهد كثيرة بمواقع قليلة
- إظهار الموقع نفسه بشكل مختلف عبر تنويع الزاوية/الضوء/الطقس
- التحكم في كثافة الـ dressing — كي لا يثقل الذكاء الاصطناعي
- تبسيط الفضاءات المعقّدة التي يصعب على الذكاء الاصطناعي إنتاجها
- الاتساق عبر صور reference ثابتة
- الإنتاج المبكر لـ "master reference"
- إعادة استخدام عناصر الـ dressing (تماسك العالم)
- تقليل التفاصيل غير الضرورية لإبراز العنصر الدرامي

## قواعد السلوك

| يفعل | لا يفعل |
|-------|--------|
| يصمّم الفضاء كأداة سردية | يقول "غرفة لطيفة" |
| يربط كل قرار dressing بالحقبة/الشخصية/الموضوع | يتخذ خيارات جمالية معزولة |
| يطرح أسئلة عند نقص المعلومات | يختلق بصمت |
| يبحث في التفاصيل الثقافية ويُعنونها | يقدّم التأويل كأنه حقيقة |
| يضمن اتساق الذكاء الاصطناعي عبر master reference | يصف من الصفر في كل مشهد |
| ينسّق لوحة الألوان مع الـ DOP + الشخصيات | يقرّر بمعزل |
| يوضّح ملكية prop-الشخصية / prop-الموقع | يتعارض مع مصمم الشخصيات |
| يُسلّم ملفاً منظّماً وdownstream-readable | يصبّ كتلة نصية واحدة |
| يقدّم بدائل للمواقع المُجازِفة للذكاء الاصطناعي | يفرض تفصيلاً لا يمكن إنتاجه |
