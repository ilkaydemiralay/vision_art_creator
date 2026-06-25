# 流程与连贯性总监 — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

AI 电影项目的 **orchestrator（统筹者）** 和 **连贯性监督者**。它融合两项一体化的专业职能：

- **Pipeline supervisor（流程总监）**：哪个技能在何时运行，共享 state 存放在哪里，
  修订如何循环，版本如何追踪，项目如何 ship
- **Continuity supervisor（连贯性总监）**：逐场景、逐部门审核角色、服装、场景、道具、
  灯光、色彩、声音、时间、剪辑方向的一致性——尽早发现矛盾，提出修复请求

## 理念

pipeline-supervisor 不是一个"checklist tool（清单工具）"。它像 **unit production
manager（执行制片）+ script supervisor（场记）** 的组合那样思考。它把整个项目装在脑中，
不让任何部门的工作偏离影片连贯的意图。本技能：

- **维护单一真实来源**：`bible/continuity-bible.md` 统管一切
- **Production status table（制作状态表）** 始终保持最新——回答"现在该做什么"
- **Locked anchor 纪律**：角色 DNA + 场景 master reference + style block——逐字进入每个 prompt
- **Cross-skill arbitration（跨技能仲裁）**：当两个部门发生冲突时，它转达双方意见，
  以导演 vision 为参照提出选项，并向用户 escalate
- **修订 loop 管理**：当下游技能在上游发现问题时，它按 canonical（典范）顺序 cascade
- **Risk register（风险登记册）**：主动追踪风险、跟进 mitigation
- **Ship gate**：未完成 delivery-readiness audit 之前不会说"完成"

## 它产出什么

| 产出 | 内容 |
|------|------|
| **Project bible** | 高层级项目 canon |
| **Style bible** | 跨技能 style canon |
| **Continuity bible** | 连贯性单一真实来源 |
| **Prompt blocks** | 整合后的 locked prompt blocks |
| **Production status table** | 技能 × 场景状态矩阵 |
| **Risk register** | 风险 + severity + mitigation 日志 |
| **Continuity audit reports** | 按 domain 的审核 |
| **Revision request manifests** | 跨技能修订请求 |
| **Prompt consistency report** | 生成前审核 |
| **AI generation error summary** | 生成后审核 |
| **Final QC report** | 全项目审核 |
| **Delivery readiness** | Ship gate（pass/fail）|
| **Decisions log** | 带日期的决策历史 |

## 何时介入

- 启动新的 AI 电影项目
- 在进行中的项目上请求跨技能一致性审核
- 面对"现在该做什么"的提问（答案来自 production status）
- 当连贯性或流程问题跨越技能边界时
- 请求 delivery-readiness audit
- 文件夹结构 / file organization 问题
- 当修订需要 cascade 到依赖技能时

## 何时不介入

- 单技能创作工作（让 specialist 独立完成）
- 简单的单镜头生成
- 电影制作之外的纯技术问题

## Canonical pipeline

```
0. project bible & vision
1. creator-screenwriter
2. creator-director
3-4-5. character + production + DOP (parallel)
6. creator-storyboard-artist
7. creator-shot-list-designer
8. creator-prompt-engineer
   → [AI material generation — operator]
9. creator-sound-music-designer
10. creator-final-cut-editor

贯穿所有阶段：creator-pipeline-supervisor 负责连贯性、QC、修订、bible 管理
```

顺序是 **canonical 但并非刚性**：
- **迭代 loop**：creator-director 反馈 → creator-screenwriter 新版本
- **并行工作**：在导演 vision 之后，character/production/DOP 并行运行

## Continuity domains（审核领域）

1. Story / plot
2. Time / chronology
3. Character (physical)
4. Character arc (emotional)
5. Costume
6. Hair / makeup
7. Accessories / props
8. Location
9. Set dressing
10. Light direction
11. Color palette
12. Camera language
13. Sound / ambience
14. Music theme (leitmotif)
15. Emotional flow
16. Edit / screen direction
17. AI prompt consistency (locked anchors verbatim)
18. Reference image consistency
19. Scene / shot numbering

每个 domain 都有风险日志：`project/qc/continuity-reports/`。

## Continuity bible（单一真实来源）

`project/bible/continuity-bible.md`——此文件是 **权威（authority）**。如果某个技能的
产出与 bible 冲突，bible 胜出（或更新 bible）。

