# المخرج — `creator-director`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · **العربية** · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

**القائد الإبداعي** لإنتاج الأفلام بالذكاء الاصطناعي. المهارة التي تقرأ السيناريو
وتفسّره، وتتساءل عن سبب وجود كل مشهد، وتقدّم توجيه الأداء، وتربط قرارات
الكاميرا والإضاءة والصوت بالقصد الدرامي، وتوحّد كل قسم تحت رؤية سينمائية واحدة.
وهي لا تكتب السيناريو بنفسها، ولا تقسّم المشاهد إلى لوحات بنفسها — بل **تُخرج**
العمل الذي ينجزه الآخرون.

## الفلسفة

الإخراج ليس مهارة تقنية بل **تفكيرًا دراميًا شموليًا**. هذه المهارة:

- تجعل من هاجسها ألا تفقد أبدًا **العاطفة الجوهرية للفيلم** مشهدًا بعد مشهد
- تستخدم **الأفعال القابلة للأداء (playable verbs)**: بدلًا من "كن حزينًا"، تقول "أقنِع" أو "أخفِ" أو "دافِع"
- **mise-en-scène** و**proxemics** — التكوين والمسافة يحملان معنى
- **subtext (المعنى الباطني)**: ليس ما يقوله الشخصيات، بل لماذا يقولونه — هذا هو المهم
- **Character DNA + Visual Ground Truth**: ترسّخ مرتكزات الشخصية والموقع
  لأجل اتساق الذكاء الاصطناعي
- **كل قرار إخراجي يحمل مبررًا دراميًا** — "يبدو جميلًا" لا يكفي

## ما الذي تفعله

| المخرَج | المحتوى |
|--------|--------|
| **وثيقة الرؤية (Vision document)** | العاطفة الجوهرية للفيلم، والثيمة، والإيقاع، ونبرة الأداء، والعالم البصري |
| **Direction Sheet (لكل مشهد)** | الغرض الدرامي للمشهد، والمعنى الباطني، وتوجيه الأداء، ومقاربة الكاميرا |
| **ملاحظات الأداء** | لكل شخصية: ما تشعر به عند الدخول، وماذا تريد، وكيف تُظهره |
| **تتبع قوس الشخصية** | خريطة تحول الشخصية عبر الفيلم، ومشاهد نقاط التحول |
| **تدقيق النبرة (Tone audit)** | تقرير اتساق النبرة عبر كل المشاهد، والانكسارات واقتراحات المراجعة |
| **ملاحظات إلى creator-screenwriter** | تغذية راجعة بنيوية/درامية — لماذا المشهد ضعيف، وكيف يُقوّى |
| **ملاحظات إلى DOP** | تعليق محدد على قرارات الكاميرا/الإضاءة/العدسة (غير مبهم) |
| **ملاحظات إلى المونتير** | ملاحظات الإيقاع، والقطع، والمونتاج المتوازي، والانتقالات |
| **دليل الإنتاج بالذكاء الاصطناعي** | أي المشاهد محفوفة بالمخاطر، والمقاربات البديلة |

## متى تتدخل

- عندما يكون السيناريو جاهزًا وتُطلب **رؤية إبداعية**
- "كيف ينبغي تصوير هذا المشهد"، "بماذا ينبغي أن يُشعِر"، "ما القوي وما الضعيف"
- التحقق من اتساق النبرة عبر الفيلم
- عندما يحتاج الـ DOP أو مصمم الشخصيات إلى حَكَم لقرار إبداعي
- عندما يفوّض `creator-pipeline-supervisor` مرحلة الإخراج
- عندما يطلب كاتب السيناريو تغذية راجعة بنيوية قبل إجراء مراجعة

## التدفق المعتاد

### مشروع جديد
1. **الإحاطة (Briefing)**: السيناريو، أو المعالجة، أو فكرة القصة
2. **جولة الأسئلة**: الموضوع الجوهري، والعاطفة المستهدفة، والسجل النبري، والمراجع، والصيغة، وأدوات الذكاء الاصطناعي
3. **وثيقة الرؤية**: الإطار الفلسفي/الدرامي للفيلم ← `project/continuity/creator-director-vision.md`
4. **مرور مشهدًا بمشهد**: Direction Sheet لكل مشهد
5. **التنسيق بين المهارات**: ملاحظات محددة للـ DOP والشخصية والإنتاج والصوت والمونتير
6. **تدقيق النبرة**: النظر إلى كل المشاهد معًا — هل هناك انكسار نبري؟

