# Storyboardeur — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Une skill qui transforme un scénario écrit en **narration visuelle lisible**. En
réduisant au minimum le nombre de panneaux, elle garantit que chaque panneau
existe pour une raison dramatique. Elle capture les moments critiques d'une scène,
préserve le screen direction, suit l'eyeline continuity et effectue un hand-off
net vers les prompts image/vidéo d'IA.

## Philosophie

Un storyboard n'est pas « dessiner la scène » — c'est un **système de narration visuelle**. Cette skill :

- **Panel economy** : peu de panneaux + choix tranchés — pas beaucoup de panneaux + décisions faibles
- **Screen direction (180°)** et **eyeline continuity** : cohérence spatiale d'un cut à l'autre
- **Graphic dynamics** : où se pose le regard ? quel est le point focal ?
- **Continuity awareness** : costume, décor, direction de la lumière, direction d'écran, mouvement
- **Locked anchors** : character DNA + location master reference dans chaque panneau
- **Producibility** : connaît les contraintes de production par IA et signale les scènes à risque

## À quoi ça sert

| Sortie | Contenu |
|--------|---------|
| **Per-scene storyboard** | Liste de panneaux scène par scène (toutes les données du panneau) |
| **Per-panel sheets** | Fichier détaillé d'un panneau unique pour les scènes complexes |
| **AI image prompts** | Prompt prêt pour la production par panneau |
| **AI video prompts** | Prompt vidéo pour les panneaux animés |
| **Continuity log** | Signalements de risques de costume/décor/direction |
| **Animatic plan** | Planifie l'ordonnancement de l'animatic de toutes les scènes |
| **Director / DOP notes** | Notes visuelles/techniques brèves pour le réalisateur et le DOP |
| **Handoff to shot-list** | Données de panneau au format creator-shot-list-designer |

## Quand elle intervient

- Un scénario est en main et un découpage visuel est souhaité
- Lorsque le réalisateur veut visualiser une scène à l'avance
- Lorsqu'un concept visuel est nécessaire avant les décisions d'optique/lumière du DOP
- Lorsqu'on souhaite la logique du storyboard avant la génération de prompts d'IA
- Lorsque `creator-pipeline-supervisor` délègue l'étape de storyboard

## Panel content (champs canoniques)

Chaque panneau enregistre ces champs :

```
Scene 04 — Panel 04.03
Shot type: medium close
Camera angle: eye level
Frame: Demir merkez-sağ; kettle ön plan-sol; arka plan
       dolap soft-focus; sağ kenar negatif alan açık
Lens feeling: 50mm (eye-equivalent, samimi)
Character position: Demir sandalyede, omuzlar düşmüş, eller masada
Character movement: yok — duraksama
Camera movement: static
Setting / dressing: kireçli mutfak — pencere doğu, kettle ateşte
Light / atmosphere: pencereden yumuşak gri sabah, mum yok
Emotional emphasis: bastırılmış yas; ilk gerçek duygu kırılması
Dialogue / action note: sessizlik; kettle ıslığı
Dramatic justification: Demir'in iç çatışmasını yüzeye getiren ilk an
Transition to next panel: J-cut — kettle sesi devam ederken Panel 4.04 başlar
AI image prompt: [tam prompt]
AI video prompt: [tam prompt, 6s]
Continuity note: palto sahne başında; ceket askıda; kettle aktif
```

## Où elle écrit ses sorties

Sous `project/storyboards/` :

| Fichier | Contenu |
|---------|---------|
| `scene-{NN}/storyboard.md` | Liste de panneaux par scène (canonique) |
| `scene-{NN}/panel-{PP}.md` | Panneau unique détaillé (dans les scènes complexes) |
| `scene-{NN}/prompts.md` | Prompts d'IA par panneau (image + video) |
| `scene-{NN}/continuity.md` | Signalements de continuity |
| `animatic-plan.md` | Notes d'ordonnancement de l'animatic pour tout le film |
| `notes-to-creator-director.md` | Questions/avertissements pour le réalisateur |
| `handoff-to-shot-list.md` | Données de panneau formatées pour le shot-list designer |

## Glossaire des shot type (avec leur équivalent dramatique)

| Type | Usage dramatique |
|------|------------------|
| Establishing | Situe le spectateur dans l'espace |
| Master | Géométrie de la scène, fallback |
| Wide/Full | Relation personnage–environnement |
| Medium | Dialogue neutre |
| Close | Conflit intérieur, émotion intime |
| Extreme close | Intensité subjective |
| Insert | Emphase sur un objet |
| Cutaway | Information parallèle/externe |
| Reaction | Réaction plutôt qu'action |
| OTS | Perspective de dialogue |
| POV | Subjectivité du personnage |
| 2-shot / group | Géométrie de la relation |
| Silhouette | Anonymat, mystère |
| Negative-space frame | Isolement, petitesse |
| Symmetrical | Pouvoir, formalité, immobilité troublante |
| Tracking | Suivi continu |
| Static | Observation, le sens du silence |

« Utilise un close-up » ne suffit pas — la question est **pourquoi** un close-up est nécessaire.

## Continuity audit

Suivi de panneau à panneau, de scène à scène :

- Costume
- Cheveux/maquillage/accessoires
- Identité du décor (avec locked anchor)
- Direction de la lumière
- Jour/nuit
- Screen direction (règle des 180°)
- Logique spatiale des personnages
- Flux de l'action
- Position des props

Lorsqu'un risque est détecté, il est écrit explicitement dans le champ `continuity note` du panneau.

## Coordination avec les autres skills

- **Lit** : scénario, vision du réalisateur + direction sheets, plan per-scene du DOP,
  character DNA + FACS, anchors de décor
- **Écrit** : `project/storyboards/*`
- **Délègue** :
  - `creator-shot-list-designer` (panel → shot list)
  - `creator-prompt-engineer` (panel prompt → optimisation spécifique à l'outil)
- **Reçoit du feedback de** : Réalisateur, Pipeline Supervisor

## Solutions axées sur la production par IA

- Découpe les scènes complexes en panneaux simples
- Clarifie le point focal visuel dans les scènes à plusieurs personnages
- Simplifie les mouvements avec lesquels l'IA aurait du mal
- Utilise des anchors fixes pour le même décor/personnage
- Propose une alternative sûre en plan statique plutôt qu'un mouvement de caméra
- Suggère un cadrage sélectif dans les scènes chargées
- Suggère des cuts rythmés plutôt qu'une action rapide

## Règles de comportement

| Fait | Ne fait pas |
|------|-------------|
| Écrit une justification dramatique pour chaque panneau | Remplit avec « un panneau de plus » pour remplir |
| Peu de panneaux + choix tranchés | Beaucoup de panneaux + décisions faibles |
| Unifie scénariste + réalisateur + DOP + personnage + production | Écrase l'upstream en silence |
| Préserve le screen direction et l'eyeline | Mélange la direction lors d'un cut |
| Met les locked anchors dans chaque prompt | Redécrit de zéro dans chaque panneau |
| Découpe la scène complexe en panneaux | La surcharge sur un seul frame |
| Flag de risque IA + alternative sûre | Suggère un mouvement improductible |
| Sortie structurée, lisible en aval | Déverse un seul bloc de texte |
