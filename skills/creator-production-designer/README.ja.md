# プロダクションデザイナー — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

映画の**世界**を構築する skill。ロケーション、セット、props、時代の空気感、色彩と
素材の言語を扱う。「美しい村」と言うのではなく、壁の質感、床の素材、家具の密度、
光に影響する表面、経年劣化の跡のレベルまで設計する。長尺の AI 映画制作を通じて
**ロケーションの一貫性**を保つ master reference を確立する。

## 哲学

空間は背景ではなく、**語りの道具**である。この skill は：

- まず **World bible** —— 次に per-location、次に per-scene（top-down）
- **Master reference**：各主要ロケーションごとのロックされた AI prompt block ——
  50 シーン後でも同じ家を産出できるように
- **生活感のデザイン**：ひび割れ、染み、日焼けによる退色、摩耗、補修の跡
- **Class-coded design**：あらゆる素材／色が社会階層を物語る
- **Coordinated palette**：DOP のライティングやキャラクターの衣裳と合わせて考える
- **Period research**：歴史的／文化的な正確さが求められる場合の出典付きリサーチ

## 何の役に立つか

| アウトプット | 内容 |
|-------|--------|
| **World bible** | 映画全体の世界ルール（時代、階層、建築、素材） |
| **Color & texture bible** | カラーパレット、素材の言語、摩耗パターン |
| **Location dossier** | 各主要ロケーションの包括的ドキュメント（ロック + バリエーション） |
| **Master reference (AI)** | ロケーションのアイデンティティを固定する AI prompt block |
| **Props inventory** | セットのオブジェクトとそのドラマ的機能 |
| **Per-scene plan** | シーンごとのプロダクションデザイン（dressing、props、光源） |
| **Continuity log** | シーン間のロケーション一貫性チェック |
| **Period research** | 出典付きの歴史的／文化的リサーチ |
| **Notes to DOP / creator-director** | 双方向のコミュニケーション |

## いつ起動するか

- 脚本が手元にあり、世界 / ロケーション / セットのデザインが必要なとき
- 「この空間はどう見えるべきか」「set dressing」「prop リスト」
- AI 制作のための一貫したロケーション reference
- 時代リサーチ（歴史的、文化的、地域的）
- `creator-pipeline-supervisor` がプロダクションデザイン段階を委譲したとき

## 典型的な流れ

1. **ブリーフィング** + `creator-director-vision.md` + DOP visual-language の読み込み
2. **質問ラウンド**：時代、地理、トーン、階層、AI ツール
3. **World bible**：映画全体の世界ルール
4. **Color & texture bible**：素材と色の言語
5. **Major locations**：各主要ロケーションの dossier
6. **Master references**：AI 一貫性のためのロックされた prompt block
7. **Per-scene sheets**：シーンごとの set dressing + prop メモ
8. **Continuity audit**：同じロケーションが異なるシーンで一貫しているか？

## アウトプットの書き込み先

`project/production-design/` の下（cinematography を除く —— それは DOP のもの）：

| ファイル | 内容 |
|-------|--------|
| `world-bible.md` | 映画の世界ルール |
| `color-texture-bible.md` | 色 + 素材の言語 |
| `locations/{slug}/location-doc.md` | per-location dossier |
| `locations/{slug}/master-reference.md` | ロックされた AI base prompt |
| `props/{slug}.md` または `props-list.md` | prop インベントリ |
| `scenes/scene-{NN}.md` | シーンごとのプロダクションデザイン計画 |
| `continuity-notes.md` | ロケーション一貫性チェックのログ |
| `period-research.md` | 出典付きの時代リサーチ |
| `notes-to-creator-director.md` | 監督への質問／提案 |
| `notes-to-creator-cinematographer.md` | DOP との表面／奥行き／光の調整 |

## Location dossier テンプレート（要約）

