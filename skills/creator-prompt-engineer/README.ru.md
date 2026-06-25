# Промпт-инженер — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Русский** · [日本語](README.ja.md) · [한국어](README.ko.md)

**Слой перевода** между творческим пайплайном и ИИ-генераторами.
Превращает решения, выработанные скиллами сценариста, режиссёра, оператора-постановщика,
персонажей, художника-постановщика, раскадровки и шот-листа, в **действительно
производимые и согласованные** промпты. Оптимизирует под каждый инструмент
(Midjourney ≠ Sora ≠ Stable Diffusion), встраивает зафиксированные якоря
в каждый промпт и создаёт безопасные альтернативы для рискованных сцен.

## Философия

Промпт-инженер **не изобретает изображения** — он кодирует решения вышестоящего
звена (upstream). Этот скилл:

- **Locked anchors**: character DNA + location master reference + style block —
  даже после 50 промптов тот же персонаж выходит с тем же лицом
- **Tool fitness**: у каждого ИИ-инструмента свой язык промптов
- **Producibility audit**: эта сцена положит генератор — предложи альтернативу
- **Consistency discipline**: для полного метра промпты — это система, а не отдельные элементы
- **FACS expression coding**: AU1 + AU4 + AU15 вместо «грустный» — более согласованный результат
- **Никогда не перезаписывает upstream молча**: помечает и переспрашивает при необходимости

## Для чего нужен

| Результат | Содержание |
|-----------|------------|
| **Character prompts** | Зафиксированная DNA + посценная вариация |
| **Location prompts** | Master reference + вариация день/ночь/погода |
| **Style anchors** | Визуальный/технический блок для всего фильма |
| **Negative prompts** | Банк негативных промптов по категориям |
| **Panel prompts** | Промпт генерации изображения из панели раскадровки |
| **Shot prompts** | Промпт генерации ИИ-видео из шот-листа |
| **Character sheets** | Генерация референса спереди/сбоку/сзади/крупно |
| **Producibility risk report** | Риск на уровне сцены/кадра + безопасная альтернатива |
| **Tool guide** | Заметки по конкретным инструментам для оператора |

## Когда вступает в дело

- До производства нужны ИИ-промпты для изображений/видео
- Нужно выстроить систему якорей для согласованности персонажа/локации
- Вывод раскадровки или шот-листа нужно превратить в промпты инструмента
- Существующий промпт рискован — нужна безопасная альтернатива
- Когда `creator-pipeline-supervisor` делегирует этап промптов

## Руководство по оптимизации под инструменты (сводка)

### Midjourney
- Параметры `--ar`, `--style raw`, `--s`
- `--cref` и `--cw` для референса персонажа
- `--sref` для референса стиля
- Компактная формулировка — нагромождение прилагательных ослабляет сигнал

### DALL·E
- Естественный язык > свалка тегов
- Прописывайте пространственные отношения
- Избегайте генерации текста внутри изображения

### Stable Diffusion (SDXL / SD3)
- Positive + negative раздельно
- Заметки LoRA / reference / seed для согласованности персонажа
- Важные термины в начало (token weight)

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- Одно основное движение камеры
- Контролируемое число персонажей
- Чёткие opening + closing frame
- Короткая длительность (обычно 3–10 с)
- Лимиты по конкретным инструментам:
  - Sora 2: ~20 с
  - Kling 3.0: subject binding для согласованности
  - Veo: сильная motion fidelity
  - Runway Gen-3/4: движение осмысленное, lip sync слабый

## Система зафиксированных якорей (для полного метра)

### Character DNA block

Копируется **дословно** из `project/characters/{slug}/ai-prompts.md`:

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

