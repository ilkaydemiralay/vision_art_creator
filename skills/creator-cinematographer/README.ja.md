# 撮影監督 — `creator-cinematographer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

脚本と監督のビジョンを**映画的なビジュアル言語**へと翻訳する skill。光、カメラ、レンズ、
フレーミング、色、空気感、動き——あらゆるビジュアル上の判断が、ドラマ上の根拠に結び
ついている。「見栄えが良い」では不十分であり、**motivated lighting**、
**chiaroscuro**、**depth as psychology**、**camera as character** の論理で動作する。

## 哲学

DOP は単に「良い画」を作る人ではない。DOP は**ビジュアルの意味のエンジニア**である。
この skill は：

- **Motivated lighting**：すべての光源にはシーンの世界における理由がある
- **Chiaroscuro**：光と影のコントラストは意味を担い、単なる美ではない
- **Depth of field**：被写界深度は心理的な選択である
- **Negative space**：余白＝孤独／孤立
- **Camera as character**：カメラは観察者か、追跡者か、それとも告発者か？
- AI 制作の制約を**知り**、リスクに flag を立てる存在

## 何の役に立つか

| アウトプット | 内容 |
|-------|--------|
| **Visual language doc** | リファレンスとともに映画のビジュアルコンセプトを定義する |
| **Lighting bible** | 映画全体で一貫した照明アプローチ |
| **Color script** | 映画のカラー進行（シーンごと） |
| **Lens list** | シーンタイプごとのレンズ選択とその根拠 |
| **Per-scene plan** | シーン単位の照明＋カメラ＋レンズ＋色のプラン |
| **Moodboard** | リファレンス画像の説明、出典付き |
| **AI cinema prompts** | 撮影の知識を AI プロンプトへ翻訳する |
| **DOP notes to/from creator-director** | 監督との双方向のコミュニケーション |

## いつ働き始めるか

- 脚本＋監督のビジョンがあり、ビジュアルデザインが必要なとき
- 「このシーンはどう照明すべきか／どのレンズか／どのフレーミングか」
- カラーパレットまたは color script が求められるとき
- AI 制作のための映画的プロンプトへの翻訳
- `creator-pipeline-supervisor` が DOP フェーズを委譲したとき
- 監督がカメラ／照明について具体的なフィードバックを求めたとき

## 典型的なフロー

1. **ブリーフィング**と `creator-director-vision.md` の読み込み
2. **質問ラウンド**：ジャンル、トーン、リファレンス、時代、AI ツール
3. **Visual language**：master palette、リファレンス映画、ビジュアルマニフェスト
4. **Lighting bible**：映画全体の照明アプローチ
5. **Color script**：ドラマのアークに沿ったカラーの変容
6. **Per-scene**：シーンごとのプラン
7. **AI prompt hand-off**：構造化された映画的知識を creator-prompt-engineer へ

## アウトプットの書き込み先

`project/production-design/cinematography/` の下：

| ファイル | 内容 |
|-------|--------|
| `visual-language.md` | 映画全体のビジュアルマニフェスト |
| `lighting-bible.md` | マスターとなる照明アプローチ |
| `color-script.md` | シーンごとのカラー進行 |
| `lens-list.md` | レンズ選択と根拠 |
| `scene-{NN}.md` | シーンごとのプラン（照明＋カメラ＋レンズ＋色） |
| `moodboard.md` | リファレンス画像の説明 |
| `notes-to-creator-director.md` | 監督への質問／提案 |
| `ai-production-cinema-notes.md` | AI 制作のための映画ガイド |

## レンズの心理学（要約）

| Focal | 効果 | 用途 |
|-------|------|----------|
| 14–24mm wide | ディストーション、閉所恐怖 | 夢／悪夢、攻撃的な接近 |
| 28–35mm | ドキュメンタリーの質感 | 自然、観察的 |
| 40–50mm | アイレベル | ニュートラル、親密な対話 |
| 75–100mm | 圧縮、孤立 | 美、憧憬、監視 |
| 135mm+ | 強い圧縮 | 距離、恐怖 |
| Anamorphic | ワイドな aspect、楕円の bokeh | 叙事的、映画的 |
| Macro | 極端なディテール | オブジェクトの意味、感覚的 |

## 光の言語（要約）

- **Key**：メイン光源——シーンの世界においてどこから来るのか？
- **Fill**：影のモジュレーション、レシオの選択
- **Backlight**：背景からの分離、rim halo
- **Practical**：ランプ、ろうそく、炎、スクリーン——シーン内の実在する光源
- **Hard vs. soft**：硬さは質感を露わにし、意図を定める
- **Color temp**：warm（3200K、親密／記憶）、cool（5600K+、距離／臨床的）、mixed（緊張）
- **Contrast**：高（ドラマ、noir）、低（ドキュメンタリー、メランコリー、夜明け）

## 他の skill との連携

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

- **読む**：`project/screenplay/*`、`creator-director-vision.md`、`notes-to-dop.md`、
  プロダクションデザインのアウトプット、キャラクターのカラーパレット
- **書く**：`project/production-design/cinematography/*`
- **委譲する先**：Prompt engineer、storyboard、shot-list designer
- **フィードバックを受ける相手**：監督、Pipeline Supervisor

## AI 制作のための映画的プロンプト形式

撮影を AI プロンプトへ翻訳する際、常に以下を含める：

- Shot scale ＋ アングル
- Lens（focal ＋ DoF の効果）
- 光の方向、質、色温度
- カラーパレットと mood
- 空気感（霧、煙、雨、塵）
- ロケーションの詳細（時代、質感、素材）
- キャラクターの位置とアクション
- Aspect ratio（2.39:1、1.85:1、16:9、9:16）
- スタイルリファレンス（映画タイトル、写真家、時代）
- Negative prompt（除外要素）

この構造は `creator-prompt-engineer` skill への hand-off に向けて準備が整っている。

## ふるまいのルール

| する | しない |
|-------|--------|
| すべての光にドラマ上の根拠を与える | 「良く見えるように」と言う |
| motivated lighting を適用する | 光源の不明な光を置く |
| レンズの心理学を説明する | 美的理由でレンズを選ぶ |
| カラーパレットを監督／プロダクション／キャラクターと連携させる | 孤立して決定する |
| AI リスクに flag を立てる | 制作不可能なシーンを計画する |
| low-budget の代替案を提示する | 理想版だけを書く |
| 歴史的時代を調査し、ラベル付けする | 解釈を事実のように提示する |
| 撮影前に `notes-to-creator-director.md` で質問を伝える | 黙って先へ進む |
