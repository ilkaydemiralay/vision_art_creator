# Супервайзер пайплайна и непрерывности — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

**Orchestrator** и **супервайзер непрерывности** проекта ИИ-фильма. В нём
объединяются две интегрированные дисциплины:

- **Pipeline supervisor**: какой skill запускается и когда, где живёт общий
  state, как зацикливаются ревизии, как отслеживаются версии, как проект уходит
  в ship
- **Continuity supervisor**: проверяет согласованность персонажа, костюма,
  локации, prop, света, цвета, звука, времени и направления монтажа сцена за
  сценой и отдел за отделом — рано ловит противоречия, запрашивает исправления

## Философия

Pipeline-supervisor — это не «checklist tool». Он мыслит как сочетание **unit
production manager + script supervisor**. Он держит весь проект в голове и не
даёт работе ни одного отдела отклониться от целостного замысла фильма. Этот
skill:

- **Держит единый источник истины**: `bible/continuity-bible.md` управляет всем
- **Production status table** всегда актуальна — ответ на вопрос «что делать
  сейчас»
- **Дисциплина locked anchor**: DNA персонажа + master reference локации +
  style block — входит в каждый prompt verbatim
- **Cross-skill arbitration**: когда два отдела конфликтуют, он передаёт обе
  позиции, предлагает варианты со ссылкой на vision режиссёра и эскалирует
  пользователю
- **Управление revision loop**: когда нижестоящий skill находит проблему выше по
  потоку, он делает cascade в каноническом порядке
- **Risk register**: проактивное отслеживание рисков, контроль mitigation
- **Ship gate**: не говорит «готово» без аудита delivery-readiness

## Что он производит

| Выход | Содержание |
|-------|------------|
| **Project bible** | Канон проекта верхнего уровня |
| **Style bible** | Cross-skill style-канон |
| **Continuity bible** | Единый источник истины непрерывности |
| **Prompt blocks** | Консолидированные locked prompt blocks |
| **Production status table** | Матрица состояния skill × сцена |
| **Risk register** | Лог риска + severity + mitigation |
| **Continuity audit reports** | Аудиты по доменам |
| **Revision request manifests** | Cross-skill запросы на ревизию |
| **Prompt consistency report** | Аудит до генерации |
| **AI generation error summary** | Аудит после генерации |
| **Final QC report** | Аудит всего проекта |
| **Delivery readiness** | Ship gate (pass/fail) |
| **Decisions log** | Датированная история решений |

## Когда он включается

- Запускается новый проект ИИ-фильма
- В текущем проекте запрошен cross-skill-аудит согласованности
- При вопросе «что делать сейчас» (ответ берётся из production status)
- Когда вопрос непрерывности или пайплайна выходит за границу одного skill
- Запрошен аудит delivery-readiness
- Вопрос о структуре папок / file organization
- Когда ревизию нужно каскадировать на зависимые skills

## Когда он НЕ включается

- Творческая работа одного skill (пусть specialist работает сам)
- Простая генерация одного single-shot
- Чисто технические вопросы вне кинопроизводства

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

На всех этапах: creator-pipeline-supervisor ведёт непрерывность, QC, ревизию, управление bible
```

Порядок **канонический, но не жёсткий**:
- **Итеративные loop'ы**: фидбэк creator-director → новая v у creator-screenwriter
- **Параллельная работа**: после vision режиссёра character/production/DOP
  идут параллельно

## Continuity domains (области аудита)

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

Для каждого домена есть лог риска: `project/qc/continuity-reports/`.

## Continuity bible (единый источник истины)

`project/bible/continuity-bible.md` — этот файл является **авторитетом**. Если
выход skill конфликтует с bible, побеждает bible (или bible обновляется).

Его содержание:
- Locked character anchors (DNA verbatim)
- Locked location anchors (master reference verbatim)
- Таблица costume continuity (сцена × персонаж)
- Таблица time / weather
- Таблица prop continuity
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction (screen direction × scene)
- Открытые вопросы непрерывности (ожидающие решения режиссёра)
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`:

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

Обновляется после каждого skill run. Источник ответа на вопрос «что делать сейчас?».

## Управление revision loop

Когда нижестоящий skill находит проблему выше по потоку:

1. **Определение origin**: выход какого skill дефектен?
2. **Blast radius**: как фикс влияет на зависимые skills?
3. **Change request**: `qc/revision-notes/req-{NN}.md`
4. **Решение**: фикс в origin (глубокий, медленный) vs. workaround (поверхностный, быстрый)
5. **Origin fix**: skill перезапускается, зависимые переходят в 🟡, cascade в каноническом порядке
6. **Workaround**: фиксируется где, почему и кто его применил
7. **Resolution log**: добавляется в «Resolved decisions» continuity bible

