# 分镜师 — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

一个将书面剧本转化为**可读视觉叙事**的技能。它通过最小化分镜数量，
确保每一格分镜都因戏剧性理由而存在。它捕捉场景的关键时刻，保持
screen direction，跟踪 eyeline continuity，并向 AI 图像/视频 prompt 做出清晰交接。

## 理念

分镜不是"场景绘图"，而是一套**视觉叙事系统**。本技能：

- **Panel economy**：少分镜 + 精准取舍——而非多分镜 + 薄弱决策
- **Screen direction（180°）** 与 **eyeline continuity**：剪辑间的空间一致性
- **Graphic dynamics**：视线落在哪里？焦点是什么？
- **Continuity awareness**：服装、场景、光线方向、画面方向、运动
- **Locked anchors**：每格分镜中的 character DNA + location master reference
- **Producibility**：了解 AI 生成限制，并标记有风险的场景

## 用途

| 输出 | 内容 |
|------|------|
| **Per-scene storyboard** | 逐场景分镜列表（全部分镜数据） |
| **Per-panel sheets** | 复杂场景的详细单格分镜文件 |
| **AI image prompts** | 每格分镜的可生产 prompt |
| **AI video prompts** | 用于运动分镜的视频 prompt |
| **Continuity log** | 服装/场景/方向风险的标记 |
| **Animatic plan** | 规划所有场景的 animatic 排序 |
| **Director / DOP notes** | 给导演和 DOP 的简短视觉/技术备注 |
| **Handoff to shot-list** | 以 creator-shot-list-designer 格式提供的分镜数据 |

## 何时启用

- 剧本在手，需要视觉拆解时
- 导演希望提前对场景进行视觉叙事时
- 在 DOP 决定镜头/灯光之前需要视觉概念时
- 在生成 AI prompt 之前需要分镜逻辑时
- 当 `creator-pipeline-supervisor` 委派分镜阶段时

## Panel content（规范字段）

每格分镜记录以下字段：

```
Scene 04 — Panel 04.03
Shot type: medium close
Camera angle: eye level
Frame: Demir merkez-sağ; kettle ön plan-sol; arka plan
       dolap soft-focus; sağ kenar negatif alan açık
Lens feeling: 50mm (eye-equivalent, samimi)
Character position: Demir sandalyede, omuzlar düşmüş, eller masada
Character movement: yok — duraksama
Camera movement: static
Setting / dressing: kireçli mutfak — pencere doğu, kettle ateşte
Light / atmosphere: pencereden yumuşak gri sabah, mum yok
Emotional emphasis: bastırılmış yas; ilk gerçek duygu kırılması
Dialogue / action note: sessizlik; kettle ıslığı
Dramatic justification: Demir'in iç çatışmasını yüzeye getiren ilk an
Transition to next panel: J-cut — kettle sesi devam ederken Panel 4.04 başlar
AI image prompt: [tam prompt]
AI video prompt: [tam prompt, 6s]
Continuity note: palto sahne başında; ceket askıda; kettle aktif
```

## 输出写入位置

写入 `project/storyboards/` 下：

| 文件 | 内容 |
|------|------|
| `scene-{NN}/storyboard.md` | 基于场景的分镜列表（规范） |
| `scene-{NN}/panel-{PP}.md` | 详细单格分镜（用于复杂场景） |
| `scene-{NN}/prompts.md` | 每格分镜的 AI prompt（image + video） |
| `scene-{NN}/continuity.md` | Continuity 标记 |
| `animatic-plan.md` | 全片 animatic 排序备注 |
| `notes-to-creator-director.md` | 给导演的问题/提示 |
| `handoff-to-shot-list.md` | 给 shot-list designer 的格式化分镜数据 |

## Shot type 词汇表（附戏剧性对应）

| 类型 | 戏剧性用途 |
|------|-----------|
| Establishing | 在空间中为观众定位 |
| Master | 场景几何，fallback |
| Wide/Full | 角色与环境的关系 |
| Medium | 中性对白 |
| Close | 内心冲突，亲密情感 |
| Extreme close | 主观强度 |
| Insert | 物件强调 |
| Cutaway | 平行/外部信息 |
| Reaction | 反应重于动作 |
| OTS | 对白视角 |
| POV | 角色主观性 |
| 2-shot / group | 关系几何 |
| Silhouette | 匿名性，神秘 |
| Negative-space frame | 孤立，渺小 |
| Symmetrical | 力量、正式、令人不安的静止 |
| Tracking | 持续跟随 |
| Static | 观察，沉默的意义 |

"用一个 close-up"是不够的——问题在于**为什么**需要 close-up。

## Continuity audit

从分镜到分镜、从场景到场景的跟踪：

- 服装
- 发型/妆容/配饰
- 场景身份（配合 locked anchor）
- 光线方向
- 日/夜
- Screen direction（180° 规则）
- 角色的空间逻辑
- 动作流
- 道具位置

一旦发现风险，会在分镜的 `continuity note` 字段中明确写出。

## 与其他技能的协作

- **读取**：剧本、导演愿景 + direction sheets、DOP per-scene plan、
  character DNA + FACS、location anchors
- **写入**：`project/storyboards/*`
- **委派**：
  - `creator-shot-list-designer`（panel → shot list）
  - `creator-prompt-engineer`（panel prompt → 针对工具的优化）
- **接收反馈来源**：导演、Pipeline Supervisor

## 面向 AI 生成的解决方案

- 将复杂场景拆分为简单分镜
- 在多角色场景中厘清视觉焦点
- 简化 AI 难以处理的运动
- 对同一场景/角色使用固定 anchor
- 用安全的静态镜头替代摄影机运动
- 在拥挤场景中建议有选择的取景
- 用富有节奏的剪辑替代快速动作

## 行为准则

| 会做 | 不会做 |
|------|--------|
| 为每格分镜写出戏剧性理由 | 为凑数填上"再来一格" |
| 少分镜 + 精准取舍 | 多分镜 + 薄弱决策 |
| 整合编剧 + 导演 + DOP + 角色 + 制作 | 悄悄覆盖上游 |
| 保持 screen direction 与 eyeline | 在剪辑处搞乱方向 |
| 将 locked anchors 放入每个 prompt | 在每格分镜中从零重述 |
| 将复杂场景拆分为多格分镜 | 堆进单一过载画面 |
| AI 风险标记 + 安全替代方案 | 建议无法生成的运动 |
| 结构化、可供下游读取的输出 | 倾倒一整块文本 |
