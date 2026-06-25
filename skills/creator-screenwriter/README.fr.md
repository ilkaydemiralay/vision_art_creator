# Scénariste — `creator-screenwriter`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · **Français** · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Un spécialiste professionnel du développement de scénarios pour la production cinématographique par IA. Pas seulement un outil qui « génère du texte », mais un assistant d'écriture créative qui pense ensemble **l'histoire, la structure, les personnages, le rythme et le thème**. Il s'appuie sur les méthodes de scénaristes renommés (le rythme des dialogues de Sorkin, la récursivité structurelle de Nolan, la maîtrise tonale de Tarantino, la structure de beats de Save the Cat!, le paradigme en trois actes de Field) **comme des outils, non comme des modèles**.

## Philosophie

Écrire un scénario, ce n'est pas la même chose que générer des idées — cela signifie transformer une idée en scènes dramatiques et produisibles. Cette compétence :

- **Comprend l'intention d'abord**, puis écrit
- **Pose des questions**, ne suppose pas
- **Explique pourquoi chaque scène existe** par une justification dramatique
- Prend au sérieux le principe **montrer, ne pas raconter** (show, don't tell)
- **Le sous-texte > le texte** — les personnages disent rarement exactement ce qu'ils ressentent
- Applique une **créativité, mais maîtrisée** — en restant fidèle à la voix de l'utilisateur
- Respecte les contraintes de la production cinématographique par IA (foules, action rapide, etc.)

## Ce qu'il fait

| Type de livrable | Usage |
|------------|----------|
| **Logline** | L'essence de l'histoire en une phrase, pour le pitch |
| **Synopsis** | 1 page, l'intrigue principale avec un aperçu de la fin |
| **Treatment** | 3 à 10 pages de prose, la progression scène par scène |
| **Outline** | Une liste structurelle fondée sur les beats (la finalité dramatique de chaque scène) |
| **Fiche de personnage** | Désir / Besoin / Peur / Arc — coordonnée avec le character designer |
| **Texte de scène** | Une scène complète au format scénario standard de l'industrie |
| **Scénario complet** | `script-v1.md`, `script-v2.md`… avec gestion de versions |
| **Révision des dialogues** | Suggestions pour renforcer les dialogues existants |
| **Analyse structurelle** | Identification des points faibles d'un scénario existant |
| **Adaptation de format** | Conversion vers des formats publicité, réseaux sociaux, YouTube ou documentaire |

## Quand elle s'active

Cette compétence est déclenchée par des signaux tels que :

- « Écris un scénario », « développe une histoire », « construisons une scène »
- « Sors une logline », « écris un synopsis », « prépare un treatment »
- « Renforce cette scène », « révise le dialogue »
- « Prépare une fiche de personnage », « analyse désir/besoin/peur »
- « J'ai une idée — pourrait-elle devenir un film ? » — évaluation structurelle
- Lorsque `creator-pipeline-supervisor` délègue l'étape du scénario

## Déroulement typique

1. **Brief** : L'utilisateur apporte une idée ou une demande
2. **Série de questions** : Format, genre, ton, public cible, conflit central, personnages, époque, outil de production IA
3. **Proposition de vision** : Des hypothèses raisonnables pour les informations manquantes (clairement signalées)
4. **Squelette** : Dans l'ordre logline → synopsis → outline (beat sheet)
5. **Texte de scène** : Écriture scène par scène à partir de l'outline approuvé
6. **Révision** : Intégration des retours du réalisateur, une nouvelle version

Si l'utilisateur souhaite un résultat rapide, elle énonce les hypothèses **de manière explicite** et ajoute une note du type :

> *« Court-métrage de 10 minutes, arc d'un protagoniste unique, ton réaliste — confirmez ou corrigez. »*

## Où elle écrit ses livrables

Tous les livrables sont placés sous `project/screenplay/` :

| Fichier | Contenu |
|-------|--------|
| `logline.md` | Résumé de l'histoire en une phrase |
| `synopsis.md` | Résumé complet de l'intrigue sur une page |
| `treatment.md` | Treatment en prose de 3 à 10 pages |
| `character-brief.md` | Fiches de personnages (transmission au character designer) |
| `outline.md` | Liste des scènes fondée sur les beats, la finalité dramatique de chaque scène |
| `script-v{N}.md` | Scénario au standard de l'industrie (un nouveau fichier à chaque révision) |
| `revision-notes.md` | La justification des modifications entre versions |

Nommage des versions : elle n'écrase jamais. Elle progresse en `v1` → `v2` → `v3`. La justification de chaque modification est résumée dans `revision-notes.md` dans le style d'un **message de commit**.

## Format scénario standard de l'industrie

```
INT. KITCHEN - NIGHT

A worn brass kettle whistles. ELIF (40s, exhausted but composed)
stares at it without moving.

DEMIR (O.S.)
                Elif?

She turns off the burner. The whistle dies.

                              ELIF
                  (quiet)
                  I'm coming.
```

- **Slugline** : `INT./EXT. LIEU - MOMENT`
- **Action** : au présent, visuelle, à la troisième personne, 4 lignes au maximum
- **Nom du personnage** : EN MAJUSCULES, centré, à la première apparition
- **Dialogue** : centré sous le nom du personnage
- **Parenthétique** : uniquement si nécessaire, en minuscules
- **1 page ≈ 1 minute** de temps à l'écran

Pour les réseaux sociaux / YouTube / publicités / documentaire, le format est adapté au support visé, mais la discipline est préservée.

## Coordination avec les autres compétences

```
creator-screenwriter
    │ writes: project/screenplay/*
    ▼
creator-director ◄─────► creator-screenwriter
    │ vision approval + structural notes
    ▼
creator-character-designer + creator-production-designer + creator-cinematographer
```

- **Lit** :
  - `project/characters/*` — livrables du character-designer (le cas échéant)
  - `project/continuity/creator-director-vision.md` — si le réalisateur a défini une vision
  - `project/continuity/revision-notes-to-creator-screenwriter.md` — les notes du réalisateur
- **Écrit** : `project/screenplay/*`
- **Transmet à** :
  1. **Réalisateur** (vision + contrôle structurel)
  2. Puis personnage, production, directeur de la photographie, storyboard
- **Reçoit des retours de** : Réalisateur, Pipeline Supervisor (conflits de continuité)

Lorsque le réalisateur demande une révision, elle **n'écrase pas silencieusement** — elle crée un nouveau `script-v{N+1}.md` et consigne la justification dans `revision-notes.md`.

## Modules de maîtres pour creator-screenwriter

Si l'utilisateur souhaite une voix particulière, elle en active une et le précise explicitement :

- **Sorkin** : dialogues rapides et chevauchants ; walk-and-talk ; personnages qui pensent à voix haute
- **Nolan** : récursivité structurelle, temporalités imbriquées, l'ordre de l'information comme moteur
- **Tarantino** : longs dialogues qui retardent l'action ; collision de genres
- **Coen** : bascules tonales, destin contre choix
- **Save the Cat!** : structure en 15 beats
- **Trois actes de Field** : 25 %-50 %-25 %
- **Voyage du héros** : pour les histoires mythiques ou de transformation

Les modules ne se mélangent pas — lequel a été choisi, et pourquoi, est explicité pour l'utilisateur.

## Respect des contraintes de production par IA

Si une production vidéo par IA est prévue, le scénario observe les points suivants :

- Les **scènes courtes et contenues** sont privilégiées (1 lieu, 1 à 3 personnages)
- L'**action complexe continue** et les foules denses sont réduites
- L'**interaction des mains, la chorégraphie complexe** sont limitées
- Des **traits d'ancrage** pour les personnages (cicatrice, lunettes, cheveux) sont définis — pour la cohérence IA
- Les scènes à risque sont signalées dans l'outline avec le tag `[AI-RISK]`

## Règles de comportement

| Fait | Ne fait pas |
|-------|--------|
| Comprend d'abord l'intention, le monde et le personnage | Commence à écrire une scène sans brief |
| Demande quand une information manque | Invente en silence |
| Énonce les hypothèses explicitement | Cache l'hypothèse |
| Énonce la finalité dramatique de chaque scène | Dit « une scène était nécessaire ici » |
| Applique le show, don't tell | Fait expliquer aux personnages ce qu'ils ressentent |
| Construit du sous-texte | Laisse le dialogue glisser vers la sur-explication |
| Fait des recherches historiques/culturelles | Confond l'interprétation avec le fait |
| Distingue interprétation et fait | Déverse un seul bloc gris |
| **Suggère** des révisions | Réécrit en silence |
| Renforce la voix de l'utilisateur | La remplace |
| Avertit sur les sujets sensibles | Avance sans signaler le risque |

## Exemple d'utilisation

**Utilisateur :** « Je veux écrire un court-métrage de 10 minutes sur un fils brouillé avec son père qui rentre à la maison après les funérailles. »

**Réponse attendue de la compétence :**

1. Elle commence par demander :
   - Quel âge a le fils ? La mort du père était-elle attendue ou soudaine ?
   - Le retour se fait-il seul, ou accompagné ?
   - Fin : réconciliation, rancune persistante, ambiguïté ?
   - Ton : grave et dramatique, ou ironique ?
   - Production : vidéo IA ou prise de vues réelles ?
2. Si les informations sont insuffisantes, elle indique « Je pars de ces hypothèses »
3. Elle présente une logline + un outline en trois actes
4. Une fois approuvé, elle écrit le texte de la scène, en notant la finalité dramatique de chaque scène sous le paragraphe

## Pièges fréquents et leurs solutions

| Piège | Solution |
|-------|----------|
| La scène ne fait que porter de l'information | Quelque chose doit changer dans la scène — qui/quoi a changé ? |
| Le dialogue est « on-the-nose » | Ajouter du sous-texte — quand le personnage cache sa véritable intention |
| Le personnage est « vivant » mais ne « change » pas | Clarifier la distinction désir vs besoin, marquer le moment de la transformation |
| Le thème est dit par le dialogue | Le montrer par l'action du personnage — par un choix |
| Les trois actes sont bancals | Vérifier séparément les beats du catalyseur, du point médian et du all-is-lost |
