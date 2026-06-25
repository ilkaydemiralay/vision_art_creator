# प्रोडक्शन डिज़ाइनर — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

वह skill जो फ़िल्म की **दुनिया** गढ़ता है: लोकेशन, सेट, props, कालखंड का
वातावरण, रंग और सामग्री की भाषा। "एक सुंदर गाँव" कहने के बजाय यह दीवार की बनावट,
फ़र्श की सामग्री, फ़र्नीचर का घनत्व, प्रकाश को प्रभावित करने वाली सतहों और घिसावट
के निशानों के स्तर तक डिज़ाइन करता है। यह वे master reference स्थापित करता है जो
लंबी AI फ़िल्म निर्माण में **लोकेशन की निरंतरता** बनाए रखते हैं।

## दर्शन

स्थान कोई पृष्ठभूमि नहीं, बल्कि एक **कथात्मक उपकरण** है। यह skill:

- पहले **World bible** — फिर per-location, फिर per-scene (top-down)
- **Master reference**: हर मुख्य लोकेशन के लिए एक लॉक किया हुआ AI prompt block —
  ताकि 50 दृश्य बाद भी वही घर तैयार किया जा सके
- **जिए-बसे होने का डिज़ाइन**: दरारें, दाग, धूप से रंग उड़ना, घिसावट, मरम्मत के निशान
- **Class-coded design**: हर सामग्री/रंग सामाजिक वर्ग की कहानी कहता है
- **Coordinated palette**: DOP की रोशनी और किरदार के पोशाक के साथ मिलकर सोचा गया
- **Period research**: जहाँ ऐतिहासिक/सांस्कृतिक सटीकता ज़रूरी हो, वहाँ स्रोत-सहित शोध

## यह किस काम आता है

| आउटपुट | सामग्री |
|-------|--------|
| **World bible** | फ़िल्म की समग्र दुनिया के नियम (कालखंड, वर्ग, वास्तुकला, सामग्री) |
| **Color & texture bible** | रंग पैलेट, सामग्री की भाषा, घिसावट के पैटर्न |
| **Location dossier** | हर मुख्य लोकेशन के लिए विस्तृत दस्तावेज़ (लॉक + वैरिएशन) |
| **Master reference (AI)** | लोकेशन की पहचान का स्थिर AI prompt block |
| **Props inventory** | सेट के वस्तुएँ, उनके नाटकीय कार्यों सहित |
| **Per-scene plan** | दृश्य-दर-दृश्य प्रोडक्शन डिज़ाइन (dressing, props, प्रकाश स्रोत) |
| **Continuity log** | दृश्यों के बीच लोकेशन की निरंतरता की जाँच |
| **Period research** | स्रोत-सहित ऐतिहासिक/सांस्कृतिक शोध |
| **Notes to DOP / creator-director** | द्विदिशीय संचार |

## यह कब सक्रिय होता है

- स्क्रिप्ट हाथ में है, दुनिया / लोकेशन / सेट डिज़ाइन की ज़रूरत है
- "यह स्थान कैसा दिखना चाहिए", "set dressing", "prop सूची"
- AI निर्माण के लिए सुसंगत लोकेशन reference
- कालखंड शोध (ऐतिहासिक, सांस्कृतिक, क्षेत्रीय)
- जब `creator-pipeline-supervisor` प्रोडक्शन डिज़ाइन चरण सौंपता है

## सामान्य प्रवाह

1. **ब्रीफ़िंग** + `creator-director-vision.md` + DOP visual-language पढ़ना
2. **प्रश्न दौर**: कालखंड, भूगोल, टोन, वर्ग, AI उपकरण
3. **World bible**: फ़िल्म की समग्र दुनिया के नियम
4. **Color & texture bible**: सामग्री और रंग की भाषा
5. **Major locations**: हर मुख्य लोकेशन के लिए dossier
6. **Master references**: AI निरंतरता के लिए लॉक किए गए prompt block
7. **Per-scene sheets**: दृश्य-दर-दृश्य set dressing + prop नोट्स
8. **Continuity audit**: क्या वही लोकेशन अलग-अलग दृश्यों में सुसंगत है?

## यह अपने आउटपुट कहाँ लिखता है

`project/production-design/` के अंतर्गत (cinematography को छोड़कर — वह DOP का है):

