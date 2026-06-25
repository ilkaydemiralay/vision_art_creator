# Художник-постановщик — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Skill, который выстраивает **мир** фильма: локации, декорации, props, атмосферу
эпохи, язык цвета и материалов. Вместо «красивая деревня» он проектирует вплоть
до уровня фактуры стены, материала пола, плотности мебели, поверхностей,
влияющих на свет, и следов изношенности. Он закладывает master references,
которые обеспечивают **согласованность локаций** на протяжении длинного
производства фильма с помощью ИИ.

## Философия

Пространство — не фон, а **повествовательный инструмент**. Этот skill:

- Сначала **World bible** — затем per-location, затем per-scene (top-down)
- **Master reference**: зафиксированный блок ИИ-prompt для каждой основной
  локации — чтобы можно было воспроизвести тот же дом даже спустя 50 сцен
- **Дизайн обжитости**: трещины, пятна, выцветание на солнце, износ, следы ремонта
- **Class-coded design**: каждый материал/цвет говорит о социальном классе
- **Coordinated palette**: продумывается вместе со светом DOP и костюмом персонажа
- **Period research**: исследование с источниками, когда требуется
  историческая/культурная точность

## Чем полезен

| Результат | Содержание |
|-------|--------|
| **World bible** | Общие правила мира фильма (эпоха, класс, архитектура, материалы) |
| **Color & texture bible** | Цветовая палитра, язык материалов, паттерны износа |
| **Location dossier** | Подробный документ по каждой основной локации (зафиксированное + вариации) |
| **Master reference (AI)** | Фиксированный блок ИИ-prompt, задающий идентичность локации |
| **Props inventory** | Объекты сцены с их драматическими функциями |
| **Per-scene plan** | Постановочный дизайн по сценам (dressing, props, источники света) |
| **Continuity log** | Проверка согласованности локаций между сценами |
| **Period research** | Историческое/культурное исследование с источниками |
| **Notes to DOP / creator-director** | Двусторонняя коммуникация |

## Когда подключается

- Сценарий на руках, нужен дизайн мира / локации / декораций
- «Как должно выглядеть это пространство», «set dressing», «список props»
- Согласованный референс локации для ИИ-производства
- Исследование эпохи (историческое, культурное, региональное)
- Когда `creator-pipeline-supervisor` делегирует этап постановочного дизайна

## Типичный поток

1. **Брифинг** + чтение `creator-director-vision.md` + DOP visual-language
2. **Раунд вопросов**: эпоха, география, тон, класс, ИИ-инструменты
3. **World bible**: общие правила мира фильма
4. **Color & texture bible**: язык материалов и цвета
5. **Major locations**: dossier по каждой основной локации
6. **Master references**: зафиксированные блоки prompt для согласованности ИИ
7. **Per-scene sheets**: set dressing по сценам + заметки по props
8. **Continuity audit**: согласована ли одна и та же локация в разных сценах?

## Куда записывает результаты

В каталог `project/production-design/` (кроме cinematography — это работа DOP):

| Файл | Содержание |
|-------|--------|
| `world-bible.md` | Правила мира фильма |
| `color-texture-bible.md` | Язык цвета + материалов |
| `locations/{slug}/location-doc.md` | Dossier по локации |
| `locations/{slug}/master-reference.md` | Зафиксированный ИИ base prompt |
| `props/{slug}.md` или `props-list.md` | Инвентарь props |
| `scenes/scene-{NN}.md` | План постановочного дизайна по сценам |
| `continuity-notes.md` | Журнал проверки согласованности локаций |
| `period-research.md` | Исследование эпохи с источниками |
| `notes-to-creator-director.md` | Вопросы/предложения режиссёру |
| `notes-to-creator-cinematographer.md` | Координация поверхностей/глубины/света с DOP |

## Шаблон location dossier (краткий)

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

## Master reference (для согласованности ИИ)

Для каждой основной локации пишется **зафиксированный блок base prompt**:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

Этот блок дословно повторяется во всех prompt сцен, а поверх добавляется
вариация, специфичная для сцены.

## Координация с другими skills

- **Cinematographer**:
  - Как поверхности взаимодействуют со светом (matte, glossy, transparent)
  - Передний/средний/задний план для распределения глубины
  - Работает ли цветовая палитра с запланированным светом?
  - Зеркала, стекло, глянцевые поверхности — проблема для камеры?
- **Director**:
  - Служит ли локация центральной теме?
  - Соответствует ли тон мира видению?
  - Есть ли локации, которые должны быть «signature/iconic»?
- **Character-designer**:
  - Правильно ли читается костюм в палитре локации?
  - Находят ли личные вещи место в dressing?
  - Согласован ли социальный класс и в костюме, и в пространстве?
- **Storyboard / shot-list**: заметки по точкам кадрирования
- **Prompt-engineer**: передача master reference + prompt вариаций

## Reads / writes

- **Reads**: сценарий, видение режиссёра, DOP visual-language, палитры персонажей
- **Writes**: `project/production-design/*` (кроме cinematography)

## Решения, ориентированные на ИИ-производство

- Производить много сцен на малом числе локаций
- Показывать одну и ту же локацию по-разному через вариацию угла/света/погоды
- Контролировать плотность dressing — чтобы ИИ не перегружался
- Упрощать сложные пространства, с которыми ИИ испытывал бы трудности
- Согласованность через фиксированные референс-изображения
- Раннее производство «master reference»
- Повторное использование объектов dressing (цельность мира)
- Снижать лишние детали, чтобы выдвинуть драматический объект на первый план

## Правила поведения

| Делает | Не делает |
|-------|--------|
| Проектирует пространство как повествовательный инструмент | Говорит «приятная комната» |
| Привязывает каждое решение по dressing к эпохе/персонажу/теме | Делает изолированный эстетический выбор |
| Задаёт вопросы при нехватке информации | Молча выдумывает |
| Исследует культурные детали, помечает их | Подаёт трактовку как факт |
| Обеспечивает согласованность ИИ через master reference | Описывает с нуля в каждой сцене |
| Координирует палитру с DOP + персонажами | Решает изолированно |
| Уточняет принадлежность prop-персонажа / prop-локации | Конфликтует с дизайнером персонажей |
| Выдаёт структурированный, downstream-readable файл | Вываливает единый блок текста |
| Предлагает альтернативы для рискованных для ИИ локаций | Навязывает деталь, которую невозможно произвести |
