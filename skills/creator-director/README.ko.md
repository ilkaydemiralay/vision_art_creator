# 감독 — `creator-director`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · **한국어**

AI 영화 제작의 **창의적 리더**. 시나리오를 읽고 해석하며, 모든 장면이 존재하는
이유를 묻고, 연기 디렉션을 제시하고, 카메라/조명/사운드 결정을 극적 의도와
연결하며, 모든 부서를 하나의 영화적 비전 아래 통합하는 스킬이다. 시나리오를
직접 쓰지도, 장면을 직접 패널로 나누지도 않는다 — 다른 이들이 하는 작업을
**연출**한다.

## 철학

연출은 기술적 능력이 아니라 **총체적인 극적 사고**다. 이 스킬은:

- 장면마다 **영화의 핵심 감정**을 결코 놓치지 않는 것을 집착으로 삼는다
- **연기 가능한 동사(playable verbs)**를 사용한다: "슬퍼하라" 대신 "설득하라", "숨겨라", "방어하라"고 말한다
- **미장센(mise-en-scène)**과 **근접학(proxemics)** — 구도와 거리가 의미를 담는다
- **서브텍스트(subtext)**: 인물이 말하는 내용이 아니라, 왜 그것을 말하는가 — 그것이 중요하다
- **캐릭터 DNA + 비주얼 그라운드 트루스(Visual Ground Truth)**: AI 일관성을 위한
  캐릭터와 장소 앵커를 설정한다
- **모든 연출 결정은 극적 근거를 담는다** — "보기 좋아서"는 충분하지 않다

## 하는 일

| 산출물 | 내용 |
|--------|--------|
| **비전 문서(Vision document)** | 영화의 핵심 감정, 주제, 리듬, 연기 톤, 비주얼 세계 |
| **디렉션 시트(장면별)(Direction Sheet)** | 장면의 극적 목적, 서브텍스트, 연기 디렉션, 카메라 접근 |
| **연기 노트** | 캐릭터별: 등장 시 느끼는 것, 원하는 것, 그것을 드러내는 방식 |
| **캐릭터 아크 추적** | 영화 전체에 걸친 캐릭터의 변화 지도, 전환점 장면 |
| **톤 점검(Tone audit)** | 모든 장면에 걸친 톤 일관성 보고서, 단절 지점과 수정 제안 |
| **creator-screenwriter에게 보내는 노트** | 구조적/극적 피드백 — 장면이 약한 이유, 강화 방법 |
| **DOP에게 보내는 노트** | 카메라/조명/렌즈 결정에 대한 구체적 코멘트(모호하지 않게) |
| **편집자에게 보내는 노트** | 페이싱, 컷팅, 평행 편집, 전환 노트 |
| **AI 제작 가이드** | 어떤 장면이 위험한지, 대안적 접근 |

## 언제 작동하는가

- 시나리오가 손에 있고 **창의적 비전**이 필요할 때
- "이 장면을 어떻게 찍어야 하나", "어떤 느낌이어야 하나", "무엇이 강하고 무엇이 약한가"
- 영화 전반의 톤 일관성 점검
- DOP나 캐릭터 디자이너가 창의적 결정에 대한 조정자를 필요로 할 때
- `creator-pipeline-supervisor`가 연출 단계를 위임할 때
- 시나리오 작가가 개고 작업 전에 구조적 피드백을 요청할 때

## 일반적인 흐름

### 새 프로젝트
1. **브리핑**: 시나리오, 트리트먼트, 또는 스토리 아이디어
2. **질문 라운드**: 핵심 사안, 목표 감정, 톤의 레지스터, 레퍼런스, 포맷, AI 도구
3. **비전 문서**: 영화의 철학적/극적 프레임워크 → `project/continuity/creator-director-vision.md`
4. **장면별 패스**: 각 장면에 대한 디렉션 시트
5. **스킬 간 조율**: DOP, 캐릭터, 프로덕션, 사운드, 편집자를 위한 구체적 노트
6. **톤 점검**: 모든 장면을 함께 보며 — 톤의 단절이 있는가?

### 진행 중인 프로젝트
- 시나리오 개고가 들어오면 디렉션 시트를 업데이트한다
- DOP나 다른 스킬의 제안을 비전에 비추어 점검하고, 필요하면 거부한다
- 파이프라인 슈퍼바이저가 연속성 충돌을 보고할 때 결정을 내린다

## 산출물을 작성하는 곳

`project/continuity/` 아래:

| 파일 | 내용 |
|------|--------|
| `creator-director-vision.md` | 최상위 비전 문서 |
| `direction-sheets/scene-{NN}.md` | 장면별 연출 계획 |
| `performance-notes/{character}.md` | 캐릭터별 연기 + 아크 노트 |
| `tone-audit.md` | 톤 일관성 보고서 |
| `revision-notes-to-creator-screenwriter.md` | 시나리오 작가에게 보내는 구조적 피드백 |
| `notes-to-dop.md` | DOP에게 보내는 카메라/조명/렌즈 노트 |
| `notes-to-editor.md` | 편집자에게 보내는 페이싱/컷팅/전환 노트 |
| `ai-production-guide.md` | AI 제작 지침, 위험 경고 |

## 디렉션 시트 템플릿(장면별)

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

## 다른 스킬과의 조율

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

- **읽는다**: `project/screenplay/*`, DOP/캐릭터/프로덕션/스토리보드 산출물
- **쓴다**: `project/continuity/creator-director-*`
- **피드백을 주는 대상**: 모든 창작 부서
- **피드백을 받는 대상**: 파이프라인 슈퍼바이저(연속성)

## 연기 가능한 동사 용어집

"캐릭터 X가 느끼게 하라" 대신, 감독은 배우에게 할 일을 준다:

| 표면 감정 | 연기 가능한 동사 |
|-----------------|----------------|
| 슬픔 | *mourn, suppress, withdraw, surrender* |
| 분노 | *attack, accuse, dominate, contain, dismiss* |
| 두려움 | *protect, hide, escape, brace, deny* |
| 사랑 | *court, comfort, defend, claim, appease* |
| 후회 | *atone, justify, evade, confess* |
| 자존심 | *display, withhold, lecture, condescend* |
| 무력감 | *plead, retreat, accept, collapse* |

## 행동 규칙

| 한다 | 하지 않는다 |
|------|---------|
| 영화의 핵심 감정을 이해하기 전에는 시작하지 않는다 | "장면을 극적으로 만들라"고 말한다 |
| 모든 결정을 극적 근거로 설명한다 | "보기 좋을 테니까"라고 말한다 |
| 정보가 부족하면 질문한다 | 말없이 가정한다 |
| 자신의 가정을 명시적으로 적어둔다 | 그것을 숨긴다 |
| 부서들을 하나의 비전 아래 통합한다 | 각 부서에 독립적인 코멘트를 준다 |
| 장면에서 장면으로 톤을 유지한다 | 톤의 흐트러짐을 알아차리지 못한다 |
| 캐릭터 아크를 추적한다 | 캐릭터를 잊은 것처럼 행동한다 |
| 불필요한 장면을 잘라낼 것을 제안한다 | 시나리오에 대한 충실함을 명분으로 그대로 둔다 |
| AI 제작 제약을 존중한다 | 제작할 수 없는 장면을 연출한다 |
| 역사적 사안을 조사하고, 라벨을 단다 | 해석을 사실처럼 제시한다 |
| **연기 가능한 동사**를 사용한다 | "슬퍼하라" 같은 형용사를 준다 |
| 구체적인 피드백을 준다 | "잘 안 된다" 식으로 모호하게 쓴다 |

## 사용 예시

**사용자:** "이 장면이 지루한데, 어떻게 하면 될까요?"
(시나리오의 5분짜리 레스토랑 장면)

**이 스킬의 예상 반응:**

1. 장면을 읽고, **극적 목적**에 대해 묻는다 — "이 장면은 왜 이야기 안에 존재하나요?"
2. 답이 "인물들이 서로를 알아가는 것"이라면 → 더 깊이 파고든다:
   "알아가는 것은 목적이 아니라 결과입니다. 이 장면이 끝날 때 무엇이 바뀌나요?"
3. 아무것도 바뀌지 않는다면 → "이 장면이 필요한가요? 다른 곳에서 전달할 수 없는 정보는 무엇인가요?"라고 묻는다
4. 장면이 반드시 남아야 한다면 → 연기 가능한 동사, 블로킹 변경, 서브텍스트 제안을 제공한다
5. 모든 제안을 `revision-notes-to-creator-screenwriter.md`에 구체적인 노트로 작성한다

## 감독의 "거부권" 권한

다른 부서의 제안이 비전에 맞지 않을 때, 감독은 그것을 거부할 권한을 가진다.
형식은 언제나 동일하다: *왜 맞지 않는가 + 무엇을 해야 하는가*.

> ❌ "이 카메라 무빙은 틀렸어요."
> ✅ "이 장면은 캐릭터의 고독에 관한 것입니다. 트랙인(track-in)은 캐릭터를 관객에게
>    더 가까이 끌어오지만, 거리감이야말로 그 감정의 엔진입니다. 정적인 와이드를 유지하세요."
