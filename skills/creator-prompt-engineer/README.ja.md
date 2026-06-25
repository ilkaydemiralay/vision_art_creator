# プロンプトエンジニア — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · **日本語** · [한국어](README.ko.md)

クリエイティブ・パイプラインと AI ジェネレーターをつなぐ**翻訳レイヤー**。
脚本家・監督・撮影監督・キャラクター・プロダクション・ストーリーボード・ショットリスト
の各スキルが生み出した判断を、**本当に生成可能で一貫した**プロンプトへと変換する。
ツールごとに最適化し（Midjourney ≠ Sora ≠ Stable Diffusion）、ロックされたアンカーを
すべてのプロンプトに埋め込み、リスクの高いシーンには安全な代替案を生成する。

## 哲学

プロンプトエンジニアは**ビジュアルを発明しない** — 上流（upstream）の判断を
エンコードする。このスキルは：

- **Locked anchors**：character DNA + location master reference + style block —
  50 個のプロンプトを経ても、同じキャラクターが同じ顔で出てくる
- **Tool fitness**：各 AI ツールにはそれぞれ固有のプロンプト言語がある
- **Producibility audit**：このシーンはジェネレーターを打ち負かす — 代替案を提示する
- **Consistency discipline**：長編では、プロンプトは孤立した存在ではなくシステムである
- **FACS expression coding**：「悲しい」ではなく AU1 + AU4 + AU15 — より一貫した結果
- **上流を黙って上書きしない**：必要ならフラグを立てて問い返す

## 何の役に立つか

| 出力 | 内容 |
|------|------|
| **Character prompts** | ロックされた DNA + シーンごとのバリエーション |
| **Location prompts** | Master reference + 昼/夜/天候のバリエーション |
| **Style anchors** | 作品全体のビジュアル/技術ブロック |
| **Negative prompts** | カテゴリ別のネガティブプロンプト・バンク |
| **Panel prompts** | ストーリーボードのコマから画像を生成するプロンプト |
| **Shot prompts** | ショットリストから AI 動画を生成するプロンプト |
| **Character sheets** | 正面/側面/背面/クローズの参照生成 |
| **Producibility risk report** | シーン/ショット単位のリスク + 安全な代替案 |
| **Tool guide** | オペレーター向けのツール固有メモ |

## いつ稼働するか

- 制作前に AI 画像/動画プロンプトが必要なとき
- キャラクター/ロケーションの一貫性のためアンカーシステムを構築すべきとき
- ストーリーボードやショットリストの出力をツールプロンプトに変換するとき
- 既存のプロンプトがリスキー — 安全な代替案がほしいとき
- `creator-pipeline-supervisor` がプロンプト工程を委譲したとき

## ツール最適化ガイド（要約）

### Midjourney
- `--ar`、`--style raw`、`--s` パラメータ
- キャラクター参照用の `--cref` と `--cw`
- スタイル参照用の `--sref`
- 簡潔な記述 — 形容詞の積み重ねはシグナルを弱める

### DALL·E
- 自然言語 > タグの羅列
- 空間的な関係を書き出す
- 画像内テキストの生成を避ける

### Stable Diffusion (SDXL / SD3)
- Positive + negative を分離
- キャラクターの一貫性のための LoRA / reference / seed メモ
- 重要な語を先頭へ（token weight）

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- 主要なカメラ動作はひとつ
- キャラクター数を制御
- 明確な opening + closing frame
- 尺は短め（一般に 3〜10 秒）
- ツール固有の上限：
  - Sora 2：約 20 秒
  - Kling 3.0：一貫性のための subject binding
  - Veo：motion fidelity が強い
  - Runway Gen-3/4：動きは妥当、lip sync は弱い

## ロックされたアンカーシステム（長編向け）

### Character DNA block

`project/characters/{slug}/ai-prompts.md` から**そのまま逐語的に**コピーする：

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

`project/production-design/locations/{slug}/master-reference.md` から逐語的に：

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

