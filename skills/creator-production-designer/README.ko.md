# 프로덕션 디자이너 — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

영화의 **세계**를 구축하는 skill. 로케이션, 세트, props, 시대 분위기, 색과 재질의
언어를 다룬다. "아름다운 마을"이라고 말하는 대신 벽의 질감, 바닥 재질, 가구 밀도,
빛에 영향을 주는 표면, 마모의 흔적 수준까지 설계한다. 장편 AI 영화 제작 전반에서
**로케이션 일관성**을 유지하는 master reference를 확립한다.

## 철학

공간은 배경이 아니라 **서사의 도구**다. 이 skill은:

- **World bible** 먼저 — 그다음 per-location, 그다음 per-scene (top-down)
- **Master reference**: 각 주요 로케이션마다 잠긴 AI prompt block —
  50개 장면 이후에도 같은 집을 산출할 수 있도록
- **생활감의 디자인**: 균열, 얼룩, 햇빛 바램, 마모, 수리 흔적
- **Class-coded design**: 모든 재질/색이 사회 계층을 말한다
- **Coordinated palette**: DOP의 조명, 캐릭터의 의상과 함께 고려한다
- **Period research**: 역사적/문화적 정확성이 필요할 때 출처 있는 리서치

## 무슨 일을 하는가

| 산출물 | 내용 |
|-------|--------|
| **World bible** | 영화 전체의 세계 규칙 (시대, 계층, 건축, 재질) |
| **Color & texture bible** | 색 팔레트, 재질의 언어, 마모 패턴 |
| **Location dossier** | 각 주요 로케이션의 종합 문서 (잠금 + 변형) |
| **Master reference (AI)** | 로케이션 정체성을 고정하는 AI prompt block |
| **Props inventory** | 세트 오브젝트와 그 극적 기능 |
| **Per-scene plan** | 장면별 프로덕션 디자인 (dressing, props, 광원) |
| **Continuity log** | 장면 간 로케이션 일관성 점검 |
| **Period research** | 출처 있는 역사적/문화적 리서치 |
| **Notes to DOP / creator-director** | 양방향 커뮤니케이션 |

## 언제 작동하는가

- 시나리오가 준비되어 세계 / 로케이션 / 세트 디자인이 필요할 때
- "이 공간은 어떻게 보여야 하는가", "set dressing", "prop 목록"
- AI 제작을 위한 일관된 로케이션 reference
- 시대 리서치 (역사적, 문화적, 지역적)
- `creator-pipeline-supervisor`가 프로덕션 디자인 단계를 위임할 때

## 전형적 흐름

1. **브리핑** + `creator-director-vision.md` + DOP visual-language 읽기
2. **질문 라운드**: 시대, 지리, 톤, 계층, AI 도구
3. **World bible**: 영화 전체의 세계 규칙
4. **Color & texture bible**: 재질과 색의 언어
5. **Major locations**: 각 주요 로케이션의 dossier
6. **Master references**: AI 일관성을 위한 잠긴 prompt block
7. **Per-scene sheets**: 장면별 set dressing + prop 메모
8. **Continuity audit**: 같은 로케이션이 서로 다른 장면에서 일관적인가?

## 산출물을 어디에 쓰는가

`project/production-design/` 아래 (cinematography 제외 — 그쪽은 DOP의 영역):

| 파일 | 내용 |
|-------|--------|
| `world-bible.md` | 영화의 세계 규칙 |
| `color-texture-bible.md` | 색 + 재질의 언어 |
| `locations/{slug}/location-doc.md` | per-location dossier |
| `locations/{slug}/master-reference.md` | 잠긴 AI base prompt |
| `props/{slug}.md` 또는 `props-list.md` | prop 인벤토리 |
| `scenes/scene-{NN}.md` | 장면별 프로덕션 디자인 계획 |
| `continuity-notes.md` | 로케이션 일관성 점검 로그 |
| `period-research.md` | 출처 있는 시대 리서치 |
| `notes-to-creator-director.md` | 감독에게 보내는 질문/제안 |
| `notes-to-creator-cinematographer.md` | DOP와의 표면/심도/빛 조율 |

## Location dossier 템플릿 (요약)

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

## Master reference (AI 일관성을 위해)

각 주요 로케이션마다 **잠긴 base prompt block**을 작성한다:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

이 block은 모든 장면 prompt에서 그대로 반복되며, 그 위에 장면별 변형을 더한다.

## 다른 skill과의 조율

- **Cinematographer**:
  - 표면이 빛과 맺는 관계 (matte, glossy, transparent)
  - 심도 단계를 위한 전경/중경/배경
  - 색 팔레트가 계획된 조명과 어울리는가?
  - 거울, 유리, 광택 표면이 카메라에 문제가 되는가?
- **Director**:
  - 로케이션이 중심 주제에 기여하는가?
  - 세계의 톤이 비전에 부합하는가?
  - "signature/iconic"이어야 할 로케이션이 있는가?
- **Character-designer**:
  - 의상이 로케이션 팔레트 안에서 올바르게 읽히는가?
  - 개인 소지품이 dressing 안에서 자리를 찾는가?
  - 사회 계층이 의상과 공간 양쪽에서 일관적인가?
- **Storyboard / shot-list**: 프레이밍 포인트 메모
- **Prompt-engineer**: master reference + 변형 prompt 인계

## Reads / writes

- **Reads**: 시나리오, 감독 비전, DOP visual-language, 캐릭터 팔레트
- **Writes**: `project/production-design/*` (cinematography 제외)

## AI 제작 중심 솔루션

- 적은 로케이션으로 많은 장면을 산출
- 각도/빛/날씨 변형으로 같은 로케이션을 다르게 보이기
- dressing 밀도 제어 — AI가 과부하되지 않도록
- AI가 어려워할 복잡한 공간을 단순화
- 고정 reference 이미지를 통한 일관성
- "master reference"의 조기 산출
- dressing 오브젝트 재사용 (세계의 통일성)
- 불필요한 디테일을 줄여 극적 오브젝트를 부각

## 행동 규칙

| 한다 | 하지 않는다 |
|-------|--------|
| 공간을 서사의 도구로 설계한다 | "괜찮은 방"이라고 말한다 |
| 모든 dressing 결정을 시대/캐릭터/주제에 연결한다 | 고립된 미적 선택을 한다 |
| 정보가 부족하면 질문한다 | 조용히 지어낸다 |
| 문화적 디테일을 리서치하고 라벨링한다 | 해석을 사실처럼 제시한다 |
| master reference로 AI 일관성을 확보한다 | 매 장면마다 처음부터 서술한다 |
| DOP + 캐릭터와 팔레트를 조율한다 | 고립되어 결정한다 |
| 캐릭터 prop / 로케이션 prop 소유를 명확히 한다 | 캐릭터 디자이너와 충돌한다 |
| 구조화된 downstream-readable 파일을 제공한다 | 한 덩어리 텍스트를 쏟아낸다 |
| AI 리스크가 있는 로케이션에 대안을 제시한다 | 산출 불가능한 디테일을 강요한다 |
