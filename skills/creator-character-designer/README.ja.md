# キャラクターデザイナー — `creator-character-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

キャラクターを **名前 + 年齢 + 外見** という三要素から引き上げ、**一貫した存在**
として設計するスキル。ドラマ上の機能、心理、伝記、ボディランゲージ、衣装、props、
キャスティングプロファイル、そして **FACS Action Unit でコード化された表情ライブラリ**
を生成します。長尺の AI 映画制作を通じてキャラクターの一貫性を保つ「Character DNA」
アンカーを確立します。

## 哲学

キャラクターはランダムに生成されるものではなく、脚本のニーズ、監督のビジョン、DOP の
視覚世界から導かれます。このスキルは:

- **すべてのキャラクターはあるドラマ上の問いへの答えである** — そうでなければ、そのキャラクターを削ることを提案する
- すべての主要キャラクターについて **Want / Need / Fear / Wound** の四要素を必須で確立する
- **FACS Action Units**:「悲しい」と言う代わりに AU1+AU4+AU15 と表す——
  AI モデルやアニメーターは解剖学的コードをより一貫して解釈する
- **Character DNA**:AI の一貫性のためにロックされたアンカー特徴を定義する
- **Visual distinction audit**:複数のキャラクターがいる場合、シルエット・色・エネルギーの区別を監査する

## 何の役に立つか

| 出力 | 内容 |
|------|------|
| **Character sheet** | キャラクターファイル——心理、衣装、prop、FACS、AI prompt |
| **Costume bible** | 映画全体における衣装のバリエーションと連続性 |
| **Props list** | キャラクターの私物とそのドラマ上の用途 |
| **FACS expression library** | キャラクターごとに 3〜5 の代表的表情、AU コード付き |
| **Casting brief** | 俳優に求めるプロファイル（名前は提案せず、特徴を定義する） |
| **AI prompts** | 一貫したキャラクター参照のための base prompt + シーンのバリエーション |
| **Arc tracker** | 監督の arc tracking と連携したキャラクターの変容 |
| **Continuity notes** | シーンごとの衣装/prop の連続性 |

## いつ動き出すか

- 脚本が手元にあり、キャラクターを発展させたいとき
- 「character sheet を用意して」「衣装を設計して」「キャスティングプロファイルを作って」
- AI 映画のために一貫したキャラクター参照が必要なとき
- 監督または `creator-pipeline-supervisor` がキャラクター段階を委譲したとき
- 既存キャラクターの視覚的区別が問われているとき

## FACS の活用——なぜ、どのように

**Facial Action Coding System（Ekman & Friesen, 1978）** は顔面筋の解剖学的
コード化です。Action Unit（AU）= 特定の筋肉の動き。

### なぜこのスキルはこれを使うのか？

- **AI ジェネレーター** は「happy face」のような抽象的な入力を一貫せず解釈する;
  「AU6 + AU12（Duchenne smile）」のほうがより信頼できる結果を生む
- **アニメーション/VFX チーム** は AU コードを通じて単一の参照セットを共有する
- **キャラクターの代表的表情** はファイル化できる——例えば「Demir は抑え込んだ
  悲しみを AU4 + AU17（眉をひそめ、顎を上げ、AU15 なし）で担う」

### よくある AU の組み合わせ

| 表情 | AU |
|------|-----|
| Duchenne smile（本物の幸福） | AU6 + AU12 |
| Polite smile（作り笑い/社交的） | AU12 単独 |
| 悲しみ | AU1 + AU4 + AU15 |
| 怒り | AU4 + AU5 + AU7 + AU23 |
| 恐怖 | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26 |
| 嫌悪 | AU9 + AU15 + AU16 |
| 驚き | AU1 + AU2 + AU5B + AU26 |
| 侮蔑（非対称） | AU12（片側） + AU14 |
| 抑え込んだ悲嘆 | AU4 + AU17（AU15 なし） |
| 張りつめた静けさ | AU7 + AU23 + AU24 |

## character sheet テンプレート（要約）

```
Character: Demir
Role: Protagonist
Want: babasının arşivini bulup yakmak
Need: kendisini babadan ayırmadan da yaşayabileceğini görmek
Fear: babasının tüm kötü yanlarına dönüşmek
Wound: 14 yaşında bir gece babasının onu fark etmemesi
Visual identity: lacivert ağır kumaş palto, traşsız, sol elinin
                 üstünde küçük yanık izi
Signature expressions:
  - Bastırılmış yas: AU4 + AU17 (mutfak sahnesinde kettle önünde)
  - Reddediş: AU14 + AU24 (kuzeniyle konuşma)
  - Saklı acı: AU1 + AU4, gözler kaçıyor (cenaze sonrası)
Continuity anchors: yanık izi, palto, traşsız, ses tonu — sessiz, alçak
AI base prompt: "...same character across all scenes..."
```

