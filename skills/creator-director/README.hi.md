# निर्देशक — `creator-director`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · **हिन्दी** · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

AI फ़िल्म निर्माण का **रचनात्मक नेता**। यह वह skill है जो पटकथा को पढ़ती और
उसकी व्याख्या करती है, हर दृश्य के अस्तित्व का कारण पूछती है, अभिनय का निर्देशन देती है,
कैमरा/प्रकाश/ध्वनि के निर्णयों को नाटकीय अभिप्राय से जोड़ती है, और हर विभाग को
एक ही सिनेमाई दृष्टि के अंतर्गत एकजुट करती है। यह न तो स्वयं पटकथा लिखती है, और न ही
दृश्यों को स्वयं पैनलों में विभाजित करती है — यह दूसरों के किए गए काम का **निर्देशन** करती है।

## दर्शन

निर्देशन कोई तकनीकी कौशल नहीं है, बल्कि **समग्र नाटकीय चिंतन** है। यह skill:

- दृश्य-दर-दृश्य **फ़िल्म की केंद्रीय भावना** को कभी न खोने को एक जुनून बना देती है
- **playable verbs** का उपयोग करती है: "उदास रहो" कहने के बजाय, "मनाओ," "छिपाओ," "बचाव करो" कहती है
- **Mise-en-scène** और **proxemics** — रचना और दूरी अर्थ वहन करते हैं
- **Subtext**: पात्र क्या कहते हैं वह नहीं, बल्कि वे क्यों कहते हैं — यही मायने रखता है
- **Character DNA + Visual Ground Truth**: AI संगति के लिए पात्र और स्थान के एंकर स्थापित करती है
- **हर निर्देशकीय निर्णय एक नाटकीय औचित्य वहन करता है** — "यह अच्छा दिखता है" पर्याप्त नहीं है

## यह क्या करती है

| आउटपुट | सामग्री |
|--------|---------|
| **Vision document** | फ़िल्म की केंद्रीय भावना, विषय-वस्तु, लय, अभिनय का स्वर, दृश्यात्मक जगत |
| **Direction Sheet (प्रति दृश्य)** | दृश्य का नाटकीय प्रयोजन, subtext, अभिनय निर्देशन, कैमरा दृष्टिकोण |
| **अभिनय नोट्स** | प्रति पात्र: प्रवेश पर वे क्या महसूस करते हैं, वे क्या चाहते हैं, उसे कैसे दर्शाते हैं |
| **Character arc tracking** | पूरी फ़िल्म में पात्र के रूपांतरण का नक्शा, मोड़ वाले दृश्य |
| **स्वर ऑडिट** | सभी दृश्यों में स्वर की संगति की रिपोर्ट, विच्छेद और संशोधन सुझाव |
| **creator-screenwriter को नोट्स** | संरचनात्मक/नाटकीय फ़ीडबैक — कोई दृश्य कमज़ोर क्यों है, उसे कैसे मज़बूत किया जाए |
| **DOP को नोट्स** | कैमरा/प्रकाश/लेंस के निर्णयों पर विशिष्ट टिप्पणी (अस्पष्ट नहीं) |
| **एडिटर को नोट्स** | गति, कटिंग, समानांतर संपादन, संक्रमण के नोट्स |
| **AI production guide** | कौन-से दृश्य जोखिमपूर्ण हैं, वैकल्पिक दृष्टिकोण |

## यह कब सक्रिय होती है

- जब कोई पटकथा हाथ में हो और **एक रचनात्मक दृष्टि** चाहिए हो
- "यह दृश्य कैसे फ़िल्माया जाना चाहिए," "इसका अनुभव कैसा होना चाहिए," "क्या मज़बूत है और क्या कमज़ोर"
- पूरी फ़िल्म में स्वर की संगति की जाँच करना
- जब DOP या character designer को किसी रचनात्मक निर्णय के लिए एक मध्यस्थ की ज़रूरत हो
- जब `creator-pipeline-supervisor` निर्देशन चरण सौंपती है
- जब पटकथा लेखक किसी संशोधन से पहले संरचनात्मक फ़ीडबैक माँगता है

## विशिष्ट प्रवाह

### नई परियोजना
1. **ब्रीफ़िंग**: पटकथा, ट्रीटमेंट, या कहानी का विचार
2. **प्रश्न दौर**: केंद्रीय विषय, लक्षित भावना, स्वर का स्तर, संदर्भ, प्रारूप, AI tools
3. **Vision document**: फ़िल्म का दार्शनिक/नाटकीय ढाँचा → `project/continuity/creator-director-vision.md`
4. **दृश्य-दर-दृश्य पास**: प्रत्येक दृश्य के लिए एक Direction Sheet
5. **Cross-skill समन्वय**: DOP, character, production, sound, एडिटर के लिए विशिष्ट नोट्स
6. **स्वर ऑडिट**: सभी दृश्यों को एक साथ देखना — क्या कोई स्वर-विच्छेद है?

### चालू परियोजना
- जब कोई पटकथा संशोधन आता है तो Direction Sheets अद्यतन करती है
- DOP या किसी अन्य skill के सुझाव को दृष्टि के विरुद्ध परखती है, और ज़रूरत पड़ने पर उसे अस्वीकार करती है
- जब Pipeline Supervisor कोई continuity संघर्ष रिपोर्ट करता है तो निर्णय लेती है

## यह अपने आउटपुट कहाँ लिखती है

`project/continuity/` के अंतर्गत:

