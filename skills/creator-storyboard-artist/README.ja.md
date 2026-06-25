# ストーリーボードアーティスト — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

書かれた脚本を**読みやすい視覚的語り**へと変換するスキル。パネル数を最小化する
ことで、各パネルがドラマ的な理由をもって存在することを保証する。シーンの決定的
な瞬間を捉え、screen direction を維持し、eyeline continuity を追跡し、
AI image/video prompt へ明確に hand-off する。

## 哲学

ストーリーボードは「シーンの作画」ではなく、**視覚的語りのシステム**である。このスキルは：

- **Panel economy**：少ないパネル + 鋭い選択 — 多いパネル + 弱い判断ではない
- **Screen direction（180°）** と **eyeline continuity**：カット間の空間的一貫性
- **Graphic dynamics**：視線はどこに落ちるか？フォーカスは何か？
- **Continuity awareness**：衣装、ロケーション、光の方向、画面の方向、動き
- **Locked anchors**：各パネルにおける character DNA + location master reference
- **Producibility**：AI 生成の制約を理解し、リスクのあるシーンを flag する

## 何の役に立つか

| 出力 | 内容 |
|------|------|
| **Per-scene storyboard** | シーンごとのパネルリスト（全パネルデータ） |
| **Per-panel sheets** | 複雑なシーン向けの詳細な単一パネルファイル |
| **AI image prompts** | パネルごとの生成可能な prompt |
| **AI video prompts** | 動きのあるパネル向けの video prompt |
| **Continuity log** | 衣装/ロケーション/方向のリスクの flag |
| **Animatic plan** | 全シーンの animatic 順序を計画する |
| **Director / DOP notes** | 監督と DOP への簡潔な視覚的/技術的メモ |
| **Handoff to shot-list** | creator-shot-list-designer 形式のパネルデータ |

## いつ起動するか

- 脚本が手元にあり、視覚的な分割が求められるとき
- 監督がシーンを事前に視覚化したいとき
- DOP のレンズ/光の決定の前に視覚的コンセプトが必要なとき
- AI prompt 生成の前にストーリーボードの論理が求められるとき
- `creator-pipeline-supervisor` がストーリーボード段階を委任したとき

## Panel content（正準フィールド）

各パネルは以下のフィールドを記録する：

```
Scene 04 — Panel 04.03
Shot type: medium close
Camera angle: eye level
Frame: Demir merkez-sağ; kettle ön plan-sol; arka plan
       dolap soft-focus; sağ kenar negatif alan açık
Lens feeling: 50mm (eye-equivalent, samimi)
Character position: Demir sandalyede, omuzlar düşmüş, eller masada
Character movement: yok — duraksama
Camera movement: static
Setting / dressing: kireçli mutfak — pencere doğu, kettle ateşte
Light / atmosphere: pencereden yumuşak gri sabah, mum yok
Emotional emphasis: bastırılmış yas; ilk gerçek duygu kırılması
Dialogue / action note: sessizlik; kettle ıslığı
Dramatic justification: Demir'in iç çatışmasını yüzeye getiren ilk an
Transition to next panel: J-cut — kettle sesi devam ederken Panel 4.04 başlar
AI image prompt: [tam prompt]
AI video prompt: [tam prompt, 6s]
Continuity note: palto sahne başında; ceket askıda; kettle aktif
```

## 出力の書き込み先

`project/storyboards/` の下：

| ファイル | 内容 |
|----------|------|
| `scene-{NN}/storyboard.md` | シーン単位のパネルリスト（正準） |
| `scene-{NN}/panel-{PP}.md` | 詳細な単一パネル（複雑なシーンで） |
| `scene-{NN}/prompts.md` | パネルごとの AI prompt（image + video） |
| `scene-{NN}/continuity.md` | Continuity の flag |
| `animatic-plan.md` | 全編の animatic 順序メモ |
| `notes-to-creator-director.md` | 監督への質問/注意 |
| `handoff-to-shot-list.md` | shot-list designer 向けの整形済みパネルデータ |

## Shot type 用語集（ドラマ的対応つき）

| タイプ | ドラマ的用途 |
|--------|--------------|
| Establishing | 空間内で観客を位置づける |
| Master | シーンの幾何、fallback |
| Wide/Full | キャラクターと環境の関係 |
| Medium | 中立的な対話 |
| Close | 内的葛藤、親密な感情 |
| Extreme close | 主観的強度 |
| Insert | 物体の強調 |
| Cutaway | 並行/外部の情報 |
| Reaction | アクションよりリアクション |
| OTS | 対話の視点 |
| POV | キャラクターの主観性 |
| 2-shot / group | 関係性の幾何 |
| Silhouette | 匿名性、ミステリー |
| Negative-space frame | 孤立、小ささ |
| Symmetrical | 力、形式性、不穏な静止 |
| Tracking | 継続的な追従 |
| Static | 観察、沈黙の意味 |

「close-up を使え」では足りない — **なぜ** close-up が必要かが問われる。

## Continuity audit

パネルからパネルへ、シーンからシーンへの追跡：

- 衣装
- 髪/メイク/アクセサリー
- ロケーションのアイデンティティ（locked anchor とともに）
- 光の方向
- 昼/夜
- Screen direction（180° ルール）
- キャラクターの空間的論理
- アクションの流れ
- prop の位置

リスクが検出された場合、パネルの `continuity note` フィールドに明示的に書き込まれる。

## 他のスキルとの連携

- **読む**：脚本、監督のビジョン + direction sheets、DOP の per-scene plan、
  character DNA + FACS、ロケーションの anchor
- **書く**：`project/storyboards/*`
- **委任する**：
  - `creator-shot-list-designer`（panel → shot list）
  - `creator-prompt-engineer`（panel prompt → ツール固有の最適化）
- **フィードバックを受ける**：監督、Pipeline Supervisor

## AI 生成に焦点を当てた解決策

- 複雑なシーンを単純なパネルに分割する
- 複数キャラクターのシーンで視覚的フォーカスを明確にする
- AI が苦手とする動きを簡素化する
- 同じロケーション/キャラクターに固定 anchor を使う
- カメラの動きの代わりに安全な静止ショットの代替を提示する
- 混雑したシーンで選択的なフレーミングを提案する
- 速いアクションの代わりにリズミカルなカットを提案する

## 振る舞いのルール

| する | しない |
|------|--------|
| 各パネルにドラマ的根拠を書く | 埋めるために「もう一枚パネル」を入れる |
| 少ないパネル + 鋭い選択 | 多いパネル + 弱い判断 |
| 脚本家 + 監督 + DOP + キャラクター + 製作を統合する | upstream を黙って上書きする |
| screen direction と eyeline を維持する | カットで方向を混乱させる |
| locked anchor を各 prompt に入れる | 各パネルでゼロから記述する |
| 複雑なシーンをパネルに分割する | 単一の過負荷な frame に詰め込む |
| AI リスク flag + 安全な代替 | 生成不可能な動きを提案する |
| 構造化され、下流で読める出力 | 単一のテキストブロックを吐き出す |
