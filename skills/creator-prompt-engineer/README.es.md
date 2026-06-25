# Ingeniero de Prompts — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · **Español** · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

La **capa de traducción** entre el pipeline creativo y los generadores de IA.
Convierte las decisiones producidas por las skills de guionista, director, DOP,
personajes, producción, storyboard y lista de planos en prompts **realmente
producibles y consistentes**. Optimiza por herramienta (Midjourney ≠ Sora ≠
Stable Diffusion), incrusta los anchors bloqueados en cada prompt y genera
alternativas seguras para escenas arriesgadas.

## Filosofía

El ingeniero de prompts **no inventa imágenes** — codifica las decisiones del
upstream. Esta skill:

- **Locked anchors**: character DNA + location master reference + style block —
  incluso después de 50 prompts el mismo personaje sale con la misma cara
- **Tool fitness**: cada herramienta de IA tiene su propio lenguaje de prompt
- **Producibility audit**: esta escena vencerá al generador — propón una alternativa
- **Consistency discipline**: para un largometraje, los prompts son un sistema, no algo aislado
- **FACS expression coding**: AU1 + AU4 + AU15 en lugar de «triste» — resultados más consistentes
- **Nunca sobrescribe el upstream en silencio**: lo señala y vuelve a preguntar cuando hace falta

## Para qué sirve

| Salida | Contenido |
|--------|-----------|
| **Character prompts** | DNA bloqueado + variación escena por escena |
| **Location prompts** | Master reference + variación día/noche/clima |
| **Style anchors** | Bloque visual/técnico para toda la película |
| **Negative prompts** | Banco de prompts negativos por categoría |
| **Panel prompts** | Prompt de generación de imagen a partir de un panel de storyboard |
| **Shot prompts** | Prompt de generación de vídeo IA a partir de la lista de planos |
| **Character sheets** | Generación de referencia frontal/lateral/posterior/primer plano |
| **Producibility risk report** | Riesgo a nivel de escena/plano + alternativa segura |
| **Tool guide** | Notas específicas por herramienta para el operador |

## Cuándo entra en acción

- Se necesitan prompts de imagen/vídeo IA antes de la producción
- Hay que montar un sistema de anchors para la consistencia de personaje/lugar
- Una salida de storyboard o lista de planos se va a convertir en prompts de herramienta
- Un prompt existente es arriesgado — se quiere una alternativa segura
- Cuando `creator-pipeline-supervisor` delega la etapa de prompts

## Guía de optimización por herramienta (resumen)

### Midjourney
- Parámetros `--ar`, `--style raw`, `--s`
- `--cref` y `--cw` para referencia de personaje
- `--sref` para referencia de estilo
- Redacción compacta — apilar adjetivos debilita la señal

### DALL·E
- Lenguaje natural > volcado de tags
- Escribe las relaciones espaciales
- Evita generar texto dentro de la imagen

### Stable Diffusion (SDXL / SD3)
- Positive + negative separados
- Notas de LoRA / reference / seed para la consistencia del personaje
- Términos importantes al principio (token weight)

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- Un único movimiento de cámara principal
- Número de personajes controlado
- Opening + closing frame claros
- Duración corta (3–10s típico)
- Límites específicos por herramienta:
  - Sora 2: ~20s
  - Kling 3.0: subject binding para consistencia
  - Veo: motion fidelity fuerte
  - Runway Gen-3/4: el movimiento tiene sentido, lip sync débil

## Sistema de anchors bloqueados (para un largometraje)

### Character DNA block

Se copia **literalmente** desde `project/characters/{slug}/ai-prompts.md`:

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

Literalmente desde `project/production-design/locations/{slug}/master-reference.md`:

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

Estos bloques se **repiten literalmente en cada prompt** de esa escena/personaje/lugar.
Esta disciplina es el motor de la consistencia.

## Categorías de prompt negativo

