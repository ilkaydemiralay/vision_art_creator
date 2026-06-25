# स्टोरीबोर्ड आर्टिस्ट — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

एक skill जो लिखित पटकथा को **पठनीय दृश्य कथन** में बदलती है। पैनल की संख्या को
न्यूनतम रखकर, यह सुनिश्चित करती है कि हर पैनल किसी नाटकीय कारण से ही मौजूद हो।
यह दृश्य के निर्णायक क्षणों को पकड़ती है, screen direction को बनाए रखती है, eyeline
continuity का अनुसरण करती है, और AI image/video prompt को साफ-सुथरा hand-off करती है।

## दर्शन

स्टोरीबोर्ड "दृश्य का चित्रण" नहीं है — यह एक **दृश्य कथन प्रणाली** है। यह skill:

- **Panel economy**: कम पैनल + तीक्ष्ण चयन — न कि अधिक पैनल + कमजोर निर्णय
- **Screen direction (180°)** और **eyeline continuity**: कट्स के बीच स्थानिक संगति
- **Graphic dynamics**: नज़र कहाँ टिकती है? फोकस क्या है?
- **Continuity awareness**: वेशभूषा, स्थान, प्रकाश की दिशा, स्क्रीन दिशा, गति
- **Locked anchors**: हर पैनल में character DNA + location master reference
- **Producibility**: AI उत्पादन की सीमाओं को जानती है और जोखिम भरे दृश्यों को flag करती है

## यह किस काम आती है

| आउटपुट | सामग्री |
|--------|---------|
| **Per-scene storyboard** | दृश्य-दर-दृश्य पैनल सूची (समस्त पैनल डेटा) |
| **Per-panel sheets** | जटिल दृश्य के लिए विस्तृत एकल-पैनल फ़ाइल |
| **AI image prompts** | प्रति पैनल उत्पादन-तैयार prompt |
| **AI video prompts** | गतिशील पैनल के लिए video prompt |
| **Continuity log** | वेशभूषा/स्थान/दिशा जोखिमों के flag |
| **Animatic plan** | सभी दृश्यों के animatic क्रम की योजना बनाती है |
| **Director / DOP notes** | निर्देशक और DOP के लिए संक्षिप्त दृश्य/तकनीकी नोट्स |
| **Handoff to shot-list** | creator-shot-list-designer प्रारूप में पैनल डेटा |

## यह कब सक्रिय होती है

- पटकथा हाथ में हो और दृश्य विभाजन चाहिए हो
- जब निर्देशक दृश्य का पूर्वावलोकन दृश्य रूप में चाहे
- जब DOP के lens/light निर्णय से पहले दृश्य अवधारणा की आवश्यकता हो
- जब AI prompt बनाने से पहले स्टोरीबोर्ड तर्क चाहिए हो
- जब `creator-pipeline-supervisor` स्टोरीबोर्ड चरण को सौंपे

## Panel content (कैनोनिकल फ़ील्ड)

हर पैनल इन फ़ील्ड्स को दर्ज करता है:

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

## यह अपने आउटपुट कहाँ लिखती है

`project/storyboards/` के अंतर्गत:

| फ़ाइल | सामग्री |
|-------|---------|
| `scene-{NN}/storyboard.md` | दृश्य-आधारित पैनल सूची (कैनोनिकल) |
| `scene-{NN}/panel-{PP}.md` | विस्तृत एकल पैनल (जटिल दृश्यों में) |
| `scene-{NN}/prompts.md` | प्रति-पैनल AI prompts (image + video) |
| `scene-{NN}/continuity.md` | Continuity flag |
| `animatic-plan.md` | पूरी फ़िल्म के animatic क्रम के नोट्स |
| `notes-to-creator-director.md` | निर्देशक के लिए प्रश्न/चेतावनी |
| `handoff-to-shot-list.md` | shot-list designer के लिए प्रारूपित पैनल डेटा |

## Shot type शब्दावली (नाटकीय समकक्ष के साथ)

