# vision_art_creator

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · **العربية** · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

> حزمة مهارات لإنتاج الأفلام بالذكاء الاصطناعي مخصصة لـ [Claude Code](https://claude.com/claude-code).

تجمع `vision_art_creator` بين **11 مهارة `creator-*`** تغطي كل قسم من
أقسام إنتاج الفيلم — من السيناريو وصولًا إلى المونتاج النهائي — في
مستودع واحد. ثبّتها على أي جهاز عبر `git clone` و`./install.sh`.

> صُمّمت المهارات لتُحيل بعضها إلى بعض
> (تتولى `creator-pipeline-supervisor` تنسيق البقية). يُنصح بتثبيتها
> جميعًا معًا.

---

## التثبيت

```bash
git clone https://github.com/ilkaydemiralay/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

ينشئ `install.sh` **رابطًا رمزيًا (symlink)** لكل مهارة ضمن
`~/.claude/skills/<skill-name>` يشير إلى داخل هذا المستودع. والميزة من
ذلك: للتحديث، يكفي `git pull` بسيط — دون الحاجة إلى إعادة التثبيت.

### الخيارات

```bash
./install.sh --target /path/to/skills   # التثبيت في مجلد مهارات مختلف
./install.sh --force                    # الكتابة فوق الأسماء الموجودة
./uninstall.sh                          # إزالة الروابط الرمزية
```

يزيل `uninstall.sh` فقط الروابط الرمزية التي تشير إلى هذا المستودع — أما
الروابط الغريبة والمجلدات الفعلية فيتركها دون مساس (ما لم تستخدم
`--force`).

### التحقق

بعد التثبيت، أعد تشغيل Claude Code واكتب:

```
/creator-pipeline-supervisor
```

تحقق من ظهور المهارات الإحدى عشرة `creator-*` جميعها في قائمة المهارات.

---

## محتوى الحزمة

| المهارة | الوصف |
|---|---|
| `creator-pipeline-supervisor` | تنسّق الإنتاج بأكمله، وترتّب تسلسل الأقسام، وتفرض الاستمرارية، وتُجري مراقبة الجودة، وتنتج تقرير الجاهزية للتسليم. |
| `creator-director` | تترجم السيناريو إلى رؤية إخراجية موحّدة: توجيه المشاهد، والأداء، والـ blocking، والتحكم في النبرة. |
| `creator-screenwriter` | كتابة ومراجعة السيناريوهات والمعالجات والـ loglines ومخططات المشاهد والحوار. |
| `creator-character-designer` | تصمم الشخصية ككلٍّ متكامل: علم النفس، والسيرة، والهوية البصرية، والأزياء، والإكسسوارات، وتعبيرات الوجه المرمّزة بنظام FACS. |
| `creator-production-designer` | تبني عالم الفيلم: المواقع، والديكورات، والإكسسوارات، وأجواء الحقبة الزمنية، ولغة الألوان والمواد، ومراسي الاستمرارية. |
| `creator-cinematographer` | تصمم اللغة البصرية: الإضاءة، والكاميرا، والعدسة، والتأطير، واللون، والأجواء، والحركة. |
| `creator-storyboard-artist` | تصوّر المشاهد لوحةً تلو الأخرى: مقاسات اللقطات، والزوايا، والـ blocking، والتكوين، وموجّهات الذكاء الاصطناعي. |
| `creator-shot-list-designer` | تحوّل المشاهد والـ storyboards إلى قائمة لقطات تقنية، مقسّمة إلى وحدات قابلة للإنتاج بالذكاء الاصطناعي. |
| `creator-sound-music-designer` | العالم الصوتي للفيلم: الأجواء، والـ foley، والمؤثرات الصوتية، والموسيقى التصويرية، والثيمات المتكررة (leitmotifs)، وخطة موسيقية مشهدًا بمشهد، وموجّهات الصوت بالذكاء الاصطناعي. |
| `creator-prompt-engineer` | تحوّل مخرجات كل قسم إلى موجّهات متسقة لـ GPT Image 2.0 وNano Banana وSora وVeo وRunway وKling وHiggsfield وغيرها. |
| `creator-final-cut-editor` | تجمّع اللقطات والصوت والموسيقى والرسوميات المولّدة بالذكاء الاصطناعي في فيلم مكتمل: المونتاج الأولي والدقيق والنهائي، وفرز أخطاء الذكاء الاصطناعي، وصيغ التسليم. |

يوجد التعريف الكامل لكل مهارة في ملف `SKILL.md` الخاص بها.

---

## كيف يعمل

تعتمد الحزمة على **حالة مشتركة قائمة على نظام الملفات**. تقرأ جميع المهارات
من شجرة `project/` مشتركة وتكتب إليها (`bible/`، `screenplay/`،
`characters/`، `storyboards/`، `prompts/`، `cuts/`، `qc/`، …). تحافظ
`creator-pipeline-supervisor` على الملفات المرجعية (المرجعَين الأساسيَّين
للمشروع والاستمرارية) وتدقّق مخرجات كل قسم في ضوئها.

خط الإنتاج المرجعي:

```
0. project bible & vision
1. creator-screenwriter        → screenplay
2. creator-director            → vision, direction sheets, arcs
3-4-5. creator-character-designer + creator-production-designer
        + creator-cinematographer        (run in parallel)
6. creator-storyboard-artist   → panels with prompts
7. creator-shot-list-designer  → shot list + edit plan
8. creator-prompt-engineer     → tool-fit image + video prompts
   → [AI material generation — operator]
9. creator-sound-music-designer → sound + score plan
10. creator-final-cut-editor   → rough → fine → final cut → delivery

Throughout: creator-pipeline-supervisor enforces continuity, runs QC,
manages revision loops, and holds the bibles.
```

التسلسل مرجعي لكنه ليس جامدًا: يمكن لملاحظات المخرج أن تعيد تفعيل كاتب
السيناريو، وعادةً ما تعمل أقسام الشخصيات والإنتاج والتصوير السينمائي
بالتوازي بمجرد ترسيخ الرؤية الإخراجية.

---

## التحديث

```bash
cd ~/projects/vision_art_creator
git pull
```

نظرًا لأن المهارات مرتبطة بروابط رمزية، فلا حاجة إلى أي خطوة إضافية.

---

## التطوير

1. عدّل مهارة داخل المستودع (`skills/creator-*/SKILL.md`).
2. اختبر التغيير في Claude Code — وبما أنه رابط رمزي، فإنه يسري مفعوله
   فورًا.
3. نفّذ commit ثم push.

لإضافة مهارة creator جديدة:

```bash
mkdir -p skills/creator-new-skill
# write SKILL.md and README.md
./install.sh   # create the symlink for the new skill
```

---

## الترجمات

يتوفر ملف README هذا وملف `README.md` الخاص بكل مهارة بـ 12 لغة (انظر
محدّد اللغة في الأعلى). أما ملفات التعليمات `SKILL.md` فتُحفظ بالإنجليزية
عن قصد — إذ يستجيب Claude بلغة المستخدم وقت التشغيل، ووجود مجموعة تعليمات
مرجعية واحدة يتجنب تكرار أسماء المهارات.

---

## الترخيص

[MIT](LICENSE) © 2026 İlkay Demiralay.
