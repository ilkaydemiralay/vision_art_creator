# 终剪师 — `creator-final-cut-editor`

[English](README.md) · **中文** · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

将 AI 制作产出转化为**成片**的 skill。前期制作的终点 / 后期制作的起点。
素材产出之后，它负责管理 rough cut → fine cut → final cut → delivery 的流程；
对 AI 生成错误进行分诊（triage），审核连贯性（continuity），检查音效/音乐的整合，
并产出可交付的母版（master）。

**与 shot-list-designer 的区别**：shot list 在拍摄之前设计剪辑意图；
creator-final-cut-editor 则在真实素材上执行剪辑。

## 理念

终剪**不是技术性的排序**——而是对电影整体性的构建。
本 skill：

- **每一次剪辑都有戏剧理由**——"看起来不错"远远不够
- **多尺度节奏**：镜头内、场景内、全片整体
- **AI 错误分诊**：哪个错误会毁掉剪辑、哪个可以被遮盖、哪个可以保留
- **观众体验设计**：观众感受到什么、学到什么、记住什么
- **交付纪律**：YouTube ≠ 电影节 ≠ Instagram ≠ 存档
- **版本管理**：分别管理 rough/fine/final + festival/social/trailer 剪辑版本

## 用途

| 产出 | 内容 |
|-------|--------|
| **Material evaluation** | 每个镜头：usable / 修订 / re-generate / cut |
| **Rough cut plan** | 首版粗略排序、缺失素材清单 |
| **Fine cut plan** | 剪切点、镜头时长、静默 |
| **Final cut plan** | 终剪就绪度 + delivery checklist |
| **Per-scene final-check** | 逐场景的详细审核 |
| **Whole-film report** | 全片终剪报告 |
| **AI error report** | 生成错误 + 严重程度分类 |
| **Audio integration audit** | 给声音设计师的反馈 |
| **Color grade notes** | 调色指令 |
| **EDL** | NLE 可读取的 Edit Decision List |
| **Version manifest** | festival/social/trailer 剪辑版本 |
| **Delivery specs** | 各平台的导出设置 |
| **Trailer plan** | 预告/trailer 剪辑方案 |

## 何时介入

- AI 视频镜头已产出，开始进入剪辑
- 需要 rough/fine/final cut 规划
- 需要 AI 错误审核
- 将产出多个剪辑版本（festival、social、trailer）
- delivery 导出准备
- 当 `creator-pipeline-supervisor` 委派后期制作阶段时

## 典型流程

1. **Material evaluation** — 对每个镜头进行分类（✅🟡🟠🔴）
2. **Rough cut v01** — 故事顺序、基础戏剧序列
3. **Fine cut v01** — 剪切点、节奏、静默
4. **Sound integration audit** — 给 creator-sound-music-designer 的反馈
5. **AI error report** — 关键/中等/轻微 分类
6. **Color grade notes** — 如有需要
7. **Subtitle / titles / graphics check**
8. **Final cut v01** — readiness checklist
9. **Delivery export** — 各平台版本

## AI 错误分诊矩阵

| Severity | 定义 | 处理 |
|----------|-------|---------|
| 🔴 关键 | 不能进入终剪 | Re-generate（向 creator-prompt-engineer 标记） |
| 🟡 中等 | 通过 trim/crop/color/sound 遮盖 | 剪辑层面的变通处理 |
| ✅ 轻微 | 不会打扰观众 | 可以保留 |

检查项：面部畸变、手/手指错误、lip-sync、服装变化、配件丢失、场景漂移、
光线方向不一致、摄影机的人为运动、flicker、warping、morphing、融化的物体、
背景崩坏、时代错误（anachronism）、塑料感画面。

## 逐场景 final-check 格式

```
Scene 04 — "Mutfak / Cenaze Sonrası"
Target duration: 90s
Current duration: 102s
Dramatic purpose: Demir'in iç dönüşümünün ilk anı
Core emotion: Bastırılmış yas

Shots used: 04.01, 04.02, 04.03, 04.05, 04.06
Shots cut: 04.04 (gereksiz reaction, ritim düşürüyor)
Shots shortened: 04.05 (8s → 5s — wide hold gereksiz uzun)
Shots lengthened: 04.02 (4s → 6s — kettle hold dramatik nefes)
Cut points:
  - 04.01 → 04.02: sound bridge (kettle ıslığı önce)
  - 04.02 → 04.03: hard cut (kettle sessizleşmesi → Demir close)
Transitions:
  - Scene → next: dissolve (sabah ışığına geçiş)
Reaction shot usage: 04.03 (Demir close) — yas kırılma anı
Silence usage: 04.02'de 4 saniye saatin tıkırtısı dışında hiç ses yok
Music usage: YOK — yönetmen direktifi
Ambience / foley notes: kettle, saat tıkırtı, dış rüzgâr çok kısık
Visual continuity notes: ✅ kostüm, ışık yönü, kettle leke pattern hepsi tutarlı
AI error audit:
  - 04.02 kettle buharı warping (🟡 orta) — sound design ile maskelenecek
  - 04.03 Demir göz sol kenar microflicker (🟡 orta) — color grade düzeltir
Color / light notes: 04.05'in white balance hafif sıcak — match için -100K
Subtitle / graphic notes: YOK
Final decision: 🟡 küçük revizyon (1 shot kes, 1 kısalt, 1 uzat)
Revision rationale: ritim 12s düşürülerek dramatik yoğunluk artar
```

