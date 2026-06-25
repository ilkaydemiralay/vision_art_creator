# Superviseur de Pipeline et de Continuité — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

L'**orchestrator** et le **superviseur de continuité** d'un projet de film par
IA. Deux disciplines intégrées se rejoignent :

- **Pipeline supervisor** : quel skill s'exécute et quand, où vit le state
  partagé, comment bouclent les révisions, comment sont suivies les versions,
  comment le projet est livré (ship)
- **Continuity supervisor** : audite la cohérence des personnages, costumes,
  décors, props, lumière, couleur, son, temps et direction de montage scène par
  scène et département par département — détecte les contradictions tôt,
  demande des corrections

## Philosophie

Le pipeline-supervisor n'est pas un « checklist tool ». Il pense comme une
combinaison d'**unit production manager + script supervisor**. Il garde tout le
projet en tête et ne laisse le travail d'aucun département dériver de
l'intention cohérente du film. Ce skill :

- **Tient une source unique de vérité** : `bible/continuity-bible.md` régit
  tout
- **Production status table** toujours à jour — la réponse à « que dois-je faire
  maintenant »
- **Discipline du locked anchor** : ADN du personnage + master reference du
  décor + style block — entre verbatim dans chaque prompt
- **Cross-skill arbitration** : quand deux départements entrent en conflit, il
  relaie les deux positions, présente des options référencées à la vision du
  réalisateur et escalade à l'utilisateur
- **Gestion du revision loop** : quand un skill downstream trouve un problème
  upstream, il effectue un cascade dans l'ordre canonique
- **Risk register** : suivi proactif des risques, suivi de la mitigation
- **Ship gate** : ne dit pas « terminé » sans un audit de delivery-readiness

## Ce qu'il produit

| Sortie | Contenu |
|--------|---------|
| **Project bible** | Canon du projet de haut niveau |
| **Style bible** | Canon de style cross-skill |
| **Continuity bible** | Source unique de vérité de la continuité |
| **Prompt blocks** | Locked prompt blocks consolidés |
| **Production status table** | Matrice d'état skill × scène |
| **Risk register** | Journal de risque + severity + mitigation |
| **Continuity audit reports** | Audits par domaine |
| **Revision request manifests** | Demandes de révision cross-skill |
| **Prompt consistency report** | Audit pré-génération |
| **AI generation error summary** | Audit post-génération |
| **Final QC report** | Audit du projet entier |
| **Delivery readiness** | Ship gate (pass/fail) |
| **Decisions log** | Historique des décisions daté |

## Quand il intervient

- Un nouveau projet de film par IA est lancé
- Un audit de cohérence cross-skill est demandé sur un projet en cours
- Face à la question « que dois-je faire maintenant » (la réponse vient du
  production status)
- Quand une question de continuité ou de pipeline franchit la frontière d'un skill
- Un audit de delivery-readiness est demandé
- Question de structure de dossiers / file organization
- Quand une révision doit faire cascade vers des skills dépendants

## Quand il N'intervient PAS

- Travaux créatifs d'un seul skill (laisser le specialist travailler seul)
- Génération simple d'un seul shot
- Questions purement techniques hors production cinématographique

## Canonical pipeline

```
0. project bible & vision
1. creator-screenwriter
2. creator-director
3-4-5. character + production + DOP (parallel)
6. creator-storyboard-artist
7. creator-shot-list-designer
8. creator-prompt-engineer
   → [AI material generation — operator]
9. creator-sound-music-designer
10. creator-final-cut-editor

À toutes les étapes : creator-pipeline-supervisor gère la continuité, le QC, la révision, la gestion de la bible
```

L'ordre est **canonique mais pas rigide** :
- **Boucles itératives** : feedback de creator-director → nouvelle v de creator-screenwriter
- **Travail en parallèle** : après la vision du réalisateur, character/production/DOP
  s'exécutent en parallèle

## Continuity domains (domaines d'audit)

1. Story / plot
2. Time / chronology
3. Character (physical)
4. Character arc (emotional)
5. Costume
6. Hair / makeup
7. Accessories / props
8. Location
9. Set dressing
10. Light direction
11. Color palette
12. Camera language
13. Sound / ambience
14. Music theme (leitmotif)
15. Emotional flow
16. Edit / screen direction
17. AI prompt consistency (locked anchors verbatim)
18. Reference image consistency
19. Scene / shot numbering

Il existe un journal de risque pour chaque domaine : `project/qc/continuity-reports/`.

## Continuity bible (source unique de vérité)

`project/bible/continuity-bible.md` — ce fichier fait **autorité**. Si la sortie
d'un skill entre en conflit avec la bible, la bible l'emporte (ou la bible est
mise à jour).

