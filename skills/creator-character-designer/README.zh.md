# 角色设计师 — `creator-character-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

一个让角色超越**姓名 + 年龄 + 外貌**三要素、将其设计为**完整生命体**的技能。它产出
戏剧功能、心理、传记、肢体语言、服装、道具、选角档案，以及一套 **FACS Action Unit
编码的表情库**。它建立可在长篇 AI 影片制作中保持角色一致性的「Character DNA」锚点。

## 理念

角色不是随机生成的——它源自剧本的需求、导演的愿景和 DOP 的视觉世界。本技能：

- **每个角色都是对某个戏剧问题的回答**——否则便建议删去该角色
- 为每个主要角色强制建立 **Want / Need / Fear / Wound** 四要素
- **FACS Action Units**：与其说「悲伤」，不如说 AU1+AU4+AU15——
  AI 模型和动画师对解剖学编码的解读更为一致
- **Character DNA**：为 AI 一致性定义锁定的锚点特征
- **Visual distinction audit**：当存在多个角色时，审查剪影、色彩与能量上的区分

## 它的用途

| 输出 | 内容 |
|------|------|
| **Character sheet** | 角色档案——心理、服装、道具、FACS、AI prompt |
| **Costume bible** | 整部影片中的服装变体与连续性 |
| **Props list** | 属于角色的个人物品及其戏剧用途 |
| **FACS expression library** | 每个角色 3–5 个标志性表情，以 AU 编码 |
| **Casting brief** | 对演员的要求档案（不提名字，定义特征） |
| **AI prompts** | 用于一致角色参考的 base prompt + 场景变体 |
| **Arc tracker** | 与导演的 arc tracking 协调的角色转变 |
| **Continuity notes** | 逐场的服装/道具连续性 |

## 何时介入

- 剧本在手，需要发展角色
- 「准备一份 character sheet」「设计服装」「拟一份选角档案」
- AI 影片需要一致的角色参考
- 当导演或 `creator-pipeline-supervisor` 委派角色阶段时
- 当现有角色的视觉区分受到质疑时

## 使用 FACS——为何与如何

**面部动作编码系统（Facial Action Coding System，Ekman & Friesen，1978）**是对面部
肌肉的解剖学编码。Action Unit（AU）= 某一特定的肌肉运动。

### 本技能为何使用它？

- **AI 生成器**对「happy face」这类抽象输入的解读不一致；
  「AU6 + AU12（Duchenne smile）」能产出更可靠的结果
- **动画/VFX 团队**借由 AU 编码共享同一套参考
- **角色的标志性表情**可被归档——例如「Demir 以 AU4 + AU17
  （眉头紧锁、下巴抬起、无 AU15）承载他压抑的悲痛」

### 常见的 AU 组合

| 表情 | AU |
|------|----|
| Duchenne smile（真正的快乐） | AU6 + AU12 |
| Polite smile（虚假/社交性） | 仅 AU12 |
| 悲伤 | AU1 + AU4 + AU15 |
| 愤怒 | AU4 + AU5 + AU7 + AU23 |
| 恐惧 | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26 |
| 厌恶 | AU9 + AU15 + AU16 |
| 惊讶 | AU1 + AU2 + AU5B + AU26 |
| 轻蔑（不对称） | AU12（单侧） + AU14 |
| 压抑的悲痛 | AU4 + AU17（无 AU15） |
| 紧绷的平静 | AU7 + AU23 + AU24 |

## Character sheet 模板（摘要）

```
Character: Demir
Role: Protagonist
Want: babasının arşivini bulup yakmak
Need: kendisini babadan ayırmadan da yaşayabileceğini görmek
Fear: babasının tüm kötü yanlarına dönüşmek
Wound: 14 yaşında bir gece babasının onu fark etmemesi
Visual identity: lacivert ağır kumaş palto, traşsız, sol elinin
                 üstünde küçük yanık izi
Signature expressions:
  - Bastırılmış yas: AU4 + AU17 (mutfak sahnesinde kettle önünde)
  - Reddediş: AU14 + AU24 (kuzeniyle konuşma)
  - Saklı acı: AU1 + AU4, gözler kaçıyor (cenaze sonrası)
Continuity anchors: yanık izi, palto, traşsız, ses tonu — sessiz, alçak
AI base prompt: "...same character across all scenes..."
```

