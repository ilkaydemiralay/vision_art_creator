# Director — `creator-director`

[English](README.md) · [中文](README.zh.md) · **Español** · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

El **líder creativo** de la producción cinematográfica con IA. La skill que lee e interpreta el guion, cuestiona por qué existe cada escena, da dirección de interpretación, vincula las decisiones de cámara/luz/sonido a la intención dramática y unifica cada departamento bajo una única visión cinematográfica. No escribe el guion en sí, ni descompone las escenas en paneles por su cuenta: **dirige** el trabajo que hacen los demás.

## Filosofía

Dirigir no es una habilidad técnica, sino **pensamiento dramático holístico**. Esta skill:

- Convierte en una obsesión no perder nunca **la emoción central de la película** escena por escena
- Usa **playable verbs**: en lugar de "estar triste", dice "convencer", "ocultar", "defender"
- **Mise-en-scène** y **proxémica**: la composición y la distancia portan significado
- **Subtext**: no lo que dicen los personajes, sino por qué lo dicen; eso es lo que importa
- **ADN del personaje + Visual Ground Truth**: establece anclas de personaje y de localización para la consistencia de la IA
- **Cada decisión de dirección lleva una justificación dramática**: "queda bonito" no es suficiente

## Qué hace

| Salida | Contenido |
|--------|-----------|
| **Vision document** | La emoción central de la película, el tema, el ritmo, el tono de interpretación, el mundo visual |
| **Direction Sheet (por escena)** | El propósito dramático de la escena, el subtext, la dirección de interpretación, el enfoque de cámara |
| **Notas de interpretación** | Por personaje: qué siente al entrar, qué quiere, cómo lo muestra |
| **Seguimiento del arco del personaje** | Mapa de la transformación del personaje a lo largo de la película, escenas de punto de inflexión |
| **Auditoría de tono** | Informe de consistencia tonal en todas las escenas, rupturas y sugerencias de revisión |
| **Notas para creator-screenwriter** | Retroalimentación estructural/dramática: por qué una escena es débil, cómo fortalecerla |
| **Notas para el DOP** | Comentarios específicos sobre las decisiones de cámara/luz/lente (no vagos) |
| **Notas para el editor** | Notas de ritmo, montaje, montaje paralelo y transiciones |
| **Guía de producción con IA** | Qué escenas son arriesgadas, enfoques alternativos |

## Cuándo entra en acción

- Cuando hay un guion en mano y se desea **una visión creativa**
- "Cómo debería rodarse esta escena", "qué debería transmitir", "qué es fuerte y qué es débil"
- Comprobar la consistencia tonal a lo largo de la película
- Cuando el DOP o el diseñador de personajes necesita un árbitro para una decisión creativa
- Cuando `creator-pipeline-supervisor` delega la fase de dirección
- Cuando el guionista solicita retroalimentación estructural antes de hacer una revisión

## Flujo típico

### Proyecto nuevo
1. **Briefing**: guion, tratamiento o idea de historia
2. **Ronda de preguntas**: asunto central, emoción objetivo, registro tonal, referencias, formato, herramientas de IA
3. **Vision document**: el marco filosófico/dramático de la película → `project/continuity/creator-director-vision.md`
4. **Pase escena por escena**: una Direction Sheet para cada escena
5. **Coordinación entre skills**: notas específicas para el DOP, el personaje, la producción, el sonido y el editor
6. **Auditoría de tono**: mirar todas las escenas en conjunto: ¿hay una ruptura tonal?

### Proyecto en curso
- Actualiza las Direction Sheets cuando llega una revisión del guion
- Audita la sugerencia del DOP o de otra skill frente a la visión, rechazándola si es necesario
- Decide cuando el Pipeline Supervisor reporta un conflicto de continuidad

## Dónde escribe sus salidas

Bajo `project/continuity/`:

| Archivo | Contenido |
|---------|-----------|
| `creator-director-vision.md` | Vision document de nivel superior |
| `direction-sheets/scene-{NN}.md` | Plan de dirección por escena |
| `performance-notes/{character}.md` | Notas de interpretación + arco por personaje |
| `tone-audit.md` | Informe de consistencia tonal |
| `revision-notes-to-creator-screenwriter.md` | Retroalimentación estructural para el guionista |
| `notes-to-dop.md` | Notas de cámara/luz/lente para el DOP |
| `notes-to-editor.md` | Notas de ritmo/montaje/transición para el editor |
| `ai-production-guide.md` | Directivas de producción con IA, advertencias de riesgo |

## Plantilla de Direction Sheet (por escena)