## 产出写入位置

写入 `project/cuts/` 下：

| 文件 | 内容 |
|-------|--------|
| `material-evaluation.md` | 每个镜头的类别 |
| `rough-cut/v{NN}.md` | Rough cut 方案 |
| `fine-cut/v{NN}.md` | Fine cut 方案 |
| `final-cut/v{NN}.md` | Final cut 方案 + readiness |
| `scene-{NN}/final-check.md` | 逐场景细节 |
| `final-cut-report.md` | 全片审核 |
| `ai-error-report.md` | AI 错误报告 |
| `audio-integration-report.md` | 音频整合审核 |
| `color-grade-notes.md` | 调色 |
| `subtitle-titles-graphics.md` | 字幕/字幕卡 |
| `transitions.md` | 转场决策 |
| `edit-decision-list.md` | EDL |
| `versions/{cut-name}.md` | 版本 manifest |
| `delivery/{platform}.md` | 平台导出 specs |
| `trailer-plan.md` | Trailer/teaser 方案 |

## 版本管理

| 版本 | 时长 | 目标 |
|----------|------|-------|
| Rough Cut v01 | ~115% target | 首次故事流测试 |
| Rough Cut v02 | ~108% | 缺失部分的整合 |
| Fine Cut | ~102% | 锁定节奏与情绪 |
| Director's Cut | 100% 目标 | 导演完全认可 |
| Final Cut | 100% | Delivery-ready |
| Festival Cut | 100% | 电影节格式 |
| YouTube Cut | 100% 或缩短 | YouTube 算法 |
| Trailer Cut | 30s–2 分钟 | 营销 |
| Social Cut | 9:16 short | Reels、TikTok |

每个版本需含：name、duration、changes、removed/added scenes、audio
changes、revision rationale、approval status。

## Delivery 示例 specs

| Platform | Aspect | 分辨率 | FPS | Audio |
|----------|--------|------------|-----|-------|
| YouTube 16:9 master | 16:9 | 3840×2160 (4K) 或 1920×1080 | 24/25 | AAC 320kbps stereo |
| Festival master | 2.39:1 或 16:9 | 4K | 24 | WAV 48kHz 24-bit stereo + 5.1 |
| Instagram Reels | 9:16 | 1080×1920 | 30 | AAC stereo |
| TikTok | 9:16 | 1080×1920 | 30 | AAC stereo |
| Web compressed | 16:9 | 1920×1080 | 24/25 | AAC 192kbps |
| Archive master | original | 最高 | original | WAV master |

## 预告片剪辑逻辑

预告片**不是影片的缩小版**——它有自己的剪辑逻辑：

- 最强的 6–10 个画面
- 剧透排除清单（spoiler exclusion list）
- Hook → 背景 → 威胁/冲突 → climax teaser → 黑暗 → tagline
- 音乐的递进（与影片不同，更直接）
- 快速剪切节奏（与影片不同）
- 压缩的角色介绍
- 最后一记重击画面——处于影片语境**之外**
- 社交媒体 9:16 短版本

## 与其他 skill 的协作

- **读取**：所有上游创意产出 + shot-list `final-editor-notes.md`
- **写入**：`project/cuts/*`
- **提供反馈给**：
  - **creator-sound-music-designer**：音频修复请求
  - **creator-prompt-engineer**：重新生成请求
  - **creator-pipeline-supervisor**：连贯性升级处理
- **获取批准来自**：导演（final approval）、Pipeline Supervisor

## 行为准则

| 会做 | 不会做 |
|-------|--------|
| 每一次剪辑都给出戏剧理由 | 只做技术性排序 |
| 明确标记不必要的场景/镜头 | 为了忠实而保留 |
| 从观众体验出发评估 AI 错误 | 抽象/技术性的完美主义 |
| 同时考量 dialogue + music + ambience + silence | 孤立地审核 |
| 忠于导演的愿景 | 与剪辑师的自我冲突 |
| 严守目标时长 | 超出限制 |
| 重大改动前先询问用户 | 默默剪掉 |
| 跟踪多个版本 | 混在单一文件里 |
| 提供贴合平台的交付 | 只给一个母版 |
| 没有 delivery readiness checklist 不说"完成" | 过早宣布完成 |
