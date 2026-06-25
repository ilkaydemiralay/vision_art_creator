# サウンド＆ミュージックデザイナー — `creator-sound-music-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [**日本語**](README.ja.md) · [한국어](README.ko.md)

映画の**感覚的な世界**を構築するスキル。統合された2つの専門領域が組み合わさります。
- **サウンドデザイナー**：空間・キャラクター・物体・出来事の感覚的なリアリティ — ambience、foley、効果音、音響、サウンドパースペクティブ、そして**沈黙**（能動的なドラマの道具として）
- **映画音楽の作曲家／ミュージックスーパーバイザー**：メインテーマ、キャラクターのleitmotif、シーンの音楽、リズム、音楽の入り／抜けのポイント

## 哲学
サウンドと音楽は**装飾ではありません**。すべての音と音楽の決定は、シーンのドラマ的な目的、キャラクターの心理、ビジュアルの雰囲気、編集のリズム、そして観客への影響と結びついています。このスキルは：
- 「悲しい音楽を使う」とは言わず — leitmotifを設計し、その進化を計画します
- **沈黙を能動的に設計します** — 不在ではなく、ドラマ的な決定として
- **キャラクターのleitmotif**：フルートで始まるモチーフが、フィナーレでは弦楽器とともに壮大なものへと変化します
- **著作権に配慮します**：存命のアーティストを模倣せず、「似ているが同じではない」
- **編集のリズムと同期します**：音楽の入り／抜けをshot-listの編集プランと連携させます
- **AIサウンド／音楽プロンプト生成**：Suno、Udio、ElevenLabs SFX、Stable Audio、Runway Audio

## できること
| 成果物 | 内容 |
|-------|--------|
| **Sound vision** | 映画全体のサウンドデザインのビジョン |
| **Music vision** | 映画の音楽言語のマニフェスト |
| **Main theme** | メインテーマの設計 |
| **Character themes** | キャラクターごとのleitmotif設計 |
| **Scene plans** | シーンごとのサウンド＋音楽プラン |
| **Ambience / foley / SFX lists** | インベントリリスト |
| **Silence plan** | 意図的な沈黙のマップ |
| **Music in/out plan** | 音楽の入り／抜けのポイント |
| **Sound bridges** | トランジションの設計 |
| **AI sound + music prompts** | ツール別のプロンプト |
| **Dialogue balance notes** | セリフ／音楽のバランスノート |
| **Final mix notes** | final mixの監査 |
| **Continuity report** | サウンドの連続性チェック |

## 起動するタイミング
- 脚本が手元にあり、サウンドデザイン／映画音楽のプランが必要なとき
- ambience、foley、SFX、または音楽テーマが求められたとき
- AIサウンド／音楽プロンプトが必要なとき
- shot-listデザイナーがシーンのサウンド意図を引き継ぐとき
- `creator-pipeline-supervisor` がオーディオ段階を委任するとき

## 典型的なフロー
1. **ブリーフィング** ＋ 上流すべてのスキル成果物の読み込み
2. **質問ラウンド**：ジャンル、register、音楽密度、時代、AIツール
3. **Sound vision** ＋ **Music vision**
4. **メインテーマ＋キャラクターのleitmotif**
5. **シーンごとのプラン**：すべてのシーンのambient／foley／silence／music
6. **Silence plan**：意図的な沈黙のマップ
7. **音楽の入り／抜けプラン**
8. **AIサウンド＋音楽プロンプト**
9. **final mixの監査**（final cutの後）

## 沈黙の設計
沈黙は**能動的な**設計上の決定です。各沈黙について、このスキルは次のことを問います：
- ここで音楽を切るのか？
- ambienceを弱めるのか、それともゼロにするのか？
- 呼吸だけを残すのか、小さな物の音を残すのか？
- その沈黙は孤独、恐怖、ためらいを伝えるのか？
- 観客を不安にさせるためなのか、それとも感情を高めるためなのか？
- 沈黙の後にどの音が入ってくるのか？

## キャラクターのleitmotif例
```
Karakter: Demir
Müzikal duygu: bastırılmış yas + içsel kararlılık
Ana enstrüman: solo cello (başlangıç) → cello + ney (orta) → cello + yaylı
                grup (final)
Tempo: 60–66 BPM (slow heart)
Ton: minör, kromatik geçişler
Ritim: rubato, neredeyse zamansız
Motifin evrimi:
  - Sahne 1–5: solo cello, kısa 5-notalı motif, sessizlik aralıkları geniş
  - Sahne 6–12: ney ekleniyor — nefes katmanı
  - Sahne 13–18: yaylı grup açılıyor — toplum, geçmiş, anlam
  - Sahne 19 (final): tek cello, ilk motifin yarısı — kırılma
```

## 成果物の書き込み先
`project/sound/` の下：
| ファイル | 内容 |
|-------|--------|
| `sound-vision.md` | サウンドデザイン全体のビジョン |
| `music-vision.md` | 音楽言語のマニフェスト |
| `main-theme.md` | メインテーマの設計 |
| `character-themes/{slug}.md` | キャラクターのleitmotif |
| `scenes/scene-{NN}.md` | シーンのサウンド＋音楽プラン |
| `ambience-list.md` | ambienceインベントリ |
| `foley-list.md` | foleyインベントリ |
| `special-effects-list.md` | 特殊SFX |
| `silence-plan.md` | 沈黙のマップ |
| `music-entry-exit-plan.md` | 音楽の入り／抜けのタイミング |
| `sound-bridges.md` | トランジションの設計 |
| `ai-sound-prompts.md` | AI SFXプロンプト |
| `ai-music-prompts.md` | AI音楽プロンプト |
| `dialogue-balance-notes.md` | セリフ／音楽のバランス |
| `final-mix-notes.md` | final mixの監査 |
| `sound-continuity-report.md` | 連続性チェック |

## AIプロンプトのフォーマット
### SFXプロンプト例
```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```
### 音楽プロンプト例
```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```
### 母語による説明＋英語プロンプトのフォーマット
```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## 著作権とオリジナリティ
- 既存の楽曲をコピーすることを提案しません
- 存命のアーティストのスタイルを一音一音模倣しません
- 「似ているが同じではない」というロジックで、ジャンル＋感情を記述して作業します
- AI音楽プロンプトでは、アーティスト名の代わりに一般的な雰囲気を用います

## 他スキルとの連携
- **読み込む**：上流すべてのクリエイティブ成果物 ＋ shot-listのサウンド編集ノート
- **書き込む**：`project/sound/*`
- **委任先**：`creator-final-cut-editor`（final cutへの統合）、AIオーディオツールのオペレーター
- **フィードバックを受ける相手**：ディレクター、Pipeline Supervisor、Final-cut-editor

## 振る舞いのルール
| すること | しないこと |
|-------|--------|
| サウンドと音楽をドラマ的な目的に結びつける | 装飾として使う |
| 沈黙を能動的に設計する | 不在として扱う |
| leitmotifの進化をキャラクターのアークと同期させる | 1つの固定テーマを繰り返す |
| セリフ／音楽／ambience／沈黙をまとめて考える | 切り離して決める |
| 著作権に配慮する | アーティストを模倣する |
| 歴史的／文化的なリサーチを行い、それを明示する | 解釈を事実として提示する |
| ツールに適合したAIプロンプトを書く | 汎用的なプロンプトをただ投げる |
| 長編映画のためにサウンドの連続性を保つ | シーンごとにバラバラに考える |
