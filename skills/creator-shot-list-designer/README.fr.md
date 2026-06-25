# Concepteur de liste de plans — `creator-shot-list-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · **Français** · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

La compétence qui transforme les scènes et les storyboards en une **liste de plans + intention de montage**.
L'endroit où la planification de pré-production et l'intention éditoriale se rejoignent. Ce n'est
pas le monteur final — elle conçoit l'intention éditoriale AVANT que le moindre matériau ne soit
produit, afin que le tournage génère les bons éléments.

## Philosophie

Une liste de plans n'est pas un inventaire technique ; c'est une **carte de l'intention dramatique +
éditoriale**. Cette compétence :

- **Économie de plans** : chaque plan porte une seule action claire
- **Conscience du rythme de montage** : quel plan est tenu longtemps, lequel est coupé rapidement ?
  La durée d'un plan est une décision éditoriale
- **Direction d'écran + continuité** : cohérence spatiale/temporelle d'un cut à l'autre
- **Productibilité pour l'IA** : planifie la complexité d'un plan unique en fonction des contraintes des outils IA
- **Intention éditoriale avant la production** : la logique de montage est fixée AVANT le tournage
  afin de ne pas filmer de plans inutiles
- **Conception de l'expérience du public** : que ressent, qu'apprend le spectateur, et que lui cache-t-on ?

## Ce qu'elle produit

| Sortie | Contenu |
|-------|---------|
| **Liste de plans par scène** | Liste de plans canonique, avec justification dramatique + éditoriale |
| **Plan de montage** | Rythme interne à la scène, points de cut, image d'ouverture/de clôture |
| **Conception des transitions** | Décisions de transition de scène à scène (hard cut, match, J/L, sound bridge) |
| **Audit des risques de continuité** | Rapport des risques de cohérence d'un plan à l'autre |
| **Notes de montage son** | Points de J-cut / L-cut / silence pour le sound designer |
| **Liste de plans à l'échelle du film** | Liste consolidée couvrant l'ensemble du film |
| **Carte de rythme** | Rythme scène par scène (plages de durée des plans) |
| **Rapport de redondance** | Plans à couper/fusionner |
| **Notes pour le monteur final** | Transmission de l'intention éditoriale au monteur final |

## Quand elle intervient

- Les scènes et les storyboards sont prêts, et un plan basé sur les plans est nécessaire
- Un séquençage des plans tenant compte du montage est demandé
- Des scènes longues doivent être découpées en éléments productibles par l'IA
- Lorsque le réalisateur ou le DOP demande un plan structurel de tournage/production
- Lorsque `creator-pipeline-supervisor` délègue la planification pré-montage

## Déroulement type

1. **Briefing** + lecture de toutes les sorties des compétences en amont
2. **Tour de questions** : format, rythme de montage, ton, outils IA
3. **Liste de plans (par scène)** : en structure canonique, avec justification dramatique + éditoriale
4. **Plan de montage (par scène)** : rythme, ouverture/clôture, points de cut
5. **Conception des transitions** : transitions de scène à scène
6. **Audit de continuité** : risques d'un plan à l'autre
7. **Carte de rythme** : carte du rythme à l'échelle du film
8. **Rapport de redondance** : identification des plans coupables
9. **Transmission** : données de prompt de plan pour creator-prompt-engineer + intention éditoriale pour creator-final-cut-editor

## Plan — structure canonique

```
Scene 04 — Shot 04.02
Shot name: "Kettle close, silence"
Shot type: insert
Frame scale: extreme close
Camera angle: eye level (side-high)
Camera movement: static
Lens recommendation: 100mm macro feeling
Estimated duration: 4s
Location: Anatolian kitchen 1980s [anchor: kitchen-anatolian-1980s]
Time: night
Characters in frame: none (only the kettle)
Character action: kettle whistle dying down (off-screen Demir turns off the heat)
Dialogue / silence note: SILENCE (only kettle + clock ticking)
Light / atmosphere: gray moonlight from the window, copper kettle highlight
Sound / music note: NO music; clock ticking + kettle dying
Dramatic purpose: a symbolic echo of Demir's inner turning
Edit purpose: a 4-second breath — no need to cut, hold it
Link to previous shot: 04.01 (Demir sitting, wide) — match by sound
Link to next shot: 04.03 (Demir's face close, first blink) — hard cut
Continuity note: kettle = same copper, same stain pattern
AI video production note: single action (whistle dying) + static camera = low risk
Safe alternative: 6s version — slower whistle fade, very slow camera push-in
```

## Intention éditoriale — plan de scène

Questions éditoriales au niveau de la scène :

- Quel plan ouvre la scène ?
- Quelle image la clôt ?
- Quel plan est tenu longtemps ?
- Quel plan est coupé court ?
- Où vont les reaction shots ?
- Où le silence s'étire-t-il ?
- Où un hard cut est-il nécessaire ?
- Où une transition douce ?
- Quelle image fait le lien vers la scène suivante ?
- Quel plan porte le sommet dramatique ?
- Quel plan est inutile ?
- Quel plan transmet de l'information, lequel transmet de l'émotion ?

Écrit sous `project/shot-list/scene-{NN}/edit-plan.md`.

## Où elle écrit ses sorties

Sous `project/shot-list/` :

