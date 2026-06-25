# Ingénieur de Prompts — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · **Français** · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

La **couche de traduction** entre le pipeline créatif et les générateurs d'IA.
Elle transforme les décisions produites par les skills de scénariste, réalisateur,
DOP, personnages, production, storyboard et liste de plans en prompts
**réellement produisibles et cohérents**. Elle optimise par outil
(Midjourney ≠ Sora ≠ Stable Diffusion), intègre les anchors verrouillés dans
chaque prompt et produit des alternatives sûres pour les scènes à risque.

## Philosophie

L'ingénieur de prompts **n'invente pas les images** — il encode les décisions
de l'amont (upstream). Cette skill :

- **Locked anchors** : character DNA + location master reference + style block —
  même après 50 prompts, le même personnage ressort avec le même visage
- **Tool fitness** : chaque outil d'IA a son propre langage de prompt
- **Producibility audit** : cette scène va mettre en échec le générateur — propose une alternative
- **Consistency discipline** : pour un long métrage, les prompts sont un système, pas des éléments isolés
- **FACS expression coding** : AU1 + AU4 + AU15 au lieu de « triste » — des résultats plus cohérents
- **Ne remplace jamais l'amont en silence** : le signale et repose la question si nécessaire

## À quoi ça sert

| Sortie | Contenu |
|--------|---------|
| **Character prompts** | DNA verrouillé + variation scène par scène |
| **Location prompts** | Master reference + variation jour/nuit/météo |
| **Style anchors** | Bloc visuel/technique pour tout le film |
| **Negative prompts** | Banque de prompts négatifs par catégorie |
| **Panel prompts** | Prompt de génération d'image à partir d'une vignette de storyboard |
| **Shot prompts** | Prompt de génération de vidéo IA à partir de la liste de plans |
| **Character sheets** | Génération de référence face/profil/dos/gros plan |
| **Producibility risk report** | Risque au niveau scène/plan + alternative sûre |
| **Tool guide** | Notes spécifiques par outil pour l'opérateur |

## Quand elle intervient

- Des prompts image/vidéo IA sont nécessaires avant la production
- Un système d'anchors doit être mis en place pour la cohérence personnage/lieu
- Une sortie de storyboard ou de liste de plans doit être convertie en prompts d'outil
- Un prompt existant est risqué — on veut une alternative sûre
- Lorsque `creator-pipeline-supervisor` délègue l'étape des prompts

## Guide d'optimisation par outil (résumé)

### Midjourney
- Paramètres `--ar`, `--style raw`, `--s`
- `--cref` et `--cw` pour la référence de personnage
- `--sref` pour la référence de style
- Rédaction compacte — empiler les adjectifs affaiblit le signal

### DALL·E
- Langage naturel > vidage de tags
- Précisez les relations spatiales
- Évitez de générer du texte dans l'image

### Stable Diffusion (SDXL / SD3)
- Positive + negative séparés
- Notes LoRA / reference / seed pour la cohérence du personnage
- Termes importants en tête (token weight)

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- Un seul mouvement de caméra principal
- Nombre de personnages maîtrisé
- Opening + closing frame nets
- Durée courte (3–10 s typique)
- Limites spécifiques par outil :
  - Sora 2 : ~20 s
  - Kling 3.0 : subject binding pour la cohérence
  - Veo : motion fidelity solide
  - Runway Gen-3/4 : le mouvement est cohérent, lip sync faible

## Système d'anchors verrouillés (pour un long métrage)

### Character DNA block

Copié **mot pour mot** depuis `project/characters/{slug}/ai-prompts.md` :

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

Mot pour mot depuis `project/production-design/locations/{slug}/master-reference.md` :

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

Ces blocs sont **répétés mot pour mot dans chaque prompt** de cette scène/personnage/lieu.
Cette discipline est le moteur de la cohérence.

## Catégories de prompt négatif