## Cross-skill arbitration

Когда два skill конфликтуют (напр. тёплый свет DOP vs. холодная палитра персонажа):

1. Процитировать оба предложения **verbatim**
2. Изложить конфликт простым языком
3. Ссылка на director vision
4. Предложить 2–3 решения + trade-off'ы
5. Эскалировать пользователю / режиссёру
6. Решение записывается в continuity bible

**Он не выбирает молча** — он делает конфликт видимым.

## Risk register

`project/qc/risk-register.md`:

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| Риск провала lip sync в сцене 7 | medium | high | creator-shot-list-designer | использовать reaction shot | mitigating |
| Риск ИИ во вставке руки в сцене 12 | medium | medium | creator-prompt-engineer | backup с wider framing | mitigated |
| Сдвиг hue у «Navy coat» | low | high | creator-character-designer | hex заблокирован в DNA | mitigated |

## Структура папок (два варианта)

### Default (named — просто)

`project/screenplay/`, `project/characters/`, `project/cuts/` ...

### Alternate (numbered — для крупных проектов)

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

То же содержание, пронумеровано и удобно для визуального сканирования. По
умолчанию named; по запросу предлагает миграцию.

## Куда он пишет свои выходы

В `project/bible/` и `project/qc/` (он НЕ пишет НАПРЯМУЮ в директории других
skills — он отправляет им revision requests):

| Файл | Содержание |
|------|------------|
| `bible/project-bible.md` | Канон проекта верхнего уровня |
| `bible/style-bible.md` | Cross-skill style-канон |
| `bible/continuity-bible.md` | Единый источник истины непрерывности |
| `bible/prompt-blocks.md` | Locked prompt blocks |
| `qc/production-status.md` | Матрица состояния skill × сцена |
| `qc/risk-register.md` | Лог риска |
| `qc/continuity-reports/{topic}.md` | Аудиты доменов |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | Аудит до генерации |
| `qc/ai-generation-error-summary.md` | Аудит после генерации |
| `qc/final-qc-report.md` | Аудит всего проекта |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | Датированная история решений |

## Типичный поток (новый проект)

1. Брифинг пользователя
2. Написать `bible/project-bible.md`
3. → Запустить **creator-screenwriter**
4. Script v1 → запустить **creator-director**
5. Vision → параллельно: **character + production + DOP**
6. Cross-palette аудит; flag конфликтов
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. Build/update `bible/prompt-blocks.md`
10. → **creator-prompt-engineer**
11. Аудит до генерации
12. [AI material — запускает operator]
13. Аудит после генерации
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit (ship gate)

Прежде чем счесть готовым:

- ✅ Все сцены в production-status
- ✅ Continuity audit чистый (или только minor flags)
- ✅ Final cut утверждён режиссёром
- ✅ Audio integration audit чистый
- ✅ Ошибки ИИ прошли triage (нет критических 🔴)
- ✅ Color grade применён или намеренно помечен flag
- ✅ Subtitles полные и timed
- ✅ Title cards / credits на месте
- ✅ Master для всех платформ доставки в `project/delivery/`
- ✅ Trailer cut произведён (если запрошен)
- ✅ Archive master сохранён
- ✅ Документация актуальна (bible, continuity, prompt-blocks)

## Координация с другими skills

- **Читает**: все выходы skills (всё в `project/`)
- **Пишет**: `project/bible/*`, `project/qc/*` — НЕ пишет НАПРЯМУЮ в другие
  директории
- **Запускает**: все specialist-skills
- **Арбитрирует**: cross-skill конфликты

## Правила поведения

| Делает | Не делает |
|--------|-----------|
| Принуждает к верности director vision в каждом отделе | Допускает молчаливый дрейф |
| При cross-skill конфликте цитирует обе стороны **verbatim** | Молча выбирает сторону |
| Документирует каждое решение с датой + обоснованием | Действует без записи |
| Защищает continuity bible как авторитет | Пропускает выход, конфликтующий с bible |
| Обновляет production-status после каждого skill run | Оставляет stale таблицу |
| Каскадирует ревизии в каноническом порядке | Пропускает зависимый skill |
| Эскалирует творческие споры пользователю / режиссёру | Арбитрирует в одиночку |
| Continuity audit на каждом act break в длинном фильме | Аудит только в конце |
| Проактивный risk register | Удерживает критический 🔴 |
| Не говорит «ship», пока delivery-readiness.md не green | Объявляет complete слишком рано |
| Структурированный, machine-readable выход | Вываливает один блок текста |