| प्रकार | नाटकीय उपयोग |
|--------|--------------|
| Establishing | दर्शक को स्थान में स्थापित करता है |
| Master | दृश्य की ज्यामिति, fallback |
| Wide/Full | पात्र–परिवेश संबंध |
| Medium | तटस्थ संवाद |
| Close | आंतरिक संघर्ष, अंतरंग भावना |
| Extreme close | व्यक्तिनिष्ठ तीव्रता |
| Insert | वस्तु पर ज़ोर |
| Cutaway | समानांतर/बाहरी जानकारी |
| Reaction | क्रिया से अधिक प्रतिक्रिया |
| OTS | संवाद का परिप्रेक्ष्य |
| POV | पात्र की व्यक्तिनिष्ठता |
| 2-shot / group | संबंध की ज्यामिति |
| Silhouette | अनामता, रहस्य |
| Negative-space frame | अलगाव, लघुता |
| Symmetrical | शक्ति, औपचारिकता, बेचैन कर देने वाली स्थिरता |
| Tracking | निरंतर अनुसरण |
| Static | अवलोकन, मौन का अर्थ |

"close-up का प्रयोग करो" पर्याप्त नहीं है — प्रश्न यह है कि close-up **क्यों** आवश्यक है।

## Continuity audit

पैनल से पैनल, दृश्य से दृश्य तक अनुसरण:

- वेशभूषा
- बाल/मेकअप/एक्सेसरीज़
- स्थान की पहचान (locked anchor के साथ)
- प्रकाश की दिशा
- दिन/रात
- Screen direction (180° नियम)
- पात्रों का स्थानिक तर्क
- क्रिया का प्रवाह
- prop की स्थिति

जब कोई जोखिम पहचाना जाता है, तो उसे पैनल के `continuity note` फ़ील्ड में स्पष्ट रूप से लिखा जाता है।

## अन्य skills के साथ समन्वय

- **पढ़ती है**: पटकथा, निर्देशक की दृष्टि + direction sheets, DOP per-scene plan,
  character DNA + FACS, location anchors
- **लिखती है**: `project/storyboards/*`
- **सौंपती है**:
  - `creator-shot-list-designer` (panel → shot list)
  - `creator-prompt-engineer` (panel prompt → tool-specific optimization)
- **फ़ीडबैक प्राप्त करती है**: निर्देशक, Pipeline Supervisor

## AI-उत्पादन केंद्रित समाधान

- जटिल दृश्यों को सरल पैनलों में विभाजित करती है
- बहु-पात्र दृश्यों में दृश्य फोकस स्पष्ट करती है
- उन गतियों को सरल बनाती है जिनमें AI को कठिनाई होगी
- एक ही स्थान/पात्र के लिए स्थिर anchor का उपयोग करती है
- कैमरा गति के बजाय सुरक्षित स्थिर-शॉट विकल्प देती है
- भीड़भाड़ वाले दृश्यों में चयनात्मक फ़्रेमिंग का सुझाव देती है
- तेज़ क्रिया के बजाय लयबद्ध कट्स का सुझाव देती है

## व्यवहार नियम

| करती है | नहीं करती |
|---------|-----------|
| हर पैनल के लिए नाटकीय औचित्य लिखती है | केवल "एक और पैनल" कहकर भर देती है |
| कम पैनल + तीक्ष्ण चयन | अधिक पैनल + कमजोर निर्णय |
| पटकथाकार + निर्देशक + DOP + पात्र + उत्पादन को एकीकृत करती है | upstream को चुपचाप दबा देती है |
| screen direction और eyeline को बनाए रखती है | कट पर दिशा गड़बड़ कर देती है |
| locked anchors को हर prompt में डालती है | हर पैनल में शून्य से वर्णन करती है |
| जटिल दृश्य को पैनलों में बाँटती है | एक ही अतिभारित frame पर लाद देती है |
| AI जोखिम flag + सुरक्षित विकल्प | अनुत्पाद्य गति का सुझाव देती है |
| संरचित, downstream-पठनीय आउटपुट | टेक्स्ट का एक ही ब्लॉक उड़ेल देती है |