| Problema | Término negativo |
|----------|-----------------|
| Distorsión facial | distorted face, malformed face, asymmetric eyes, blurred features |
| Error de manos | extra fingers, missing fingers, fused fingers, deformed hand |
| Anacronismo | modern clothes, modern tech, plastic, neon, smartphone |
| Artefacto de IA | warping, morphing, flickering, jittery motion |
| Calidad | low quality, low resolution, jpeg artifacts, oversaturated |
| Texto | unwanted text, watermark, signature, logo |
| Composición | extra characters, cropped subject, duplicate subject |
| Cámara | unintended shake, fisheye distortion |

Algunas herramientas ignoran el prompt negativo — en ese caso escríbelo dentro
del positive prompt como una pista *"avoid: ..."*.

## Auditoría de producibilidad de vídeo IA

Comprobaciones antes de emitir un prompt de vídeo:

- ¿Demasiada acción en un solo plano?
- ¿Demasiados personajes?
- ¿El movimiento de cámara es complejo?
- ¿El detalle de mano/dedos/cara es arriesgado?
- ¿Se puede mantener la consistencia de vestuario/atrezo?
- ¿El lugar está demasiado lleno?
- ¿Luz y momento del día son consistentes?
- ¿Debería dividirse la escena en partes en vez de un solo prompt?
- ¿Hace falta lip sync? (señálalo)
- ¿El prompt es innecesariamente abstracto?

Si hay riesgo, da una **alternativa segura simplificada**.

## Generación de variaciones

Variaciones enfocadas para la misma escena:

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

Se **anota el propósito de cada variación** — por qué y en qué caso se usa.

## Dónde escribe sus salidas

Bajo `project/prompts/`:

| Archivo | Contenido |
|---------|-----------|
| `character-prompts/{slug}.md` | DNA bloqueado + variaciones de escena |
| `location-prompts/{slug}.md` | Master anchor + variaciones |
| `style-anchors.md` | Style block(s) de toda la película |
| `negative-prompts.md` | Banco de prompts negativos |
| `scene-{NN}/panel-{PP}.md` | Prompts de imagen de panel |
| `scene-{NN}/shot-{SS}.md` | Prompts de vídeo de plano |
| `character-sheets/{slug}.md` | Prompts de generación de sheet frontal/lateral/posterior/primer plano |
| `prompt-system.md` | Documentación del sistema de anchors |
| `producibility-risk-report.md` | Marcas de riesgo + alternativa segura |
| `tool-guide.md` | Notas para el operador específicas por herramienta |

## Formato de prompt bilingüe

Cuando el usuario quiere una explicación en su idioma + un prompt en inglés:

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

## Coordinación con otras skills

- **Lee**: todas las salidas creativas del upstream
- **Escribe**: `project/prompts/*`
- **Delega**:
  - al operador humano que ejecutará las herramientas de IA
  - feedback al **storyboard artist** o al **shot-list designer** si la
    auditoría de producibilidad exige cambiar el upstream
- **Recibe feedback**: Pipeline Supervisor (deriva de consistencia)

## Reglas de comportamiento

| Hace | No hace |
|------|---------|
| Pone los locked anchors en cada prompt en trabajos multi-plano | Describe desde cero cada vez |
| Escribe prompts adaptados a la herramienta | Da el mismo prompt a toda herramienta |
| Auditoría de producibilidad + alternativa segura | Pasa por alto el riesgo en silencio |
| Usa códigos FACS AU | Amontona adjetivos como «triste» |
| Reduce el exceso de adjetivos | Rellena con palabras rebuscadas |
| Preserva la decisión del upstream, sin sobrescribir en silencio | Añade invención creativa |
| Respeta la investigación de época | Deja anacronismos |
| Salida estructurada, legible aguas abajo | Vuelca un prompt de un solo bloque |
| Formato de explicación en idioma nativo + prompt en inglés (si se pide) | Impone siempre el inglés |