## 出力をどこに書き込むか

`project/characters/{character-slug}/` の下に:

| ファイル | 内容 |
|---------|------|
| `character-sheet.md` | 正典となるキャラクターファイル |
| `costume-bible.md` | すべての衣装バリエーション + 連続性 |
| `props.md` | キャラクターの所持品、ドラマ上の用途 |
| `facs-expressions.md` | 代表的表情ライブラリ、AU コード付き |
| `casting-brief.md` | 俳優プロファイル / AI face prompt の基礎 |
| `ai-prompts.md` | Base prompt + シーンごとのバリエーション |
| `arc-tracker.md` | 監督の arc tracking との sync |
| `continuity-notes.md` | シーンごとの衣装/prop の連続性 |

さらに上位ディレクトリには `cast-list.md` がある——すべてのキャラクターを要約したリスト。

## Visual distinction audit

複数のキャラクターがいる場合、スキルは以下のチェックを行います:

- シルエットの区別（身長、姿勢、衣装の形状）
- 色世界の区別（または意図的な対比）
- エネルギー register の区別
- 話し方パターンの区別
- 画面上の存在感の区別（foreground / background タイプ）

2 人のキャラクターが互いに「混ざり合う」場合、報告して修正を提案します。

## AI の一貫性（Character DNA）

50 シーンにわたって同じ顔/衣装で同一キャラクターを生成するために:

1. **Base prompt** — 主要特徴（顔の形、髪、識別マーク）を固定
2. **Anchor descriptors** — そのうち 2〜3 個が各シーンの prompt で繰り返し登場する
3. **FACS による表情** — 形容詞ではなく AU コード化
4. **早期の character sheet 制作** — front/side/back/close の参照画像
5. **シーン prompt 内での参照**:「consistent with `characters/demir/sheet.png`」

## 他のスキルとの連携

- **読む**:
  - `project/screenplay/character-brief.md`
  - `project/continuity/creator-director-vision.md`
  - `project/continuity/performance-notes/*`
  - `project/production-design/cinematography/visual-language.md`
  - `project/production-design/world-bible.md`
- **書く**:`project/characters/*`
- **委譲する**:プロンプトエンジニア、storyboard、DOP（パレット調整）
- **フィードバックを受ける**:監督、Pipeline Supervisor

## 衣装デザインのアプローチ

衣装はキャラクターを語る——単に「着ている」ものではない:

- 主要パーツ + その機能
- 生地:重い、柔らかい、硬い、繊維質
- 色:パレットとの調和/対比
- 着古し / 新しさ / 損傷 / 修繕の跡
- 時代考証の正確さ
- キャラクターの心情との関係
- 可動性への影響
- 光との相互作用（マット、光沢、透明、埃をまとう）

各メインシーンごとに衣装の連続性ノートを:シーン内で変わるのか、シーン間で変わるのか、
なぜ?

## props のアプローチ

props は物語の道具である——装飾ではない:

- 名前 + 機能
- キャラクターとの関係
- 外観、素材、色、状態
- キャラクターにとっての意味（形見、アイデンティティ、関係）
- ドラマ上の用途（伏線、payoff、開示）
- カメラがどう捉えるか（近接、ディテール、通り過ぎる）
- 連続性（各シーンでどこにあるか）

キャラクター-prop / ロケーション-prop の所有を明確にし、
**creator-production-designer** と連携します。

## 振る舞いのルール

| する | しない |
|------|--------|
| ドラマ上の根拠とともにキャラクターを生成する | 「もう一人キャラクターが必要」と言う |
| すべての視覚的選択を arc / 機能 / テーマに結びつける | 孤立した美的選択をする |
| 情報が欠けているときに質問する | こっそり捏造する |
| 文化的ディテールを調査する | 推測を事実として提示する |
| FACS AU コードで表情を定義する | 「悲しい」のような形容詞を使う |
| visual distinction audit を行う | 2 人のキャラクターを混ぜ合わせる |
| continuity anchors を AI prompts に埋め込む | 各シーンでゼロから記述する |
| キャラクター-prop の所有を明確にする | プロダクションデザイナーと重複する |
| 構造化された downstream-readable なファイルを渡す | 一塊のテキストをぶちまける |