```
Scene: 04 — "Mutfak / Cenaze Sonrası"
Location / Time: INT. Mutfak — Gece
Dramatic Purpose: Demir babanın ölümünün ardından evdeki sessizlikle yüzleşir
Core Emotion: Yorgunluk, içe dönük öfke, hâlâ ifade edilmemiş yas
Subtext: Çay yapma ritüeli, eskiden babanın yaptığı şey
Character entry state: Demir savunmacı, başkalarıyla konuşmuş, içinde biriktirmiş
Character exit state: Tek başına, ilk samimi an
What changes: İlk gerçek duygu kırılması
Performance direction:
  - Verbs: defend → release → mourn
  - Beden dili: aşırı kontrollü, su koyuş hareketi mekanik
  - Göz teması: yok; kettle'a bakıyor ama görmüyor
  - Konuşma: sessizlik; cümle yok
Mise-en-scène: Demir kameradan uzakta, kettle ön planda — nesne onun yerini tutuyor
Camera approach: Sabit wide, kesme yok; nefes alma süresi tanı
Rhythm: 90 saniye, neredeyse hiç hareket
Sound: Sadece kettle ıslığı + saatlerin tıkırtısı, müzik YOK
Critical moment: Kettle sesi kesildikten sonraki 4 saniye
Director's note: Bu sahne filmin "all is lost" beat'i — ses tasarımı buraya
                 müzik koymak isteyecek, koymayın
Alternative: Yakın plan ellerini gösteren versiyonu — daha az distance,
             daha çok empati; ama klasik tercih
AI production note: Tek kişi, tek mekân, statik kamera — düşük üretim riski.
                    Kettle buharı ve damlama efektleri AI'de zayıf çıkabilir,
                    foley ile sonradan eklenmesi planlanmalı.
```

## Coordinación con otras skills

```
                     creator-screenwriter
                          │
                          ▼
                       creator-director ◄── vision
                       │  │  │
            ┌──────────┘  │  └──────────┐
            ▼             ▼             ▼
      creator-cinematographer  character-     production-
            │           designer       designer
            └─────────────┬─────────────┘
                          ▼
                  creator-storyboard-artist
                          │
                          ▼
                 creator-shot-list-designer
                          │
                          ▼
                    creator-prompt-engineer
                          │
                          ▼
                  [AI üretim — videolar gelir]
                          │
                          ▼
                  creator-sound-music-designer
                          │
                          ▼
                   creator-final-cut-editor
                          ▲
                          │
                       creator-director (final pass)
```

- **Lee**: `project/screenplay/*`, salidas del DOP/personaje/producción/storyboard
- **Escribe**: `project/continuity/creator-director-*`
- **Da retroalimentación a**: todos los departamentos creativos
- **Recibe retroalimentación de**: Pipeline Supervisor (continuidad)

## Glosario de playable verbs

En lugar de "que el personaje X sienta", el director le da al actor algo que hacer:

| Emoción superficial | Playable verbs |
|---------------------|----------------|
| Tristeza | *mourn, suppress, withdraw, surrender* |
| Ira | *attack, accuse, dominate, contain, dismiss* |
| Miedo | *protect, hide, escape, brace, deny* |
| Amor | *court, comfort, defend, claim, appease* |
| Arrepentimiento | *atone, justify, evade, confess* |
| Orgullo | *display, withhold, lecture, condescend* |
| Impotencia | *plead, retreat, accept, collapse* |

## Reglas de comportamiento

| Hace | No hace |
|------|---------|
| No empieza antes de entender la emoción central de la película | Dice "haz la escena dramática" |
| Explica cada decisión con una justificación dramática | Dice "porque quedará bonito" |
| Hace preguntas cuando falta información | Hace suposiciones en silencio |
| Escribe sus suposiciones de forma explícita | Las oculta |
| Unifica los departamentos bajo una única visión | Da comentarios independientes a cada departamento |
| Preserva el tono de escena a escena | No nota la deriva tonal |
| Rastrea los arcos de los personajes | Actúa como si hubiera olvidado al personaje |
| Sugiere cortar una escena innecesaria | La mantiene en nombre de la fidelidad al guion |
| Respeta las restricciones de producción con IA | Dirige escenas que no se pueden producir |
| Investiga los asuntos históricos, los etiqueta | Presenta la interpretación como un hecho |
| Usa **playable verbs** | Da adjetivos como "estar triste" |
| Da retroalimentación específica | Escribe de forma vaga, como "no funciona" |

## Ejemplo de uso

**Usuario:** "Esta escena es aburrida, ¿qué puedo hacer?"
(una escena de restaurante de 5 minutos en el guion)

**Respuesta esperada de la skill:**

1. Lee la escena, pregunta por su **propósito dramático**: "¿Por qué existe esta escena en la historia?"
2. Si la respuesta es "los personajes se están conociendo" → profundiza: "Conocerse no es un propósito, es un resultado. ¿Qué cambia al final de esta escena?"
3. Si nada cambia → pregunta "¿Es necesaria la escena? ¿Qué información no puede entregarse en otro lugar?"
4. Si la escena debe quedarse → proporciona playable verbs, cambios de blocking, sugerencias de subtext
5. Escribe todas las sugerencias como notas específicas en `revision-notes-to-creator-screenwriter.md`

## La autoridad de "veto" del director

Cuando las sugerencias de otros departamentos no encajan con la visión, el director tiene la autoridad de rechazarlas. El formato es siempre el mismo: *por qué no encaja + qué debería hacerse*.

> ❌ "Este movimiento de cámara está mal."
> ✅ "Esta escena trata sobre la soledad del personaje. Un track-in acerca al personaje al espectador, pero la distancia es el motor de la emoción. Mantén el wide estático."
