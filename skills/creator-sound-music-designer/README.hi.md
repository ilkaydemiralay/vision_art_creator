# साउंड और म्यूज़िक डिज़ाइनर — `creator-sound-music-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [**हिन्दी**](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

वह skill जो फ़िल्म की **संवेदी दुनिया** का निर्माण करती है। दो एकीकृत विधाएँ यहाँ एक साथ आती हैं:
- **साउंड डिज़ाइनर**: स्थानों, किरदारों, वस्तुओं और घटनाओं की संवेदी वास्तविकता — ambience, foley, इफ़ेक्ट्स, ध्वनिकी, ध्वनि का परिप्रेक्ष्य, और **मौन** (एक सक्रिय नाटकीय उपकरण के रूप में)
- **फ़िल्म कंपोज़र / म्यूज़िक सुपरवाइज़र**: मुख्य थीम, किरदार के leitmotif, सीन का संगीत, लय, संगीत के प्रवेश/निकास बिंदु

## दर्शन
ध्वनि और संगीत **सजावट नहीं** हैं। हर ध्वनि और संगीत संबंधी निर्णय सीन के नाटकीय उद्देश्य, किरदार के मनोविज्ञान, दृश्य वातावरण, edit की लय और दर्शकों पर पड़ने वाले प्रभाव से जुड़ा होता है। यह skill:
- "उदास संगीत डालो" नहीं कहती — यह leitmotif डिज़ाइन करती है और उनके विकास की योजना बनाती है
- **मौन को सक्रिय रूप से डिज़ाइन करती है** — अनुपस्थिति नहीं, बल्कि एक नाटकीय निर्णय
- **किरदार के leitmotif**: एक मोटिफ़ जो बाँसुरी पर शुरू होता है, finale में strings के साथ एक epic में बदल जाता है
- **कॉपीराइट-अनुशासित**: जीवित कलाकारों की नकल नहीं करती, "समान पर एक जैसा नहीं"
- **edit की लय के साथ तालमेल में**: संगीत का प्रवेश/निकास shot-list edit योजना के साथ समन्वित
- **AI ध्वनि/संगीत प्रॉम्प्ट निर्माण**: Suno, Udio, ElevenLabs SFX, Stable Audio, Runway Audio

## यह क्या करती है
| आउटपुट | सामग्री |
|-------|--------|
| **साउंड विज़न** | फ़िल्म का समग्र sound-design विज़न |
| **म्यूज़िक विज़न** | फ़िल्म का संगीत-भाषा घोषणापत्र |
| **मुख्य थीम** | मुख्य थीम का डिज़ाइन |
| **किरदार थीम** | प्रति-किरदार leitmotif डिज़ाइन |
| **सीन योजनाएँ** | सीन-दर-सीन ध्वनि + संगीत योजना |
| **Ambience / foley / SFX सूचियाँ** | इन्वेंट्री सूचियाँ |
| **मौन योजना** | मौन का एक सोच-समझकर बनाया गया नक्शा |
| **संगीत प्रवेश/निकास योजना** | संगीत के प्रवेश और निकास बिंदु |
| **साउंड ब्रिज** | ट्रांज़िशन डिज़ाइन |
| **AI ध्वनि + संगीत प्रॉम्प्ट** | टूल-विशिष्ट प्रॉम्प्ट |
| **संवाद संतुलन नोट्स** | संवाद/संगीत संतुलन नोट्स |
| **अंतिम mix नोट्स** | अंतिम mix ऑडिट |
| **निरंतरता रिपोर्ट** | ध्वनि निरंतरता जाँच |

## यह कब सक्रिय होती है
- एक स्क्रिप्ट हाथ में है, और एक sound-design / फ़िल्म-संगीत योजना की ज़रूरत है
- Ambience, foley, SFX, या संगीत थीम का अनुरोध किया गया है
- AI ध्वनि/संगीत प्रॉम्प्ट की ज़रूरत है
- जब shot-list डिज़ाइनर सीन की ध्वनि-मंशा सौंपता है
- जब `creator-pipeline-supervisor` ऑडियो चरण को सौंपता है

## विशिष्ट प्रवाह
1. **ब्रीफ़िंग** + सभी upstream skill आउटपुट पढ़ना
2. **प्रश्न दौर**: genre, register, संगीत घनत्व, कालखंड, AI टूल
3. **साउंड विज़न** + **म्यूज़िक विज़न**
4. **मुख्य थीम + किरदार leitmotif**
5. **प्रति-सीन योजना**: हर सीन के लिए ambient/foley/मौन/संगीत
6. **मौन योजना**: सोच-समझकर बनाया गया मौन का नक्शा
7. **संगीत प्रवेश/निकास योजना**
8. **AI ध्वनि + संगीत प्रॉम्प्ट**
9. **अंतिम mix ऑडिट** (final cut के बाद)

