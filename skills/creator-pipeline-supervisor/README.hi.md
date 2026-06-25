# पाइपलाइन और निरंतरता पर्यवेक्षक — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

AI फ़िल्म प्रोजेक्ट का **orchestrator** और **निरंतरता पर्यवेक्षक**। दो एकीकृत
विशेषज्ञताएँ एक साथ आती हैं:

- **Pipeline supervisor**: कौन-सा skill कब चलता है, साझा state कहाँ रहता है,
  revisions कैसे loop करते हैं, versions कैसे ट्रैक होते हैं, प्रोजेक्ट कैसे
  ship किया जाता है
- **Continuity supervisor**: किरदार, costume, location, prop, light, color,
  sound, time और edit direction की संगति को दृश्य-दर-दृश्य, विभाग-दर-विभाग
  ऑडिट करता है — विरोधाभासों को जल्दी पकड़ता है, fix का अनुरोध करता है

## दर्शन

pipeline-supervisor कोई "checklist tool" नहीं है। यह **unit production manager +
script supervisor** के संयोजन की तरह सोचता है। पूरे प्रोजेक्ट को अपने दिमाग में
रखता है और किसी भी विभाग के काम को फ़िल्म के सुसंगत अभिप्राय से भटकने नहीं देता।
यह skill:

- **एकल सत्य-स्रोत रखता है**: `bible/continuity-bible.md` सब कुछ नियंत्रित करता है
- **Production status table** हमेशा अद्यतन — "अब मुझे क्या करना चाहिए" का उत्तर
- **Locked anchor अनुशासन**: किरदार DNA + location master reference +
  style block — हर prompt में verbatim जाता है
- **Cross-skill arbitration**: जब दो विभाग टकराते हैं, तो यह दोनों पक्षों को
  प्रस्तुत करता है, director के vision के संदर्भ में विकल्प देता है, और उपयोगकर्ता
  तक escalate करता है
- **Revision loop प्रबंधन**: जब कोई downstream skill upstream में समस्या पाती है,
  तो यह canonical क्रम में cascade करता है
- **Risk register**: सक्रिय जोखिम ट्रैकिंग, mitigation का अनुसरण
- **Ship gate**: delivery-readiness audit के बिना "हो गया" नहीं कहता

## यह क्या उत्पन्न करता है

| आउटपुट | सामग्री |
|--------|---------|
| **Project bible** | उच्च-स्तरीय प्रोजेक्ट canon |
| **Style bible** | Cross-skill style canon |
| **Continuity bible** | निरंतरता का एकल सत्य-स्रोत |
| **Prompt blocks** | समेकित locked prompt blocks |
| **Production status table** | Skill × दृश्य स्थिति मैट्रिक्स |
| **Risk register** | जोखिम + severity + mitigation लॉग |
| **Continuity audit reports** | Domain-आधारित ऑडिट |
| **Revision request manifests** | Cross-skill revision अनुरोध |
| **Prompt consistency report** | Pre-generation ऑडिट |
| **AI generation error summary** | Post-generation ऑडिट |
| **Final QC report** | संपूर्ण-प्रोजेक्ट ऑडिट |
| **Delivery readiness** | Ship gate (pass/fail) |
| **Decisions log** | दिनांकित निर्णय इतिहास |

## यह कब सक्रिय होता है

- एक नया AI फ़िल्म प्रोजेक्ट शुरू किया जा रहा हो
- किसी चालू प्रोजेक्ट पर cross-skill consistency audit का अनुरोध हो
- "अब मुझे क्या करना चाहिए" के प्रश्न पर (उत्तर production status से आता है)
- जब कोई निरंतरता या pipeline प्रश्न किसी skill की सीमा पार करे
- delivery-readiness audit का अनुरोध हो
- फ़ोल्डर संरचना / file organization का प्रश्न
- जब किसी revision को dependent skills तक cascade करना हो

## यह कब सक्रिय नहीं होता