| फ़ाइल | सामग्री |
|-------|--------|
| `world-bible.md` | फ़िल्म की दुनिया के नियम |
| `color-texture-bible.md` | रंग + सामग्री की भाषा |
| `locations/{slug}/location-doc.md` | Per-location dossier |
| `locations/{slug}/master-reference.md` | लॉक किया हुआ AI base prompt |
| `props/{slug}.md` या `props-list.md` | Prop सूची |
| `scenes/scene-{NN}.md` | दृश्य-दर-दृश्य प्रोडक्शन डिज़ाइन योजना |
| `continuity-notes.md` | लोकेशन निरंतरता जाँच लॉग |
| `period-research.md` | स्रोत-सहित कालखंड शोध |
| `notes-to-creator-director.md` | निर्देशक के लिए प्रश्न/सुझाव |
| `notes-to-creator-cinematographer.md` | DOP के साथ सतह/गहराई/प्रकाश समन्वय |

## Location dossier टेम्पलेट (सारांश)

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

## Master reference (AI निरंतरता के लिए)

हर मुख्य लोकेशन के लिए एक **लॉक किया हुआ base prompt block** लिखा जाता है:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

यह block सभी दृश्य prompt में हूबहू दोहराया जाता है, और उसके ऊपर दृश्य-विशिष्ट
वैरिएशन जोड़ी जाती है।

## अन्य skills के साथ समन्वय

- **Cinematographer**:
  - सतहों का प्रकाश से संबंध (matte, glossy, transparent)
  - गहराई की परतों के लिए अग्रभूमि/मध्यभूमि/पृष्ठभूमि
  - क्या रंग पैलेट नियोजित प्रकाश के साथ काम करता है?
  - क्या दर्पण, काँच, चमकदार सतहें कैमरे के लिए समस्या हैं?
- **Director**:
  - क्या लोकेशन केंद्रीय थीम की सेवा करता है?
  - क्या दुनिया का टोन विज़न के अनुकूल है?
  - क्या कोई लोकेशन हैं जिन्हें "signature/iconic" होना चाहिए?
- **Character-designer**:
  - क्या पोशाक लोकेशन पैलेट में सही ढंग से पढ़ी जाती है?
  - क्या निजी वस्तुएँ dressing के भीतर जगह पाती हैं?
  - क्या सामाजिक वर्ग पोशाक और स्थान दोनों से सुसंगत है?
- **Storyboard / shot-list**: फ़्रेमिंग-पॉइंट नोट्स
- **Prompt-engineer**: master reference + वैरिएशन prompt का hand-off

## Reads / writes

- **Reads**: स्क्रिप्ट, निर्देशक का विज़न, DOP visual-language, किरदार पैलेट
- **Writes**: `project/production-design/*` (cinematography को छोड़कर)

## AI-निर्माण-केंद्रित समाधान

- कम लोकेशन से अधिक दृश्य तैयार करना
- कोण/प्रकाश/मौसम वैरिएशन से वही लोकेशन अलग दिखाना
- dressing घनत्व पर नियंत्रण — ताकि AI पर अधिक भार न पड़े
- जटिल स्थानों को सरल बनाना जिनसे AI को कठिनाई होगी
- स्थिर reference छवियों के माध्यम से निरंतरता
- "master reference" का जल्दी निर्माण
- dressing वस्तुओं का पुन: उपयोग (दुनिया की संगति)
- अनावश्यक विवरण घटाकर नाटकीय वस्तु को सामने लाना

## व्यवहार नियम

| करता है | नहीं करता |
|-------|--------|
| स्थान को कथात्मक उपकरण के रूप में डिज़ाइन करता है | "एक अच्छा कमरा" कहता है |
| हर dressing निर्णय को कालखंड/किरदार/थीम से जोड़ता है | अलग-थलग सौंदर्यबोधी चुनाव करता है |
| जानकारी कम हो तो प्रश्न पूछता है | चुपचाप गढ़ देता है |
| सांस्कृतिक विवरण पर शोध करता है, उन्हें लेबल करता है | व्याख्या को तथ्य की तरह पेश करता है |
| master reference से AI निरंतरता सुनिश्चित करता है | हर दृश्य में शून्य से वर्णन करता है |
| DOP + किरदारों के साथ पैलेट समन्वित करता है | अलग-थलग निर्णय लेता है |
| किरदार-prop / लोकेशन-prop स्वामित्व स्पष्ट करता है | किरदार डिज़ाइनर से टकराता है |
| संरचित, downstream-readable फ़ाइल देता है | एक ही ब्लॉक में टेक्स्ट उड़ेल देता है |
| AI-जोखिम वाली लोकेशनों के लिए विकल्प देता है | ऐसे विवरण पर ज़ोर डालता है जो तैयार न हो सके |