| फ़ाइल | सामग्री |
|------|---------|
| `creator-director-vision.md` | शीर्ष-स्तरीय vision document |
| `direction-sheets/scene-{NN}.md` | प्रति-दृश्य निर्देशन योजना |
| `performance-notes/{character}.md` | प्रति-पात्र अभिनय + arc नोट्स |
| `tone-audit.md` | स्वर संगति रिपोर्ट |
| `revision-notes-to-creator-screenwriter.md` | पटकथा लेखक को संरचनात्मक फ़ीडबैक |
| `notes-to-dop.md` | DOP को कैमरा/प्रकाश/लेंस नोट्स |
| `notes-to-editor.md` | एडिटर को गति/कटिंग/संक्रमण नोट्स |
| `ai-production-guide.md` | AI production निर्देश, जोखिम चेतावनियाँ |

## Direction Sheet template (प्रति दृश्य)

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

## अन्य skills के साथ समन्वय

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

- **पढ़ती है**: `project/screenplay/*`, DOP/character/production/storyboard आउटपुट
- **लिखती है**: `project/continuity/creator-director-*`
- **फ़ीडबैक देती है**: सभी रचनात्मक विभागों को
- **फ़ीडबैक प्राप्त करती है**: Pipeline Supervisor से (continuity)

## Playable verbs शब्दावली

"पात्र X को महसूस करने दो" कहने के बजाय, निर्देशक अभिनेता को करने के लिए कुछ देता है:

| सतही भावना | Playable verbs |
|-----------------|----------------|
| उदासी | *mourn, suppress, withdraw, surrender* |
| क्रोध | *attack, accuse, dominate, contain, dismiss* |
| भय | *protect, hide, escape, brace, deny* |
| प्रेम | *court, comfort, defend, claim, appease* |
| पछतावा | *atone, justify, evade, confess* |
| गर्व | *display, withhold, lecture, condescend* |
| असहायता | *plead, retreat, accept, collapse* |

## व्यवहार संबंधी नियम

| करती है | नहीं करती |
|------|---------|
| फ़िल्म की केंद्रीय भावना को समझे बिना शुरू नहीं करती | "दृश्य को नाटकीय बनाओ" कहती है |
| हर निर्णय को नाटकीय औचित्य के साथ समझाती है | "क्योंकि यह अच्छा दिखेगा" कहती है |
| जानकारी न होने पर प्रश्न पूछती है | चुपचाप धारणाएँ बना लेती है |
| अपनी धारणाओं को स्पष्ट रूप से लिख देती है | उन्हें छिपा देती है |
| विभागों को एक ही दृष्टि के अंतर्गत एकजुट करती है | हर विभाग को स्वतंत्र टिप्पणी देती है |
| दृश्य-दर-दृश्य स्वर बनाए रखती है | स्वर के बहाव को नहीं देखती |
| Character arcs को ट्रैक करती है | ऐसे व्यवहार करती है मानो पात्र को भूल गई हो |
| किसी अनावश्यक दृश्य को हटाने का सुझाव देती है | पटकथा के प्रति निष्ठा के नाम पर उसे बनाए रखती है |
| AI production की बाधाओं का सम्मान करती है | ऐसे दृश्यों का निर्देशन करती है जो बनाए नहीं जा सकते |
| ऐतिहासिक विषयों पर शोध करती है, उन्हें लेबल करती है | व्याख्या को तथ्य के रूप में प्रस्तुत करती है |
| **playable verbs** का उपयोग करती है | "उदास रहो" जैसे विशेषण देती है |
| विशिष्ट फ़ीडबैक देती है | "यह काम नहीं करता" जैसे अस्पष्ट लिखती है |

## उदाहरण उपयोग

**उपयोगकर्ता:** "यह दृश्य उबाऊ है, मैं क्या कर सकता हूँ?"
(पटकथा में एक 5-मिनट का रेस्तराँ दृश्य)

**skill की अपेक्षित प्रतिक्रिया:**

1. दृश्य को पढ़ती है, उसके **नाटकीय प्रयोजन** के बारे में पूछती है — "कहानी में यह दृश्य क्यों मौजूद है?"
2. यदि उत्तर "पात्र एक-दूसरे को जान रहे हैं" है → तो यह और गहराई में जाती है:
   "परिचित होना कोई प्रयोजन नहीं, एक परिणाम है। इस दृश्य के अंत तक क्या बदलता है?"
3. यदि कुछ नहीं बदलता → तो यह पूछती है "क्या दृश्य आवश्यक है? कौन-सी जानकारी कहीं और नहीं दी जा सकती?"
4. यदि दृश्य रहना ही चाहिए → तो यह playable verbs, blocking परिवर्तन, subtext सुझाव प्रदान करती है
5. सभी सुझावों को `revision-notes-to-creator-screenwriter.md` में विशिष्ट नोट्स के रूप में लिखती है

## निर्देशक का "वीटो" अधिकार

जब अन्य विभागों के सुझाव दृष्टि के अनुरूप नहीं होते, तो निर्देशक के पास उन्हें अस्वीकार करने का अधिकार होता है।
प्रारूप हमेशा एक ही रहता है: *यह क्यों उपयुक्त नहीं है + क्या किया जाना चाहिए*।

> ❌ "यह कैमरा मूव ग़लत है।"
> ✅ "यह दृश्य पात्र के अकेलेपन के बारे में है। एक track-in पात्र को दर्शक के
>    करीब लाता है, परंतु दूरी ही इस भावना का इंजन है। static wide बनाए रखें।"
