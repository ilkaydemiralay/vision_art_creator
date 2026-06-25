# 编剧 — `creator-screenwriter`

[English](README.md) · **中文** · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

面向 AI 影视制作的专业剧本开发专家。它不只是一个"生成文字"的工具，而是一位将 **故事、结构、人物、节奏与主题** 一并考量的创意写作助手。它把名家编剧的方法（Sorkin 的对白节奏、Nolan 的结构递归、Tarantino 的语调掌控、Save the Cat! 节拍结构、Field 的三幕范式）**当作工具而非模板** 来运用。

## 理念

写剧本不同于产生创意——它意味着把创意转化为可制作的、戏剧化的场景。本技能：

- **先理解意图**，再下笔
- **提出问题**，而非臆测
- 用戏剧性的理由 **解释每一场戏为何存在**
- 认真对待 **show, don't tell** 原则
- **潜台词 > 台词**——人物极少直说自己的真实感受
- 运用 **有节制的创造力**——忠于用户自己的声音
- 尊重 AI 影视制作的限制（人群、快速动作等）

## 它能做什么

| 产出类型 | 用途 |
|------------|----------|
| **Logline** | 一句话概括故事内核，用于 pitch |
| **故事梗概（Synopsis）** | 1 页，主线剧情并预示结局 |
| **Treatment** | 3–10 页散文体，逐场推进 |
| **Outline** | 基于节拍的结构清单（每场戏的戏剧目的） |
| **人物简介** | Want / Need / Fear / Arc——与角色设计师协同 |
| **场景文本** | 行业标准剧本格式的完整场景 |
| **完整剧本** | 版本受控的 `script-v1.md`、`script-v2.md` …… |
| **对白修订** | 强化既有对白的建议 |
| **结构分析** | 找出现有剧本中的薄弱环节 |
| **格式改编** | 转换为广告、社交媒体、YouTube、纪录片格式 |

## 何时触发

本技能在以下信号下被触发：

- "写个剧本"、"开发一个故事"、"我们来搭一场戏"
- "提炼 logline"、"写故事梗概"、"准备 treatment"
- "强化这场戏"、"修改对白"
- "准备人物简介"、"want/need/fear 分析"
- "我有个点子，能拍成电影吗？"——结构性评估
- 当 `creator-pipeline-supervisor` 委派剧本阶段时

## 典型流程

1. **任务说明**：用户带来一个想法或请求
2. **提问环节**：格式、类型、语调、目标受众、核心冲突、人物、年代、AI 制作工具
3. **方案提议**：对缺失信息作出合理假设（明确标注）
4. **骨架**：Logline → 故事梗概 → outline（节拍表）的顺序
5. **场景文本**：依据已批准的 outline 逐场写作
6. **修订**：整合导演的反馈，生成新版本

如果用户想要快速结果，它会 **明确** 说明所作的假设，并附上类似这样的备注：

> *"10 分钟短片，单一主角弧线，写实语调——请确认或更正。"*

## 产出写入何处

所有产出都写入 `project/screenplay/` 之下：

| 文件 | 内容 |
|-------|--------|
| `logline.md` | 一句话故事概要 |
| `synopsis.md` | 一页篇幅的完整剧情概要 |
| `treatment.md` | 3–10 页散文体 treatment |
| `character-brief.md` | 人物简介（交接给角色设计师） |
| `outline.md` | 基于节拍的场景清单，每场戏的戏剧目的 |
| `script-v{N}.md` | 行业标准剧本（每次修订一个新文件） |
| `revision-notes.md` | 版本之间变更的理由 |

版本命名：从不覆盖。按 `v1` → `v2` → `v3` 推进。每次变更的理由以 **commit message** 的方式在 `revision-notes.md` 中概述。

## 行业标准剧本格式

```
INT. KITCHEN - NIGHT

A worn brass kettle whistles. ELIF (40s, exhausted but composed)
stares at it without moving.

DEMIR (O.S.)
                Elif?

She turns off the burner. The whistle dies.

                              ELIF
                  (quiet)
                  I'm coming.
```

- **Slugline**：`INT./EXT. LOCATION - TIME`
- **Action**：现在时、视觉化、第三人称，至多 4 行
- **人物名**：全大写、居中、首次出场时
- **对白**：在人物名下方居中
- **括注**：仅在必要时，小写
- **1 页 ≈ 1 分钟** 银幕时间