これらのブロックは、そのシーン/キャラクター/ロケーションの**すべてのプロンプトで
そのまま繰り返される**。この規律こそ一貫性のエンジンである。

## ネガティブプロンプトのカテゴリ

| 問題 | ネガティブ語 |
|------|--------------|
| 顔の歪み | distorted face, malformed face, asymmetric eyes, blurred features |
| 手のエラー | extra fingers, missing fingers, fused fingers, deformed hand |
| 時代錯誤 | modern clothes, modern tech, plastic, neon, smartphone |
| AI アーティファクト | warping, morphing, flickering, jittery motion |
| 品質 | low quality, low resolution, jpeg artifacts, oversaturated |
| テキスト | unwanted text, watermark, signature, logo |
| 構図 | extra characters, cropped subject, duplicate subject |
| カメラ | unintended shake, fisheye distortion |

一部のツールはネガティブプロンプトを無視する — その場合は positive prompt の中に
*"avoid: ..."* のヒントとして書く。

## AI 動画 producibility 監査

動画プロンプトを発行する前のチェック：

- 単一ショットにアクションが多すぎないか？
- キャラクター数が多すぎないか？
- カメラ動作が複雑すぎないか？
- 手/指/顔のディテールがリスキーでないか？
- 衣装/小道具の一貫性を保てるか？
- ロケーションが混み合いすぎていないか？
- 光と時間帯は一貫しているか？
- シーンを単一プロンプトでなく分割すべきか？
- lip sync が必要か？（フラグを立てる）
- プロンプトが不必要に抽象的でないか？

リスクがあれば**安全で簡素化された代替案**を提示する。

## バリエーション生成

同じシーンに対するフォーカスしたバリエーション：

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

各バリエーションの**目的を明記する** — なぜ、どの場合に使うのか。

## 出力をどこに書き出すか

`project/prompts/` 配下に：

| ファイル | 内容 |
|------|------|
| `character-prompts/{slug}.md` | ロックされた DNA + シーンのバリエーション |
| `location-prompts/{slug}.md` | Master anchor + バリエーション |
| `style-anchors.md` | 作品全体の style block(s) |
| `negative-prompts.md` | ネガティブプロンプト・バンク |
| `scene-{NN}/panel-{PP}.md` | パネル画像プロンプト |
| `scene-{NN}/shot-{SS}.md` | ショット動画プロンプト |
| `character-sheets/{slug}.md` | 正面/側面/背面/クローズのシート生成プロンプト |
| `prompt-system.md` | アンカーシステムのドキュメント |
| `producibility-risk-report.md` | リスクフラグ + 安全な代替案 |
| `tool-guide.md` | ツール固有のオペレーター・メモ |

## 二言語プロンプト形式

ユーザーが母語の説明 + 英語プロンプトを望むとき：

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

## 他スキルとの連携

- **読む**：すべての上流クリエイティブ出力
- **書く**：`project/prompts/*`
- **委譲する**：
  - AI ツールを実行する人間のオペレーターへ
  - producibility 監査が上流の変更を要する場合は **storyboard artist** または
    **shot-list designer** へフィードバック
- **フィードバックを受ける**：Pipeline Supervisor（一貫性のドリフト）

## 行動ルール

| する | しない |
|------|--------|
| マルチショット作業ではロックされたアンカーを各プロンプトに入れる | 毎回ゼロから記述する |
| ツールに適合したプロンプトを書く | 同じプロンプトをすべてのツールに渡す |
| producibility 監査 + 安全な代替案 | リスクを黙ってやり過ごす |
| FACS AU コードを使う | 「悲しい」のように形容詞を積み上げる |
| 形容詞の過剰を減らす | 飾り立てた言葉で埋める |
| 上流の判断を保ち、黙って上書きしない | 創作的な発明を加える |
| 時代考証を尊重する | 時代錯誤を放置する |
| 構造化され下流で読める出力 | 単一ブロックのプロンプトを吐き出す |
| 母語の説明 + 英語プロンプト形式（依頼があれば） | 常に英語を強制する |
