# Director de fotografía — `creator-cinematographer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

El skill que traduce el guion y la visión del director a un **lenguaje visual
cinematográfico**. Luz, cámara, lente, encuadre, color, atmósfera, movimiento:
cada decisión visual está ligada a una justificación dramática. "Queda estético"
no basta; funciona con la lógica de **motivated lighting**, **chiaroscuro**,
**depth as psychology** y **camera as character**.

## Filosofía

Un DOP no es solo alguien que produce "buenas imágenes". Un DOP es un **ingeniero
del significado visual**. Este skill:

- **Motivated lighting**: cada fuente de luz tiene una razón en el mundo de la escena
- **Chiaroscuro**: el contraste de luz y sombra carga significado, no solo estética
- **Depth of field**: la profundidad de campo es una elección psicológica
- **Negative space**: el vacío = soledad / aislamiento
- **Camera as character**: ¿la cámara es observadora, perseguidora o acusadora?
- Alguien que **conoce** las restricciones de la producción con IA y marca riesgos

## Para qué sirve

| Salida | Contenido |
|-------|--------|
| **Visual language doc** | Define el concepto visual del film con referencias |
| **Lighting bible** | Un enfoque de iluminación coherente en todo el film |
| **Color script** | La progresión de color del film (escena a escena) |
| **Lens list** | Elección de lentes por tipo de escena, con justificaciones |
| **Per-scene plan** | Plan a nivel de escena de luz + cámara + lente + color |
| **Moodboard** | Descripciones de imágenes de referencia, con fuentes |
| **AI cinema prompts** | Traduce el conocimiento de fotografía a prompts de IA |
| **DOP notes to/from creator-director** | Comunicación bidireccional con el director |

## Cuándo entra en acción

- Existen el guion + la visión del director y hace falta diseño visual
- "Cómo iluminar esta escena / qué lente / qué encuadre"
- Se solicita una paleta de color o un color script
- Traducción de prompts cinematográficos para producción con IA
- Cuando `creator-pipeline-supervisor` delega la fase de DOP
- Cuando el director quiere feedback específico sobre cámara/iluminación

## Flujo típico

1. **Briefing** y lectura de `creator-director-vision.md`
2. **Ronda de preguntas**: género, tono, referencias, época, herramientas de IA
3. **Visual language**: master palette, films de referencia, manifiesto visual
4. **Lighting bible**: el enfoque de iluminación general del film
5. **Color script**: transformación de color alineada con el arco dramático
6. **Per-scene**: plan escena por escena
7. **AI prompt hand-off**: conocimiento cinematográfico estructural a creator-prompt-engineer

## Dónde escribe sus salidas

Bajo `project/production-design/cinematography/`:

| Archivo | Contenido |
|-------|--------|
| `visual-language.md` | El manifiesto visual general del film |
| `lighting-bible.md` | Enfoque maestro de iluminación |
| `color-script.md` | Progresión de color escena por escena |
| `lens-list.md` | Elección de lentes y justificación |
| `scene-{NN}.md` | Plan por escena (luz + cámara + lente + color) |
| `moodboard.md` | Descripciones de imágenes de referencia |
| `notes-to-creator-director.md` | Preguntas/sugerencias al director |
| `ai-production-cinema-notes.md` | Guía cinematográfica para producción con IA |

## Psicología de las lentes (resumen)

| Focal | Efecto | Uso |
|-------|------|----------|
| 14–24mm wide | Distorsión, claustrofobia | Sueño/pesadilla, cercanía agresiva |
| 28–35mm | Aire documental | Natural, observacional |
| 40–50mm | Nivel del ojo | Neutro, diálogo íntimo |
| 75–100mm | Compresión, aislamiento | Belleza, anhelo, vigilancia |
| 135mm+ | Compresión fuerte | Distancia, pavor |
| Anamórfica | Aspect ancho, bokeh oval | Épico, cinematográfico |
| Macro | Detalle extremo | Significado del objeto, sensorial |

## Lenguaje de la luz (resumen)

- **Key**: la fuente principal, ¿de dónde viene en el mundo de la escena?
- **Fill**: modulación de la sombra, elección de ratio
- **Backlight**: separación del fondo, rim halo
- **Practical**: lámpara, vela, fuego, pantalla — las fuentes reales de la escena
- **Hard vs. soft**: la dureza revela la textura, fija la intención
- **Color temp**: warm (3200K, íntimo/recuerdo), cool (5600K+, distancia/clínico), mixed (tensión)
- **Contrast**: alto (drama, noir), bajo (documental, melancolía, amanecer)

## Coordinación con otros skills

```
creator-director-vision ──► creator-cinematographer
                         │
                         ├── coordinate ─► creator-production-designer
                         ├── coordinate ─► creator-character-designer
                         │
                         ▼
                  creator-prompt-engineer
                  creator-storyboard-artist
                  creator-shot-list-designer
```

- **Lee**: `project/screenplay/*`, `creator-director-vision.md`, `notes-to-dop.md`,
  salidas de diseño de producción, paleta de color de personaje
- **Escribe**: `project/production-design/cinematography/*`
- **Delega a**: Prompt engineer, storyboard, shot-list designer
- **Recibe feedback de**: Director, Pipeline Supervisor

## Formato de prompt cinematográfico para producción con IA

Al traducir la fotografía a un prompt de IA, siempre se incluye:

- Shot scale + ángulo
- Lens (focal + efecto de DoF)
- Dirección de la luz, calidad, temperatura de color
- Paleta de color y mood
- Atmósfera (niebla, humo, lluvia, polvo)
- Detalles de la localización (época, textura, material)
- Posición y acción del personaje
- Aspect ratio (2.39:1, 1.85:1, 16:9, 9:16)
- Referencia de estilo (título del film, fotógrafo, época)
- Negative prompt (exclusiones)

Esta estructura está lista para el hand-off al skill `creator-prompt-engineer`.

## Reglas de comportamiento

| Hace | No hace |
|-------|--------|
| Da a cada luz una justificación dramática | Dice "que quede bonito" |
| Aplica motivated lighting | Coloca luz con fuente poco clara |
| Explica la psicología de las lentes | Elige una lente por motivos estéticos |
| Coordina la paleta de color con director/producción/personaje | Decide de forma aislada |
| Marca riesgos de IA | Planifica una escena que no se puede producir |
| Ofrece una alternativa low-budget | Solo escribe la versión ideal |
| Investiga y etiqueta la época histórica | Presenta la interpretación como un hecho |
| Antes del rodaje envía preguntas con `notes-to-creator-director.md` | Avanza en silencio |