- एकल-skill रचनात्मक कार्य (specialist को अकेले काम करने दें)
- सरल single-shot generation
- फ़िल्म निर्माण से बाहर के विशुद्ध तकनीकी प्रश्न

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

सभी चरणों में: creator-pipeline-supervisor निरंतरता, QC, revision, bible प्रबंधन संभालता है
```

क्रम **canonical है पर कठोर नहीं**:
- **पुनरावृत्त loops**: creator-director feedback → creator-screenwriter नया v
- **समानांतर कार्य**: director के vision के बाद character/production/DOP समानांतर चलते हैं

## Continuity domains (ऑडिट क्षेत्र)

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

प्रत्येक domain के लिए एक जोखिम लॉग है: `project/qc/continuity-reports/`।

## Continuity bible (एकल सत्य-स्रोत)

`project/bible/continuity-bible.md` — यह फ़ाइल **प्राधिकरण** है। यदि किसी skill का
आउटपुट bible से टकराता है, तो bible जीतती है (या bible अद्यतन की जाती है)।

इसकी सामग्री:
- Locked character anchors (DNA verbatim)
- Locked location anchors (master reference verbatim)
- Costume continuity तालिका (दृश्य × किरदार)
- Time / weather तालिका
- Prop continuity तालिका
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction (screen direction × scene)
- खुले निरंतरता प्रश्न (director के निर्णय की प्रतीक्षा में)
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`:

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

हर skill run के बाद अद्यतन। "अब मुझे क्या करना चाहिए?" के उत्तर का स्रोत।

## Revision loop प्रबंधन

जब कोई downstream skill upstream में समस्या पाती है:

1. **Origin की पहचान**: किस skill का आउटपुट दोषपूर्ण है?
2. **Blast radius**: fix dependent skills को कैसे प्रभावित करता है?
3. **Change request**: `qc/revision-notes/req-{NN}.md`
4. **निर्णय**: origin पर fix (गहरा, धीमा) बनाम workaround (उथला, तेज़)
5. **Origin fix**: skill फिर से ट्रिगर होती है, dependents 🟡 हो जाते हैं, canonical क्रम में cascade
6. **Workaround**: कहाँ, क्यों और किसने लागू किया दर्ज किया जाता है
7. **Resolution log**: continuity bible के "Resolved decisions" में append

## Cross-skill arbitration

जब दो skills टकराती हैं (जैसे DOP की गर्म light बनाम किरदार की cool palette):

1. दोनों प्रस्ताव **verbatim** उद्धृत करें
2. टकराव को सरल भाषा में बताएँ
3. director vision का संदर्भ दें
4. 2–3 समाधान + trade-offs प्रस्तुत करें
5. उपयोगकर्ता / director तक escalate करें
6. निर्णय continuity bible में लिखा जाता है

**यह चुपचाप चुनाव नहीं करता** — यह टकराव को दृश्यमान बनाता है।

## Risk register

`project/qc/risk-register.md`:

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| दृश्य 7 में lip sync fail का जोखिम | medium | high | creator-shot-list-designer | reaction shot का उपयोग करें | mitigating |
| दृश्य 12 हाथ insert AI जोखिम | medium | medium | creator-prompt-engineer | wider framing backup | mitigated |
| "Navy coat" hue drift | low | high | creator-character-designer | DNA में hex लॉक्ड | mitigated |

## फ़ोल्डर संरचना (दो विकल्प)

### Default (named — सरल)

`project/screenplay/`, `project/characters/`, `project/cuts/` ...

### Alternate (numbered — बड़े प्रोजेक्ट के लिए)

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

समान सामग्री, संख्यांकित और दृश्य स्कैनिंग के अनुकूल। Default named है; मांग पर
migration प्रदान करता है।

## यह अपने आउटपुट कहाँ लिखता है

`project/bible/` और `project/qc/` के अंतर्गत (यह अन्य skills की directories में
सीधे नहीं लिखता — उन्हें revision requests भेजता है):

