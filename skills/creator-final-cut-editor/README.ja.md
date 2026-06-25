# ファイナルカット・エディター — `creator-final-cut-editor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · **日本語** · [한국어](README.ko.md)

AIの制作アウトプットを**完成した映画**へと仕上げるスキル。プリプロダクションの
終わり/ポストプロダクションの始まりにあたります。素材が制作されたら、ラフカット
→ ファインカット → ファイナルカット → 納品という流れを管理します。AI生成のエラー
をトリアージし、連続性を監査し、音声/音楽の統合をチェックして、納品可能なマスター
を仕上げます。

**shot-list-designerとの違い**: ショットリストは撮影の前に編集意図を設計します。
creator-final-cut-editorは実際の素材に対して編集を実行します。

## 哲学

ファイナルカットは**技術的なシーケンス作業ではなく**、映画としての一体性を構築する
作業です。このスキルは次を重視します。

- **すべてのカットに劇的な根拠を** — 「見栄えがいい」だけでは不十分
- **複数スケールのリズム**: ショット内、シーン内、映画全体にわたって
- **AIエラーのトリアージ**: どのエラーがカットを壊すか、どれを隠せるか、どれを残せるか
- **観客の体験設計**: 観客が何を感じ、何を理解し、何を持ち帰るか
- **納品の規律**: YouTube ≠ 映画祭 ≠ Instagram ≠ アーカイブ
- **バージョン管理**: ラフ/ファイン/ファイナル + 映画祭/ソーシャル/予告編カットを別々に管理

## 何をするか

| アウトプット | 内容 |
|-------|---------|
| **素材評価** | ショットごと: 使用可 / 修正 / 再生成 / カット |
| **ラフカット計画** | 最初のラフなシーケンス、不足素材のリスト |
| **ファインカット計画** | カットポイント、ショットの尺、サイレンス |
| **ファイナルカット計画** | 最終的な準備状況 + 納品チェックリスト |
| **シーンごとの最終チェック** | シーン単位の詳細な監査 |
| **映画全体レポート** | 映画全体のファイナルカットレポート |
| **AIエラーレポート** | 生成エラー + 深刻度の分類 |
| **音声統合監査** | サウンドデザイナーへのフィードバック |
| **カラーグレードノート** | 色補正の指示 |
| **EDL** | NLEで読み込めるEdit Decision List |
| **バージョンマニフェスト** | 映画祭/ソーシャル/予告編のカットバージョン |
| **納品仕様** | プラットフォーム別のエクスポート設定 |
| **予告編計画** | ティザー/予告編のカット計画 |

## いつ起動するか

- AIビデオショットが制作され、編集が始まるとき
- ラフ/ファイン/ファイナルカットの計画が必要なとき
- AIエラーの監査が要求されたとき
- 複数のカット(映画祭、ソーシャル、予告編)を制作するとき
- 納品エクスポートの準備をするとき
- `creator-pipeline-supervisor`がポストプロダクション段階を委任するとき

## 典型的な流れ

1. **素材評価** — 各ショットを分類(✅🟡🟠🔴)
2. **ラフカット v01** — ストーリー順、基本的な劇的シーケンス
3. **ファインカット v01** — カットポイント、リズム、サイレンス
4. **音声統合監査** — creator-sound-music-designerへのフィードバック
5. **AIエラーレポート** — クリティカル/中程度/軽微の分類
6. **カラーグレードノート** — 必要な場合
7. **字幕 / タイトル / グラフィックのチェック**
8. **ファイナルカット v01** — 準備状況チェックリスト
9. **納品エクスポート** — プラットフォーム別バージョン

## AIエラー・トリアージマトリクス

| 深刻度 | 定義 | アクション |
|----------|------------|--------|
| 🔴 クリティカル | ファイナルカットに含められない | 再生成(creator-prompt-engineerにフラグ) |
| 🟡 中程度 | トリム/クロップ/カラー/サウンドで隠せる | 編集上の回避策 |
| ✅ 軽微 | 観客を妨げない | 残してよい |

チェック項目: 顔の歪み、手/指のエラー、リップシンク、衣装の変化、
アクセサリーの消失、ロケーションのドリフト、光の方向の不整合、不自然な
カメラの動き、フリッカー、ワーピング、モーフィング、溶けるオブジェクト、背景の
崩壊、時代考証の誤り、プラスチックのような質感。

## シーンごとの最終チェック・フォーマット

```
Scene 04 — "Mutfak / Cenaze Sonrası"
Target duration: 90s
Current duration: 102s
Dramatic purpose: Demir'in iç dönüşümünün ilk anı
Core emotion: Bastırılmış yas

Shots used: 04.01, 04.02, 04.03, 04.05, 04.06
Shots cut: 04.04 (gereksiz reaction, ritim düşürüyor)
Shots shortened: 04.05 (8s → 5s — wide hold gereksiz uzun)
Shots lengthened: 04.02 (4s → 6s — kettle hold dramatik nefes)
Cut points:
  - 04.01 → 04.02: sound bridge (kettle ıslığı önce)
  - 04.02 → 04.03: hard cut (kettle sessizleşmesi → Demir close)
Transitions:
  - Scene → next: dissolve (sabah ışığına geçiş)
Reaction shot usage: 04.03 (Demir close) — yas kırılma anı
Silence usage: 04.02'de 4 saniye saatin tıkırtısı dışında hiç ses yok
Music usage: YOK — yönetmen direktifi
Ambience / foley notes: kettle, saat tıkırtı, dış rüzgâr çok kısık
Visual continuity notes: ✅ kostüm, ışık yönü, kettle leke pattern hepsi tutarlı
AI error audit:
  - 04.02 kettle buharı warping (🟡 orta) — sound design ile maskelenecek
  - 04.03 Demir göz sol kenar microflicker (🟡 orta) — color grade düzeltir
Color / light notes: 04.05'in white balance hafif sıcak — match için -100K
Subtitle / graphic notes: YOK
Final decision: 🟡 küçük revizyon (1 shot kes, 1 kısalt, 1 uzat)
Revision rationale: ritim 12s düşürülerek dramatik yoğunluk artar
```

