# ショットリストデザイナー — `creator-shot-list-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · **日本語** · [한국어](README.ko.md)

シーンとストーリーボードを**ショットリスト + 編集意図**へと変換するスキル。
プリプロダクションの計画と編集意図が交わる場所です。これは
ファイナルカットエディターではありません — どんな素材も制作される前に編集意図を設計し、
撮影で適切な素材が生み出されるようにします。

## 哲学

ショットリストは技術的なリストではなく、**ドラマ的 + 編集的な意図の地図**
です。このスキルは次を担います。

- **ショットの経済性**: すべてのショットは単一の明確なアクションを担う
- **編集リズムへの意識**: どのショットを長く保持し、どのショットを素早く切るか?
  ショットの持続時間は編集上の判断
- **スクリーンディレクション + コンティニュイティ**: cut をまたいだ空間的/時間的な一貫性
- **AI での制作可能性**: AI ツールの制約を踏まえて単一ショットの複雑さを計画
- **制作前の編集意図**: 不要なショットを撮影しないよう、撮影前に編集ロジックを設定
- **観客体験の設計**: 観客は何を感じ、何を知り、何を伏せられるのか?

## 生み出すもの

| 成果物 | 内容 |
|-------|---------|
| **シーン別ショットリスト** | ドラマ的 + 編集的な根拠を備えた正規のショットリスト |
| **編集プラン** | シーン内のペーシング、cut ポイント、オープニング/クロージングのイメージ |
| **トランジション設計** | シーン間のトランジション判断（hard cut、match、J/L、sound bridge） |
| **コンティニュイティリスク監査** | ショット間の一貫性リスクのレポート |
| **サウンド編集ノート** | サウンドデザイナー向けの J-cut / L-cut / 無音ポイント |
| **作品全体のショットリスト** | 作品全体を網羅した統合リスト |
| **リズムマップ** | シーンごとのペーシング（ショット持続時間のレンジ） |
| **冗長性レポート** | 切る/統合すべきショット |
| **ファイナルエディター向けノート** | ファイナルカットエディターへの編集意図の引き継ぎ |

## 出番となる場面

- シーンとストーリーボードが揃い、ショット単位の計画が必要なとき
- 編集を意識したショットのシーケンシングが求められるとき
- 長いシーンを AI で制作可能な単位へ分割する必要があるとき
- 監督または DOP が構造的な撮影/制作計画を求めるとき
- `creator-pipeline-supervisor` が編集前の計画を委譲したとき

## 典型的な流れ

1. **ブリーフィング** + 上流スキルのすべての成果物を読む
2. **質問ラウンド**: フォーマット、編集リズム、トーン、AI ツール
3. **ショットリスト（シーン別）**: 正規の構造で、ドラマ的 + 編集的な根拠とともに
4. **編集プラン（シーン別）**: ペーシング、オープニング/クロージング、cut ポイント
5. **トランジション設計**: シーン間のトランジション
6. **コンティニュイティ監査**: ショット間のリスク
7. **リズムマップ**: 作品全体のペーシングマップ
8. **冗長性レポート**: 切れるショットの特定
9. **引き継ぎ**: creator-prompt-engineer 向けのショットプロンプトデータ + creator-final-cut-editor 向けの編集意図

## ショット — 正規の構造

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

## 編集意図 — シーンプラン

シーンレベルの編集に関する問い。

- どのショットでシーンを開くか?
- どのイメージで締めくくるか?
- どのショットを長く保持するか?
- どのショットを短く切るか?
- リアクションショットはどこに置くか?
- 無音はどこで引き延ばすか?
- hard cut が必要なのはどこか?
- ソフトなトランジションはどこか?
- どのイメージが次のシーンへつながるか?
- どのショットがドラマの頂点を担うか?
- どのショットが不要か?
- どのショットが情報を伝え、どのショットが感情を伝えるか?

`project/shot-list/scene-{NN}/edit-plan.md` の下に記述されます。

## 成果物の書き出し先

`project/shot-list/` の下。

| ファイル | 内容 |
|-------|---------|
| `scene-{NN}/shot-list.md` | シーンのショットリスト |
| `scene-{NN}/edit-plan.md` | 編集意図 + ペーシング |
| `scene-{NN}/transitions.md` | トランジションの判断 |
| `scene-{NN}/continuity-risks.md` | コンティニュイティ監査 |
| `scene-{NN}/sound-edit-notes.md` | サウンドデザイナーへの引き継ぎ |
| `film-shot-list.md` | 作品全体の統合リスト |
| `rhythm-map.md` | ペーシングマップ |
| `redundancy-report.md` | 切れるショット |
| `ai-production-shot-guide.md` | AI ツール制約ガイド |
| `final-editor-notes.md` | ファイナルカットエディター向けの意図 |