| फ़ाइल | सामग्री |
|-------|---------|
| `bible/project-bible.md` | उच्च-स्तरीय प्रोजेक्ट canon |
| `bible/style-bible.md` | Cross-skill style canon |
| `bible/continuity-bible.md` | निरंतरता का एकल सत्य-स्रोत |
| `bible/prompt-blocks.md` | Locked prompt blocks |
| `qc/production-status.md` | Skill × दृश्य स्थिति मैट्रिक्स |
| `qc/risk-register.md` | जोखिम लॉग |
| `qc/continuity-reports/{topic}.md` | Domain ऑडिट |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | Pre-generation ऑडिट |
| `qc/ai-generation-error-summary.md` | Post-generation ऑडिट |
| `qc/final-qc-report.md` | संपूर्ण-प्रोजेक्ट ऑडिट |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | दिनांकित निर्णय इतिहास |

## विशिष्ट प्रवाह (नया प्रोजेक्ट)

1. उपयोगकर्ता briefing
2. `bible/project-bible.md` लिखें
3. → **creator-screenwriter** ट्रिगर करें
4. Script v1 → **creator-director** ट्रिगर करें
5. Vision → समानांतर: **character + production + DOP**
6. Cross-palette audit; टकराव flag करें
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. `bible/prompt-blocks.md` build/update करें
10. → **creator-prompt-engineer**
11. Pre-generation ऑडिट
12. [AI material — operator इसे चलाता है]
13. Post-generation ऑडिट
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit (ship gate)

इसे संपन्न कहने से पहले:

- ✅ सभी दृश्य production-status में हैं
- ✅ Continuity audit साफ़ है (या केवल minor flags)
- ✅ Final cut director-अनुमोदित है
- ✅ Audio integration audit साफ़ है
- ✅ AI errors triage किए गए (कोई critical 🔴 नहीं)
- ✅ Color grade लागू या जानबूझकर flag किया गया
- ✅ Subtitles पूर्ण और timed
- ✅ Title cards / credits यथास्थान
- ✅ सभी deliverable platforms का master `project/delivery/` के अंतर्गत
- ✅ Trailer cut उत्पन्न (यदि अनुरोध किया गया हो)
- ✅ Archive master संग्रहीत
- ✅ दस्तावेज़ीकरण अद्यतन (bible, continuity, prompt-blocks)

## अन्य skills के साथ समन्वय

- **पढ़ता है**: सभी skill आउटपुट (`project/` में सब कुछ)
- **लिखता है**: `project/bible/*`, `project/qc/*` — अन्य directories में सीधे नहीं लिखता
- **ट्रिगर करता है**: सभी specialist skills
- **arbitrate करता है**: cross-skill टकराव

## व्यवहार नियम

| करता है | नहीं करता |
|---------|-----------|
| हर विभाग में director vision के प्रति निष्ठा लागू करता है | चुपचाप भटकने देता है |
| cross-skill टकराव में दोनों पक्षों को **verbatim** उद्धृत करता है | चुपचाप एक पक्ष चुनता है |
| हर निर्णय को दिनांक + औचित्य के साथ दस्तावेज़ करता है | बिना रिकॉर्ड के कार्य करता है |
| continuity bible को प्राधिकरण के रूप में सुरक्षित रखता है | bible से टकराने वाले आउटपुट को पास करता है |
| हर skill run के बाद production-status अद्यतन करता है | stale तालिका छोड़ता है |
| revisions को canonical क्रम में cascade करता है | किसी dependent skill को छोड़ देता है |
| रचनात्मक विवादों को उपयोगकर्ता / director तक escalate करता है | अकेले arbitrate करता है |
| लंबी फ़िल्म में हर act break पर continuity audit | केवल अंत में audit |
| सक्रिय risk register | critical 🔴 को रोके रखता है |
| delivery-readiness.md green होने तक "ship" नहीं कहता | समय से पहले complete कहता है |
| संरचित, machine-readable आउटपुट | पाठ का एक ही ब्लॉक उड़ेल देता है |
