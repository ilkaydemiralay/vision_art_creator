# vision_art_creator

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · **हिन्दी** · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

> [Claude Code](https://claude.com/claude-code) के लिए एक AI फ़िल्म‑प्रोडक्शन स्किल पैक।

`vision_art_creator` में **11 `creator-*` स्किल्स** शामिल हैं, जो एक ही
रिपॉज़िटरी में किसी फ़िल्म प्रोडक्शन के हर विभाग को कवर करती हैं — पटकथा से
लेकर फ़ाइनल कट तक। इसे `git clone` + `./install.sh` के ज़रिए किसी भी मशीन पर
इंस्टॉल करें।

> ये स्किल्स इस तरह डिज़ाइन की गई हैं कि वे एक‑दूसरे का संदर्भ लें
> (`creator-pipeline-supervisor` बाकी सबका संचालन करती है)। इन्हें एक साथ
> इंस्टॉल करने की सलाह दी जाती है।

---

## इंस्टॉलेशन

```bash
git clone https://github.com/<your-username>/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

`install.sh` प्रत्येक स्किल के लिए `~/.claude/skills/<skill-name>` के अंतर्गत
एक **symlink** बनाती है, जो वापस इसी रिपो की ओर इशारा करता है। इसका फ़ायदा:
अपडेट करने के लिए केवल `git pull` ही काफ़ी है — दोबारा इंस्टॉल करने की ज़रूरत
नहीं।

### विकल्प

```bash
./install.sh --target /path/to/skills   # किसी अलग skills dir में इंस्टॉल करें
./install.sh --force                    # मौजूदा नामों को ओवरराइट करें
./uninstall.sh                          # symlinks हटाएँ
```

`uninstall.sh` केवल उन्हीं symlinks को हटाती है जो इस रिपो की ओर इशारा करते
हैं — यह बाहरी लिंक और असली डायरेक्ट्रीज़ को छेड़ती नहीं (जब तक `--force` न
दिया जाए)।

### सत्यापन

इंस्टॉल करने के बाद, Claude Code को दोबारा शुरू करें और टाइप करें:

```
/creator-pipeline-supervisor
```

जाँचें कि स्किल सूची में सभी 11 `creator-*` स्किल्स दिखाई दे रही हैं।

---

## पैक में क्या है

| स्किल | सारांश |
|---|---|
| `creator-pipeline-supervisor` | पूरे प्रोडक्शन का संचालन करती है, विभागों को क्रमबद्ध करती है, निरंतरता लागू करती है, QC चलाती है, और डिलीवरी‑रेडीनेस रिपोर्ट तैयार करती है। |
| `creator-director` | पटकथा को एक एकीकृत निर्देशकीय दृष्टि में बदलती है: दृश्य निर्देशन, अभिनय, ब्लॉकिंग, टोनल नियंत्रण। |
| `creator-screenwriter` | पटकथाएँ, ट्रीटमेंट, logline, दृश्य रूपरेखाएँ और संवाद लिखना और संशोधित करना। |
| `creator-character-designer` | पात्र को एक समग्र इकाई के रूप में गढ़ती है: मनोविज्ञान, जीवनी, दृश्य पहचान, वेशभूषा, props, FACS‑कोडित भाव। |
| `creator-production-designer` | फ़िल्म की दुनिया रचती है: लोकेशन, सेट, props, कालखंड का वातावरण, रंग/सामग्री की भाषा, निरंतरता के एंकर। |
| `creator-cinematographer` | दृश्य भाषा डिज़ाइन करती है: प्रकाश, कैमरा, lens, framing, रंग, वातावरण, गति। |
| `creator-storyboard-artist` | दृश्यों को पैनल‑दर‑पैनल दर्शाती है: shot scales, कोण, ब्लॉकिंग, संरचना, AI prompts। |
| `creator-shot-list-designer` | दृश्यों और storyboard को एक तकनीकी shot list में बदलती है, जिसे AI‑उत्पादन योग्य खंडों में विभाजित किया जाता है। |
| `creator-sound-music-designer` | फ़िल्म की ध्वनि‑दुनिया: वातावरण, foley, SFX, score, leitmotif, दृश्य‑दर‑दृश्य संगीत योजना, AI audio prompts। |
| `creator-prompt-engineer` | हर विभाग के आउटपुट को GPT Image 2.0, Nano Banana, Sora, Veo, Runway, Kling, Higgsfield और अन्य के लिए सुसंगत prompts में बदलती है। |
| `creator-final-cut-editor` | AI‑जनित shots/audio/music/graphics को एक तैयार फ़िल्म में जोड़ती है: rough/fine/final cut, AI‑त्रुटि triage, डिलीवरी फ़ॉर्मेट। |

प्रत्येक स्किल की पूरी परिभाषा उसकी अपनी `SKILL.md` फ़ाइल में रहती है।

---

## यह कैसे काम करता है

यह पैक **filesystem‑आधारित साझा स्थिति (shared state)** पर चलता है। सभी स्किल्स
एक साझा `project/` ट्री (`bible/`, `screenplay/`, `characters/`,
`storyboards/`, `prompts/`, `cuts/`, `qc/`, …) से पढ़ती और उसमें लिखती हैं।
`creator-pipeline-supervisor` canonical फ़ाइलें (project व continuity "bibles")
बनाए रखती है और प्रत्येक विभाग के आउटपुट का उनके विरुद्ध ऑडिट करती है।

canonical पाइपलाइन:

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

यह क्रम canonical है पर कठोर नहीं: निर्देशक की प्रतिक्रिया screenwriter को
फिर से सक्रिय कर सकती है, और निर्देशकीय दृष्टि तय हो जाने के बाद आमतौर पर
character/production/cinematography समानांतर रूप से चलते हैं।

---

## अपडेट करना

```bash
cd ~/projects/vision_art_creator
git pull
```

चूँकि स्किल्स symlink की गई हैं, इसलिए किसी अतिरिक्त चरण की ज़रूरत नहीं।

---

## विकास

1. रिपो में किसी स्किल को संपादित करें (`skills/creator-*/SKILL.md`)।
2. बदलाव को Claude Code में परखें — चूँकि यह एक symlink है, यह तुरंत प्रभावी
   हो जाता है।
3. Commit + push करें।

एक नई creator स्किल जोड़ने के लिए:

```bash
mkdir -p skills/creator-new-skill
# write SKILL.md and README.md
./install.sh   # create the symlink for the new skill
```

---

## अनुवाद

यह README और प्रत्येक स्किल की `README.md` 12 भाषाओं में उपलब्ध है (शीर्ष पर
भाषा चयनकर्ता देखें)। `SKILL.md` निर्देश फ़ाइलें जानबूझकर अंग्रेज़ी में रखी
गई हैं — Claude रनटाइम पर उपयोगकर्ता की भाषा में उत्तर देता है, और एक ही
canonical निर्देश‑समूह डुप्लिकेट स्किल नामों से बचाता है।

---

## लाइसेंस

[MIT](LICENSE) © 2026 İlkay Demiralay.
