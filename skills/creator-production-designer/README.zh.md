# 美术指导 — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

构建影片**世界**的 skill：场景、布景、道具、时代氛围、色彩与材质语言。它不会
只说"一个美丽的村庄"，而是细化到墙面质感、地面材料、家具密度、影响光线的表面、
磨损痕迹的层面。它建立 master reference，在长篇 AI 影片制作中保持**场景一致性**。

## 理念

空间不是背景，而是一种**叙事工具**。本 skill：

- **先有 World bible** —— 然后是 per-location，再是 per-scene（自上而下）
- **Master reference**：为每个主要场景设定一个锁定的 AI prompt block ——
  这样即使在 50 个镜头之后仍能产出同一栋房子
- **生活痕迹设计**：裂缝、污渍、日晒褪色、磨损、修补痕迹
- **Class-coded design**：每种材质/色彩都在诉说社会阶层
- **Coordinated palette**：与 DOP 的布光和角色服装一起统筹考量
- **Period research**：在需要历史/文化准确性时进行有出处的研究

## 它的作用

| 产出 | 内容 |
|-------|--------|
| **World bible** | 影片的整体世界规则（时代、阶层、建筑、材质） |
| **Color & texture bible** | 色彩调板、材质语言、磨损图样 |
| **Location dossier** | 每个主要场景的完整文档（锁定 + 变体） |
| **Master reference (AI)** | 场景身份的固定 AI prompt block |
| **Props inventory** | 布景物件，连同其戏剧功能 |
| **Per-scene plan** | 逐场景的美术设计（陈设、道具、光源） |
| **Continuity log** | 跨场景的场景一致性检查 |
| **Period research** | 有出处的历史/文化研究 |
| **Notes to DOP / creator-director** | 双向沟通 |

## 何时介入

- 剧本到手，需要世界 / 场景 / 布景设计
- "这个空间应该是什么样"、"set dressing"、"道具清单"
- 用于 AI 制作的一致性场景参考
- 时代研究（历史、文化、地域）
- 当 `creator-pipeline-supervisor` 委派美术设计阶段时

## 典型流程

1. **简报** + 阅读 `creator-director-vision.md` + DOP visual-language
2. **提问环节**：时代、地理、基调、阶层、AI 工具
3. **World bible**：影片的整体世界规则
4. **Color & texture bible**：材质与色彩语言
5. **Major locations**：为每个主要场景编写 dossier
6. **Master references**：用于 AI 一致性的锁定 prompt block
7. **Per-scene sheets**：逐场景的 set dressing + 道具笔记
8. **Continuity audit**：同一场景在不同镜头中是否一致？

## 产出写入何处

写入 `project/production-design/` 之下（不含 cinematography —— 那是 DOP 的）：

| 文件 | 内容 |
|-------|--------|
| `world-bible.md` | 影片的世界规则 |
| `color-texture-bible.md` | 色彩 + 材质语言 |
| `locations/{slug}/location-doc.md` | Per-location dossier |
| `locations/{slug}/master-reference.md` | 锁定的 AI base prompt |
| `props/{slug}.md` 或 `props-list.md` | 道具清单 |
| `scenes/scene-{NN}.md` | 逐场景的美术设计方案 |
| `continuity-notes.md` | 场景一致性检查日志 |
| `period-research.md` | 有出处的时代研究 |
| `notes-to-creator-director.md` | 向导演提出的问题/建议 |
| `notes-to-creator-cinematographer.md` | 与 DOP 的表面/纵深/光线协调 |

## Location dossier 模板（摘要）

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

## Master reference（用于 AI 一致性）

为每个主要场景写一个**锁定的 base prompt block**：

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

该 block 在所有场景 prompt 中原样重复，并在其上叠加场景特定的变体。

## 与其他 skill 的协调

- **Cinematographer**：
  - 表面与光线的关系（matte、glossy、transparent）
  - 用于纵深分层的前景/中景/背景
  - 色彩调板是否与计划的布光配合？
  - 镜子、玻璃、光亮表面对摄影机是否构成问题？
- **Director**：
  - 场景是否服务于核心主题？
  - 世界基调是否契合愿景？
  - 是否有必须"signature/iconic"的场景？
- **Character-designer**：
  - 服装在场景调板中是否读得正确？
  - 个人物品在陈设中是否找到位置？
  - 社会阶层在服装和空间两方面是否一致？
- **Storyboard / shot-list**：取景点笔记
- **Prompt-engineer**：master reference + 变体 prompt 的交接

## Reads / writes

- **Reads**：剧本、导演愿景、DOP visual-language、角色调板
- **Writes**：`project/production-design/*`（不含 cinematography）

## 面向 AI 制作的解决方案

- 用少量场景产出多个镜头
- 通过角度/光线/天气变体让同一场景呈现不同面貌
- 控制陈设密度 —— 让 AI 不至过载
- 简化 AI 难以处理的复杂空间
- 通过固定参考图保持一致性
- 尽早产出 "master reference"
- 复用陈设物件（世界的整体性）
- 减少不必要的细节，让戏剧物件凸显出来

## 行为准则

| 会做 | 不会做 |
|-------|--------|
| 把空间设计成叙事工具 | 说"一个不错的房间" |
| 把每个陈设决策绑定到时代/角色/主题 | 做孤立的美学选择 |
| 信息缺失时提问 | 默不作声地编造 |
| 对文化细节进行研究并标注 | 把解读当作事实呈现 |
| 通过 master reference 保证 AI 一致性 | 每个镜头都从零描述 |
| 与 DOP + 角色协调调板 | 孤立地做决定 |
| 厘清角色道具 / 场景道具的归属 | 与角色设计师产生冲突 |
| 交付结构化、downstream-readable 的文件 | 倾倒一整块文字 |
| 为 AI 风险场景提供替代方案 | 强求无法产出的细节 |