## मौन का डिज़ाइन
मौन एक **सक्रिय** डिज़ाइन निर्णय है। प्रत्येक मौन के लिए, यह skill पूछती है:
- क्या यहाँ संगीत बंद हो जाएगा?
- क्या ambience को मद्धम किया गया है, या शून्य कर दिया गया है?
- क्या केवल एक साँस बची रहेगी, या किसी छोटी वस्तु की आवाज़?
- क्या यह मौन अकेलापन, भय, या झिझक व्यक्त करता है?
- क्या यह दर्शकों को असहज करने के लिए है, या भावना को तीव्र करने के लिए?
- मौन के बाद कौन-सी ध्वनि प्रवेश करती है?

## किरदार leitmotif उदाहरण
```
Karakter: Demir
Müzikal duygu: bastırılmış yas + içsel kararlılık
Ana enstrüman: solo cello (başlangıç) → cello + ney (orta) → cello + yaylı
                grup (final)
Tempo: 60–66 BPM (slow heart)
Ton: minör, kromatik geçişler
Ritim: rubato, neredeyse zamansız
Motifin evrimi:
  - Sahne 1–5: solo cello, kısa 5-notalı motif, sessizlik aralıkları geniş
  - Sahne 6–12: ney ekleniyor — nefes katmanı
  - Sahne 13–18: yaylı grup açılıyor — toplum, geçmiş, anlam
  - Sahne 19 (final): tek cello, ilk motifin yarısı — kırılma
```

## यह अपने आउटपुट कहाँ लिखती है
`project/sound/` के अंतर्गत:
| फ़ाइल | सामग्री |
|-------|--------|
| `sound-vision.md` | समग्र sound-design विज़न |
| `music-vision.md` | संगीत-भाषा घोषणापत्र |
| `main-theme.md` | मुख्य थीम का डिज़ाइन |
| `character-themes/{slug}.md` | किरदार leitmotif |
| `scenes/scene-{NN}.md` | सीन ध्वनि + संगीत योजना |
| `ambience-list.md` | Ambience इन्वेंट्री |
| `foley-list.md` | Foley इन्वेंट्री |
| `special-effects-list.md` | विशेष SFX |
| `silence-plan.md` | मौन का नक्शा |
| `music-entry-exit-plan.md` | संगीत प्रवेश/निकास timing |
| `sound-bridges.md` | ट्रांज़िशन डिज़ाइन |
| `ai-sound-prompts.md` | AI SFX प्रॉम्प्ट |
| `ai-music-prompts.md` | AI संगीत प्रॉम्प्ट |
| `dialogue-balance-notes.md` | संवाद/संगीत संतुलन |
| `final-mix-notes.md` | अंतिम mix ऑडिट |
| `sound-continuity-report.md` | निरंतरता जाँच |

## AI प्रॉम्प्ट प्रारूप
### SFX प्रॉम्प्ट उदाहरण
```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```
### संगीत प्रॉम्प्ट उदाहरण
```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```
### मूल-भाषा विवरण + अंग्रेज़ी प्रॉम्प्ट प्रारूप
```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## कॉपीराइट और मौलिकता
- मौजूदा रचनाओं की नकल का सुझाव नहीं देती
- किसी जीवित कलाकार की शैली की नोट-दर-नोट नकल नहीं करती
- "समान पर एक जैसा नहीं" तर्क पर काम करती है, genre + भावना का वर्णन करते हुए
- AI संगीत प्रॉम्प्ट में, किसी कलाकार के नाम के बजाय सामान्य वातावरण का उपयोग करती है

## अन्य skills के साथ समन्वय
- **पढ़ती है**: सभी upstream रचनात्मक आउटपुट + shot-list ध्वनि edit नोट्स
- **लिखती है**: `project/sound/*`
- **सौंपती है**: `creator-final-cut-editor` (final cut एकीकरण), AI ऑडियो टूल संचालक को
- **फ़ीडबैक प्राप्त करती है**: डायरेक्टर, Pipeline Supervisor, Final-cut-editor से

## व्यवहार संबंधी नियम
| करती है | नहीं करती |
|-------|--------|
| ध्वनि और संगीत को नाटकीय उद्देश्य से जोड़ती है | उन्हें सजावट के रूप में उपयोग करती है |
| मौन को सक्रिय रूप से डिज़ाइन करती है | उसे अनुपस्थिति मानती है |
| leitmotif के विकास को किरदार के arc के साथ सिंक करती है | एक स्थिर थीम को दोहराती है |
| संवाद/संगीत/ambience/मौन को एक साथ सोचती है | अलग-थलग होकर निर्णय लेती है |
| कॉपीराइट-अनुशासित | कलाकारों की नकल करती है |
| ऐतिहासिक/सांस्कृतिक शोध करती है और उसे लेबल करती है | व्याख्या को तथ्य के रूप में प्रस्तुत करती है |
| टूल-अनुकूल AI प्रॉम्प्ट लिखती है | सामान्य प्रॉम्प्ट उड़ेल देती है |
| एक लंबी फ़िल्म के लिए ध्वनि निरंतरता बनाए रखती है | सीन-दर-सीन और बिखरा हुआ सोचती है |
