# مشرف خط الإنتاج والاستمرارية — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

إنه **orchestrator** و**مشرف الاستمرارية** لمشروع فيلم بالذكاء الاصطناعي. يندمج
فيه تخصصان متكاملان:

- **Pipeline supervisor**: أي skill يعمل ومتى، أين يعيش الـ state المشترك،
  كيف تدور المراجعات، كيف تُتتبَّع الإصدارات، كيف يُجرى ship للمشروع
- **Continuity supervisor**: يدقّق اتساق الشخصية والأزياء والموقع والـ prop
  والإضاءة واللون والصوت والزمن واتجاه المونتاج مشهدًا بمشهد وقسمًا بقسم —
  يلتقط التناقضات مبكرًا، ويطلب الإصلاحات

## الفلسفة

الـ pipeline-supervisor ليس "checklist tool". إنه يفكّر مثل مزيج من **unit
production manager + script supervisor**. يحفظ المشروع بأكمله في ذهنه ولا يدع
عمل أي قسم ينحرف عن النية المتسقة للفيلم. هذا الـ skill:

- **يحتفظ بمصدر حقيقة واحد**: `bible/continuity-bible.md` يحكم كل شيء
- **Production status table** محدَّث دائمًا — الإجابة على "ماذا أفعل الآن"
- **انضباط locked anchor**: حمض الشخصية النووي (DNA) + master reference للموقع +
  style block — يدخل كل prompt حرفيًا (verbatim)
- **Cross-skill arbitration**: عند تعارض قسمين، ينقل كلا الموقفين، ويعرض خيارات
  مرجعية إلى رؤية المخرج، ويصعّد (escalate) إلى المستخدم
- **إدارة revision loop**: عندما يجد skill في المراحل اللاحقة مشكلة في مرحلة
  سابقة، ينفّذ cascade بالترتيب القانوني (canonical)
- **Risk register**: تتبّع استباقي للمخاطر، متابعة الـ mitigation
- **Ship gate**: لا يقول "تمّ" دون تدقيق delivery-readiness

## ماذا يُنتِج

| المُخرَج | المحتوى |
|---------|---------|
| **Project bible** | canon المشروع رفيع المستوى |
| **Style bible** | canon الأسلوب عبر المهارات |
| **Continuity bible** | مصدر الحقيقة الواحد للاستمرارية |
| **Prompt blocks** | locked prompt blocks مُجمَّعة |
| **Production status table** | مصفوفة حالة skill × مشهد |
| **Risk register** | سجل المخاطر + severity + mitigation |
| **Continuity audit reports** | تدقيقات حسب الـ domain |
| **Revision request manifests** | طلبات مراجعة عبر المهارات |
| **Prompt consistency report** | تدقيق قبل التوليد |
| **AI generation error summary** | تدقيق بعد التوليد |
| **Final QC report** | تدقيق المشروع بالكامل |
| **Delivery readiness** | Ship gate (pass/fail) |
| **Decisions log** | سجل قرارات مؤرَّخ |

## متى يتدخّل

- بدء مشروع فيلم جديد بالذكاء الاصطناعي
- طلب تدقيق اتساق عبر المهارات في مشروع جارٍ
- عند سؤال "ماذا أفعل الآن" (الإجابة تأتي من production status)
- عندما يتجاوز سؤال استمرارية أو pipeline حدود أحد الـ skills
- طلب تدقيق delivery-readiness
- سؤال بنية المجلدات / file organization
- عندما يجب أن تنتقل مراجعة (cascade) إلى الـ skills التابعة

## متى لا يتدخّل

- أعمال إبداعية لمهارة واحدة (دع الـ specialist يعمل بمفرده)
- توليد بسيط لـ single-shot
- أسئلة تقنية بحتة خارج إنتاج الأفلام

## Canonical pipeline

```
0. project bible & vision
1. creator-screenwriter
2. creator-director
3-4-5. character + production + DOP (parallel)
6. creator-storyboard-artist
7. creator-shot-list-designer
8. creator-prompt-engineer
   → [AI material generation — operator]
9. creator-sound-music-designer
10. creator-final-cut-editor

عبر جميع المراحل: creator-pipeline-supervisor يتولّى الاستمرارية وQC والمراجعة وإدارة الـ bible
```