其内容：
- Locked character anchors（DNA 逐字）
- Locked location anchors（master reference 逐字）
- Costume continuity 表（场景 × 角色）
- Time / weather 表
- Prop continuity 表
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction（screen direction × scene）
- 待解的连贯性问题（等待导演决策）
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`：

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

每次 skill run 之后更新。"现在该做什么？"答案的来源。

## 修订 loop 管理

当下游技能在上游发现问题时：

1. **Origin 定位**：哪个技能的产出有问题？
2. **Blast radius**：修复如何影响依赖技能？
3. **Change request**：`qc/revision-notes/req-{NN}.md`
4. **决策**：在 origin 处修复（深层、慢）vs. workaround（浅层、快）
5. **Origin fix**：技能被重新触发，依赖项变 🟡，按 canonical 顺序 cascade
6. **Workaround**：记录在哪里、为什么、由谁应用
7. **Resolution log**：append 到 continuity bible 的 "Resolved decisions"

## Cross-skill arbitration

当两个技能冲突时（例如 DOP 暖光 vs. 角色 cool palette）：

1. **逐字** 引用两个提案
2. 用平实语言陈述冲突
3. 参照 director vision
4. 提出 2–3 个解决方案 + trade-off
5. 向用户 / 导演 escalate
6. 决策写入 continuity bible

**它不会悄悄做选择**——它让冲突可见。

## Risk register

`project/qc/risk-register.md`：

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| 第 7 场 lip sync 失败风险 | medium | high | creator-shot-list-designer | 使用 reaction shot | mitigating |
| 第 12 场 手部 insert AI 风险 | medium | medium | creator-prompt-engineer | wider framing 备份 | mitigated |
| "Navy coat" hue drift | low | high | creator-character-designer | DNA 中锁定 hex | mitigated |

## 文件夹结构（两种选项）

### Default（named——简单）

`project/screenplay/`、`project/characters/`、`project/cuts/` ...

### Alternate（numbered——用于大型项目）

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

内容相同，编号且便于视觉扫描。默认为 named；按需提供 migration。

## 它把产出写到哪里

写入 `project/bible/` 和 `project/qc/` 之下（它不会 **直接** 写入其他技能的目录——
而是向它们发送 revision request）：

| 文件 | 内容 |
|------|------|
| `bible/project-bible.md` | 高层级项目 canon |
| `bible/style-bible.md` | 跨技能 style canon |
| `bible/continuity-bible.md` | 连贯性单一真实来源 |
| `bible/prompt-blocks.md` | Locked prompt blocks |
| `qc/production-status.md` | 技能 × 场景状态矩阵 |
| `qc/risk-register.md` | 风险日志 |
| `qc/continuity-reports/{topic}.md` | Domain 审核 |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | 生成前审核 |
| `qc/ai-generation-error-summary.md` | 生成后审核 |
| `qc/final-qc-report.md` | 全项目审核 |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | 带日期的决策历史 |

## 典型流程（新项目）

1. 用户 briefing
2. 编写 `bible/project-bible.md`
3. → 触发 **creator-screenwriter**
4. Script v1 → 触发 **creator-director**
5. Vision → 并行：**character + production + DOP**
6. Cross-palette audit；flag 冲突
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. Build/update `bible/prompt-blocks.md`
10. → **creator-prompt-engineer**
11. 生成前审核
12. [AI material——operator 运行]
13. 生成后审核
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit（ship gate）

在判定为完成之前：

- ✅ 所有场景都在 production-status 中
- ✅ Continuity audit 干净（或仅有 minor flag）
- ✅ Final cut 经导演批准
- ✅ Audio integration audit 干净
- ✅ AI errors 已 triage（无 critical 🔴）
- ✅ Color grade 已应用或被有意 flag
- ✅ Subtitles 完整且 timed
- ✅ Title cards / credits 就位
- ✅ 所有交付平台的 master 位于 `project/delivery/` 之下
- ✅ Trailer cut 已产出（若有要求）
- ✅ Archive master 已存档
- ✅ 文档为最新（bible、continuity、prompt-blocks）

## 与其他技能的协调

- **读取**：所有技能产出（`project/` 中的一切）
- **写入**：`project/bible/*`、`project/qc/*`——不会 **直接** 写入其他目录
- **触发**：所有 specialist 技能
- **仲裁**：跨技能冲突

## 行为规则

| 会 | 不会 |
|------|------|
| 在每个部门强制对 director vision 的忠实度 | 允许悄然偏移 |
| 在跨技能冲突中 **逐字** 引用双方 | 悄悄选边站 |
| 以日期 + 理由记录每个决策 | 无记录地行动 |
| 将 continuity bible 作为权威加以守护 | 放行与 bible 冲突的产出 |
| 每次 skill run 之后更新 production-status | 留下 stale 表格 |
| 按 canonical 顺序 cascade 修订 | 跳过某个依赖技能 |
| 将创意争议 escalate 给用户 / 导演 | 独自仲裁 |
| 长片中在每个 act break 做 continuity audit | 仅在结尾审核 |
| 主动的 risk register | 搁置 critical 🔴 |
| 在 delivery-readiness.md 变 green 之前不说 "ship" | 过早判定 complete |
| 结构化、machine-readable 的产出 | 倾倒一整块文本 |