对于社交媒体 / YouTube / 广告 / 纪录片，格式会适配目标媒介，但纪律保持不变。

## 与其他技能的协同

```
creator-screenwriter
    │ writes: project/screenplay/*
    ▼
creator-director ◄─────► creator-screenwriter
    │ vision approval + structural notes
    ▼
creator-character-designer + creator-production-designer + creator-cinematographer
```

- **读取**：
  - `project/characters/*` —— 角色设计师的产出（若有）
  - `project/continuity/creator-director-vision.md` —— 若导演已设定视觉构想
  - `project/continuity/revision-notes-to-creator-screenwriter.md` —— 来自导演的备注
- **写入**：`project/screenplay/*`
- **交接给**：
  1. **导演**（视觉构想 + 结构把控）
  2. 之后是角色、美术、摄影指导（DOP）、storyboard
- **接收反馈**：导演、Pipeline Supervisor（连续性冲突）

当导演要求修订时，它 **不会悄悄覆盖**——而是创建新的 `script-v{N+1}.md`，并把理由记入 `revision-notes.md`。

## Master creator-screenwriter 模块

如果用户想要某种特定的声音，它会启用其一并明确说明：

- **Sorkin**：快速、交叠的对白；walk-and-talk；人物大声思考
- **Nolan**：结构递归、嵌套时间线、以信息顺序作为驱动
- **Tarantino**：延宕动作的冗长对白；类型碰撞
- **Coen**：语调转折，命运 vs. 选择
- **Save the Cat!**：15 节拍结构
- **Field 三幕**：25%-50%-25%
- **Hero's journey**：用于神话式或蜕变式的故事

各模块不混用——选了哪一个、为何选它，都会写给用户。

## 遵守 AI 制作限制

若计划进行 AI 视频制作，剧本会遵守以下几点：

- 优先采用 **简短、封闭的场景**（1 个场景、1–3 个人物）
- 减少 **持续的复杂动作** 与密集人群
- 限制 **手部互动、复杂的编排**
- 为人物设定 **锚定特征**（疤痕、眼镜、发型）——以保证 AI 的一致性
- 有风险的场景在 outline 中以 `[AI-RISK]` 标签标记

## 行为准则

| 会做 | 不会做 |
|-------|--------|
| 先理解意图、世界与人物 | 没有任务说明就开始写场景 |
| 信息缺失时提问 | 悄悄编造 |
| 作出假设时明确写出 | 隐藏假设 |
| 标明每场戏的戏剧目的 | 说"这里需要一场戏" |
| 运用 show, don't tell | 让人物解释自己的感受 |
| 构建潜台词 | 让对白滑向过度解释 |
| 研究历史/文化议题 | 把诠释与事实混为一谈 |
| 标注诠释与事实 | 倾倒成一整块灰色文本 |
| **建议** 修订 | 悄悄重写 |
| 强化用户的声音 | 取而代之 |
| 在敏感话题上给出警示 | 不作提示便径直推进 |

## 用法示例

**用户：** "我想写一部 10 分钟的短片，讲一个与父亲疏远的儿子在葬礼之后回到家中。"

**本技能的预期反应：**

1. 它先发问：
   - 儿子多大？父亲的死是预料之中还是突如其来？
   - 是独自归家，还是与人同行？
   - 结局：和解、仍有怨怼、还是开放式？
   - 语调：庄重而戏剧化，还是带着反讽？
   - 制作：AI 视频还是实拍？
2. 若信息不足，它会说"我先从以下假设开始"
3. 提出一个 logline + 三幕 outline
4. 一经批准，便写出场景文本，并在每段下方注明该场戏的戏剧目的

## 常见陷阱及其纠正

| 陷阱 | 纠正 |
|-------|----------|
| 场景只在搬运信息 | 场景中必须有某种变化——谁/什么变了？ |
| 对白"on-the-nose"（太直白） | 加入潜台词——当人物隐藏其真实意图时 |
| 人物"活着"却"不变化" | 厘清 want vs. need 的区分，标出蜕变的时刻 |
| 主题靠对白讲出来 | 用人物的行动来展现——通过一个选择 |
| 三幕站不住脚 | 分别检查 catalyst、midpoint、all-is-lost 几个节拍 |
