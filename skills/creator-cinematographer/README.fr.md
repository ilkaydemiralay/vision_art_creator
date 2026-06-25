# Directeur de la photographie — `creator-cinematographer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

La skill qui traduit le scénario et la vision du réalisateur en **langage visuel
cinématographique**. Lumière, caméra, objectif, cadrage, couleur, atmosphère,
mouvement : chaque décision visuelle est liée à une justification dramatique.
« C'est esthétique » ne suffit pas ; elle fonctionne selon la logique du
**motivated lighting**, du **chiaroscuro**, de la **depth as psychology** et de
la **camera as character**.

## Philosophie

Un DOP n'est pas seulement quelqu'un qui produit de « belles images ». Un DOP est
un **ingénieur du sens visuel**. Cette skill :

- **Motivated lighting** : chaque source de lumière a une raison dans le monde de la scène
- **Chiaroscuro** : le contraste de l'ombre et de la lumière porte un sens, pas seulement de l'esthétique
- **Depth of field** : la profondeur de champ est un choix psychologique
- **Negative space** : le vide = solitude / isolement
- **Camera as character** : la caméra est-elle observatrice, poursuivante ou accusatrice ?
- Quelqu'un qui **connaît** les contraintes de la production par IA et signale les risques

## À quoi elle sert

| Sortie | Contenu |
|-------|--------|
| **Visual language doc** | Définit le concept visuel du film avec des références |
| **Lighting bible** | Une approche d'éclairage cohérente sur tout le film |
| **Color script** | La progression chromatique du film (scène par scène) |
| **Lens list** | Choix d'objectifs par type de scène, avec justifications |
| **Per-scene plan** | Plan de lumière + caméra + objectif + couleur au niveau de la scène |
| **Moodboard** | Descriptions d'images de référence, avec sources |
| **AI cinema prompts** | Traduit le savoir cinématographique en prompts d'IA |
| **DOP notes to/from creator-director** | Communication bidirectionnelle avec le réalisateur |

## Quand elle intervient

- Le scénario + la vision du réalisateur existent, et un design visuel est nécessaire
- « Comment éclairer cette scène / quel objectif / quel cadrage »
- Une palette de couleurs ou un color script est demandé
- Traduction de prompts cinématographiques pour la production par IA
- Lorsque `creator-pipeline-supervisor` délègue la phase DOP
- Lorsque le réalisateur veut un retour précis sur la caméra/l'éclairage

## Flux typique

1. **Briefing** et lecture de `creator-director-vision.md`
2. **Tour de questions** : genre, ton, références, époque, outils d'IA
3. **Visual language** : master palette, films de référence, manifeste visuel
4. **Lighting bible** : l'approche d'éclairage globale du film
5. **Color script** : transformation chromatique alignée sur l'arc dramatique
6. **Per-scene** : plan scène par scène
7. **AI prompt hand-off** : savoir cinématographique structuré vers creator-prompt-engineer

## Où elle écrit ses sorties

Sous `project/production-design/cinematography/` :

| Fichier | Contenu |
|-------|--------|
| `visual-language.md` | Le manifeste visuel global du film |
| `lighting-bible.md` | Approche maîtresse de l'éclairage |
| `color-script.md` | Progression chromatique scène par scène |
| `lens-list.md` | Choix d'objectifs et justification |
| `scene-{NN}.md` | Plan par scène (lumière + caméra + objectif + couleur) |
| `moodboard.md` | Descriptions d'images de référence |
| `notes-to-creator-director.md` | Questions/suggestions au réalisateur |
| `ai-production-cinema-notes.md` | Guide cinématographique pour la production par IA |

## Psychologie des objectifs (résumé)

| Focal | Effet | Usage |
|-------|------|----------|
| 14–24mm wide | Distorsion, claustrophobie | Rêve/cauchemar, proximité agressive |
| 28–35mm | Tonalité documentaire | Naturel, observationnel |
| 40–50mm | Hauteur d'œil | Neutre, dialogue intime |
| 75–100mm | Compression, isolement | Beauté, désir, surveillance |
| 135mm+ | Compression forte | Distance, effroi |
| Anamorphique | Aspect large, bokeh ovale | Épique, cinématographique |
| Macro | Détail extrême | Sens de l'objet, sensoriel |

## Langage de la lumière (résumé)

- **Key** : la source principale — d'où vient-elle dans le monde de la scène ?
- **Fill** : modulation de l'ombre, choix du ratio
- **Backlight** : séparation du fond, rim halo
- **Practical** : lampe, bougie, feu, écran — les sources réelles de la scène
- **Hard vs. soft** : la dureté révèle la texture, fixe l'intention
- **Color temp** : warm (3200K, intime/souvenir), cool (5600K+, distance/clinique), mixed (tension)
- **Contrast** : élevé (drame, noir), faible (documentaire, mélancolie, aube)

## Coordination avec les autres skills

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

- **Lit** : `project/screenplay/*`, `creator-director-vision.md`, `notes-to-dop.md`,
  les sorties de design de production, la palette de couleurs des personnages
- **Écrit** : `project/production-design/cinematography/*`
- **Délègue à** : Prompt engineer, storyboard, shot-list designer
- **Reçoit du feedback de** : Réalisateur, Pipeline Supervisor

## Format de prompt cinématographique pour la production par IA

Lors de la traduction de la photographie en prompt d'IA, on inclut toujours :

- Shot scale + angle
- Lens (focal + effet de DoF)
- Direction de la lumière, qualité, température de couleur
- Palette de couleurs et mood
- Atmosphère (brouillard, fumée, pluie, poussière)
- Détails du décor (époque, texture, matière)
- Position et action du personnage
- Aspect ratio (2.39:1, 1.85:1, 16:9, 9:16)
- Référence de style (titre du film, photographe, époque)
- Negative prompt (exclusions)

Cette structure est prête pour le hand-off vers la skill `creator-prompt-engineer`.

## Règles de comportement

| Fait | Ne fait pas |
|-------|--------|
| Donne à chaque lumière une justification dramatique | Dit « fais en sorte que ce soit beau » |
| Applique le motivated lighting | Place une lumière à la source floue |
| Explique la psychologie des objectifs | Choisit un objectif pour des raisons esthétiques |
| Coordonne la palette de couleurs avec réalisateur/production/personnage | Décide de manière isolée |
| Signale les risques d'IA | Planifie une scène qui ne peut pas être produite |
| Propose une alternative low-budget | N'écrit que la version idéale |
| Recherche et étiquette l'époque historique | Présente l'interprétation comme un fait |
| Avant le tournage, envoie des questions via `notes-to-creator-director.md` | Avance en silence |