## アウトプットの書き出し先

`project/cuts/` 配下:

| ファイル | 内容 |
|-------|---------|
| `material-evaluation.md` | 各ショットの分類 |
| `rough-cut/v{NN}.md` | ラフカット計画 |
| `fine-cut/v{NN}.md` | ファインカット計画 |
| `final-cut/v{NN}.md` | ファイナルカット計画 + 準備状況 |
| `scene-{NN}/final-check.md` | シーン単位の詳細 |
| `final-cut-report.md` | 映画全体の監査 |
| `ai-error-report.md` | AIエラーレポート |
| `audio-integration-report.md` | 音声統合監査 |
| `color-grade-notes.md` | 色補正 |
| `subtitle-titles-graphics.md` | 字幕/タイトル |
| `transitions.md` | トランジションの決定 |
| `edit-decision-list.md` | EDL |
| `versions/{cut-name}.md` | バージョンマニフェスト |
| `delivery/{platform}.md` | プラットフォーム別エクスポート仕様 |
| `trailer-plan.md` | 予告編/ティザー計画 |

## バージョン管理

| バージョン | 尺 | 目標 |
|----------|----------|------|
| Rough Cut v01 | 目標の約115% | 最初のストーリー進行テスト |
| Rough Cut v02 | 約108% | 不足ピースの統合 |
| Fine Cut | 約102% | リズムと感情のロック |
| Director's Cut | 目標の100% | 監督による完全承認 |
| Final Cut | 100% | 納品可能 |
| Festival Cut | 100% | 映画祭フォーマット |
| YouTube Cut | 100%または短縮版 | YouTubeアルゴリズム |
| Trailer Cut | 30秒〜2分 | マーケティング |
| Social Cut | 9:16 ショート | Reels、TikTok |

各バージョンについて: 名称、尺、変更点、削除/追加されたシーン、音声の
変更、改訂の根拠、承認ステータス。

## 納品仕様の例

| プラットフォーム | アスペクト | 解像度 | FPS | 音声 |
|----------|--------|------------|-----|-------|
| YouTube 16:9 マスター | 16:9 | 3840×2160 (4K) または 1920×1080 | 24/25 | AAC 320kbps ステレオ |
| 映画祭マスター | 2.39:1 または 16:9 | 4K | 24 | WAV 48kHz 24-bit ステレオ + 5.1 |
| Instagram Reels | 9:16 | 1080×1920 | 30 | AAC ステレオ |
| TikTok | 9:16 | 1080×1920 | 30 | AAC ステレオ |
| Web圧縮版 | 16:9 | 1920×1080 | 24/25 | AAC 192kbps |
| アーカイブマスター | オリジナル | 最高画質 | オリジナル | WAV マスター |

## 予告編カットのロジック

予告編は**映画のミニチュアではなく**、独自の編集ロジックを持ちます。

- 最も強力な6〜10のビジュアル
- ネタバレ除外リスト
- フック → 背景 → 脅威/対立 → クライマックスのティザー → 暗転 → タグライン
- 音楽のビルドアップ(映画とは異なり、よりダイレクトに)
- 速いカッティングのリズム(映画とは異なる)
- 圧縮されたキャラクター紹介
- 最後のパンチとなる一枚 — 映画の文脈の**外側**
- 短いソーシャルメディア向け9:16バージョン

## 他スキルとの連携

- **読み込む**: すべての上流クリエイティブのアウトプット + shot-listの`final-editor-notes.md`
- **書き込む**: `project/cuts/*`
- **フィードバックを渡す**:
  - **creator-sound-music-designer**: 音声修正のリクエスト
  - **creator-prompt-engineer**: 再生成のリクエスト
  - **creator-pipeline-supervisor**: 連続性に関するエスカレーション
- **承認を得る**: 監督(最終承認)、パイプライン・スーパーバイザー

## 振る舞いのルール

| すること | しないこと |
|-------|---------|
| すべてのカットに劇的な根拠を与える | 単なる技術的なシーケンス作業 |
| 不要なシーン/ショットを明確にフラグする | 義理立てのために残す |
| AIエラーを観客の体験から評価する | 抽象的/技術的な完璧主義 |
| 台詞 + 音楽 + アンビエンス + サイレンスを一体で考える | 切り離して監査する |
| 監督のビジョンに忠実 | 編集のエゴと衝突する |
| 目標の尺に対して規律を守る | 上限を超過する |
| 大きな変更の前にユーザーに確認する | 無断でカットする |
| 複数のバージョンを管理する | 1つのファイルに混在させる |
| プラットフォームに適した納品を行う | 1つのマスターだけを渡す |
| 納品準備チェックリストなしに「完了」と言わない | 早々に完成を宣言する |
