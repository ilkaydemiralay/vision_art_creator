# Diseñador de Producción — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

El skill que construye el **mundo** de la película: localizaciones, decorados,
props, atmósfera de época, lenguaje de color y de materiales. En lugar de decir
"un pueblo bonito", diseña al nivel de la textura del muro, el material del
suelo, la densidad del mobiliario, las superficies que afectan a la luz y las
huellas del desgaste. Establece las master references que mantienen la
**consistencia de localización** a lo largo de una producción de cine con IA de
formato largo.

## Filosofía

Un espacio no es un fondo: es un **instrumento narrativo**. Este skill:

- **World bible** primero — luego per-location, luego per-scene (top-down)
- **Master reference**: un bloque de prompt de IA bloqueado para cada
  localización principal — para poder producir la misma casa incluso 50 escenas
  después
- **Diseño de lo vivido**: grietas, manchas, decoloración por el sol, desgaste,
  marcas de reparación
- **Class-coded design**: cada material/color habla de la clase social
- **Coordinated palette**: pensada junto con la iluminación del DOP y el
  vestuario del personaje
- **Period research**: investigación con fuentes cuando se requiere precisión
  histórica/cultural

## Para qué sirve

| Salida | Contenido |
|-------|--------|
| **World bible** | Las reglas generales del mundo de la película (época, clase, arquitectura, materiales) |
| **Color & texture bible** | Paleta de color, lenguaje de materiales, patrones de desgaste |
| **Location dossier** | Un documento exhaustivo para cada localización principal (bloqueado + variaciones) |
| **Master reference (AI)** | El bloque de prompt de IA fijo de la identidad de una localización |
| **Props inventory** | Objetos de escena, con sus funciones dramáticas |
| **Per-scene plan** | Diseño de producción escena por escena (dressing, props, fuentes de luz) |
| **Continuity log** | Control de consistencia de localización entre escenas |
| **Period research** | Investigación histórica/cultural con fuentes |
| **Notes to DOP / creator-director** | Comunicación bidireccional |

## Cuándo entra en acción

- Guion en mano, se necesita diseño de mundo / localización / decorado
- "Cómo debe verse este espacio", "set dressing", "lista de props"
- Referencia de localización consistente para producción con IA
- Investigación de época (histórica, cultural, regional)
- Cuando `creator-pipeline-supervisor` delega la fase de diseño de producción

## Flujo típico

1. **Briefing** + lectura de `creator-director-vision.md` + DOP visual-language
2. **Ronda de preguntas**: época, geografía, tono, clase, herramientas de IA
3. **World bible**: las reglas generales del mundo de la película
4. **Color & texture bible**: lenguaje de materiales y de color
5. **Major locations**: un dossier para cada localización principal
6. **Master references**: bloques de prompt bloqueados para la consistencia con IA
7. **Per-scene sheets**: set dressing escena por escena + notas de props
8. **Continuity audit**: ¿es la misma localización consistente en distintas escenas?

## Dónde escribe sus salidas

Bajo `project/production-design/` (excluyendo cinematography — eso es del DOP):

| Archivo | Contenido |
|-------|--------|
| `world-bible.md` | Las reglas del mundo de la película |
| `color-texture-bible.md` | Lenguaje de color + materiales |
| `locations/{slug}/location-doc.md` | Dossier per-location |
| `locations/{slug}/master-reference.md` | Base prompt de IA bloqueado |
| `props/{slug}.md` o `props-list.md` | Inventario de props |
| `scenes/scene-{NN}.md` | Plan de diseño de producción escena por escena |
| `continuity-notes.md` | Registro de control de consistencia de localización |
| `period-research.md` | Investigación de época con fuentes |
| `notes-to-creator-director.md` | Preguntas/sugerencias al director |
| `notes-to-creator-cinematographer.md` | Coordinación de superficie/profundidad/luz con el DOP |

## Plantilla de location dossier (resumen)

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

## Master reference (para la consistencia con IA)

Se escribe un **bloque de base prompt bloqueado** para cada localización principal:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

Este bloque se repite tal cual en todos los prompts de escena, y encima se
añade la variación específica de la escena.

## Coordinación con otros skills

- **Cinematographer**:
  - Cómo se relacionan las superficies con la luz (matte, glossy, transparent)
  - Primer plano/plano medio/fondo para escalonar la profundidad
  - ¿Funciona la paleta de color con la iluminación planificada?
  - ¿Son los espejos, el cristal y las superficies brillantes un problema para la cámara?
- **Director**:
  - ¿Sirve la localización al tema central?
  - ¿Encaja el tono del mundo con la visión?
  - ¿Hay localizaciones que deban ser "signature/iconic"?
- **Character-designer**:
  - ¿Se lee el vestuario correctamente dentro de la paleta de la localización?
  - ¿Encuentran los objetos personales un lugar dentro del dressing?
  - ¿Es la clase social consistente tanto desde el vestuario como desde el espacio?
- **Storyboard / shot-list**: notas de los puntos de encuadre
- **Prompt-engineer**: hand-off de la master reference + prompts de variación

## Reads / writes

- **Reads**: guion, visión del director, DOP visual-language, paletas de personaje
- **Writes**: `project/production-design/*` (excluyendo cinematography)

## Soluciones orientadas a la producción con IA

- Producir muchas escenas con pocas localizaciones
- Mostrar la misma localización de forma distinta variando ángulo/luz/clima
- Controlar la densidad del dressing — para que la IA no se sobrecargue
- Simplificar espacios complejos con los que la IA tendría dificultades
- Consistencia mediante imágenes de referencia fijas
- Producción temprana de la "master reference"
- Reutilizar objetos del dressing (coherencia del mundo)
- Reducir el detalle innecesario para hacer destacar el objeto dramático

## Reglas de comportamiento

| Hace | No hace |
|-------|--------|
| Diseña el espacio como instrumento narrativo | Dice "una habitación bonita" |
| Liga cada decisión de dressing a la época/personaje/tema | Hace elecciones estéticas aisladas |
| Pregunta cuando falta información | Inventa en silencio |
| Investiga los detalles culturales y los etiqueta | Presenta la interpretación como un hecho |
| Garantiza la consistencia con IA mediante la master reference | Describe desde cero en cada escena |
| Coordina la paleta con el DOP + los personajes | Decide en aislamiento |
| Aclara la propiedad prop-de-personaje / prop-de-localización | Choca con el diseñador de personajes |
| Entrega un archivo estructurado y downstream-readable | Suelta un único bloque de texto |
| Ofrece alternativas para localizaciones de riesgo para la IA | Fuerza un detalle que no se puede producir |
