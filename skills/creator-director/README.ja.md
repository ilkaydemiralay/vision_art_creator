# 監督 — `creator-director`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · **日本語** · [한국어](README.ko.md)

AI映画制作における**クリエイティブ・リーダー**。脚本を読み解いて解釈し、なぜすべてのシーンが存在するのかを問い、演技の演出を与え、カメラ・照明・音響の判断をドラマ的意図に結びつけ、すべての部門を単一の映画的ビジョンのもとに統合するスキルです。脚本そのものを書くわけでも、シーンをパネルへ分解するわけでもなく、他者の仕事を**演出する**ものです。

## 哲学

監督業は技術的スキルではなく、**全体的なドラマ的思考**です。このスキルは次のことを行います。

- シーンごとに**映画の核となる感情**を決して見失わないことを執念とする
- **演じられる動詞（playable verbs）**を用いる。「悲しんで」ではなく、「説得する」「隠す」「守る」と言う
- **ミザンセーヌ（mise-en-scène）**と**プロクセミクス（proxemics）** — 構図と距離が意味を担う
- **サブテキスト（subtext）** — 登場人物が何を言うかではなく、なぜそれを言うのか、それこそが重要
- **キャラクターDNA + ビジュアル・グラウンドトゥルース** — AIの一貫性のためにキャラクターとロケーションのアンカーを確立する
- **すべての演出上の判断はドラマ的根拠を伴う** — 「見栄えがいい」だけでは不十分

## できること

| アウトプット | 内容 |
|--------|--------|
| **Vision document（ビジョン文書）** | 映画の核となる感情、テーマ、リズム、演技のトーン、ビジュアルの世界 |
| **Direction Sheet（シーンごと）** | そのシーンのドラマ的目的、サブテキスト、演技の演出、カメラのアプローチ |
| **演技ノート** | キャラクターごと：登場時に何を感じているか、何を望むか、それをどう示すか |
| **キャラクターアークの追跡** | 映画全体にわたるキャラクターの変化のマップ、転換点となるシーン |
| **トーン監査** | 全シーンにわたるトーンの一貫性レポート、破綻と修正の提案 |
| **creator-screenwriter へのノート** | 構成上・ドラマ上のフィードバック — なぜそのシーンが弱いか、どう強化するか |
| **DOP へのノート** | カメラ・照明・レンズの判断への具体的なコメント（曖昧でない） |
| **エディターへのノート** | ペーシング、カッティング、並行編集、トランジションのノート |
| **AI制作ガイド** | どのシーンがリスクを伴うか、代替アプローチ |

## 発動するタイミング

- 脚本が手元にあり、**クリエイティブなビジョン**が求められているとき
- 「このシーンはどう撮るべきか」「どんな雰囲気にすべきか」「何が強くて何が弱いか」
- 映画全体のトーンの一貫性をチェックするとき
- DOP やキャラクターデザイナーがクリエイティブな判断の裁定者を必要とするとき
- `creator-pipeline-supervisor` が演出フェーズを委譲するとき
- 脚本家が改稿前に構成上のフィードバックを求めるとき

## 典型的なフロー

### 新規プロジェクト
1. **ブリーフィング**：脚本、トリートメント、または物語のアイデア
2. **質問ラウンド**：核となる主題、目標とする感情、トーンのレジスター、参照作品、フォーマット、AIツール
3. **Vision document**：映画の哲学的・ドラマ的フレームワーク → `project/continuity/creator-director-vision.md`
4. **シーンごとのパス**：各シーンの Direction Sheet
5. **スキル横断の調整**：DOP、キャラクター、プロダクション、サウンド、エディターへの具体的なノート
6. **トーン監査**：全シーンを並べて見る — トーンの破綻はないか？

### 進行中のプロジェクト
- 脚本の改稿が来たら Direction Sheet を更新する
- DOP や他のスキルの提案をビジョンに照らして監査し、必要なら却下する
- Pipeline Supervisor が継続性の衝突を報告したときに判断を下す

## アウトプットの書き出し先

`project/continuity/` 配下：

| ファイル | 内容 |
|------|--------|
| `creator-director-vision.md` | 最上位のビジョン文書 |
| `direction-sheets/scene-{NN}.md` | シーンごとの演出プラン |
| `performance-notes/{character}.md` | キャラクターごとの演技 + アークのノート |
| `tone-audit.md` | トーンの一貫性レポート |
| `revision-notes-to-creator-screenwriter.md` | 脚本家への構成上のフィードバック |
| `notes-to-dop.md` | DOP へのカメラ・照明・レンズのノート |
| `notes-to-editor.md` | エディターへのペーシング・カッティング・トランジションのノート |
| `ai-production-guide.md` | AI制作の指示、リスク警告 |

## Direction Sheet テンプレート（シーンごと）

