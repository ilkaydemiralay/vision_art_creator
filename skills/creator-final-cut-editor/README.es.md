# Editor de Montaje Final — `creator-final-cut-editor`

[English](README.md) · [中文](README.zh.md) · **Español** · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

La skill que convierte los resultados de producción de IA en una **película
terminada**. El final de la preproducción / el inicio de la posproducción. Una
vez que el material ha sido producido, gestiona el flujo rough cut → fine cut →
final cut → entrega; clasifica los errores de generación de IA, audita la
continuidad, verifica la integración de audio/música y produce másteres listos
para la entrega.

**Diferencia con shot-list-designer**: el shot list diseña la intención de
montaje ANTES del rodaje; creator-final-cut-editor EJECUTA el montaje sobre el
material real.

## Filosofía

El montaje final **no es una secuenciación técnica** — es la construcción de una
totalidad cinematográfica. Esta skill:

- **Una justificación dramática para cada corte** — «se ve bien» no basta
- **Ritmo multiescala**: dentro de un plano, dentro de una escena, a lo largo de toda la película
- **Triaje de errores de IA**: qué error rompe el montaje, cuál puede ocultarse, cuál puede quedarse
- **Diseño de la experiencia del público**: qué siente, aprende y se lleva el espectador
- **Disciplina de entrega**: YouTube ≠ festival ≠ Instagram ≠ archivo
- **Versionado**: gestiona rough/fine/final + cortes para festival/redes/tráiler por separado

## Qué hace

| Resultado | Contenido |
|-------|---------|
| **Evaluación de material** | Por plano: utilizable / revisar / regenerar / cortar |
| **Plan de rough cut** | Primera secuenciación tosca, lista de material faltante |
| **Plan de fine cut** | Puntos de corte, duraciones de planos, silencio |
| **Plan de final cut** | Preparación final + checklist de entrega |
| **Final-check por escena** | Auditoría detallada escena por escena |
| **Informe de toda la película** | Informe de final cut de la película completa |
| **Informe de errores de IA** | Errores de generación + clasificación de severidad |
| **Auditoría de integración de audio** | Feedback para el diseñador de sonido |
| **Notas de color grade** | Directivas de corrección de color |
| **EDL** | Edit Decision List legible por NLE |
| **Manifiesto de versiones** | Versiones de corte para festival/redes/tráiler |
| **Especificaciones de entrega** | Ajustes de exportación específicos por plataforma |
| **Plan de tráiler** | Plan de corte de teaser/tráiler |

## Cuándo se activa

- Se han producido planos de vídeo de IA, comienza el montaje
- Se requiere la planificación de rough/fine/final cut
- Se solicita una auditoría de errores de IA
- Se van a producir múltiples cortes (festival, redes, tráiler)
- Preparación de la exportación de entrega
- Cuando `creator-pipeline-supervisor` delega la fase de posproducción

## Flujo típico

1. **Evaluación de material** — cada plano se categoriza (✅🟡🟠🔴)
2. **Rough cut v01** — orden narrativo, secuencia dramática básica
3. **Fine cut v01** — puntos de corte, ritmo, silencio
4. **Auditoría de integración de sonido** — feedback para creator-sound-music-designer
5. **Informe de errores de IA** — clasificación crítico/medio/menor
6. **Notas de color grade** — si es necesario
7. **Verificación de subtítulos / títulos / gráficos**
8. **Final cut v01** — checklist de preparación
9. **Exportación de entrega** — versión específica por plataforma

## Matriz de triaje de errores de IA

| Severidad | Definición | Acción |
|----------|------------|--------|
| 🔴 Crítico | No puede entrar en el final cut | Regenerar (marcar a creator-prompt-engineer) |
| 🟡 Medio | Se oculta mediante trim/crop/color/sonido | Solución de montaje |
| ✅ Menor | No molesta al espectador | Puede quedarse |

Verificado: distorsión facial, errores de manos/dedos, lip-sync, cambios de
vestuario, pérdida de accesorios, deriva de localización, inconsistencia en la
dirección de la luz, movimiento de cámara artificial, flicker, warping,
morphing, objetos que se derriten, descomposición del fondo, anacronismo,
aspecto plástico.

## Formato de final-check por escena

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

## Dónde escribe sus resultados

Bajo `project/cuts/`:

| Archivo | Contenido |
|-------|---------|
| `material-evaluation.md` | Categoría de cada plano |
| `rough-cut/v{NN}.md` | Plan de rough cut |
| `fine-cut/v{NN}.md` | Plan de fine cut |
| `final-cut/v{NN}.md` | Plan de final cut + preparación |
| `scene-{NN}/final-check.md` | Detalle escena por escena |
| `final-cut-report.md` | Auditoría de toda la película |
| `ai-error-report.md` | Informe de errores de IA |
| `audio-integration-report.md` | Auditoría de integración de audio |
| `color-grade-notes.md` | Corrección de color |
| `subtitle-titles-graphics.md` | Subtítulos/títulos |
| `transitions.md` | Decisiones de transición |
| `edit-decision-list.md` | EDL |
| `versions/{cut-name}.md` | Manifiesto de versiones |
| `delivery/{platform}.md` | Especificaciones de exportación por plataforma |
| `trailer-plan.md` | Plan de tráiler/teaser |

## Gestión de versiones

| Versión | Duración | Objetivo |
|----------|----------|------|
| Rough Cut v01 | ~115% del objetivo | Primera prueba del flujo narrativo |
| Rough Cut v02 | ~108% | Integración de las piezas faltantes |
| Fine Cut | ~102% | Fijar ritmo y emoción |
| Director's Cut | 100% del objetivo | Aprobación completa del director |
| Final Cut | 100% | Listo para entrega |
| Festival Cut | 100% | Formato de festival |
| YouTube Cut | 100% o acortado | Algoritmo de YouTube |
| Trailer Cut | 30s–2 min | Marketing |
| Social Cut | 9:16 corto | Reels, TikTok |

Para cada versión: nombre, duración, cambios, escenas eliminadas/añadidas,
cambios de audio, justificación de la revisión, estado de aprobación.

## Ejemplo de especificaciones de entrega

| Plataforma | Aspecto | Resolución | FPS | Audio |
|----------|--------|------------|-----|-------|
| Máster YouTube 16:9 | 16:9 | 3840×2160 (4K) o 1920×1080 | 24/25 | AAC 320kbps estéreo |
| Máster de festival | 2.39:1 o 16:9 | 4K | 24 | WAV 48kHz 24-bit estéreo + 5.1 |
| Instagram Reels | 9:16 | 1080×1920 | 30 | AAC estéreo |
| TikTok | 9:16 | 1080×1920 | 30 | AAC estéreo |
| Web comprimido | 16:9 | 1920×1080 | 24/25 | AAC 192kbps |
| Máster de archivo | original | máxima | original | máster WAV |

## Lógica del corte de tráiler

Un tráiler **no es una miniatura de la película** — tiene su propia lógica de montaje:

- Los 6–10 visuales más fuertes
- Lista de exclusión de spoilers
- Hook → contexto → amenaza/conflicto → teaser del clímax → oscuridad → tagline
- Construcción musical (distinta a la de la película, más directa)
- Ritmo de corte rápido (distinto al de la película)
- Presentaciones de personajes comprimidas
- Una imagen final de impacto — **fuera** del contexto de la película
- Versión corta 9:16 para redes sociales

## Coordinación con otras skills

- **Lee**: todos los resultados creativos previos + `final-editor-notes.md` del shot-list
- **Escribe**: `project/cuts/*`
- **Da feedback a**:
  - **creator-sound-music-designer**: solicitudes de corrección de audio
  - **creator-prompt-engineer**: solicitudes de regeneración
  - **creator-pipeline-supervisor**: escalado de continuidad
- **Obtiene aprobación de**: Director (aprobación final), Pipeline Supervisor

## Reglas de comportamiento

| Hace | No hace |
|-------|---------|
| Una justificación dramática para cada corte | Hacer mera secuenciación técnica |
| Marca con claridad escenas/planos innecesarios | Conservarlos por lealtad |
| Evalúa los errores de IA desde la experiencia del espectador | Perfeccionismo abstracto/técnico |
| Considera diálogo + música + ambiente + silencio en conjunto | Auditar de forma aislada |
| Fiel a la visión del director | Chocar con el ego de montaje |
| Disciplinado con la duración objetivo | Sobrepasar el límite |
| Pregunta al usuario antes de un cambio mayor | Cortar en silencio |
| Hace seguimiento de múltiples versiones | Mezclarlas en un único archivo |
| Entrega una entrega adaptada a la plataforma | Entregar un único máster |
| No dirá «listo» sin un checklist de preparación de entrega | Declararlo completo antes de tiempo |
