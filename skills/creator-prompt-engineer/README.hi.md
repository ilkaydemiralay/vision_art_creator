# प्रॉम्प्ट इंजीनियर — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · **हिन्दी** · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

रचनात्मक पाइपलाइन और AI जनरेटरों के बीच का **अनुवाद-स्तर (translation layer)**।
यह पटकथा-लेखक, निर्देशक, DOP, चरित्र, प्रोडक्शन, स्टोरीबोर्ड और शॉट-लिस्ट स्किल्स
द्वारा लिए गए निर्णयों को **वास्तव में उत्पादन-योग्य और सुसंगत** प्रॉम्प्ट में बदलता है।
यह हर टूल के लिए अलग से अनुकूलन करता है (Midjourney ≠ Sora ≠ Stable Diffusion),
locked anchors को हर प्रॉम्प्ट में जड़ देता है, और जोखिमपूर्ण दृश्यों के लिए सुरक्षित
विकल्प तैयार करता है।

## दर्शन

प्रॉम्प्ट इंजीनियर **दृश्य का आविष्कार नहीं करता** — वह upstream के निर्णयों को
encode करता है। यह स्किल:

- **Locked anchors**: character DNA + location master reference + style block —
  50 प्रॉम्प्ट के बाद भी वही चरित्र वही चेहरा लेकर सामने आता है
- **Tool fitness**: हर AI टूल की अपनी प्रॉम्प्ट-भाषा होती है
- **Producibility audit**: यह दृश्य जनरेटर को हरा देगा — कोई विकल्प सुझाओ
- **Consistency discipline**: लंबी फ़िल्म के लिए प्रॉम्प्ट एक प्रणाली हैं, अलग-थलग नहीं
- **FACS expression coding**: «उदास» के बजाय AU1 + AU4 + AU15 — अधिक सुसंगत परिणाम
- **upstream को कभी चुपचाप नहीं बदलता**: ज़रूरत होने पर flag करता है और वापस पूछता है

## यह किस काम आता है

| आउटपुट | सामग्री |
|--------|---------|
| **Character prompts** | Locked DNA + दृश्य-दर-दृश्य भिन्नता |
| **Location prompts** | Master reference + दिन/रात/मौसम की भिन्नता |
| **Style anchors** | पूरी फ़िल्म का दृश्य/तकनीकी ब्लॉक |
| **Negative prompts** | श्रेणी-आधारित नेगेटिव प्रॉम्प्ट बैंक |
| **Panel prompts** | स्टोरीबोर्ड पैनल से छवि-उत्पादन प्रॉम्प्ट |
| **Shot prompts** | शॉट-लिस्ट से AI वीडियो उत्पादन प्रॉम्प्ट |
| **Character sheets** | Front/side/back/close संदर्भ-उत्पादन |
| **Producibility risk report** | दृश्य/शॉट स्तर पर जोखिम + सुरक्षित विकल्प |
| **Tool guide** | ऑपरेटर के लिए टूल-विशिष्ट नोट्स |

## यह कब सक्रिय होता है

- उत्पादन से पहले AI image/video प्रॉम्प्ट की ज़रूरत हो
- चरित्र/स्थान की निरंतरता के लिए anchor प्रणाली बनानी हो
- स्टोरीबोर्ड या शॉट-लिस्ट आउटपुट को टूल प्रॉम्प्ट में बदलना हो
- मौजूदा प्रॉम्प्ट जोखिमपूर्ण है — सुरक्षित विकल्प चाहिए
- जब `creator-pipeline-supervisor` प्रॉम्प्ट चरण सौंपता है

## टूल अनुकूलन मार्गदर्शिका (सारांश)

### Midjourney
- `--ar`, `--style raw`, `--s` पैरामीटर
- चरित्र संदर्भ के लिए `--cref` और `--cw`
- शैली संदर्भ के लिए `--sref`
- संक्षिप्त लेखन — विशेषणों का ढेर संकेत को कमज़ोर करता है

### DALL·E
- स्वाभाविक भाषा > टैग-ढेर
- स्थानिक संबंध स्पष्ट लिखें
- छवि के भीतर टेक्स्ट बनाने से बचें

### Stable Diffusion (SDXL / SD3)
- Positive + negative अलग
- चरित्र की निरंतरता के लिए LoRA / reference / seed नोट्स
- महत्वपूर्ण शब्द शुरुआत में (token weight)

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- एकल मुख्य कैमरा-गति
- नियंत्रित चरित्र-संख्या
- स्पष्ट opening + closing frame
- अवधि छोटी (आमतौर पर 3–10s)
- टूल-विशिष्ट सीमाएँ:
  - Sora 2: ~20s
  - Kling 3.0: निरंतरता के लिए subject binding
  - Veo: motion fidelity मज़बूत
  - Runway Gen-3/4: गति तर्कसंगत, lip sync कमज़ोर

## Locked anchor प्रणाली (लंबी फ़िल्म के लिए)

### Character DNA block

`project/characters/{slug}/ai-prompts.md` से **हू-ब-हू** कॉपी किया जाता है:

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

`project/production-design/locations/{slug}/master-reference.md` से हू-ब-हू:

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

ये ब्लॉक उस दृश्य/चरित्र/स्थान के **हर प्रॉम्प्ट में हू-ब-हू दोहराए जाते हैं**।
यही अनुशासन निरंतरता का इंजन है।