## 它把输出写到哪里

写入 `project/characters/{character-slug}/`：

| 文件 | 内容 |
|------|------|
| `character-sheet.md` | 规范的角色档案 |
| `costume-bible.md` | 所有服装变体 + 连续性 |
| `props.md` | 角色的物品、戏剧用途 |
| `facs-expressions.md` | 标志性表情库，以 AU 编码 |
| `casting-brief.md` | 演员档案 / AI 面部 prompt 的基础 |
| `ai-prompts.md` | Base prompt + 逐场变体 |
| `arc-tracker.md` | 与导演的 arc tracking 同步 |
| `continuity-notes.md` | 逐场的服装/道具连续性 |

此外，上级目录中还有 `cast-list.md`——一份汇总所有角色的清单。

## Visual distinction audit

当存在多个角色时，本技能执行以下检查：

- 剪影区分（身高、姿态、服装形态）
- 色彩世界区分（或刻意的对比）
- 能量 register 区分
- 说话方式区分
- 银幕存在感区分（foreground / background 类型）

若两个角色「混淆」在一起，它会报告并建议修订。

## AI 一致性（Character DNA）

为了在 50 个场景中以相同的面孔/服装生成同一角色：

1. **Base prompt**——固定关键特征（脸型、头发、辨识标记）
2. **Anchor descriptors**——其中 2–3 个在每个场景 prompt 中反复出现
3. **以 FACS 表达表情**——使用 AU 编码，而非形容词
4. **尽早产出 character sheet**——front/side/back/close 参考图
5. **在场景 prompt 中引用**：「consistent with `characters/demir/sheet.png`」

## 与其他技能的协调

- **读取**：
  - `project/screenplay/character-brief.md`
  - `project/continuity/creator-director-vision.md`
  - `project/continuity/performance-notes/*`
  - `project/production-design/cinematography/visual-language.md`
  - `project/production-design/world-bible.md`
- **写入**：`project/characters/*`
- **委派给**：Prompt 工程师、storyboard、DOP（调色板协调）
- **接收反馈**：导演、Pipeline Supervisor

## 服装设计方法

服装讲述角色——而不仅仅是「穿什么」：

- 主件 + 其功能
- 面料：厚重、柔软、硬挺、纤维感
- 色彩：与调色板的协调/对比
- 磨损 / 崭新 / 损坏 / 修补痕迹
- 时代准确性
- 与角色心境的关系
- 对行动能力的影响
- 与光的互动（哑光、光泽、透明、易沾灰）

为每个主要场景写一条服装连续性说明：场景内是否变化、场景间是否变化、为何？

## 道具方法

道具是叙事工具——而非装饰：

- 名称 + 功能
- 与角色的关系
- 外观、材质、色彩、状况
- 对角色的意义（纪念物、身份、关系）
- 戏剧用途（伏笔、回收、揭示）
- 摄影机如何看到它（特写、细节、掠过）
- 连续性（每个场景中它在哪里）

明确角色-道具 / 场景-道具的归属，并与 **creator-production-designer** 协调。

## 行为准则

| 会做 | 不会做 |
|------|--------|
| 以戏剧理据生成角色 | 说「再来一个角色」 |
| 将每个视觉选择绑定到 arc / 功能 / 主题 | 做孤立的美学选择 |
| 信息缺失时提问 | 默默编造 |
| 研究文化细节 | 把猜测当作事实呈现 |
| 用 FACS AU 编码定义表情 | 使用「悲伤」这类形容词 |
| 执行 visual distinction audit | 让两个角色混淆 |
| 把 continuity anchor 嵌入 AI prompt | 在每个场景从头描述 |
| 明确角色-道具归属 | 与制作设计师重叠 |
| 交付结构化、downstream-readable 的文件 | 倾倒一整块文字 |
