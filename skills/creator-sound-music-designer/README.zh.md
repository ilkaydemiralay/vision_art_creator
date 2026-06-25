# 声音与音乐设计师 — `creator-sound-music-designer`

[English](README.md) · [**中文**](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

构建影片**感官世界**的技能。两门相互融合的专业汇聚于此：

- **声音设计师**：空间、角色、物件与事件的感官真实——
  ambience、foley、音效、声学、声音透视，以及**沉默**（作为一种主动的
  戏剧手段）
- **电影配乐作曲家 / 音乐监制**：主题、角色
  leitmotif、场景音乐、节奏、音乐进出点

## 理念

声音与音乐**不是装饰**。每一个声音与音乐决策都服务于场景的戏剧
目的、角色心理、视觉氛围、剪辑节奏与观众
感受。本技能：

- 不会说"用悲伤的音乐"——而是设计 leitmotif，并规划其演变
- **主动设计沉默**——不是缺席，而是一种戏剧决策
- **角色 leitmotif**：以长笛起始的动机，在结尾随弦乐
  化为史诗
- **遵循版权纪律**：不模仿在世艺术家，"相似但不相同"
- **与剪辑节奏同步**：音乐进出点与 shot-list 剪辑计划协调
- **AI 声音/音乐 prompt 生成**：Suno、Udio、ElevenLabs SFX、Stable Audio、Runway Audio

## 用途

| 产出 | 内容 |
|-------|--------|
| **Sound vision** | 影片整体声音设计愿景 |
| **Music vision** | 影片音乐语言宣言 |
| **Main theme** | 主题设计 |
| **Character themes** | 按角色划分的 leitmotif 设计 |
| **Scene plans** | 逐场声音 + 音乐计划 |
| **Ambience / foley / SFX lists** | 清单列表 |
| **Silence plan** | 刻意安排的沉默地图 |
| **Music in/out plan** | 音乐进出点 |
| **Sound bridges** | 转场设计 |
| **AI sound + music prompts** | 工具专属 prompt |
| **Dialogue balance notes** | 对白/音乐平衡笔记 |
| **Final mix notes** | 终混审查 |
| **Continuity report** | 声音连续性检查 |

## 何时启用

- 剧本已就位，需要声音设计 / 电影配乐计划
- 需要 ambience、foley、SFX 或音乐主题
- 需要 AI 声音/音乐 prompt
- 当 shot-list designer 交接场景声音意图时
- 当 `creator-pipeline-supervisor` 委派音频阶段时

## 典型流程

1. **简报** + 阅读所有上游技能产出
2. **提问轮**：类型、register、音乐密度、时代、AI 工具
3. **Sound vision** + **Music vision**
4. **Main theme + character leitmotifs**
5. **逐场计划**：为每个场景安排 ambient/foley/silence/music
6. **Silence plan**：刻意沉默的地图
7. **Music entry/exit plan**
8. **AI sound + music prompts**
9. **终混审查**（final cut 之后）

## 沉默设计

沉默是一项**主动的**设计决策。对每一处沉默，本技能都会询问：

- 这里音乐会切断吗？
- ambience 是被压低，还是归零？
- 只留下一口呼吸，还是一个细小物件的声响？
- 这片沉默传达的是孤独、恐惧，还是犹疑？
- 它是要让观众不安，还是为了强化情绪？
- 沉默之后进入的是哪一种声音？

## 角色 leitmotif 示例

```
Karakter: Demir
Müzikal duygu: bastırılmış yas + içsel kararlılık
Ana enstrüman: solo cello (başlangıç) → cello + ney (orta) → cello + yaylı
                grup (final)
Tempo: 60–66 BPM (slow heart)
Ton: minör, kromatik geçişler
Ritim: rubato, neredeyse zamansız
Motifin evrimi:
  - Sahne 1–5: solo cello, kısa 5-notalı motif, sessizlik aralıkları geniş
  - Sahne 6–12: ney ekleniyor — nefes katmanı
  - Sahne 13–18: yaylı grup açılıyor — toplum, geçmiş, anlam
  - Sahne 19 (final): tek cello, ilk motifin yarısı — kırılma
```

## 产出写入位置

写入 `project/sound/` 之下：

| 文件 | 内容 |
|-------|--------|
| `sound-vision.md` | 整体声音设计愿景 |
| `music-vision.md` | 音乐语言宣言 |
| `main-theme.md` | 主题设计 |
| `character-themes/{slug}.md` | 角色 leitmotif |
| `scenes/scene-{NN}.md` | 场景声音 + 音乐计划 |
| `ambience-list.md` | Ambience 清单 |
| `foley-list.md` | Foley 清单 |
| `special-effects-list.md` | 特殊 SFX |
| `silence-plan.md` | 沉默地图 |
| `music-entry-exit-plan.md` | 音乐 in/out 时序 |
| `sound-bridges.md` | 转场设计 |
| `ai-sound-prompts.md` | AI SFX prompt |
| `ai-music-prompts.md` | AI 音乐 prompt |
| `dialogue-balance-notes.md` | 对白/音乐平衡 |
| `final-mix-notes.md` | 终混审查 |
| `sound-continuity-report.md` | 连续性检查 |

## AI prompt 格式

### SFX prompt 示例

```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```

### 音乐 prompt 示例

```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```

### 母语描述 + 英文 prompt 格式

```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## 版权与原创性

- 不建议复制现有作曲
- 不逐音模仿在世艺术家的风格
- 以"相似但不相同"的逻辑，描述类型 + 情绪
- 在 AI 音乐 prompt 中，用整体氛围替代艺术家姓名

## 与其他技能的协作

- **读取**：所有上游创意产出 + shot-list 声音剪辑笔记
- **写入**：`project/sound/*`
- **委派给**：`creator-final-cut-editor`（final cut 整合）、AI 音频工具
  操作者
- **接收反馈来自**：导演、Pipeline Supervisor、Final-cut-editor

## 行为准则

| 会做 | 不会做 |
|-------|--------|
| 将声音与音乐绑定到戏剧目的 | 当作装饰使用 |
| 主动设计沉默 | 视其为缺席 |
| 让 leitmotif 演变与角色弧线同步 | 重复一个固定主题 |
| 把对白/音乐/ambience/沉默一同考量 | 孤立地做决定 |
| 遵循版权纪律 | 模仿艺术家 |
| 进行历史/文化研究并加以标注 | 把诠释当作事实呈现 |
| 写出贴合工具的 AI prompt | 抛出泛泛的 prompt |
| 为长片维护声音连续性 | 逐场思考、彼此脱节 |
