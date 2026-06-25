# 分镜表设计师 — `creator-shot-list-designer`

[English](README.md) · **中文** · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

将场景与故事板转化为**分镜表 + 剪辑意图**的技能。
这是前期制作规划与剪辑意图交汇之处。它不是 final-cut editor——
它在任何素材被生产出来之前就设计好剪辑意图，
从而让拍摄能够产出正确的片段。

## 理念

分镜表不是一份技术清单；它是一张**戏剧 + 剪辑意图的地图**。本技能：

- **shot 经济性**：每个 shot 只承载一个清晰的动作
- **剪辑节奏意识**：哪个 shot 长时间停留，哪个 shot 快速 cut 掉？
  shot 时长是一个剪辑决策
- **screen direction + continuity**：cut 之间的空间/时间一致性
- **面向 AI 的可生产性**：围绕 AI 工具的限制来规划单 shot 的复杂度
- **生产前确立剪辑意图**：剪辑逻辑在拍摄之前就已设定，
  从而避免拍摄不必要的 shot
- **观众体验设计**：观众感受到什么、学到什么，又有什么被刻意保留？

## 它产出什么

| 输出 | 内容 |
|-------|---------|
| **逐场景分镜表** | 标准分镜表，附戏剧 + 剪辑理由 |
| **剪辑方案** | 场景内的节奏、cut 点、开场/收尾画面 |
| **转场设计** | 场景到场景的转场决策（hard cut、match、J/L、sound bridge） |
| **连续性风险审计** | 各 shot 之间一致性风险的报告 |
| **声音剪辑笔记** | 给 sound designer 的 J-cut / L-cut / 静默点 |
| **全片分镜表** | 覆盖整部影片的整合清单 |
| **节奏图谱** | 逐场景节奏（shot 时长范围） |
| **冗余报告** | 应被 cut 掉/合并的 shot |
| **终剪师笔记** | 交接给 final-cut editor 的剪辑意图 |

## 它何时介入

- 场景与故事板已就绪，需要一份基于 shot 的规划
- 需要剪辑感知的 shot 排序
- 长场景需要被拆分成 AI 可生产的片段
- 当导演或 DOP 要求一份结构化的拍摄/制作方案时
- 当 `creator-pipeline-supervisor` 委派前期剪辑规划时

## 典型流程

1. **简报**（briefing）+ 阅读所有上游技能的输出
2. **提问轮次**：格式、剪辑节奏、基调、AI 工具
3. **分镜表（逐场景）**：采用标准结构，附戏剧 + 剪辑理由
4. **剪辑方案（逐场景）**：节奏、开场/收尾、cut 点
5. **转场设计**：场景到场景的转场
6. **连续性审计**：跨 shot 的风险
7. **节奏图谱**：全片节奏图
8. **冗余报告**：识别可 cut 的 shot
9. **交接**：给 creator-prompt-engineer 的 shot prompt 数据 + 给 creator-final-cut-editor 的剪辑意图

## shot — 标准结构

```
Scene 04 — Shot 04.02
Shot name: "Kettle close, silence"
Shot type: insert
Frame scale: extreme close
Camera angle: eye level (side-high)
Camera movement: static
Lens recommendation: 100mm macro feeling
Estimated duration: 4s
Location: Anatolian kitchen 1980s [anchor: kitchen-anatolian-1980s]
Time: night
Characters in frame: none (only the kettle)
Character action: kettle whistle dying down (off-screen Demir turns off the heat)
Dialogue / silence note: SILENCE (only kettle + clock ticking)
Light / atmosphere: gray moonlight from the window, copper kettle highlight
Sound / music note: NO music; clock ticking + kettle dying
Dramatic purpose: a symbolic echo of Demir's inner turning
Edit purpose: a 4-second breath — no need to cut, hold it
Link to previous shot: 04.01 (Demir sitting, wide) — match by sound
Link to next shot: 04.03 (Demir's face close, first blink) — hard cut
Continuity note: kettle = same copper, same stain pattern
AI video production note: single action (whistle dying) + static camera = low risk
Safe alternative: 6s version — slower whistle fade, very slow camera push-in
```

## 剪辑意图 — 场景方案

场景层级的剪辑问题：

- 哪个 shot 为场景开场？
- 哪个画面为场景收尾？
- 哪个 shot 长时间停留？
- 哪个 shot 被短促 cut 掉？
- reaction shot 放在哪里？
- 静默在哪里被拉长？
- 哪里需要一个 hard cut？
- 哪里是一个柔和的转场？
- 哪个画面衔接到下一个场景？
- 哪个 shot 承载戏剧高潮？
- 哪个 shot 是不必要的？
- 哪个 shot 传递信息，哪个传递情绪？

写入 `project/shot-list/scene-{NN}/edit-plan.md`。

## 它将输出写到哪里

位于 `project/shot-list/` 之下：