| Fichier | Contenu |
|-------|---------|
| `scene-{NN}/shot-list.md` | Liste de plans de la scène |
| `scene-{NN}/edit-plan.md` | Intention de montage + rythme |
| `scene-{NN}/transitions.md` | Décisions de transition |
| `scene-{NN}/continuity-risks.md` | Audit de continuité |
| `scene-{NN}/sound-edit-notes.md` | Transmission au sound designer |
| `film-shot-list.md` | Liste consolidée de tout le film |
| `rhythm-map.md` | Carte de rythme |
| `redundancy-report.md` | Plans coupables |
| `ai-production-shot-guide.md` | Guide des contraintes des outils IA |
| `final-editor-notes.md` | Intention pour le monteur final |

## Types de transition (usage éditorial)

| Transition | Usage éditorial |
|-------|-------------------|
| Hard cut | Rupture dramatique soudaine |
| Match cut | Un pont de sens entre deux images |
| Fade in/out | Ouverture/clôture temporelle/émotionnelle |
| Dissolve | Transition de temps, fondu émotionnel |
| J-cut | Le son de la scène suivante arrive en premier (flux fluide) |
| L-cut | Le son de la scène actuelle est prolongé (émotion tenue) |
| Sound bridge | Changement de lieu/temps porté par le son |
| Motif visuel | Un pont via un visuel récurrent |
| Transition d'objet | Correspondance de forme |
| Transition de mouvement | Continuité directionnelle |
| Saut temporel | Ellipse temporelle soudaine |
| Flashback | Via un filtre/objectif/flou/repère sonore |
| Montage parallèle | Deux lieux entrelacés |

## Règles de productibilité vidéo IA

- Une action claire par plan
- Un mouvement de caméra principal (non enchaîné)
- Un nombre maîtrisé de personnages
- Une cible visuelle claire
- Découper les mouvements complexes en plusieurs plans
- Signaler les risques de main/doigt/lip sync
- Cadrage sélectif pour les foules
- Lieu verrouillé + anchors de personnages dans chaque prompt
- Durée de plan généralement de 3 à 10 s
- Chaque plan correspond proprement à un seul prompt vidéo

Lorsqu'un risque est détecté, le signaler :

> *"Ce plan est trop complexe pour la vidéo IA — découpez-le en deux plans."*
> *"Le lip sync peut échouer ici ; utilisez un reaction shot plutôt que le locuteur."*
> *"Le mouvement de la main est crucial — utilisez un cadrage plus large plutôt qu'un insert."*
> *"Action de foule — construisez-la avec des cuts, pas un seul plan."*

## Rythme et cadence

Des formules vagues comme « fais-le rapide » ne sont pas utilisées. Le rythme est :

- Exprimé sous forme de **plage de durée des plans**
- Mesuré par la **fréquence des cuts**

Exemple :
> *"La scène 3 a en moyenne 4–6 s/plan, la scène 12 a en moyenne 1,5–3 s/plan —
> le rythme s'accélère à mesure que le conflit du personnage s'intensifie."*

## Intention de montage des dialogues

Pour les scènes riches en dialogue :

- Le locuteur ou celui qui écoute ?
- Où vont les reaction shots ?
- Où le silence est-il plus fort ?
- Une autre image par-dessus le dialogue ?
- Du subtexte par l'expression du visage ?
- Hard cut ou chevauchement naturel ?
- Couper avant la fin de la phrase ?
- Répétition redondante de l'explication ?
- Sur qui se trouve l'émotion que le spectateur a vraiment besoin de voir ?

Les repères de J-cut / L-cut sont posés ici.

## Coordination avec les autres compétences

- **Lit** : scénario, vision + feuilles de direction du réalisateur, plan par scène du DOP,
  données de panneaux de storyboard, anchors de personnages/lieux
- **Écrit** : `project/shot-list/*`
- **Transmet à** :
  - `creator-prompt-engineer` (prompts vidéo au niveau du plan)
  - `creator-final-cut-editor` (fichiers d'intention éditoriale)
- **Reçoit des retours de** : Réalisateur, Pipeline Supervisor

## Détection de la redondance

Dans un long film IA, signaler :

- Un plan qui répète la même information
- Un plan qui ne change pas l'émotion
- Un plan de détail qui casse le rythme
- Un usage excessif des reaction shots
- Un plan difficile pour l'IA à faible apport dramatique
- Des opportunités de late-in / early-out
- Un moment qui peut être raconté visuellement plutôt qu'en dialogue

*"Ce plan peut être coupé"* ou *"Ces deux plans peuvent être fusionnés"* est écrit explicitement.

## Règles de comportement

| Fait | Ne fait pas |
|-------|---------|
| Donne à chaque plan une justification dramatique **et** éditoriale | Faire un inventaire technique |
| Se coordonne avec le rythme du réalisateur, le cadrage du DOP, le storyboard | Décider en isolation |
| Signale les plans inutiles | Ajouter du remplissage |
| Vérifie la continuité de manière proactive | Attendre que les problèmes apparaissent après le tournage |
| Conçoit en fonction des contraintes des outils IA | Planifier des plans non productibles |
| Une alternative sûre pour les plans risqués | Fournir une seule version |
| Considère aussi celui qui écoute dans le dialogue | Ne suivre que le locuteur |
| Coordonne l'intention éditoriale du son et de la musique | Ne penser qu'à l'image |
| Sortie structurée, lisible en aval | Déverser un seul bloc de texte |