## नेगेटिव प्रॉम्प्ट श्रेणियाँ

| समस्या | नेगेटिव शब्द |
|--------|--------------|
| चेहरे की विकृति | distorted face, malformed face, asymmetric eyes, blurred features |
| हाथ की त्रुटि | extra fingers, missing fingers, fused fingers, deformed hand |
| कालविरोध | modern clothes, modern tech, plastic, neon, smartphone |
| AI artifact | warping, morphing, flickering, jittery motion |
| गुणवत्ता | low quality, low resolution, jpeg artifacts, oversaturated |
| टेक्स्ट | unwanted text, watermark, signature, logo |
| संयोजन | extra characters, cropped subject, duplicate subject |
| कैमरा | unintended shake, fisheye distortion |

कुछ टूल नेगेटिव प्रॉम्प्ट को अनदेखा कर देते हैं — ऐसे में उसे positive prompt
के भीतर *"avoid: ..."* संकेत के रूप में लिखें।

## AI वीडियो producibility ऑडिट

वीडियो प्रॉम्प्ट जारी करने से पहले जाँच:

- क्या एक ही शॉट में बहुत अधिक एक्शन है?
- क्या चरित्रों की संख्या ज़्यादा है?
- क्या कैमरा-गति जटिल है?
- क्या हाथ/उंगली/चेहरे की डिटेल जोखिमपूर्ण है?
- क्या वेशभूषा/प्रॉप की निरंतरता बनी रह सकती है?
- क्या स्थान बहुत भीड़भाड़ वाला है?
- क्या प्रकाश और समय सुसंगत हैं?
- क्या दृश्य को एकल प्रॉम्प्ट के बजाय हिस्सों में बाँटना चाहिए?
- क्या lip sync ज़रूरी है? (flag करें)
- क्या प्रॉम्प्ट अनावश्यक रूप से अमूर्त है?

जोखिम होने पर यह एक **सुरक्षित, सरलीकृत विकल्प** देता है।

## भिन्नता उत्पादन

एक ही दृश्य के लिए केंद्रित भिन्नताएँ:

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

हर भिन्नता का **उद्देश्य लिखा जाता है** — क्यों और किस स्थिति में उपयोग करें।

## यह अपने आउटपुट कहाँ लिखता है

`project/prompts/` के अंतर्गत:

| फ़ाइल | सामग्री |
|------|---------|
| `character-prompts/{slug}.md` | Locked DNA + दृश्य-भिन्नताएँ |
| `location-prompts/{slug}.md` | Master anchor + भिन्नताएँ |
| `style-anchors.md` | पूरी फ़िल्म के style block(s) |
| `negative-prompts.md` | नेगेटिव प्रॉम्प्ट बैंक |
| `scene-{NN}/panel-{PP}.md` | पैनल इमेज प्रॉम्प्ट |
| `scene-{NN}/shot-{SS}.md` | शॉट वीडियो प्रॉम्प्ट |
| `character-sheets/{slug}.md` | Front/side/back/close sheet उत्पादन प्रॉम्प्ट |
| `prompt-system.md` | Anchor प्रणाली दस्तावेज़ीकरण |
| `producibility-risk-report.md` | जोखिम flags + सुरक्षित विकल्प |
| `tool-guide.md` | टूल-विशिष्ट ऑपरेटर नोट्स |

## द्विभाषी प्रॉम्प्ट प्रारूप

जब उपयोगकर्ता मातृभाषा में विवरण + अंग्रेज़ी प्रॉम्प्ट चाहता है:

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

## अन्य स्किल्स के साथ समन्वय

- **पढ़ता है**: सभी upstream रचनात्मक आउटपुट
- **लिखता है**: `project/prompts/*`
- **सौंपता है**:
  - उस मानव ऑपरेटर को जो AI टूल चलाएगा
  - यदि producibility ऑडिट के लिए upstream बदलना ज़रूरी हो तो **storyboard
    artist** या **shot-list designer** को फ़ीडबैक
- **फ़ीडबैक प्राप्त करता है**: Pipeline Supervisor (असंगति का drift)

## व्यवहार नियम

| करता है | नहीं करता |
|---------|-----------|
| मल्टी-शॉट काम में locked anchors हर प्रॉम्प्ट में डालता है | हर बार शून्य से वर्णन करता है |
| टूल-अनुकूल प्रॉम्प्ट लिखता है | वही प्रॉम्प्ट हर टूल को देता है |
| Producibility ऑडिट + सुरक्षित विकल्प | जोखिम को चुपचाप टाल देता है |
| FACS AU कोड का उपयोग करता है | «उदास» जैसे विशेषण ढेर करता है |
| विशेषणों की भरमार घटाता है | भारी-भरकम शब्दों से भरता है |
| upstream निर्णय बनाए रखता है, चुपचाप नहीं बदलता | रचनात्मक आविष्कार जोड़ता है |
| ऐतिहासिक काल-शोध का सम्मान करता है | कालविरोध छोड़ देता है |
| संरचित, downstream-पठनीय आउटपुट | एकल-ब्लॉक प्रॉम्प्ट उड़ेल देता है |
| मातृभाषा विवरण + अंग्रेज़ी प्रॉम्प्ट प्रारूप (माँगे जाने पर) | हमेशा अंग्रेज़ी थोपता है |