| 文件 | 内容 |
|-------|---------|
| `scene-{NN}/shot-list.md` | 场景分镜表 |
| `scene-{NN}/edit-plan.md` | 剪辑意图 + 节奏 |
| `scene-{NN}/transitions.md` | 转场决策 |
| `scene-{NN}/continuity-risks.md` | 连续性审计 |
| `scene-{NN}/sound-edit-notes.md` | 给 sound designer 的交接 |
| `film-shot-list.md` | 全片整合清单 |
| `rhythm-map.md` | 节奏图 |
| `redundancy-report.md` | 可 cut 的 shot |
| `ai-production-shot-guide.md` | AI 工具限制指南 |
| `final-editor-notes.md` | 给 final-cut editor 的意图 |

## 转场类型（剪辑用途）

| 转场 | 剪辑用途 |
|-------|-------------------|
| Hard cut | 突然的戏剧性断裂 |
| Match cut | 两个画面之间的意义桥接 |
| Fade in/out | 时间/情绪的开启/收束 |
| Dissolve | 时间过渡，情绪融合 |
| J-cut | 下一场景的声音先到达（流畅承接） |
| L-cut | 当前场景的声音被延续（情绪保持） |
| Sound bridge | 借声音承载地点/时间的转换 |
| Visual motif | 借反复出现的视觉元素桥接 |
| Object transition | 形状匹配 |
| Movement transition | 方向连续性 |
| Time jump | 突然的时间跳跃 |
| Flashback | 借助滤镜/镜头/虚化/声音提示 |
| Parallel edit | 两个地点交织剪辑 |

## AI 视频可生产性规则

- 每个 shot 一个清晰的动作
- 一个主要的 camera movement（不串联）
- 受控数量的角色
- 一个清晰的视觉目标
- 将复杂运动拆分为多 shot
- 标记有风险的手部/手指/lip sync
- 对人群采用选择性取景
- 每个 prompt 中锁定 location + character anchors
- shot 时长通常为 3–10s
- 每个 shot 都能干净地对应到单个视频 prompt

当检测到风险时，将其标记出来：

> *"这个 shot 对 AI video 来说过于复杂——把它拆成两个 shot。"*
> *"此处的 lip sync 可能会失败；用一个 reaction shot 代替说话者。"*
> *"手部动作至关重要——用更宽的画框而非 insert。"*
> *"人群动作——用多个 cut 来构建，而非单个 shot。"*

## 节奏与配速

不使用诸如"快一点"之类模糊的措辞。配速是：

- 用一个 **shot 时长范围**来表达
- 用 **cut 频率**来衡量

示例：
> *"场景 3 平均每个 shot 4–6s，场景 12 平均每个 shot 1.5–3s——
> 随着角色冲突升级，节奏加快。"*

## 对白剪辑意图

对于对白密集的场景：

- 说话者还是聆听者？
- reaction shot 放在哪里？
- 静默在哪里更有力量？
- 在对白之上叠加另一个画面？
- 通过面部表情传递潜台词？
- hard cut 还是自然 overlap？
- 在句子结束之前就 cut？
- 解释是否有冗余重复？
- 观众真正需要看到的情绪落在谁身上？

J-cut / L-cut 标记在此处设定。

## 与其他技能的协同

- **读取**：剧本、导演愿景 + direction sheets、DOP 逐场景方案、
  故事板分镜数据、角色/场景 anchors
- **写入**：`project/shot-list/*`
- **交接给**：
  - `creator-prompt-engineer`（shot 层级的视频 prompt）
  - `creator-final-cut-editor`（剪辑意图文件）
- **接收反馈来自**：导演、Pipeline Supervisor

## 冗余检测

在一部长篇 AI 影片中，标记出：

- 重复同一信息的 shot
- 不改变情绪的 shot
- 让节奏掉下来的细节 shot
- 过度使用的 reaction shot
- 戏剧贡献低却对 AI 来说很难的 shot
- late-in / early-out 的机会
- 可以用视觉而非对白来讲述的时刻

明确写出 *"这个 shot 可以 cut 掉"* 或 *"这两个 shot 可以合并"*。

## 行为准则

| 会做 | 不会做 |
|-------|---------|
| 为每个 shot 给出戏剧**与**剪辑双重理由 | 做一份技术清单 |
| 与导演节奏、DOP 取景、故事板协同 | 孤立地做决定 |
| 标记不必要的 shot | 加入填充内容 |
| 主动检查 continuity | 等到拍摄之后问题才浮现 |
| 围绕 AI 工具限制来设计 | 规划无法生产的 shot |
| 为有风险的 shot 提供安全替代方案 | 只提供单一版本 |
| 在对白中也考虑聆听者 | 只跟随说话者 |
| 协同声音与音乐的剪辑意图 | 只考虑画面 |
| 结构化、下游可读的输出 | 倾倒一整块文字 |