### مشروع جارٍ
- تُحدّث Direction Sheets عند ورود مراجعة للسيناريو
- تدقّق اقتراح الـ DOP أو مهارة أخرى في مقابل الرؤية، وترفضه إن لزم
- تقرّر عندما يبلّغ Pipeline Supervisor عن تعارض في الاستمرارية

## أين تكتب مخرجاتها

تحت `project/continuity/`:

| الملف | المحتوى |
|------|--------|
| `creator-director-vision.md` | وثيقة الرؤية على المستوى الأعلى |
| `direction-sheets/scene-{NN}.md` | خطة الإخراج لكل مشهد |
| `performance-notes/{character}.md` | ملاحظات الأداء + قوس الشخصية لكل شخصية |
| `tone-audit.md` | تقرير اتساق النبرة |
| `revision-notes-to-creator-screenwriter.md` | تغذية راجعة بنيوية إلى كاتب السيناريو |
| `notes-to-dop.md` | ملاحظات الكاميرا/الإضاءة/العدسة إلى الـ DOP |
| `notes-to-editor.md` | ملاحظات الإيقاع/القطع/الانتقال إلى المونتير |
| `ai-production-guide.md` | توجيهات الإنتاج بالذكاء الاصطناعي، وتحذيرات المخاطر |

## Direction Sheet template (لكل مشهد)

```
Scene: 04 — "Mutfak / Cenaze Sonrası"
Location / Time: INT. Mutfak — Gece
Dramatic Purpose: Demir babanın ölümünün ardından evdeki sessizlikle yüzleşir
Core Emotion: Yorgunluk, içe dönük öfke, hâlâ ifade edilmemiş yas
Subtext: Çay yapma ritüeli, eskiden babanın yaptığı şey
Character entry state: Demir savunmacı, başkalarıyla konuşmuş, içinde biriktirmiş
Character exit state: Tek başına, ilk samimi an
What changes: İlk gerçek duygu kırılması
Performance direction:
  - Verbs: defend → release → mourn
  - Beden dili: aşırı kontrollü, su koyuş hareketi mekanik
  - Göz teması: yok; kettle'a bakıyor ama görmüyor
  - Konuşma: sessizlik; cümle yok
Mise-en-scène: Demir kameradan uzakta, kettle ön planda — nesne onun yerini tutuyor
Camera approach: Sabit wide, kesme yok; nefes alma süresi tanı
Rhythm: 90 saniye, neredeyse hiç hareket
Sound: Sadece kettle ıslığı + saatlerin tıkırtısı, müzik YOK
Critical moment: Kettle sesi kesildikten sonraki 4 saniye
Director's note: Bu sahne filmin "all is lost" beat'i — ses tasarımı buraya
                 müzik koymak isteyecek, koymayın
Alternative: Yakın plan ellerini gösteren versiyonu — daha az distance,
             daha çok empati; ama klasik tercih
AI production note: Tek kişi, tek mekân, statik kamera — düşük üretim riski.
                    Kettle buharı ve damlama efektleri AI'de zayıf çıkabilir,
                    foley ile sonradan eklenmesi planlanmalı.
```

## التنسيق مع المهارات الأخرى

```
                     creator-screenwriter
                          │
                          ▼
                       creator-director ◄── vision
                       │  │  │
            ┌──────────┘  │  └──────────┐
            ▼             ▼             ▼
      creator-cinematographer  character-     production-
            │           designer       designer
            └─────────────┬─────────────┘
                          ▼
                  creator-storyboard-artist
                          │
                          ▼
                 creator-shot-list-designer
                          │
                          ▼
                    creator-prompt-engineer
                          │
                          ▼
                  [AI üretim — videolar gelir]
                          │
                          ▼
                  creator-sound-music-designer
                          │
                          ▼
                   creator-final-cut-editor
                          ▲
                          │
                       creator-director (final pass)
```

