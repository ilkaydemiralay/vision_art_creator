# 提示词工程师 — `creator-prompt-engineer`

[English](README.md) · **中文** · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

创意流程与 AI 生成器之间的**翻译层**。
它把编剧、导演、摄影指导、角色、制作、分镜、镜头表等技能产出的决策，转化为
**真正可生产、保持一致**的提示词。它针对不同工具进行优化（Midjourney ≠ Sora ≠
Stable Diffusion），将锁定锚点嵌入每一条提示词，并为有风险的场景生成安全替代方案。

## 理念

提示词工程师**不发明画面**——它对上游决策进行编码。
本技能：

- **锁定锚点（Locked anchors）**：character DNA + location master reference + style block——
  即使生成 50 条提示词之后，同一角色仍以同一张脸出现
- **工具适配（Tool fitness）**：每个 AI 工具都有自己的提示词语言
- **可生产性审查（Producibility audit）**：这个场景会击垮生成器——提出替代方案
- **一致性纪律（Consistency discipline）**：对长片而言，提示词是一个系统，而非孤立存在
- **FACS 表情编码**：用 AU1 + AU4 + AU15 取代“悲伤”——结果更一致
- **绝不悄悄覆盖上游**：必要时标记并回问

## 它能产出什么

| 产出 | 内容 |
|------|------|
| **Character prompts** | 锁定 DNA + 逐场变体 |
| **Location prompts** | Master reference + 昼/夜/天气变体 |
| **Style anchors** | 全片视觉/技术区块 |
| **Negative prompts** | 按类别划分的负面提示词库 |
| **Panel prompts** | 由分镜画格生成图像的提示词 |
| **Shot prompts** | 由镜头表生成 AI 视频的提示词 |
| **Character sheets** | 正面/侧面/背面/特写参考生成 |
| **Producibility risk report** | 场景/镜头级别的风险 + 安全替代方案 |
| **Tool guide** | 面向操作者的工具专属说明 |

## 何时介入

- 制作前需要 AI 图像/视频提示词
- 需要为角色/场景一致性建立锚点系统
- 要把分镜或镜头表的产出转化为工具提示词
- 现有提示词有风险——需要安全替代方案
- 当 `creator-pipeline-supervisor` 委派提示词阶段时

## 工具优化指南（摘要）

### Midjourney
- `--ar`、`--style raw`、`--s` 参数
- `--cref` 与 `--cw` 用于角色参考
- `--sref` 用于风格参考
- 表述紧凑——堆砌形容词会削弱信号

### DALL·E
- 自然语言 > 标签堆砌
- 写明空间关系
- 避免在画面内生成文字

### Stable Diffusion (SDXL / SD3)
- Positive + negative 分开
- LoRA / reference / seed 备注用于角色一致性
- 重要词汇放前面（token weight）

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- 单一主镜头运动
- 受控的角色数量
- 清晰的 opening + closing frame
- 时长短（通常 3–10s）
- 工具专属限制：
  - Sora 2：约 20s
  - Kling 3.0：subject binding 以保持一致性
  - Veo：motion fidelity 强
  - Runway Gen-3/4：动作合理，lip sync 较弱

## 锁定锚点系统（用于长片）

### Character DNA block

从 `project/characters/{slug}/ai-prompts.md` **逐字**复制：

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

从 `project/production-design/locations/{slug}/master-reference.md` 逐字复制：

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

这些区块会在该场景/角色/场地的**每一条提示词中原样重复**。
这种纪律正是一致性的引擎。

## 负面提示词类别

| 问题 | 负面词 |
|------|--------|
| 面部畸变 | distorted face, malformed face, asymmetric eyes, blurred features |
| 手部错误 | extra fingers, missing fingers, fused fingers, deformed hand |
| 时代错置 | modern clothes, modern tech, plastic, neon, smartphone |
| AI 瑕疵 | warping, morphing, flickering, jittery motion |
| 画质 | low quality, low resolution, jpeg artifacts, oversaturated |
| 文字 | unwanted text, watermark, signature, logo |
| 构图 | extra characters, cropped subject, duplicate subject |
| 镜头 | unintended shake, fisheye distortion |

有些工具会忽略负面提示词——这时把它作为 *"avoid: ..."* 提示写进 positive prompt 里。

## AI 视频可生产性审查

在发出视频提示词之前的检查：

- 单个镜头里动作是否太多？
- 角色数量是否过多？
- 镜头运动是否复杂？
- 手/手指/面部细节是否有风险？
- 服装/道具一致性能否维持？
- 场地是否太拥挤？
- 光线与时间是否一致？
- 该场景是否应拆成多段而非单条提示词？
- 是否需要 lip sync？（标记出来）
- 提示词是否过于抽象？

如有风险，它会给出**安全简化的替代方案**。

## 变体生成

针对同一场景的聚焦变体：

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

会**写明每个变体的用途**——为何以及在何种情况下使用。

## 它把产出写到哪里

写入 `project/prompts/` 下：

| 文件 | 内容 |
|------|------|
| `character-prompts/{slug}.md` | 锁定 DNA + 场景变体 |
| `location-prompts/{slug}.md` | Master anchor + 变体 |
| `style-anchors.md` | 全片 style block(s) |
| `negative-prompts.md` | 负面提示词库 |
| `scene-{NN}/panel-{PP}.md` | 画格图像提示词 |
| `scene-{NN}/shot-{SS}.md` | 镜头视频提示词 |
| `character-sheets/{slug}.md` | 正面/侧面/背面/特写设定生成提示词 |
| `prompt-system.md` | 锚点系统文档 |
| `producibility-risk-report.md` | 风险标记 + 安全替代方案 |
| `tool-guide.md` | 工具专属操作者说明 |

## 双语提示词格式

当用户需要母语说明 + 英文提示词时：

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

## 与其他技能的协作

- **读取**：所有上游创意产出
- **写入**：`project/prompts/*`
- **委派**：
  - 交给将运行 AI 工具的人工操作者
  - 若可生产性审查需要改动上游，则向 **storyboard artist** 或
    **shot-list designer** 反馈
- **接收反馈**：Pipeline Supervisor（一致性漂移）

## 行为准则

| 会做 | 不会做 |
|------|--------|
| 在多镜头工作中把锁定锚点放进每条提示词 | 每次都从零描述 |
| 写出贴合工具的提示词 | 把同一条提示词丢给所有工具 |
| 可生产性审查 + 安全替代方案 | 悄悄略过风险 |
| 使用 FACS AU 编码 | 像“悲伤”那样堆砌形容词 |
| 减少形容词冗余 | 用华丽词藻填充 |
| 保留上游决策，不悄悄覆盖 | 添加创意发挥 |
| 尊重时代考据 | 留下时代错置 |
| 结构化、下游可读的产出 | 倾倒单块提示词 |
| 母语说明 + 英文提示词格式（如有需要） | 一律强制英文 |