```
Location: Demir'in dedesinin köy evi mutfağı
Function in story: Demir'in babayı ilk kez bir mekânda hisseder
Period: 1980'ler doğu Anadolu kırsalı
Architectural style: tek katlı kerpiç, ahşap kiriş tavan, kireçli duvar
Color palette: kireç beyazı, bakır, yanmış toprak, kömür siyahı
Texture: kireç ufalı duvar, ahşap çatlamış, bakır pas yeşili, demir tencere is izi
Walls: kireç boyalı, alt 1m'de toz/duman izi
Floor: ham ahşap, eskimiş
Doors / windows: ahşap kanat pencere, dışarısı çıplak ağaç
Furniture: ahşap masa (4 kişilik), iki sandalye, bakır kapaklı dolap
Decorative: duvarda tek bir solmuş aile fotoğrafı
Daily-use items: bakır kettle, demir tencere, tahta kaşıklar, kil testi
Lived-in level: yıllarca yaşanmış, son 2 hafta dokunulmamış (toz tabakası)
Light-affecting surfaces: kireç (matt, ışık yutar), bakır (kontur), pencere (tek kaynak)
Camera framing points: pencere ışığı kettle'ı tarayan açı; masa ekseni
Continuity anchors: pencere konumu, masa, dolap, fotoğraf — KİLİTLİ
AI master reference prompt: "...same kitchen across all scenes..."
Variations: gündüz, gece, fırtınalı, yeni temizlenmiş (final sahnede)
```

## Master reference（AI 一貫性のために）

各主要ロケーションについて、**ロックされた base prompt block** を書く：

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

この block はすべてのシーン prompt にそのまま繰り返し、その上にシーン固有の
バリエーションを追加する。

## 他の skill との連携

- **Cinematographer**：
  - 表面と光の関係（matte、glossy、transparent）
  - 奥行きの段階づけのための前景／中景／背景
  - カラーパレットは計画されたライティングで機能するか？
  - 鏡、ガラス、光沢のある表面はカメラにとって問題か？
- **Director**：
  - ロケーションは中心テーマに資するか？
  - 世界のトーンはビジョンに合っているか？
  - 「signature/iconic」であるべきロケーションはあるか？
- **Character-designer**：
  - 衣裳はロケーションのパレット内で正しく読めるか？
  - 個人の持ち物は dressing の中に居場所を見つけるか？
  - 社会階層は衣裳と空間の両方から一貫しているか？
- **Storyboard / shot-list**：フレーミングポイントのメモ
- **Prompt-engineer**：master reference + バリエーション prompt の hand-off

## Reads / writes

- **Reads**：脚本、監督のビジョン、DOP visual-language、キャラクターのパレット
- **Writes**：`project/production-design/*`（cinematography を除く）

## AI 制作に焦点を当てたソリューション

- 少ないロケーションで多くのシーンを産出する
- アングル／光／天候のバリエーションで同じロケーションを違って見せる
- dressing の密度を制御 —— AI が過負荷にならないように
- AI が苦手とする複雑な空間を簡略化する
- 固定の reference 画像による一貫性
- 「master reference」を早期に産出する
- dressing オブジェクトを再利用する（世界の一体性）
- 不要なディテールを減らしてドラマ的オブジェクトを前面に出す

## 振る舞いのルール

| する | しない |
|-------|--------|
| 空間を語りの道具として設計する | 「いい部屋」と言う |
| すべての dressing の判断を時代／キャラクター／テーマに結びつける | 孤立した美的選択をする |
| 情報が欠けているときに質問する | 黙って捏造する |
| 文化的ディテールをリサーチし、ラベルづけする | 解釈を事実のように提示する |
| master reference で AI の一貫性を確保する | 各シーンでゼロから記述する |
| DOP + キャラクターとパレットを調整する | 孤立して決める |
| キャラクター prop / ロケーション prop の所有を明確にする | キャラクターデザイナーと衝突する |
| 構造化された downstream-readable なファイルを出す | 一塊のテキストをぶちまける |
| AI でリスクのあるロケーションに代替案を出す | 産出できないディテールを強要する |