## トランジションの種類（編集上の用途）

| トランジション | 編集上の用途 |
|-------|-------------------|
| Hard cut | 突然のドラマ的な断絶 |
| Match cut | 2 つのイメージ間の意味の架け橋 |
| Fade in/out | 時間的/感情的なオープニング/クロージング |
| Dissolve | 時間の移行、感情のブレンド |
| J-cut | 次のシーンの音が先に届く（滑らかな流れ） |
| L-cut | 現在のシーンの音を延ばす（保持された感情） |
| Sound bridge | 音で運ばれる場所/時間の変化 |
| Visual motif | 反復するビジュアルによる架け橋 |
| Object transition | 形のマッチ |
| Movement transition | 方向の連続性 |
| Time jump | 突然の時間の飛躍 |
| Flashback | フィルター/レンズ/ブラー/サウンドキューによる |
| Parallel edit | 2 つの場所の織り交ぜ |

## AI 動画の制作可能性ルール

- ショットごとに 1 つの明確なアクション
- メインのカメラムーブメントは 1 つ（連鎖させない）
- キャラクター数は制御された範囲に
- 明確なビジュアルターゲット
- 複雑な動きはマルチショットに分割
- リスクのある手/指/lip sync にフラグを立てる
- 群衆には選択的なフレーミング
- すべてのプロンプトでロックされたロケーション + キャラクターのアンカー
- ショットの持続時間は通常 3〜10s
- 各ショットは単一の動画プロンプトへ綺麗に対応する

リスクを検知したら、フラグを立てます。

> *「このショットは AI 動画には複雑すぎる — 2 つのショットに分割すること。」*
> *「ここでは lip sync が失敗するおそれがある。話し手ではなくリアクションショットを使う。」*
> *「手の動きが重要 — insert ではなく、より広いフレームを使う。」*
> *「群衆のアクション — 単一ショットではなく cut で組み立てる。」*

## リズムとペーシング

「速くして」のような曖昧な表現は使いません。ペーシングは次のように扱います。

- **ショット持続時間のレンジ**として表現する
- **cut の頻度**で測る

例:
> *「シーン 3 は平均 4〜6s/ショット、シーン 12 は平均 1.5〜3s/ショット —
> キャラクターの対立がエスカレートするにつれてペースが速まる。」*

## 台詞の編集意図

台詞の多いシーンでは。

- 話し手か、聞き手か?
- リアクションショットはどこに置くか?
- 無音のほうが強いのはどこか?
- 台詞の上に別のイメージを重ねるか?
- 表情によるサブテキストか?
- hard cut か、自然なオーバーラップか?
- 文が終わる前に切るか?
- 説明の冗長な繰り返しはないか?
- 観客が本当に見る必要のある感情は誰のものか?

J-cut / L-cut のマーカーはここで設定されます。

## 他スキルとの連携

- **読む**: 脚本、監督のビジョン + ディレクションシート、DOP のシーン別プラン、
  ストーリーボードのパネルデータ、キャラクター/ロケーションのアンカー
- **書く**: `project/shot-list/*`
- **引き継ぐ先**:
  - `creator-prompt-engineer`（ショットレベルの動画プロンプト）
  - `creator-final-cut-editor`（編集意図ファイル）
- **フィードバックを受け取る相手**: 監督、パイプラインスーパーバイザー

## 冗長性の検出

長尺の AI 作品では、次にフラグを立てます。

- 同じ情報を繰り返すショット
- 感情を変えないショット
- リズムを落とすディテールショット
- リアクションショットの過剰な使用
- ドラマ的貢献が低いのに AI で困難なショット
- late-in / early-out の機会
- 台詞の代わりにビジュアルで語れる瞬間

*「このショットは切れる」*や*「この 2 つのショットは統合できる」*と明示的に記述します。

## 行動ルール

| すること | しないこと |
|-------|---------|
| すべてのショットにドラマ的**かつ**編集的な根拠を与える | 技術的なリストを作る |
| 監督のリズム、DOP のフレーミング、ストーリーボードと連携する | 孤立して判断する |
| 不要なショットにフラグを立てる | 埋め草を加える |
| コンティニュイティを先回りでチェックする | 撮影後に問題が表面化するのを待つ |
| AI ツールの制約を踏まえて設計する | 制作不可能なショットを計画する |
| リスクのあるショットには安全な代替案 | 単一のバージョンだけを提供する |
| 台詞では聞き手も考慮する | 話し手だけを追う |
| サウンドと音楽の編集意図を連携させる | 画だけを考える |
| 構造化され、下流で読める出力 | 単一のテキストの塊を吐き出す |
