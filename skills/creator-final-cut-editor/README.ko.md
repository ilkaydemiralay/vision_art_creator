# 파이널 컷 에디터 — `creator-final-cut-editor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · **한국어**

AI 프로덕션 결과물을 **완성된 영화**로 만들어 내는 스킬. 프리프로덕션의 끝이자
포스트프로덕션의 시작이다. 소재가 일단 생성되고 나면 러프 컷 → 파인 컷 →
파이널 컷 → 딜리버리로 이어지는 흐름을 관리한다. AI 생성 오류를 분류(triage)하고,
연속성을 점검하며, 오디오/음악 통합을 확인하고, 딜리버리 준비가 끝난 마스터를
만들어 낸다.

**shot-list-designer와의 차이점**: 숏 리스트는 촬영 이전에 편집 의도를
설계하지만, creator-final-cut-editor는 실제 소재 위에서 컷을 실행한다.

## 철학

파이널 컷은 **기술적인 시퀀싱이 아니다** — 그것은 영화적 완결성을 쌓아 올리는
작업이다. 이 스킬은 다음을 추구한다:

- **모든 컷에 대한 드라마적 근거** — "보기 좋다"만으로는 부족하다
- **다층적 리듬**: 한 숏 안에서, 한 장면 안에서, 영화 전체에 걸쳐
- **AI 오류 분류**: 어떤 오류가 컷을 망치는지, 어떤 것은 숨길 수 있는지, 어떤 것은 그대로 둘 수 있는지
- **관객 경험 설계**: 관객이 무엇을 느끼고, 배우고, 가져가는가
- **딜리버리 규율**: YouTube ≠ 영화제 ≠ Instagram ≠ 아카이브
- **버전 관리**: 러프/파인/파이널 + 영화제/소셜/예고편 컷을 각각 별도로 관리

## 하는 일

| 산출물 | 내용 |
|-------|---------|
| **소재 평가** | 숏별: 사용 가능 / 수정 / 재생성 / 컷 |
| **러프 컷 플랜** | 최초의 러프 시퀀싱, 누락 소재 목록 |
| **파인 컷 플랜** | 컷 포인트, 숏 길이, 정적(silence) |
| **파이널 컷 플랜** | 최종 준비 상태 + 딜리버리 체크리스트 |
| **장면별 최종 점검** | 장면 단위의 상세 점검 |
| **영화 전체 리포트** | 영화 전체에 대한 파이널 컷 리포트 |
| **AI 오류 리포트** | 생성 오류 + 심각도 분류 |
| **오디오 통합 점검** | 사운드 디자이너에게 전달할 피드백 |
| **컬러 그레이드 노트** | 색 보정 지시사항 |
| **EDL** | NLE에서 읽을 수 있는 Edit Decision List |
| **버전 매니페스트** | 영화제/소셜/예고편 컷 버전 |
| **딜리버리 사양** | 플랫폼별 익스포트 설정 |
| **예고편 플랜** | 티저/예고편 컷 플랜 |

## 작동하는 시점

- AI 비디오 숏이 생성되어 편집이 시작될 때
- 러프/파인/파이널 컷 기획이 필요할 때
- AI 오류 점검이 요청될 때
- 여러 컷(영화제, 소셜, 예고편)을 만들어야 할 때
- 딜리버리 익스포트 준비
- `creator-pipeline-supervisor`가 포스트프로덕션 단계를 위임할 때

## 일반적인 흐름

1. **소재 평가** — 각 숏을 분류한다 (✅🟡🟠🔴)
2. **러프 컷 v01** — 스토리 순서, 기본적인 드라마 시퀀스
3. **파인 컷 v01** — 컷 포인트, 리듬, 정적
4. **사운드 통합 점검** — creator-sound-music-designer에게 피드백
5. **AI 오류 리포트** — 치명적/중간/경미 분류
6. **컬러 그레이드 노트** — 필요한 경우
7. **자막 / 타이틀 / 그래픽 점검**
8. **파이널 컷 v01** — 준비 상태 체크리스트
9. **딜리버리 익스포트** — 플랫폼별 버전

## AI 오류 분류 매트릭스

| 심각도 | 정의 | 조치 |
|----------|------------|--------|
| 🔴 치명적 | 파이널 컷에 넣을 수 없음 | 재생성 (creator-prompt-engineer에게 플래그) |
| 🟡 중간 | 트림/크롭/컬러/사운드로 숨김 | 편집상의 우회 처리 |
| ✅ 경미 | 관객에게 거슬리지 않음 | 그대로 둘 수 있음 |

점검 대상: 얼굴 왜곡, 손/손가락 오류, 립싱크, 의상 변화, 액세서리 소실,
로케이션 드리프트, 조명 방향 불일치, 부자연스러운 카메라 움직임, 플리커, 워핑,
모핑, 녹아내리는 오브젝트, 배경 붕괴, 시대 착오(anachronism), 플라스틱한 질감.

## 장면별 최종 점검 포맷

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

