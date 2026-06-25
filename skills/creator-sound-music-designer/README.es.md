# Diseñador de Sonido y Música — `creator-sound-music-designer`

[English](README.md) · [中文](README.zh.md) · [**Español**](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

La skill que construye el **mundo sensorial** de la película. Dos disciplinas integradas se unen:

- **Diseñador de sonido**: la realidad sensorial de espacios, personajes, objetos y eventos — ambience, foley, efectos, acústica, perspectiva sonora y el **silencio** (como herramienta dramática activa)
- **Compositor de cine / supervisor musical**: tema principal, leitmotifs de personajes, música de escena, ritmo, puntos de entrada/salida de la música

## Filosofía

El sonido y la música **no son decoración**. Cada decisión de sonido y música está ligada al propósito dramático de la escena, la psicología del personaje, la atmósfera visual, el ritmo del montaje y el impacto en el público. Esta skill:

- No dice "usa música triste" — diseña leitmotifs y planifica su evolución
- **Diseña el silencio de forma activa** — no es ausencia, sino una decisión dramática
- **Leitmotifs de personaje**: un motivo que comienza en una flauta se convierte en una pieza épica con cuerdas en el final
- **Disciplinada con los derechos de autor**: no imita a artistas vivos, "similar pero no igual"
- **En sincronía con el ritmo del montaje**: entrada/salida de la música coordinada con el plan de montaje del shot-list
- **Generación de prompts de sonido/música con IA**: Suno, Udio, ElevenLabs SFX, Stable Audio, Runway Audio

## Qué hace

| Salida | Contenido |
|--------|-----------|
| **Visión sonora** | La visión global de diseño de sonido de la película |
| **Visión musical** | El manifiesto del lenguaje musical de la película |
| **Tema principal** | Diseño del tema principal |
| **Temas de personaje** | Diseño de leitmotif por personaje |
| **Planes de escena** | Plan de sonido + música escena por escena |
| **Listas de ambience / foley / SFX** | Listas de inventario |
| **Plan de silencio** | Un mapa deliberado del silencio |
| **Plan de entrada/salida de la música** | Puntos de entrada y salida de la música |
| **Puentes sonoros** | Diseño de transiciones |
| **Prompts de sonido + música con IA** | Prompts específicos por herramienta |
| **Notas de balance de diálogo** | Notas de balance diálogo/música |
| **Notas del mix final** | Auditoría del mix final |
| **Informe de continuidad** | Verificación de continuidad sonora |

## Cuándo se activa

- Hay un guion en mano y se necesita un plan de diseño de sonido / música de cine
- Se solicitan ambience, foley, SFX o temas musicales
- Se necesitan prompts de sonido/música con IA
- Cuando el diseñador del shot-list entrega la intención sonora de la escena
- Cuando `creator-pipeline-supervisor` delega la etapa de audio

## Flujo típico

1. **Briefing** + lectura de todas las salidas de las skills previas
2. **Ronda de preguntas**: género, register, densidad musical, época, herramientas de IA
3. **Visión sonora** + **Visión musical**
4. **Tema principal + leitmotifs de personaje**
5. **Plan por escena**: ambient/foley/silencio/música para cada escena
6. **Plan de silencio**: un mapa del silencio deliberado
7. **Plan de entrada/salida de la música**
8. **Prompts de sonido + música con IA**
9. **Auditoría del mix final** (después del final cut)

## Diseño del silencio

El silencio es una decisión de diseño **activa**. Para cada silencio, la skill pregunta:

- ¿Se cortará aquí la música?
- ¿La ambience se atenúa o se lleva a cero?
- ¿Quedará solo una respiración o el sonido de un pequeño objeto?
- ¿El silencio transmite soledad, miedo o vacilación?
- ¿Está ahí para inquietar al público o para intensificar la emoción?
- ¿Qué sonido entra después del silencio?

## Ejemplo de leitmotif de personaje

```
Karakter: Demir
Müzikal duygu: bastırılmış yas + içsel kararlılık
Ana enstrüman: solo cello (başlangıç) → cello + ney (orta) → cello + yaylı
                grup (final)
Tempo: 60–66 BPM (slow heart)
Ton: minör, kromatik geçişler
Ritim: rubato, neredeyse zamansız
Motifin evrimi:
  - Sahne 1–5: solo cello, kısa 5-notalı motif, sessizlik aralıkları geniş
  - Sahne 6–12: ney ekleniyor — nefes katmanı
  - Sahne 13–18: yaylı grup açılıyor — toplum, geçmiş, anlam
  - Sahne 19 (final): tek cello, ilk motifin yarısı — kırılma
```

## Dónde escribe sus salidas

En `project/sound/`:

| Archivo | Contenido |
|---------|-----------|
| `sound-vision.md` | Visión global de diseño de sonido |
| `music-vision.md` | Manifiesto del lenguaje musical |
| `main-theme.md` | Diseño del tema principal |
| `character-themes/{slug}.md` | Leitmotif de personaje |
| `scenes/scene-{NN}.md` | Plan de sonido + música de escena |
| `ambience-list.md` | Inventario de ambience |
| `foley-list.md` | Inventario de foley |
| `special-effects-list.md` | SFX especiales |
| `silence-plan.md` | Mapa del silencio |
| `music-entry-exit-plan.md` | Timing de entrada/salida de la música |
| `sound-bridges.md` | Diseño de transiciones |
| `ai-sound-prompts.md` | Prompts de SFX con IA |
| `ai-music-prompts.md` | Prompts de música con IA |
| `dialogue-balance-notes.md` | Balance diálogo/música |
| `final-mix-notes.md` | Auditoría del mix final |
| `sound-continuity-report.md` | Verificación de continuidad |

## Formato de prompt de IA

### Ejemplo de prompt de SFX

```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```

### Ejemplo de prompt de música

```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```

### Formato de descripción en lengua nativa + prompt en inglés

```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## Derechos de autor y originalidad

- No sugiere copiar composiciones existentes
- No imita nota por nota el estilo de un artista vivo
- Trabaja con una lógica de "similar pero no igual", describiendo género + emoción
- En los prompts de música con IA, usa una atmósfera general en lugar del nombre de un artista

## Coordinación con otras skills

- **Lee**: todas las salidas creativas previas + las notas de montaje sonoro del shot-list
- **Escribe**: `project/sound/*`
- **Delega en**: `creator-final-cut-editor` (integración del final cut), el operador de la herramienta de audio con IA
- **Recibe feedback de**: Director, Pipeline Supervisor, Final-cut-editor

## Reglas de comportamiento

| Hace | No hace |
|------|---------|
| Liga el sonido y la música al propósito dramático | Los usa como decoración |
| Diseña el silencio de forma activa | Lo trata como ausencia |
| Sincroniza la evolución del leitmotif con el arco del personaje | Repite un único tema fijo |
| Piensa diálogo/música/ambience/silencio en conjunto | Decide de forma aislada |
| Disciplinada con los derechos de autor | Imita a artistas |
| Investiga lo histórico/cultural y lo etiqueta | Presenta la interpretación como un hecho |
| Escribe prompts de IA ajustados a la herramienta | Vuelca prompts genéricos |
| Preserva la continuidad sonora de una película larga | Piensa escena por escena y de forma inconexa |