Son contenu :
- Locked character anchors (ADN verbatim)
- Locked location anchors (master reference verbatim)
- Table de costume continuity (scène × personnage)
- Table de time / weather
- Table de prop continuity
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction (screen direction × scene)
- Questions de continuité ouvertes (en attente d'une décision du réalisateur)
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md` :

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

Mise à jour après chaque skill run. La source de la réponse à « que dois-je faire maintenant ? ».

## Gestion du revision loop

Quand un skill downstream trouve un problème upstream :

1. **Détection de l'origin** : la sortie de quel skill est défectueuse ?
2. **Blast radius** : comment la correction affecte-t-elle les skills dépendants ?
3. **Change request** : `qc/revision-notes/req-{NN}.md`
4. **Décision** : corriger à l'origin (profond, lent) vs. workaround (superficiel, rapide)
5. **Origin fix** : le skill est re-déclenché, les dépendants passent à 🟡, cascade dans l'ordre canonique
6. **Workaround** : on consigne où, pourquoi et qui l'a appliqué
7. **Resolution log** : ajouté aux « Resolved decisions » de la continuity bible

## Cross-skill arbitration

Quand deux skills entrent en conflit (p. ex. lumière chaude du DOP vs. palette froide du personnage) :

1. Citer les deux propositions **verbatim**
2. Énoncer le conflit en langage clair
3. Référence à la director vision
4. Présenter 2–3 solutions + trade-offs
5. Escalader à l'utilisateur / réalisateur
6. La décision est écrite dans la continuity bible

**Il ne choisit pas en silence** — il rend le conflit visible.

## Risk register

`project/qc/risk-register.md` :

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| Risque d'échec de lip sync en scène 7 | medium | high | creator-shot-list-designer | utiliser un reaction shot | mitigating |
| Risque IA sur l'insert de main en scène 12 | medium | medium | creator-prompt-engineer | backup en wider framing | mitigated |
| Dérive de hue du « Navy coat » | low | high | creator-character-designer | hex verrouillé dans l'ADN | mitigated |

## Structure de dossiers (deux options)

### Default (named — simple)

`project/screenplay/`, `project/characters/`, `project/cuts/` ...

### Alternate (numbered — pour les grands projets)

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

Même contenu, numéroté et adapté au balayage visuel. Le default est named ;
propose une migration sur demande.

## Où il écrit ses sorties

Sous `project/bible/` et `project/qc/` (il N'écrit PAS DIRECTEMENT dans les
répertoires des autres skills — il leur envoie des revision requests) :

| Fichier | Contenu |
|---------|---------|
| `bible/project-bible.md` | Canon du projet de haut niveau |
| `bible/style-bible.md` | Canon de style cross-skill |
| `bible/continuity-bible.md` | Source unique de vérité de la continuité |
| `bible/prompt-blocks.md` | Locked prompt blocks |
| `qc/production-status.md` | Matrice d'état skill × scène |
| `qc/risk-register.md` | Journal de risque |
| `qc/continuity-reports/{topic}.md` | Audits de domaine |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | Audit pré-génération |
| `qc/ai-generation-error-summary.md` | Audit post-génération |
| `qc/final-qc-report.md` | Audit du projet entier |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | Historique des décisions daté |

## Flux typique (nouveau projet)

1. Briefing de l'utilisateur
2. Écrire `bible/project-bible.md`
3. → Déclencher **creator-screenwriter**
4. Script v1 → déclencher **creator-director**
5. Vision → parallèle : **character + production + DOP**
6. Audit cross-palette ; flag des conflits
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. Build/update de `bible/prompt-blocks.md`
10. → **creator-prompt-engineer**
11. Audit pré-génération
12. [AI material — l'operator l'exécute]
13. Audit post-génération
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit (ship gate)

Avant de le déclarer terminé :

- ✅ Toutes les scènes sont dans production-status
- ✅ Continuity audit propre (ou seulement des minor flags)
- ✅ Final cut approuvé par le réalisateur
- ✅ Audio integration audit propre
- ✅ Erreurs IA triées (pas de 🔴 critique)
- ✅ Color grade appliqué ou marqué intentionnellement
- ✅ Subtitles complets et timed
- ✅ Title cards / credits en place
- ✅ Master de toutes les plateformes de livraison sous `project/delivery/`
- ✅ Trailer cut produit (si demandé)
- ✅ Archive master stocké
- ✅ Documentation à jour (bible, continuity, prompt-blocks)

## Coordination avec les autres skills

- **Lit** : toutes les sorties de skill (tout dans `project/`)
- **Écrit** : `project/bible/*`, `project/qc/*` — n'écrit PAS DIRECTEMENT dans
  d'autres répertoires
- **Déclenche** : tous les skills specialist
- **Arbitre** : les conflits cross-skill

## Règles de comportement

| Fait | Ne fait pas |
|------|-------------|
| Impose la fidélité à la director vision dans chaque département | Laisse la dérive silencieuse |
| En conflit cross-skill, cite les deux parties **verbatim** | Choisit un camp en silence |
| Documente chaque décision avec date + justification | Agit sans trace |
| Protège la continuity bible comme autorité | Laisse passer une sortie qui entre en conflit avec la bible |
| Met à jour production-status après chaque skill run | Laisse une table stale |
| Effectue le cascade des révisions dans l'ordre canonique | Saute un skill dépendant |
| Escalade les différends créatifs à l'utilisateur / réalisateur | Arbitre seul |
| Continuity audit à chaque act break d'un film long | N'audite qu'à la fin |
| Risk register proactif | Retient un 🔴 critique |
| Ne dit pas « ship » tant que delivery-readiness.md n'est pas green | Déclare complete trop tôt |
| Sortie structurée et machine-readable | Déverse un seul bloc de texte |
