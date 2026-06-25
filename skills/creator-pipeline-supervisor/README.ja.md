# パイプライン＆コンティニュイティ・スーパーバイザー — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

AI 映画プロジェクトの **orchestrator** であり **コンティニュイティ監督**。2 つの
統合された専門領域が一体となります。

- **Pipeline supervisor**：どの skill がいつ走るか、共有 state がどこに存在するか、
  リビジョンがどうループするか、バージョンがどう追跡されるか、プロジェクトがどう
  ship されるか
- **Continuity supervisor**：キャラクター、衣装、ロケーション、prop、ライト、色、
  サウンド、時間、編集方向の一貫性をシーンごと・部門ごとに監査する —— 矛盾を早期に
  捕捉し、fix を要求する

## 哲学

pipeline-supervisor は「checklist tool」ではありません。**unit production
manager + script supervisor** の組み合わせのように考えます。プロジェクト全体を頭の
中に保持し、どの部門の作業も映画の一貫した意図から逸脱させません。この skill は：

- **単一の信頼できる情報源を保つ**：`bible/continuity-bible.md` がすべてを統べる
- **Production status table** が常に最新 —— 「いま何をすべきか」への答え
- **locked anchor の規律**：キャラクター DNA + ロケーション master reference +
  style block —— 各 prompt に verbatim で入る
- **Cross-skill arbitration**：2 つの部門が衝突した場合、両者の見解を伝え、監督の
  vision を参照したオプションを提示し、ユーザーに escalate する
- **リビジョン loop 管理**：下流の skill が上流に問題を見つけたとき、canonical な順序で
  cascade する
- **Risk register**：能動的なリスク追跡、mitigation のフォロー
- **Ship gate**：delivery-readiness audit なしに「完了」とは言わない

## 何を生み出すか

| 出力 | 内容 |
|------|------|
| **Project bible** | 上位レベルのプロジェクト canon |
| **Style bible** | cross-skill style canon |
| **Continuity bible** | コンティニュイティの単一信頼源 |
| **Prompt blocks** | 統合された locked prompt blocks |
| **Production status table** | skill × シーンのステータス・マトリクス |
| **Risk register** | リスク + severity + mitigation のログ |
| **Continuity audit reports** | domain 別の監査 |
| **Revision request manifests** | cross-skill のリビジョン要求 |
| **Prompt consistency report** | 生成前監査 |
| **AI generation error summary** | 生成後監査 |
| **Final QC report** | プロジェクト全体の監査 |
| **Delivery readiness** | Ship gate（pass/fail） |
| **Decisions log** | 日付付きの決定履歴 |

## いつ関与するか

- 新しい AI 映画プロジェクトが開始されるとき
- 進行中のプロジェクトで cross-skill consistency audit が要求されたとき
- 「いま何をすべきか」という問いに対して（答えは production status から）
- コンティニュイティまたはパイプラインの問いが skill の境界をまたぐとき
- delivery-readiness audit が要求されたとき
- フォルダ構造 / file organization の問い
- リビジョンを依存 skill に cascade させる必要があるとき

## いつ関与しないか

- 単一 skill のクリエイティブ作業（specialist が単独で作業すればよい）
- 単純な single-shot generation
- 映画制作外の純粋に技術的な問い

## Canonical pipeline

```
0. project bible & vision
1. creator-screenwriter
2. creator-director
3-4-5. character + production + DOP (parallel)
6. creator-storyboard-artist
7. creator-shot-list-designer
8. creator-prompt-engineer
   → [AI material generation — operator]
9. creator-sound-music-designer
10. creator-final-cut-editor

全ステージを通じて：creator-pipeline-supervisor がコンティニュイティ、QC、リビジョン、bible 管理を担う
```

順序は **canonical だが厳格ではない**：
- **反復 loop**：creator-director フィードバック → creator-screenwriter 新 v
- **並行作業**：監督の vision の後、character/production/DOP が並行して走る

## Continuity domains（監査領域）

1. Story / plot
2. Time / chronology
3. Character (physical)
4. Character arc (emotional)
5. Costume
6. Hair / makeup
7. Accessories / props
8. Location
9. Set dressing
10. Light direction
11. Color palette
12. Camera language
13. Sound / ambience
14. Music theme (leitmotif)
15. Emotional flow
16. Edit / screen direction
17. AI prompt consistency (locked anchors verbatim)
18. Reference image consistency
19. Scene / shot numbering

各 domain にはリスクログがあります：`project/qc/continuity-reports/`。

## Continuity bible（単一信頼源）

`project/bible/continuity-bible.md` —— このファイルが **権威** です。ある skill の
出力が bible と衝突した場合、bible が勝ちます（または bible が更新されます）。