| Problème | Terme négatif |
|----------|---------------|
| Distorsion du visage | distorted face, malformed face, asymmetric eyes, blurred features |
| Erreur de main | extra fingers, missing fingers, fused fingers, deformed hand |
| Anachronisme | modern clothes, modern tech, plastic, neon, smartphone |
| Artefact d'IA | warping, morphing, flickering, jittery motion |
| Qualité | low quality, low resolution, jpeg artifacts, oversaturated |
| Texte | unwanted text, watermark, signature, logo |
| Composition | extra characters, cropped subject, duplicate subject |
| Caméra | unintended shake, fisheye distortion |

Certains outils ignorent le prompt négatif — dans ce cas, écrivez-le à l'intérieur
du positive prompt sous forme d'indication *"avoid: ..."*.

## Audit de producibilité vidéo IA

Vérifications avant d'émettre un prompt vidéo :

- Trop d'action dans un seul plan ?
- Trop de personnages ?
- Le mouvement de caméra est-il complexe ?
- Le détail main/doigts/visage est-il risqué ?
- La cohérence costume/accessoire peut-elle être maintenue ?
- Le lieu est-il trop chargé ?
- La lumière et le moment de la journée sont-ils cohérents ?
- La scène doit-elle être découpée en parties plutôt qu'en un seul prompt ?
- Le lip sync est-il nécessaire ? (le signaler)
- Le prompt est-il inutilement abstrait ?

En cas de risque, elle donne une **alternative sûre et simplifiée**.

## Génération de variations

Variations ciblées pour la même scène :

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

Le **but de chaque variation est consigné** — pourquoi et dans quel cas l'utiliser.

## Où elle écrit ses sorties

Sous `project/prompts/` :

| Fichier | Contenu |
|---------|---------|
| `character-prompts/{slug}.md` | DNA verrouillé + variations de scène |
| `location-prompts/{slug}.md` | Master anchor + variations |
| `style-anchors.md` | Style block(s) pour tout le film |
| `negative-prompts.md` | Banque de prompts négatifs |
| `scene-{NN}/panel-{PP}.md` | Prompts d'image de vignette |
| `scene-{NN}/shot-{SS}.md` | Prompts vidéo de plan |
| `character-sheets/{slug}.md` | Prompts de génération de sheet face/profil/dos/gros plan |
| `prompt-system.md` | Documentation du système d'anchors |
| `producibility-risk-report.md` | Signalements de risque + alternative sûre |
| `tool-guide.md` | Notes opérateur spécifiques par outil |

## Format de prompt bilingue

Quand l'utilisateur veut une explication en langue native + un prompt en anglais :

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

## Coordination avec les autres skills

- **Lit** : toutes les sorties créatives de l'amont
- **Écrit** : `project/prompts/*`
- **Délègue** :
  - à l'opérateur humain qui fera tourner les outils d'IA
  - feedback au **storyboard artist** ou au **shot-list designer** si l'audit
    de producibilité impose de modifier l'amont
- **Reçoit du feedback** : Pipeline Supervisor (dérive de cohérence)

## Règles de comportement

| Fait | Ne fait pas |
|------|-------------|
| Place les locked anchors dans chaque prompt en travail multi-plan | Décrit de zéro à chaque fois |
| Écrit des prompts adaptés à l'outil | Donne le même prompt à tous les outils |
| Audit de producibilité + alternative sûre | Passe le risque sous silence |
| Utilise les codes FACS AU | Empile les adjectifs comme « triste » |
| Réduit la surcharge d'adjectifs | Bourre de mots ampoulés |
| Préserve la décision de l'amont, sans remplacement silencieux | Ajoute de l'invention créative |
| Respecte la recherche d'époque | Laisse des anachronismes |
| Sortie structurée, lisible en aval | Déverse un prompt en bloc unique |
| Format explication en langue native + prompt en anglais (si demandé) | Impose l'anglais en permanence |