Дословно из `project/production-design/locations/{slug}/master-reference.md`:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall, lime-washed walls with
soot stain along the lower meter, raw wooden floor, wooden table center,
copper-lidded cabinet on the north wall, copper kettle on a small iron stove
```

### Style block

```
{style}: realistic cinematic period drama, soft natural light, 35mm film
feeling, subtle film grain, muted earth-tone palette, 2.39:1 aspect ratio,
no modern objects
```

Эти блоки **дословно повторяются в каждом промпте** этой сцены/персонажа/локации.
Эта дисциплина и есть двигатель согласованности.

## Категории негативных промптов

| Проблема | Негативный термин |
|----------|-------------------|
| Искажение лица | distorted face, malformed face, asymmetric eyes, blurred features |
| Ошибка руки | extra fingers, missing fingers, fused fingers, deformed hand |
| Анахронизм | modern clothes, modern tech, plastic, neon, smartphone |
| ИИ-артефакт | warping, morphing, flickering, jittery motion |
| Качество | low quality, low resolution, jpeg artifacts, oversaturated |
| Текст | unwanted text, watermark, signature, logo |
| Композиция | extra characters, cropped subject, duplicate subject |
| Камера | unintended shake, fisheye distortion |

Некоторые инструменты игнорируют негативный промпт — в этом случае впишите его
внутрь positive prompt как подсказку *"avoid: ..."*.

## Аудит производимости ИИ-видео

Проверки перед выдачей видео-промпта:

- Не слишком ли много действия в одном кадре?
- Не слишком ли много персонажей?
- Сложное ли движение камеры?
- Рискованна ли детализация рук/пальцев/лица?
- Удержится ли согласованность костюма/реквизита?
- Не слишком ли локация перегружена?
- Согласованы ли свет и время суток?
- Не стоит ли разбить сцену на части вместо одного промпта?
- Нужен ли lip sync? (пометить)
- Не слишком ли промпт абстрактен?

При наличии риска даёт **безопасную упрощённую альтернативу**.

## Генерация вариаций

Сфокусированные вариации для одной и той же сцены:

- Realistic
- More cinematic
- Darker
- Low-budget / simpler
- Wide alt.
- Close alt.
- Night
- Daylight
- AI-safe
- Poster / key art

**Назначение каждой вариации записывается** — почему и в каком случае её использовать.

## Куда записывает свои результаты

В `project/prompts/`:

| Файл | Содержание |
|------|------------|
| `character-prompts/{slug}.md` | Зафиксированная DNA + вариации сцены |
| `location-prompts/{slug}.md` | Master anchor + вариации |
| `style-anchors.md` | Style block(s) для всего фильма |
| `negative-prompts.md` | Банк негативных промптов |
| `scene-{NN}/panel-{PP}.md` | Промпты изображений панелей |
| `scene-{NN}/shot-{SS}.md` | Промпты видео кадров |
| `character-sheets/{slug}.md` | Промпты генерации листов спереди/сбоку/сзади/крупно |
| `prompt-system.md` | Документация системы якорей |
| `producibility-risk-report.md` | Флаги риска + безопасная альтернатива |
| `tool-guide.md` | Заметки оператора по конкретным инструментам |

## Двуязычный формат промпта

Когда пользователь хочет пояснение на родном языке + промпт на английском:

```
Türkçe Açıklama:
Bu prompt karakterin yalnızlığını vurgulayan geniş bir dış mekân planı
üretmek için hazırlanmıştır.

English Prompt:
A lonely middle-aged man standing at the edge of a foggy rural road at
dawn, wide cinematic shot, 35mm lens feeling, cold blue morning light,
worn dark traditional clothing, quiet melancholic mood, realistic period
drama, subtle film grain, 16:9 aspect ratio.
```

## Координация с другими скиллами

- **Читает**: все творческие выходы вышестоящего звена
- **Пишет**: `project/prompts/*`
- **Делегирует**:
  - человеку-оператору, который будет запускать ИИ-инструменты
  - обратную связь **storyboard artist** или **shot-list designer**, если
    аудит производимости требует изменить upstream
- **Получает обратную связь**: Pipeline Supervisor (дрейф согласованности)

## Правила поведения

| Делает | Не делает |
|--------|-----------|
| Кладёт locked anchors в каждый промпт при мультикадровой работе | Описывает с нуля каждый раз |
| Пишет промпты под конкретный инструмент | Даёт один и тот же промпт всем инструментам |
| Аудит производимости + безопасная альтернатива | Молча проскакивает риск |
| Использует коды FACS AU | Нагромождает прилагательные вроде «грустный» |
| Снижает раздувание прилагательными | Набивает вычурными словами |
| Сохраняет решение upstream, без молчаливой перезаписи | Добавляет творческую отсебятину |
| Уважает исследование эпохи | Оставляет анахронизмы |
| Структурированный, читаемый ниже по потоку вывод | Вываливает промпт одним блоком |
| Формат пояснение на родном языке + промпт на английском (по запросу) | Навязывает английский всегда |
