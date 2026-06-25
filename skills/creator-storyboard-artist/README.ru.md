# Художник раскадровки — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Навык, превращающий написанный сценарий в **читаемое визуальное повествование**.
Минимизируя количество панелей, он гарантирует, что каждая панель существует по
драматической причине. Он улавливает критические моменты сцены, сохраняет screen
direction, отслеживает eyeline continuity и чисто передаёт работу в AI image/video
prompt'ы.

## Философия

Раскадровка — это не «рисование сцены», а **система визуального повествования**. Этот навык:

- **Panel economy**: мало панелей + точный выбор — а не много панелей + слабые решения
- **Screen direction (180°)** и **eyeline continuity**: пространственная согласованность между склейками
- **Graphic dynamics**: куда падает взгляд? что в фокусе?
- **Continuity awareness**: костюм, локация, направление света, направление экрана, движение
- **Locked anchors**: character DNA + location master reference в каждой панели
- **Producibility**: знает ограничения ИИ-производства и помечает рискованные сцены

## Для чего он нужен

| Вывод | Содержание |
|-------|------------|
| **Per-scene storyboard** | Список панелей сцена за сценой (все данные панели) |
| **Per-panel sheets** | Подробный файл одной панели для сложных сцен |
| **AI image prompts** | Готовый к производству prompt на каждую панель |
| **AI video prompts** | Видео-prompt для движущихся панелей |
| **Continuity log** | Метки рисков костюма/локации/направления |
| **Animatic plan** | Планирует порядок animatic для всех сцен |
| **Director / DOP notes** | Краткие визуальные/технические заметки для режиссёра и DOP |
| **Handoff to shot-list** | Данные панели в формате creator-shot-list-designer |

## Когда он вступает в действие

- Есть сценарий и нужна визуальная разбивка
- Когда режиссёр хочет заранее визуализировать сцену
- Когда нужна визуальная концепция до решений DOP по объективу/свету
- Когда нужна логика раскадровки до генерации ИИ-prompt'ов
- Когда `creator-pipeline-supervisor` делегирует этап раскадровки

## Panel content (канонические поля)

Каждая панель фиксирует эти поля:

```
Scene 04 — Panel 04.03
Shot type: medium close
Camera angle: eye level
Frame: Demir merkez-sağ; kettle ön plan-sol; arka plan
       dolap soft-focus; sağ kenar negatif alan açık
Lens feeling: 50mm (eye-equivalent, samimi)
Character position: Demir sandalyede, omuzlar düşmüş, eller masada
Character movement: yok — duraksama
Camera movement: static
Setting / dressing: kireçli mutfak — pencere doğu, kettle ateşte
Light / atmosphere: pencereden yumuşak gri sabah, mum yok
Emotional emphasis: bastırılmış yas; ilk gerçek duygu kırılması
Dialogue / action note: sessizlik; kettle ıslığı
Dramatic justification: Demir'in iç çatışmasını yüzeye getiren ilk an
Transition to next panel: J-cut — kettle sesi devam ederken Panel 4.04 başlar
AI image prompt: [tam prompt]
AI video prompt: [tam prompt, 6s]
Continuity note: palto sahne başında; ceket askıda; kettle aktif
```

## Куда он пишет свои выводы

В `project/storyboards/`:

| Файл | Содержание |
|------|------------|
| `scene-{NN}/storyboard.md` | Список панелей по сцене (канонический) |
| `scene-{NN}/panel-{PP}.md` | Подробная отдельная панель (в сложных сценах) |
| `scene-{NN}/prompts.md` | ИИ-prompt'ы по панели (image + video) |
| `scene-{NN}/continuity.md` | Метки continuity |
| `animatic-plan.md` | Заметки о порядке animatic для всего фильма |
| `notes-to-creator-director.md` | Вопросы/предупреждения режиссёру |
| `handoff-to-shot-list.md` | Отформатированные данные панели для shot-list designer |

## Словарь shot type (с драматическим эквивалентом)

| Тип | Драматическое применение |
|-----|--------------------------|
| Establishing | Помещает зрителя в пространство |
| Master | Геометрия сцены, fallback |
| Wide/Full | Отношение персонаж–среда |
| Medium | Нейтральный диалог |
| Close | Внутренний конфликт, интимная эмоция |
| Extreme close | Субъективная интенсивность |
| Insert | Акцент на объекте |
| Cutaway | Параллельная/внешняя информация |
| Reaction | Реакция важнее действия |
| OTS | Перспектива диалога |
| POV | Субъективность персонажа |
| 2-shot / group | Геометрия отношений |
| Silhouette | Анонимность, тайна |
| Negative-space frame | Изоляция, малость |
| Symmetrical | Сила, формальность, тревожная неподвижность |
| Tracking | Непрерывное следование |
| Static | Наблюдение, смысл тишины |

«Возьми close-up» недостаточно — вопрос в том, **почему** нужен close-up.

## Continuity audit

Отслеживание от панели к панели, от сцены к сцене:

- Костюм
- Причёска/макияж/аксессуары
- Идентичность локации (с locked anchor)
- Направление света
- День/ночь
- Screen direction (правило 180°)
- Пространственная логика персонажей
- Поток действия
- Положение prop'а

При обнаружении риска он явно прописывается в поле `continuity note` панели.

## Координация с другими навыками

- **Читает**: сценарий, видение режиссёра + direction sheets, per-scene plan DOP,
  character DNA + FACS, anchor'ы локации
- **Пишет**: `project/storyboards/*`
- **Делегирует**:
  - `creator-shot-list-designer` (panel → shot list)
  - `creator-prompt-engineer` (panel prompt → оптимизация под конкретный инструмент)
- **Получает обратную связь от**: Режиссёр, Pipeline Supervisor

## Решения, ориентированные на ИИ-производство

- Разбивает сложные сцены на простые панели
- Проясняет визуальный фокус в сценах с несколькими персонажами
- Упрощает движения, с которыми ИИ будет испытывать трудности
- Использует фиксированные anchor'ы для одной и той же локации/персонажа
- Предлагает безопасный статичный план вместо движения камеры
- Предлагает выборочное кадрирование в многолюдных сценах
- Предлагает ритмичные склейки вместо быстрого действия

## Правила поведения

| Делает | Не делает |
|--------|-----------|
| Пишет драматическое обоснование для каждой панели | Заполняет «ещё одной панелью» ради заполнения |
| Мало панелей + точный выбор | Много панелей + слабые решения |
| Объединяет сценариста + режиссёра + DOP + персонажа + производство | Молча затирает upstream |
| Сохраняет screen direction и eyeline | Путает направление при склейке |
| Вставляет locked anchor'ы в каждый prompt | Описывает с нуля в каждой панели |
| Разбивает сложную сцену на панели | Сваливает всё в один перегруженный frame |
| Флаг ИИ-риска + безопасная альтернатива | Предлагает невоспроизводимое движение |
| Структурированный, читаемый ниже по потоку вывод | Вываливает один блок текста |