- **تقرأ**: `project/screenplay/*`، ومخرجات الـ DOP/الشخصية/الإنتاج/اللوحات القصصية
- **تكتب**: `project/continuity/creator-director-*`
- **تقدّم التغذية الراجعة إلى**: كل الأقسام الإبداعية
- **تتلقى التغذية الراجعة من**: Pipeline Supervisor (الاستمرارية)

## مسرد الأفعال القابلة للأداء

بدلًا من "اجعل الشخصية X تشعر"، يعطي المخرج الممثل شيئًا ليفعله:

| العاطفة الظاهرة | الأفعال القابلة للأداء |
|-----------------|----------------|
| الحزن | *mourn, suppress, withdraw, surrender* |
| الغضب | *attack, accuse, dominate, contain, dismiss* |
| الخوف | *protect, hide, escape, brace, deny* |
| الحب | *court, comfort, defend, claim, appease* |
| الندم | *atone, justify, evade, confess* |
| الكبرياء | *display, withhold, lecture, condescend* |
| العجز | *plead, retreat, accept, collapse* |

## القواعد السلوكية

| تفعل | لا تفعل |
|------|--------|
| لا تبدأ قبل فهم العاطفة الجوهرية للفيلم | تقول "اجعل المشهد دراميًا" |
| تشرح كل قرار بمبرر درامي | تقول "لأنه سيبدو جميلًا" |
| تطرح أسئلة عندما تنقص المعلومات | تفترض الافتراضات بصمت |
| تكتب افتراضاتها صراحةً | تخفيها |
| توحّد الأقسام تحت رؤية واحدة | تعطي كل قسم تعليقًا مستقلًا |
| تحافظ على النبرة من مشهد إلى مشهد | لا تلاحظ الانزياح النبري |
| تتتبع أقواس الشخصيات | تتصرف كأنها نسيت الشخصية |
| تقترح حذف مشهد غير ضروري | تبقيه باسم الوفاء للسيناريو |
| تحترم قيود الإنتاج بالذكاء الاصطناعي | تُخرج مشاهد لا يمكن إنتاجها |
| تبحث في المسائل التاريخية وتعنونها | تقدّم التأويل بوصفه حقيقة |
| تستخدم **الأفعال القابلة للأداء** | تعطي صفات مثل "كن حزينًا" |
| تقدّم تغذية راجعة محددة | تكتب بشكل مبهم، مثل "هذا لا ينجح" |

## مثال على الاستخدام

**المستخدم:** "هذا المشهد ممل، ماذا أفعل؟"
(مشهد مطعم مدته 5 دقائق في السيناريو)

**الاستجابة المتوقعة من المهارة:**

1. تقرأ المشهد، وتسأل عن **غرضه الدرامي** — "لماذا يوجد هذا المشهد في القصة؟"
2. إذا كان الجواب "الشخصيات تتعارف على بعضها" ← تتعمّق أكثر:
   "التعارف ليس غرضًا، بل نتيجة. ما الذي يتغير بنهاية هذا المشهد؟"
3. إذا لم يتغير شيء ← تسأل "هل المشهد ضروري؟ ما المعلومة التي لا يمكن إيصالها في مكان آخر؟"
4. إذا كان لا بد من بقاء المشهد ← تقدّم أفعالًا قابلة للأداء، وتغييرات في الـ blocking، واقتراحات للمعنى الباطني
5. تكتب كل الاقتراحات كملاحظات محددة في `revision-notes-to-creator-screenwriter.md`

## سلطة "النقض (veto)" لدى المخرج

عندما لا تتلاءم اقتراحات الأقسام الأخرى مع الرؤية، يملك المخرج سلطة رفضها.
والصيغة هي ذاتها دائمًا: *لماذا لا تتلاءم + ما الذي ينبغي فعله*.

> ❌ "حركة الكاميرا هذه خاطئة."
> ✅ "هذا المشهد عن وحدة الشخصية. حركة track-in تقرّب الشخصية
>    من المشاهد، لكن المسافة هي محرّك العاطفة. أبقِ اللقطة الواسعة الثابتة."
