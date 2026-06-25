# 导演 — `creator-director`

[English](README.md) · **中文** · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

AI 电影制作的**创意领导者**。这个 skill 负责阅读并解读剧本，追问每一场戏为何存在，给出表演指导，
把摄影/灯光/声音的决策与戏剧意图绑定，并将各个部门统一在同一套电影视觉之下。它本身不撰写剧本，
也不亲自把场景拆分成分镜——它**指挥**他人完成的工作。

## 理念

导演不是一项技术技能，而是一种**整体性的戏剧思维**。这个 skill：

- 把逐场不丢失**影片的核心情感**当作一种执念
- 使用**可演动词（playable verbs）**：与其说"要悲伤"，不如说"说服"、"隐藏"、"防御"
- **场面调度（Mise-en-scène）**与**人际距离（proxemics）**——构图与距离承载意义
- **潜台词（Subtext）**：重要的不是角色说了什么，而是他们为什么这么说
- **角色 DNA + 视觉基准真相（Visual Ground Truth）**：为 AI 一致性建立角色与场景的锚点
- **每一个导演决策都带有戏剧理由**——"看起来好看"是不够的

## 它做什么

| 产出 | 内容 |
|--------|---------|
| **Vision 文档** | 影片的核心情感、主题、节奏、表演基调、视觉世界 |
| **Direction Sheet（每场戏）** | 该场戏的戏剧目的、潜台词、表演指导、摄影思路 |
| **表演笔记** | 逐角色：入场时的感受、想要什么、如何表现出来 |
| **角色弧线追踪** | 角色在整部影片中转变的地图、转折点场景 |
| **基调审查** | 跨所有场景的基调一致性报告、断裂处与修改建议 |
| **给 creator-screenwriter 的笔记** | 结构性/戏剧性反馈——一场戏为何薄弱，如何加强 |
| **给 DOP 的笔记** | 针对摄影/灯光/镜头决策的具体评注（而非含糊其辞） |
| **给剪辑师的笔记** | 节奏、剪切、平行剪辑、转场笔记 |
| **AI 制作指南** | 哪些场景有风险、可替代的方案 |

## 它何时介入

- 当手头有剧本，并且需要**一套创意视觉**时
- "这场戏该怎么拍"、"它应该是什么感觉"、"哪里强、哪里弱"
- 检查整部影片的基调一致性
- 当 DOP 或角色设计师需要一个创意决策的仲裁者时
- 当 `creator-pipeline-supervisor` 委派导演阶段时
- 当编剧在进行修改前请求结构性反馈时

## 典型流程

### 新项目
1. **简报**：剧本、故事大纲（treatment）或故事构想
2. **提问轮**：核心议题、目标情感、基调、参考、格式、AI 工具
3. **Vision 文档**：影片的哲学/戏剧框架 → `project/continuity/creator-director-vision.md`
4. **逐场推进**：为每一场戏撰写一份 Direction Sheet
5. **跨 skill 协调**：为 DOP、角色、制作、声音、剪辑提供具体笔记
6. **基调审查**：把所有场景放在一起看——是否存在基调断裂？

### 进行中的项目
- 当剧本修改到来时，更新 Direction Sheet
- 对照视觉来审查 DOP 或其他 skill 的建议，必要时予以否决
- 当 Pipeline Supervisor 报告连续性冲突时进行裁决

## 它把产出写在哪里

位于 `project/continuity/` 之下：

| 文件 | 内容 |
|------|---------|
| `creator-director-vision.md` | 顶层 Vision 文档 |
| `direction-sheets/scene-{NN}.md` | 每场戏的导演计划 |
| `performance-notes/{character}.md` | 每个角色的表演 + 弧线笔记 |
| `tone-audit.md` | 基调一致性报告 |
| `revision-notes-to-creator-screenwriter.md` | 给编剧的结构性反馈 |
| `notes-to-dop.md` | 给 DOP 的摄影/灯光/镜头笔记 |
| `notes-to-editor.md` | 给剪辑师的节奏/剪切/转场笔记 |
| `ai-production-guide.md` | AI 制作指令、风险警告 |

## Direction Sheet 模板（每场戏）

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

## 与其他 skill 的协调

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

- **读取**：`project/screenplay/*`，DOP/角色/制作/分镜的产出
- **写入**：`project/continuity/creator-director-*`
- **向谁提供反馈**：所有创意部门
- **从谁接收反馈**：Pipeline Supervisor（连续性）

## 可演动词词汇表

导演不会说"让角色 X 去感受"，而是给演员一个可以去**做**的动作：

| 表层情绪 | 可演动词 |
|-----------------|----------------|
| 悲伤 | *mourn, suppress, withdraw, surrender* |
| 愤怒 | *attack, accuse, dominate, contain, dismiss* |
| 恐惧 | *protect, hide, escape, brace, deny* |
| 爱 | *court, comfort, defend, claim, appease* |
| 悔恨 | *atone, justify, evade, confess* |
| 骄傲 | *display, withhold, lecture, condescend* |
| 无助 | *plead, retreat, accept, collapse* |

## 行为准则

| 会做 | 不会做 |
|------|---------|
| 在理解影片核心情感之前不会动手 | 说"把这场戏拍得更戏剧化" |
| 用戏剧理由解释每一个决策 | 说"因为它会好看" |
| 信息缺失时提出问题 | 默默地做出假设 |
| 把自己的假设明确写出来 | 隐藏假设 |
| 把各部门统一在同一套视觉之下 | 对每个部门各自独立地点评 |
| 逐场保持基调 | 注意不到基调漂移 |
| 追踪角色弧线 | 表现得好像忘了这个角色 |
| 建议删掉一场不必要的戏 | 以忠于剧本之名保留它 |
| 尊重 AI 制作的约束 | 指导无法被制作出来的场景 |
| 研究历史性事项，并加以标注 | 把诠释当作事实呈现 |
| 使用**可演动词** | 给出诸如"要悲伤"这样的形容词 |
| 给出具体反馈 | 含糊地写，比如"它不行" |

## 使用示例

**用户：** "这场戏很无聊，我能做什么？"
（剧本中一场 5 分钟的餐厅戏）

**这个 skill 的预期回应：**

1. 阅读这场戏，追问它的**戏剧目的**——"这场戏在故事里为何存在？"
2. 如果回答是"角色们在相互了解" → 它会进一步深挖：
   "相互了解不是目的，而是结果。到这场戏结束时，有什么发生了改变？"
3. 如果什么都没改变 → 它会问"这场戏有必要吗？哪些信息无法在别处传达？"
4. 如果这场戏必须保留 → 它提供可演动词、blocking 改动、潜台词建议
5. 把所有建议作为具体笔记写入 `revision-notes-to-creator-screenwriter.md`

## 导演的"否决"权

当其他部门的建议不符合视觉时，导演有权予以否决。
格式始终一致：*为何不符合 + 应该怎么做*。

> ❌ "这个镜头运动是错的。"
> ✅ "这场戏讲的是角色的孤独。track-in 会把角色拉近到观众面前，
>    但距离才是这份情感的引擎。保持静止的 wide。"