```
Scene: 04 — "Mutfak / Cenaze Sonrası"
Location / Time: INT. Mutfak — Gece
Dramatic Purpose: Demir babanın ölümünün ardından evdeki sessizlikle yüzleşir
Core Emotion: Yorgunluk, içe dönük öfke, hâlâ ifade edilmemiş yas
Subtext: Çay yapma ritüeli, eskiden babanın yaptığı şey
Character entry state: Demir savunmacı, başkalarıyla konuşmuş, içinde biriktirmiş
Character exit state: Tek başına, ilk samimi an
What changes: İlk gerçek duygu kırılması
Performance direction:
  - Verbs: defend → release → mourn
  - Beden dili: aşırı kontrollü, su koyuş hareketi mekanik
  - Göz teması: yok; kettle'a bakıyor ama görmüyor
  - Konuşma: sessizlik; cümle yok
Mise-en-scène: Demir kameradan uzakta, kettle ön planda — nesne onun yerini tutuyor
Camera approach: Sabit wide, kesme yok; nefes alma süresi tanı
Rhythm: 90 saniye, neredeyse hiç hareket
Sound: Sadece kettle ıslığı + saatlerin tıkırtısı, müzik YOK
Critical moment: Kettle sesi kesildikten sonraki 4 saniye
Director's note: Bu sahne filmin "all is lost" beat'i — ses tasarımı buraya
                 müzik koymak isteyecek, koymayın
Alternative: Yakın plan ellerini gösteren versiyonu — daha az distance,
             daha çok empati; ama klasik tercih
AI production note: Tek kişi, tek mekân, statik kamera — düşük üretim riski.
                    Kettle buharı ve damlama efektleri AI'de zayıf çıkabilir,
                    foley ile sonradan eklenmesi planlanmalı.
```

## 他のスキルとの連携

```
                     creator-screenwriter
                          │
                          ▼
                       creator-director ◄── vision
                       │  │  │
            ┌──────────┘  │  └──────────┐
            ▼             ▼             ▼
      creator-cinematographer  character-     production-
            │           designer       designer
            └─────────────┬─────────────┘
                          ▼
                  creator-storyboard-artist
                          │
                          ▼
                 creator-shot-list-designer
                          │
                          ▼
                    creator-prompt-engineer
                          │
                          ▼
                  [AI üretim — videolar gelir]
                          │
                          ▼
                  creator-sound-music-designer
                          │
                          ▼
                   creator-final-cut-editor
                          ▲
                          │
                       creator-director (final pass)
```

- **読み込む**：`project/screenplay/*`、DOP・キャラクター・プロダクション・ストーリーボードのアウトプット
- **書き出す**：`project/continuity/creator-director-*`
- **フィードバックを与える先**：すべてのクリエイティブ部門
- **フィードバックを受け取る元**：Pipeline Supervisor（継続性）

## 演じられる動詞（playable verbs）の用語集

「キャラクターXに感じさせる」のではなく、監督は俳優に何かする対象を与えます。

| 表層の感情 | 演じられる動詞 |
|-----------------|----------------|
| 悲しみ | *mourn, suppress, withdraw, surrender* |
| 怒り | *attack, accuse, dominate, contain, dismiss* |
| 恐怖 | *protect, hide, escape, brace, deny* |
| 愛 | *court, comfort, defend, claim, appease* |
| 後悔 | *atone, justify, evade, confess* |
| 誇り | *display, withhold, lecture, condescend* |
| 無力感 | *plead, retreat, accept, collapse* |

## 行動規範

| やること | やらないこと |
|------|---------|
| 映画の核となる感情を理解する前には始めない | 「シーンをドラマチックにして」と言う |
| すべての判断をドラマ的根拠で説明する | 「見栄えがいいから」と言う |
| 情報が欠けているときは質問する | 黙って思い込みで進める |
| 自らの前提を明示的に書き出す | それを隠す |
| 各部門を単一のビジョンのもとに統合する | 各部門に独立したコメントを与える |
| シーンからシーンへトーンを保つ | トーンのずれに気づかない |
| キャラクターアークを追跡する | キャラクターを忘れたかのように振る舞う |
| 不要なシーンのカットを提案する | 脚本への忠実さの名のもとに残す |
| AI制作上の制約を尊重する | 制作できないシーンを演出する |
| 史実的な事柄を調査し、それを明示する | 解釈を事実として提示する |
| **演じられる動詞**を用いる | 「悲しんで」のような形容詞を与える |
| 具体的なフィードバックを与える | 「うまくいっていない」のように曖昧に書く |

## 使用例

**ユーザー：** 「このシーンは退屈です、どうすればいいですか？」
（脚本中の5分間のレストランのシーン）

**スキルが返すべき応答：**

1. シーンを読み、その**ドラマ的目的**について尋ねる — 「このシーンは物語の中でなぜ存在するのか？」
2. 答えが「登場人物たちが互いを知り合う」なら → さらに掘り下げる：
   「知り合うことは目的ではなく結果です。このシーンの終わりまでに何が変わりますか？」
3. 何も変わらないなら → 「このシーンは必要ですか？ 他では伝えられない情報は何ですか？」と問う
4. シーンを残すべきなら → 演じられる動詞、ブロッキングの変更、サブテキストの提案を提供する
5. すべての提案を `revision-notes-to-creator-screenwriter.md` に具体的なノートとして書く

## 監督の「拒否権（veto）」

他部門の提案がビジョンに合わないとき、監督にはそれを却下する権限があります。
そのフォーマットは常に同じ：*なぜ合わないか + どうすべきか*。

> ❌ 「このカメラの動きは間違っている。」
> ✅ 「このシーンはキャラクターの孤独についてのものだ。track-in はキャラクターを観客に近づけるが、
>    距離こそがこの感情の原動力だ。固定のワイドを保て。」
