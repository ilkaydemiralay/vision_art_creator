# vision_art_creator

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · **日本語** · [한국어](README.ko.md)

> [Claude Code](https://claude.com/claude-code) と [OpenAI Codex](https://github.com/openai/codex) のための、AI 映画制作スキルパック。

`vision_art_creator` は、**11 個の `creator-*` スキル**をひとつのリポジトリにまとめたもので、脚本から最終的なファイナルカットに至るまで、映画制作のあらゆる部門をカバーします。`git clone` と `./install.sh` さえあれば、どのマシンにもインストールできます。

> これらのスキルは互いを参照し合うように設計されています（`creator-pipeline-supervisor` が残りのスキルを統括します）。すべてをまとめてインストールすることをおすすめします。

---

## デモ：*Before She Leaves*

このパックと Higgsfield（Nano Banana Pro の参照画像、Seedance 2.0 のクリップ）で制作した 26 秒のシーンと、記録されたグラフ（担当者、ハッシュ、承認）を見せる 30 秒のメイキング。Claude Code と OpenAI Codex の 2 つのエージェントが同じスキルファイルで作業しました。映像はすべて AI 生成です。

| 本編（26 秒） | メイキング（30 秒） |
|---|---|
| [![本編（26 秒）](docs/media/demo-film.jpg)](https://github.com/ilkaydemiralay/vision_art_creator/releases/download/v1.2.0/before-she-leaves-film.mp4) | [![メイキング（30 秒）](docs/media/demo-making-of.jpg)](https://github.com/ilkaydemiralay/vision_art_creator/releases/download/v1.2.0/before-she-leaves-making-of.mp4) |

---

## インストール

```bash
git clone https://github.com/ilkaydemiralay/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

OpenAI Codex を使う場合は、Codex のスキルディレクトリにインストールし、Codex を再起動してください：

```bash
./install.sh --codex   # ~/.agents/skills/
```

`install.sh` は、各スキルについて `~/.claude/skills/<skill-name>` の下に、このリポジトリを指す**シンボリックリンク**を作成します。利点は、更新したいときに単純な `git pull` だけで済むことです。再インストールは不要です。

### オプション

```bash
./install.sh --target /path/to/skills   # install into a different skills dir
./install.sh --force                    # overwrite existing names
./uninstall.sh                          # remove the symlinks
```

`uninstall.sh` は、このリポジトリを指すシンボリックリンクのみを削除します。外部のリンクや実体のあるディレクトリには手を付けません（`--force` を指定した場合を除く）。

### 確認

インストール後、Claude Code を再起動して次のように入力します。

```
/creator-pipeline-supervisor
```

11 個すべての `creator-*` スキルがスキル一覧に表示されることを確認してください。

---

## パックの内容

| スキル | 概要 |
|---|---|
| `creator-pipeline-supervisor` | 制作全体を統括し、各部門の順序を組み立て、連続性を担保し、QC を実行し、納品準備レポートを作成します。 |
| `creator-director` | 脚本を統一された演出ビジョンへと翻訳します。シーン演出、演技、ブロッキング、トーンのコントロール。 |
| `creator-screenwriter` | 脚本、トリートメント、ログライン、シーンのアウトライン、台詞の執筆と改稿。 |
| `creator-character-designer` | キャラクターを統合された全体としてデザインします。心理、経歴、ビジュアルアイデンティティ、衣装、小道具、FACS でコード化された表情。 |
| `creator-production-designer` | 映画の世界を構築します。ロケーション、セット、小道具、時代の空気感、色彩・素材の言語、連続性のアンカー。 |
| `creator-cinematographer` | ビジュアル言語をデザインします。光、カメラ、レンズ、フレーミング、色、空気感、動き。 |
| `creator-storyboard-artist` | シーンをパネル単位でビジュアル化します。ショットサイズ、アングル、ブロッキング、構図、AI プロンプト。 |
| `creator-shot-list-designer` | シーンとストーリーボードを技術的なショットリストへと変換し、AI で制作可能な単位に分割します。 |
| `creator-sound-music-designer` | 映画の音の世界。空気感、フォーリー、SFX、スコア、ライトモチーフ、シーンごとの音楽プラン、AI オーディオプロンプト。 |
| `creator-prompt-engineer` | 各部門のアウトプットを、GPT Image 2.0、Nano Banana、Sora、Veo、Runway、Kling、Higgsfield などに向けた一貫性のあるプロンプトに変換します。 |
| `creator-final-cut-editor` | AI 生成されたショット／オーディオ／音楽／グラフィックを、完成した映画へと組み上げます。ラフカット／ファインカット／ファイナルカット、AI エラーのトリアージ、納品フォーマット。 |

各スキルの完全な定義は、それぞれの `SKILL.md` ファイルに記載されています。

---

## 仕組み

このパックは、**ファイルシステムベースの共有ステート**の上で動作します。すべてのスキルは共通の `project/` ツリー（`bible/`、`screenplay/`、`characters/`、`storyboards/`、`prompts/`、`cuts/`、`qc/` など）を読み書きします。`creator-pipeline-supervisor` は正典となるファイル（プロジェクト＆連続性の「バイブル」）を維持し、各部門のアウトプットをそれらと照合して監査します。

正典となるパイプライン:

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

この順序は正典ですが、厳格に固定されているわけではありません。ディレクターのフィードバックが脚本家を再び動かすこともありますし、ディレクションのビジョンが定まれば、キャラクター／プロダクション／撮影は通常並行して進みます。

---

## 記録型グラフモード（任意・実験的）

v1.1.0 から、単一シーン向けの任意の、機械で検証できるワークフローが含まれています。`creator-pipeline-supervisor` はプリプロダクションを 12 ノードのグラフとして実行できます。各成果物は SHA-256 ハッシュとともに記録され、各承認はレビューした入力そのものに結び付けられ、修正時には影響を受けるノードだけが再実行されます。

- ワークフロー：`workflows/single-scene.v1.json`。契約：`skills/creator-pipeline-supervisor/references/graph-workflow.md`。
- `schemas/` に JSON Schema、`scripts/validate_graph.py` に読み取り専用のバリデーター、`tests/` にテストがあります。
- `examples/single-scene/` に 15 秒・3 ショットのテキストによるパイロット例があります。v00 はデザインの衝突で止まり、v01 で解決し、v02 で小道具の色を 1 つ変更します。

通常のスキル利用に Python は不要です。バリデーターの実行（Python 3.10 以上）：

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-graph.txt
.venv/bin/python -m unittest discover -s tests
.venv/bin/python scripts/validate_graph.py validate --manifest path/to/manifest.json
```

制限：これは一人の作者によるテキストのみのパイロットです。部門の並行実行、メディア生成、編集、コストは検証していません。承認者の身元とタイムスタンプはオペレーターの申告であり、署名されていません。設計と結果のメモは `docs/`（トルコ語）にあります。

---

## 更新

```bash
cd ~/projects/vision_art_creator
git pull
```

スキルはシンボリックリンクになっているため、追加の手順は不要です。

各リリースの変更点は [CHANGELOG.md](CHANGELOG.md) を参照してください。**v1.1.0：** `creator-cinematographer` と `creator-storyboard-artist` はプロンプトの下書きを各自のフォルダーに保存するようになりました。最終プロンプトを `project/prompts/` に書くのは `creator-prompt-engineer` だけです。

---

## 開発

1. リポジトリ内のスキルを編集します（`skills/creator-*/SKILL.md`）。
2. Claude Code で変更をテストします。シンボリックリンクなので、変更は即座に反映されます。
3. コミットしてプッシュします。

新しい creator スキルを追加するには:

```bash
mkdir -p skills/creator-new-skill
# write SKILL.md and README.md
./install.sh   # create the symlink for the new skill
```

---

## 翻訳

この README と各スキルの `README.md` は 12 言語で利用できます（上部の言語セレクターを参照）。`SKILL.md` の指示ファイルは意図的に英語のままにしています。Claude は実行時にユーザーの言語で応答しますし、正典となる指示セットをひとつに保つことで、スキル名の重複を避けられるからです。

---

## ライセンス

[MIT](LICENSE) © 2026 İlkay Demiralay.