その内容：
- Locked character anchors（DNA verbatim）
- Locked location anchors（master reference verbatim）
- Costume continuity テーブル（シーン × キャラクター）
- Time / weather テーブル
- Prop continuity テーブル
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction（screen direction × scene）
- 未解決のコンティニュイティの問い（監督の決定待ち）
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`：

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

各 skill run のあとに更新されます。「いま何をすべきか？」の答えの源です。

## リビジョン loop 管理

下流の skill が上流に問題を見つけたとき：

1. **Origin の特定**：どの skill の出力が不具合か？
2. **Blast radius**：fix は依存 skill にどう影響するか？
3. **Change request**：`qc/revision-notes/req-{NN}.md`
4. **決定**：origin での fix（深い・遅い）vs. workaround（浅い・速い）
5. **Origin fix**：skill が再トリガーされ、依存先は 🟡 になり、canonical 順序で cascade
6. **Workaround**：どこに・なぜ・誰が適用したかを記録
7. **Resolution log**：continuity bible の「Resolved decisions」に append

## Cross-skill arbitration

2 つの skill が衝突したとき（例：DOP の暖色ライト vs. キャラクターの cool palette）：

1. 両方の提案を **verbatim** で引用する
2. 衝突を平易な言葉で述べる
3. director vision を参照する
4. 2〜3 の解決策 + trade-off を提示する
5. ユーザー / 監督に escalate する
6. 決定を continuity bible に書き込む

**黙って選択しません** —— 衝突を可視化します。

## Risk register

`project/qc/risk-register.md`：

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| シーン 7 の lip sync 失敗リスク | medium | high | creator-shot-list-designer | reaction shot を使う | mitigating |
| シーン 12 の手の insert AI リスク | medium | medium | creator-prompt-engineer | wider framing のバックアップ | mitigated |
| 「Navy coat」の hue drift | low | high | creator-character-designer | DNA で hex をロック | mitigated |

## フォルダ構造（2 つの選択肢）

### Default（named —— シンプル）

`project/screenplay/`、`project/characters/`、`project/cuts/` ...

### Alternate（numbered —— 大規模プロジェクト向け）

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

同じ内容を、番号付きで視覚的スキャンに優しく。Default は named。要求に応じて
migration を提示します。

## 出力をどこに書き込むか

`project/bible/` と `project/qc/` の配下に書き込みます（他の skill のディレクトリには
直接書き込まず —— 彼らに revision request を送ります）：

| ファイル | 内容 |
|---------|------|
| `bible/project-bible.md` | 上位レベルのプロジェクト canon |
| `bible/style-bible.md` | cross-skill style canon |
| `bible/continuity-bible.md` | コンティニュイティの単一信頼源 |
| `bible/prompt-blocks.md` | Locked prompt blocks |
| `qc/production-status.md` | skill × シーンのステータス・マトリクス |
| `qc/risk-register.md` | リスクログ |
| `qc/continuity-reports/{topic}.md` | domain 監査 |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | 生成前監査 |
| `qc/ai-generation-error-summary.md` | 生成後監査 |
| `qc/final-qc-report.md` | プロジェクト全体の監査 |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | 日付付きの決定履歴 |

## 典型的なフロー（新規プロジェクト）

1. ユーザー briefing
2. `bible/project-bible.md` を書く
3. → **creator-screenwriter** をトリガー
4. Script v1 → **creator-director** をトリガー
5. Vision → 並行：**character + production + DOP**
6. Cross-palette audit；衝突を flag
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. `bible/prompt-blocks.md` を build/update
10. → **creator-prompt-engineer**
11. 生成前監査
12. [AI material —— operator が実行]
13. 生成後監査
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit（ship gate）

完了とみなす前に：

- ✅ すべてのシーンが production-status にある
- ✅ Continuity audit がクリーン（または minor flag のみ）
- ✅ Final cut が監督承認済み
- ✅ Audio integration audit がクリーン
- ✅ AI errors が triage 済み（critical 🔴 なし）
- ✅ Color grade が適用済み、または意図的に flag 済み
- ✅ Subtitles が完備かつ timed
- ✅ Title cards / credits が所定の位置にある
- ✅ すべての deliverable プラットフォームの master が `project/delivery/` 配下にある
- ✅ Trailer cut が制作済み（要求された場合）
- ✅ Archive master が保管済み
- ✅ ドキュメントが最新（bible、continuity、prompt-blocks）

## 他の skill との連携

- **読む**：すべての skill 出力（`project/` のすべて）
- **書く**：`project/bible/*`、`project/qc/*` —— 他のディレクトリには直接書き込まない
- **トリガー**：すべての specialist skill
- **arbitrate**：cross-skill の衝突

## 振る舞いのルール

| する | しない |
|------|--------|
| 各部門で director vision への忠実度を強制する | 黙った逸脱を許す |
| cross-skill 衝突では両者を **verbatim** で引用する | 黙ってどちらかに与する |
| 各決定を日付 + 根拠とともに文書化する | 記録なしで動く |
| continuity bible を権威として守る | bible と衝突する出力を通す |
| 各 skill run のあとに production-status を更新する | stale なテーブルを残す |
| リビジョンを canonical 順序で cascade する | 依存 skill を飛ばす |
| クリエイティブな争いをユーザー / 監督に escalate する | 単独で arbitrate する |
| 長編では各 act break ごとに continuity audit | 最後にだけ監査する |
| 能動的な risk register | critical 🔴 を放置する |
| delivery-readiness.md が green になるまで「ship」と言わない | 早すぎる段階で complete とする |
| 構造化された machine-readable な出力 | 単一のテキスト塊を吐き出す |