الترتيب **canonical لكنه ليس صارمًا**:
- **حلقات تكرارية**: ملاحظات creator-director → نسخة جديدة من creator-screenwriter
- **عمل متوازٍ**: بعد رؤية المخرج، تعمل character/production/DOP بالتوازي

## Continuity domains (مجالات التدقيق)

1. Story / plot
2. Time / chronology
3. Character (physical)
4. Character arc (emotional)
5. Costume
6. Hair / makeup
7. Accessories / props
8. Location
9. Set dressing
10. Light direction
11. Color palette
12. Camera language
13. Sound / ambience
14. Music theme (leitmotif)
15. Emotional flow
16. Edit / screen direction
17. AI prompt consistency (locked anchors verbatim)
18. Reference image consistency
19. Scene / shot numbering

لكل domain سجل مخاطر: `project/qc/continuity-reports/`.

## Continuity bible (مصدر الحقيقة الواحد)

`project/bible/continuity-bible.md` — هذا الملف هو **المرجع/السلطة**. إذا تعارض
مُخرَج أحد الـ skills مع الـ bible، تفوز الـ bible (أو تُحدَّث الـ bible).

محتواه:
- Locked character anchors (DNA verbatim)
- Locked location anchors (master reference verbatim)
- جدول costume continuity (مشهد × شخصية)
- جدول time / weather
- جدول prop continuity
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction (screen direction × scene)
- أسئلة استمرارية مفتوحة (بانتظار قرار المخرج)
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`:

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

يُحدَّث بعد كل skill run. مصدر الإجابة على "ماذا أفعل الآن؟".

## إدارة revision loop

عندما يجد skill لاحق مشكلة في مرحلة سابقة:

1. **تحديد الـ origin**: أي مُخرَج skill معيب؟
2. **Blast radius**: كيف يؤثر الإصلاح على الـ skills التابعة؟
3. **Change request**: `qc/revision-notes/req-{NN}.md`
4. **القرار**: إصلاح في الـ origin (عميق، بطيء) مقابل workaround (سطحي، سريع)
5. **Origin fix**: يُعاد تشغيل الـ skill، وتصبح التابعة 🟡، وينفَّذ cascade بالترتيب القانوني
6. **Workaround**: يُسجَّل أين ولماذا ومن طبّقه
7. **Resolution log**: يُلحَق بـ "Resolved decisions" في continuity bible

## Cross-skill arbitration

عند تعارض skillين (مثلًا إضاءة دافئة لـ DOP مقابل palette باردة للشخصية):

1. اقتبس كلا المقترحين **حرفيًا (verbatim)**
2. اذكر التعارض بلغة بسيطة
3. ارجع إلى director vision
4. اعرض 2–3 حلول + trade-offs
5. صعّد (escalate) إلى المستخدم / المخرج
6. يُكتَب القرار في continuity bible

**لا يختار في صمت** — بل يجعل التعارض مرئيًا.

## Risk register

`project/qc/risk-register.md`:

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| خطر فشل lip sync في المشهد 7 | medium | high | creator-shot-list-designer | استخدم reaction shot | mitigating |
| خطر AI لـ insert اليد في المشهد 12 | medium | medium | creator-prompt-engineer | نسخة احتياطية بـ wider framing | mitigated |
| انحراف hue لـ "Navy coat" | low | high | creator-character-designer | hex مقفل في الـ DNA | mitigated |

## بنية المجلدات (خياران)

### Default (named — بسيط)

`project/screenplay/`، `project/characters/`، `project/cuts/` ...

### Alternate (numbered — للمشاريع الكبيرة)

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

المحتوى نفسه، مرقَّم وملائم للمسح البصري. الـ default هو named؛ ويعرض migration عند الطلب.

## أين يكتب مُخرَجاته

تحت `project/bible/` و`project/qc/` (لا يكتب مباشرةً في مجلدات الـ skills الأخرى —
بل يرسل إليها revision requests):

| الملف | المحتوى |
|-------|---------|
| `bible/project-bible.md` | canon المشروع رفيع المستوى |
| `bible/style-bible.md` | canon الأسلوب عبر المهارات |
| `bible/continuity-bible.md` | مصدر الحقيقة الواحد للاستمرارية |
| `bible/prompt-blocks.md` | Locked prompt blocks |
| `qc/production-status.md` | مصفوفة حالة skill × مشهد |
| `qc/risk-register.md` | سجل المخاطر |
| `qc/continuity-reports/{topic}.md` | تدقيقات الـ domain |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | تدقيق قبل التوليد |
| `qc/ai-generation-error-summary.md` | تدقيق بعد التوليد |
| `qc/final-qc-report.md` | تدقيق المشروع بالكامل |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | سجل قرارات مؤرَّخ |

## التدفّق النموذجي (مشروع جديد)

1. briefing المستخدم
2. اكتب `bible/project-bible.md`
3. ← شغّل **creator-screenwriter**
4. Script v1 ← شغّل **creator-director**
5. Vision ← بالتوازي: **character + production + DOP**
6. تدقيق cross-palette؛ ضع flag على التعارضات
7. ← **creator-storyboard-artist**
8. ← **creator-shot-list-designer**
9. build/update لـ `bible/prompt-blocks.md`
10. ← **creator-prompt-engineer**
11. تدقيق قبل التوليد
12. [AI material — يشغّله الـ operator]
13. تدقيق بعد التوليد
14. ← **creator-sound-music-designer**
15. ← **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit (ship gate)

قبل اعتباره منجزًا:

- ✅ جميع المشاهد في production-status
- ✅ Continuity audit نظيف (أو بـ minor flags فقط)
- ✅ Final cut معتمد من المخرج
- ✅ Audio integration audit نظيف
- ✅ أخطاء AI تمّ triage لها (لا 🔴 حرجة)
- ✅ Color grade مُطبَّق أو مُعلَّم عمدًا (flag)
- ✅ Subtitles كاملة و timed
- ✅ Title cards / credits في مكانها
- ✅ master لكل منصات التسليم تحت `project/delivery/`
- ✅ Trailer cut أُنتِج (إن طُلب)
- ✅ Archive master محفوظ
- ✅ التوثيق محدَّث (bible، continuity، prompt-blocks)

## التنسيق مع الـ skills الأخرى

- **يقرأ**: جميع مُخرَجات الـ skills (كل شيء في `project/`)
- **يكتب**: `project/bible/*`، `project/qc/*` — لا يكتب مباشرةً في المجلدات الأخرى
- **يشغّل**: جميع الـ skills المتخصصة (specialist)
- **يحكِّم (arbitrate)**: التعارضات عبر المهارات

## قواعد السلوك

| يفعل | لا يفعل |
|------|---------|
| يفرض الوفاء لـ director vision في كل قسم | يسمح بالانحراف الصامت |
| في التعارض عبر المهارات، يقتبس الطرفين **حرفيًا (verbatim)** | يختار طرفًا في صمت |
| يوثّق كل قرار بالتاريخ + المبرّر | يتصرف دون سجل |
| يحمي continuity bible بصفتها المرجع | يمرّر مُخرَجًا يتعارض مع الـ bible |
| يحدّث production-status بعد كل skill run | يترك جدولًا متقادمًا (stale) |
| ينفّذ cascade للمراجعات بالترتيب القانوني | يتخطّى skill تابعًا |
| يصعّد النزاعات الإبداعية إلى المستخدم / المخرج | يحكِّم بمفرده |
| Continuity audit عند كل act break في فيلم طويل | يدقّق في النهاية فقط |
| Risk register استباقي | يؤجّل 🔴 حرجة |
| لا يقول "ship" حتى يصبح delivery-readiness.md بلون green | يعتبره complete مبكرًا |
| مُخرَج منظَّم وقابل للقراءة آليًا (machine-readable) | يصبّ كتلة نصية واحدة |
