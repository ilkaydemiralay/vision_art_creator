# vision_art_creator

[English](README.md) · **中文** · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

> 一套面向 [Claude Code](https://claude.com/claude-code) 的 AI 电影制作技能包。

`vision_art_creator` 在单个仓库中打包了 **11 个 `creator-*` 技能**，覆盖电影制作的每一个部门——从剧本一直到最终剪辑。在任意一台机器上，通过 `git clone` + `./install.sh` 即可安装。

> 这些技能在设计上会相互引用（由 `creator-pipeline-supervisor` 统筹其余技能）。建议将它们全部一起安装。

---

## 安装

```bash
git clone https://github.com/ilkaydemiralay/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

`install.sh` 会在 `~/.claude/skills/<skill-name>` 下为每个技能创建一个**符号链接**，指回本仓库。好处在于：更新时只需一条简单的 `git pull` 即可——无需重新安装。

### 选项

```bash
./install.sh --target /path/to/skills   # install into a different skills dir
./install.sh --force                    # overwrite existing names
./uninstall.sh                          # remove the symlinks
```

`uninstall.sh` 只会移除指向本仓库的符号链接——它不会触碰外部链接和真实目录（除非加上 `--force`）。

### 验证

安装完成后，重启 Claude Code 并输入：

```
/creator-pipeline-supervisor
```

检查全部 11 个 `creator-*` 技能是否都出现在技能列表中。

---

## 技能包内容

| 技能 | 概述 |
|---|---|
| `creator-pipeline-supervisor` | 统筹整个制作流程，安排各部门的先后顺序，确保连贯性，执行 QC，并产出交付就绪报告。 |
| `creator-director` | 将剧本转化为统一的导演视野：场面调度、表演、走位、基调把控。 |
| `creator-screenwriter` | 撰写与修改剧本、故事大纲（treatment）、logline、场景纲要和对白。 |
| `creator-character-designer` | 将角色作为一个有机整体来设计：心理、生平、视觉形象、服装、道具、FACS 编码的表情。 |
| `creator-production-designer` | 构建影片的世界：取景地、布景、道具、时代氛围、色彩/材质语言、连贯性锚点。 |
| `creator-cinematographer` | 设计视觉语言：光线、镜头、镜头焦段、构图、色彩、氛围、运动。 |
| `creator-storyboard-artist` | 逐格可视化场景：景别、角度、走位、构图、AI prompt。 |
| `creator-shot-list-designer` | 将场景和分镜转化为技术性的 shot list，并拆分为可由 AI 制作的小块。 |
| `creator-sound-music-designer` | 影片的声音世界：氛围、拟音、SFX、配乐、主题动机（leitmotif）、逐场景音乐方案、AI 音频 prompt。 |
| `creator-prompt-engineer` | 将每个部门的产出转化为面向 GPT Image 2.0、Nano Banana、Sora、Veo、Runway、Kling、Higgsfield 等工具的一致 prompt。 |
| `creator-final-cut-editor` | 将 AI 生成的镜头/音频/音乐/图形组装成成片：rough cut/fine cut/final cut、AI 错误甄别、交付格式。 |

每个技能的完整定义都存放在各自的 `SKILL.md` 文件中。

---

## 工作原理

本技能包运行在**基于文件系统的共享状态**之上。所有技能都从一棵公共的 `project/` 目录树（`bible/`、`screenplay/`、`characters/`、`storyboards/`、`prompts/`、`cuts/`、`qc/`、……）中读取并写入。`creator-pipeline-supervisor` 维护这些权威文件（项目与连贯性「圣经」），并依据它们审核每个部门的产出。

权威流水线：

```
0. project bible & vision
1. creator-screenwriter        → screenplay
2. creator-director            → vision, direction sheets, arcs
3-4-5. creator-character-designer + creator-production-designer
        + creator-cinematographer        (run in parallel)
6. creator-storyboard-artist   → panels with prompts
7. creator-shot-list-designer  → shot list + edit plan
8. creator-prompt-engineer     → tool-fit image + video prompts
   → [AI material generation — operator]
9. creator-sound-music-designer → sound + score plan
10. creator-final-cut-editor   → rough → fine → final cut → delivery

Throughout: creator-pipeline-supervisor enforces continuity, runs QC,
manages revision loops, and holds the bibles.
```

这一顺序是权威的，但并不僵化：导演的反馈可以重新触发编剧的工作，而一旦导演视野确定，角色/美术/摄影通常会并行推进。

---

## 更新

```bash
cd ~/projects/vision_art_creator
git pull
```

由于这些技能是通过符号链接接入的，无需任何额外步骤。

---

## 开发

1. 在仓库中编辑某个技能（`skills/creator-*/SKILL.md`）。
2. 在 Claude Code 中测试改动——由于是符号链接，改动会立即生效。
3. 提交（commit）+ 推送（push）。

新增一个 creator 技能：

```bash
mkdir -p skills/creator-new-skill
# write SKILL.md and README.md
./install.sh   # create the symlink for the new skill
```

---

## 翻译

本 README 以及每个技能的 `README.md` 都提供 12 种语言版本（见顶部的语言选择器）。`SKILL.md` 指令文件特意保持英文——Claude 会在运行时以用户的语言作答，而单一的权威指令集也能避免出现重复的技能名称。

---

## 许可证

[MIT](LICENSE) © 2026 İlkay Demiralay。