## 산출물을 기록하는 위치

`project/cuts/` 아래:

| 파일 | 내용 |
|-------|---------|
| `material-evaluation.md` | 각 숏의 분류 |
| `rough-cut/v{NN}.md` | 러프 컷 플랜 |
| `fine-cut/v{NN}.md` | 파인 컷 플랜 |
| `final-cut/v{NN}.md` | 파이널 컷 플랜 + 준비 상태 |
| `scene-{NN}/final-check.md` | 장면 단위 상세 |
| `final-cut-report.md` | 영화 전체 점검 |
| `ai-error-report.md` | AI 오류 리포트 |
| `audio-integration-report.md` | 오디오 통합 점검 |
| `color-grade-notes.md` | 색 보정 |
| `subtitle-titles-graphics.md` | 자막/타이틀 |
| `transitions.md` | 트랜지션 결정 |
| `edit-decision-list.md` | EDL |
| `versions/{cut-name}.md` | 버전 매니페스트 |
| `delivery/{platform}.md` | 플랫폼 익스포트 사양 |
| `trailer-plan.md` | 예고편/티저 플랜 |

## 버전 관리

| 버전 | 길이 | 목표 |
|----------|----------|------|
| Rough Cut v01 | 목표의 약 115% | 최초 스토리 흐름 테스트 |
| Rough Cut v02 | 약 108% | 누락된 조각의 통합 |
| Fine Cut | 약 102% | 리듬과 감정 고정 |
| Director's Cut | 목표의 100% | 감독 전면 승인 |
| Final Cut | 100% | 딜리버리 준비 완료 |
| Festival Cut | 100% | 영화제 포맷 |
| YouTube Cut | 100% 또는 단축 | YouTube 알고리즘 |
| Trailer Cut | 30s–2 min | 마케팅 |
| Social Cut | 9:16 숏폼 | Reels, TikTok |

각 버전별: 이름, 길이, 변경사항, 삭제/추가된 장면, 오디오 변경, 수정 근거,
승인 상태.

## 딜리버리 사양 예시

| 플랫폼 | 화면비 | 해상도 | FPS | 오디오 |
|----------|--------|------------|-----|-------|
| YouTube 16:9 마스터 | 16:9 | 3840×2160 (4K) 또는 1920×1080 | 24/25 | AAC 320kbps stereo |
| 영화제 마스터 | 2.39:1 또는 16:9 | 4K | 24 | WAV 48kHz 24-bit stereo + 5.1 |
| Instagram Reels | 9:16 | 1080×1920 | 30 | AAC stereo |
| TikTok | 9:16 | 1080×1920 | 30 | AAC stereo |
| 웹 압축 | 16:9 | 1920×1080 | 24/25 | AAC 192kbps |
| 아카이브 마스터 | 원본 | 최고 화질 | 원본 | WAV master |

## 예고편 컷 로직

예고편은 **영화의 축소판이 아니다** — 그 자체의 편집 로직을 가진다:

- 가장 강렬한 비주얼 6~10개
- 스포일러 제외 목록
- 훅 → 배경 → 위협/갈등 → 클라이맥스 티저 → 암전 → 태그라인
- 음악 빌드업 (영화와 다르게, 더 직접적으로)
- 빠른 컷팅 리듬 (영화와 다르게)
- 압축된 캐릭터 소개
- 마지막 한 방의 이미지 — 영화의 맥락 **바깥에 있는**
- 짧은 소셜 미디어 9:16 버전

## 다른 스킬과의 협업

- **읽음**: 모든 상류 크리에이티브 산출물 + 숏 리스트의 `final-editor-notes.md`
- **씀**: `project/cuts/*`
- **피드백을 주는 대상**:
  - **creator-sound-music-designer**: 오디오 수정 요청
  - **creator-prompt-engineer**: 재생성 요청
  - **creator-pipeline-supervisor**: 연속성 에스컬레이션
- **승인을 받는 대상**: 감독(최종 승인), 파이프라인 슈퍼바이저

## 행동 규칙

| 한다 | 하지 않는다 |
|-------|---------|
| 모든 컷에 드라마적 근거 | 단순한 기술적 시퀀싱 |
| 불필요한 장면/숏을 명확히 플래그 | 미련 때문에 그대로 보존 |
| AI 오류를 관객 경험 관점에서 평가 | 추상적/기술적 완벽주의 |
| 대사 + 음악 + 앰비언스 + 정적을 함께 고려 | 고립된 채로 점검 |
| 감독의 비전에 충실 | 편집자의 에고와 충돌 |
| 목표 길이에 규율을 지킴 | 한계를 초과 |
| 큰 변경 전에 사용자에게 질문 | 말없이 컷 |
| 여러 버전을 추적 | 하나의 파일에 뒤섞음 |
| 플랫폼에 맞춘 딜리버리 제공 | 단일 마스터만 넘김 |
| 딜리버리 준비 체크리스트 없이는 "완료"라 말하지 않음 | 일찍 완성을 선언 |
