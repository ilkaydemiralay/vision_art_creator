# 摄影指导 — `creator-cinematographer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

将剧本和导演的愿景转化为**电影视觉语言**的 skill。光线、镜头、镜头焦段、构图、色彩、
氛围、运动——每一个视觉决定都与一个戏剧性的理由相关联。"看起来好看"是不够的；它依照
**motivated lighting**、**chiaroscuro**、**depth as psychology**、
**camera as character** 的逻辑运作。

## 理念

DOP 不只是"拍出好画面"的人。DOP 是**视觉意义的工程师**。这个 skill：

- **Motivated lighting**：每一个光源在场景世界中都有其存在的理由
- **Chiaroscuro**：明暗对比承载意义，而不仅仅是美感
- **Depth of field**：景深是一种心理学选择
- **Negative space**：空白 = 孤独/被孤立
- **Camera as character**：摄影机是观察者、跟随者，还是控诉者？
- **了解** AI 制作约束并标记风险的人

## 用途

| 输出 | 内容 |
|-------|--------|
| **Visual language doc** | 用参考资料定义影片的视觉概念 |
| **Lighting bible** | 全片一致的光线处理方式 |
| **Color script** | 影片的色彩演进（逐场景） |
| **Lens list** | 按场景类型的镜头选择及其理由 |
| **Per-scene plan** | 场景级的光线 + 摄影机 + 镜头 + 色彩计划 |
| **Moodboard** | 参考图像说明，附来源 |
| **AI cinema prompts** | 将摄影知识转化为 AI prompt |
| **DOP notes to/from creator-director** | 与导演的双向沟通 |

## 何时介入

- 已有剧本 + 导演愿景，需要视觉设计
- "这个场景该如何打光 / 用哪个镜头 / 用什么构图"
- 需要色彩方案或 color script
- 为 AI 制作进行电影化的 prompt 转译
- 当 `creator-pipeline-supervisor` 委派 DOP 阶段时
- 当导演需要关于摄影机/光线的具体反馈时

## 典型流程

1. **简报**并阅读 `creator-director-vision.md`
2. **提问轮次**：类型、基调、参考、年代、AI 工具
3. **Visual language**：master palette、参考影片、视觉宣言
4. **Lighting bible**：影片的整体光线处理方式
5. **Color script**：与戏剧弧线相匹配的色彩转变
6. **Per-scene**：逐场景计划
7. **AI prompt hand-off**：向 creator-prompt-engineer 移交结构化的电影知识

## 输出写入何处

写入 `project/production-design/cinematography/` 下：

| 文件 | 内容 |
|-------|--------|
| `visual-language.md` | 影片整体的视觉宣言 |
| `lighting-bible.md` | 主光线处理方式 |
| `color-script.md` | 逐场景的色彩演进 |
| `lens-list.md` | 镜头选择及理由 |
| `scene-{NN}.md` | 逐场景计划（光线 + 摄影机 + 镜头 + 色彩） |
| `moodboard.md` | 参考图像说明 |
| `notes-to-creator-director.md` | 向导演提出的问题/建议 |
| `ai-production-cinema-notes.md` | 面向 AI 制作的电影指南 |

## 镜头心理学（摘要）

| Focal | 效果 | 用途 |
|-------|------|----------|
| 14–24mm wide | 畸变、幽闭恐惧 | 梦境/噩梦、激进的贴近 |
| 28–35mm | 纪录片感 | 自然、观察者 |
| 40–50mm | 视平线 | 中性、亲密对话 |
| 75–100mm | 压缩、隔离 | 美感、渴望、窥视 |
| 135mm+ | 强烈压缩 | 距离感、恐惧 |
| Anamorphic | 宽画幅、椭圆 bokeh | 史诗、电影感 |
| Macro | 极致细节 | 物件意义、感官 |

## 光线语言（摘要）

- **Key**：主光源，在场景世界中它从何而来？
- **Fill**：阴影调节、比例选择
- **Backlight**：与背景分离、rim halo
- **Practical**：灯、蜡烛、火、屏幕——场景中真实存在的光源
- **Hard vs. soft**：硬度揭示质感、确立意图
- **Color temp**：warm（3200K，亲密/回忆）、cool（5600K+，距离/临床）、mixed（紧张）
- **Contrast**：高（戏剧、noir）、低（纪录片、忧郁、黎明）

## 与其他 skill 的协调

```
creator-director-vision ──► creator-cinematographer
                         │
                         ├── coordinate ─► creator-production-designer
                         ├── coordinate ─► creator-character-designer
                         │
                         ▼
                  creator-prompt-engineer
                  creator-storyboard-artist
                  creator-shot-list-designer
```

- **读取**：`project/screenplay/*`、`creator-director-vision.md`、`notes-to-dop.md`、
  制作设计的输出、角色色彩方案
- **写入**：`project/production-design/cinematography/*`
- **移交给**：Prompt 工程师、storyboard、shot-list designer
- **接收反馈来自**：导演、Pipeline Supervisor

## 面向 AI 制作的电影化 prompt 格式

将摄影转化为 AI prompt 时，始终包含以下内容：

- Shot scale + 角度
- Lens（focal + DoF 效果）
- 光线方向、品质、色温
- 色彩方案与 mood
- 氛围（雾、烟、雨、尘）
- 场景细节（年代、质感、材质）
- 角色位置与动作
- Aspect ratio（2.39:1、1.85:1、16:9、9:16）
- 风格参考（片名、摄影师、年代）
- Negative prompt（排除项）

此结构已就绪，可移交给 `creator-prompt-engineer` skill。

## 行为准则

| 会做 | 不会做 |
|-------|--------|
| 为每一束光给出戏剧性理由 | 说"看起来好就行" |
| 应用 motivated lighting | 放置来源不明的光 |
| 解释镜头心理学 | 因美学原因选择镜头 |
| 与导演/制作/角色协调色彩方案 | 孤立地做决定 |
| 标记 AI 风险 | 规划无法制作的场景 |
| 提供低成本替代方案 | 只写理想版本 |
| 研究并标注历史年代 | 把解读当作事实呈现 |
| 拍摄前通过 `notes-to-creator-director.md` 传达问题 | 默默推进 |
