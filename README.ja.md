# vision_art_creator

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · **日本語** · [한국어](README.ko.md)

> [Claude Code](https://claude.com/claude-code) のための、AI 映画制作スキルパック。

`vision_art_creator` は、**11 個の `creator-*` スキル**をひとつのリポジトリにまとめたもので、脚本から最終的なファイナルカットに至るまで、映画制作のあらゆる部門をカバーします。`git clone` と `./install.sh` さえあれば、どのマシンにもインストールできます。

> これらのスキルは互いを参照し合うように設計されています（`creator-pipeline-supervisor` が残りのスキルを統括します）。すべてをまとめてインストールすることをおすすめします。

---

## インストール

```bash
git clone https://github.com/<your-username>/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
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

## 更新

```bash
cd ~/projects/vision_art_creator
git pull
```

スキルはシンボリックリンクになっているため、追加の手順は不要です。

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
