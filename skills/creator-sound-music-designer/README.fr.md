# Concepteur Son et Musique — `creator-sound-music-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [**Français**](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Le skill qui construit le **monde sensoriel** du film. Deux disciplines intégrées se rejoignent :
- **Concepteur son** : la réalité sensorielle des espaces, personnages, objets et événements — ambience, foley, effets, acoustique, perspective sonore et **silence** (en tant qu'outil dramatique actif)
- **Compositeur de film / superviseur musical** : thème principal, leitmotifs de personnages, musique de scène, rythme, points d'entrée/sortie de la musique

## Philosophie
Le son et la musique ne sont **pas une décoration**. Chaque décision sonore et musicale est liée au but dramatique de la scène, à la psychologie des personnages, à l'atmosphère visuelle, au rythme du montage et à l'impact sur le public. Ce skill :
- Ne dit pas « utilisez une musique triste » — il conçoit des leitmotifs et planifie leur évolution
- **Conçoit le silence de manière active** — pas une absence, mais une décision dramatique
- **Leitmotifs de personnages** : un motif qui commence à la flûte se transforme en épopée avec les cordes dans le finale
- **Discipliné en matière de droits d'auteur** : n'imite pas les artistes vivants, « similaire mais pas identique »
- **En phase avec le rythme du montage** : entrée/sortie de la musique coordonnée avec le plan de montage du shot-list
- **Génération de prompts son/musique par IA** : Suno, Udio, ElevenLabs SFX, Stable Audio, Runway Audio

## Ce qu'il fait
| Livrable | Contenu |
|-------|--------|
| **Vision sonore** | La vision globale du sound design du film |
| **Vision musicale** | Le manifeste du langage musical du film |
| **Thème principal** | Conception du thème principal |
| **Thèmes de personnages** | Conception du leitmotif par personnage |
| **Plans de scène** | Plan son + musique scène par scène |
| **Listes d'ambience / foley / SFX** | Listes d'inventaire |
| **Plan de silence** | Une carte délibérée du silence |
| **Plan d'entrée/sortie de la musique** | Points d'entrée et de sortie de la musique |
| **Sound bridges** | Conception des transitions |
| **Prompts IA son + musique** | Prompts spécifiques aux outils |
| **Notes d'équilibre des dialogues** | Notes d'équilibre dialogue/musique |
| **Notes de mix final** | Audit du mix final |
| **Rapport de continuité** | Vérification de la continuité sonore |

## Quand il intervient
- Un scénario est en main, et un plan de sound design / musique de film est nécessaire
- De l'ambience, du foley, des SFX ou des thèmes musicaux sont demandés
- Des prompts son/musique par IA sont nécessaires
- Lorsque le concepteur de shot-list transmet l'intention sonore de la scène
- Lorsque `creator-pipeline-supervisor` délègue l'étape audio

## Flux typique
1. **Briefing** + lecture de toutes les sorties des skills en amont
2. **Série de questions** : genre, register, densité musicale, époque, outils IA
3. **Vision sonore** + **Vision musicale**
4. **Thème principal + leitmotifs de personnages**
5. **Plan par scène** : ambient/foley/silence/musique pour chaque scène
6. **Plan de silence** : une carte du silence délibéré
7. **Plan d'entrée/sortie de la musique**
8. **Prompts IA son + musique**
9. **Audit du mix final** (après le final cut)

## Conception du silence
Le silence est une décision de conception **active**. Pour chaque silence, le skill demande :
- La musique s'arrête-t-elle ici ?
- L'ambience est-elle atténuée, ou réduite à zéro ?
- Ne reste-t-il qu'un souffle, ou le son d'un petit objet ?
- Le silence traduit-il la solitude, la peur ou l'hésitation ?
- Est-il là pour déstabiliser le public, ou pour intensifier l'émotion ?
- Quel son entre après le silence ?

## Exemple de leitmotif de personnage
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

## Où il écrit ses sorties
Sous `project/sound/` :
| Fichier | Contenu |
|-------|--------|
| `sound-vision.md` | Vision globale du sound design |
| `music-vision.md` | Manifeste du langage musical |
| `main-theme.md` | Conception du thème principal |
| `character-themes/{slug}.md` | Leitmotif de personnage |
| `scenes/scene-{NN}.md` | Plan son + musique de scène |
| `ambience-list.md` | Inventaire d'ambience |
| `foley-list.md` | Inventaire de foley |
| `special-effects-list.md` | SFX spéciaux |
| `silence-plan.md` | Carte du silence |
| `music-entry-exit-plan.md` | Timing d'entrée/sortie de la musique |
| `sound-bridges.md` | Conception des transitions |
| `ai-sound-prompts.md` | Prompts SFX par IA |
| `ai-music-prompts.md` | Prompts musique par IA |
| `dialogue-balance-notes.md` | Équilibre dialogue/musique |
| `final-mix-notes.md` | Audit du mix final |
| `sound-continuity-report.md` | Vérification de la continuité |

## Format des prompts IA
### Exemple de prompt SFX
```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```
### Exemple de prompt musique
```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```
### Format description en langue native + prompt anglais
```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## Droits d'auteur et originalité
- Ne suggère pas de copier des compositions existantes
- N'imite pas note pour note le style d'un artiste vivant
- Fonctionne sur une logique « similaire mais pas identique », en décrivant genre + émotion
- Dans les prompts musicaux IA, utilise une atmosphère générale au lieu du nom d'un artiste

## Coordination avec les autres skills
- **Lit** : toutes les sorties créatives en amont + notes de montage sonore du shot-list
- **Écrit** : `project/sound/*`
- **Délègue à** : `creator-final-cut-editor` (intégration du final cut), l'opérateur de l'outil audio IA
- **Reçoit des retours de** : Réalisateur, Pipeline Supervisor, Final-cut-editor

## Règles de comportement
| Fait | Ne fait pas |
|------|--------|
| Lie le son et la musique au but dramatique | Les utilise comme décoration |
| Conçoit le silence de manière active | Le traite comme une absence |
| Synchronise l'évolution du leitmotif avec l'arc du personnage | Répète un seul thème fixe |
| Pense ensemble dialogue/musique/ambience/silence | Décide de manière isolée |
| Discipliné en matière de droits d'auteur | Imite les artistes |
| Fait des recherches historiques/culturelles et les étiquette | Présente l'interprétation comme un fait |
| Écrit des prompts IA adaptés à l'outil | Déverse des prompts génériques |
| Préserve la continuité sonore pour un film long | Pense scène par scène, de manière décousue |
