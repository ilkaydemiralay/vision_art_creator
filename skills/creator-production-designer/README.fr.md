# Chef décorateur — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Le skill qui construit le **monde** du film : décors, lieux, props, atmosphère
d'époque, langage de couleur et de matières. Au lieu de dire « un beau
village », il conçoit jusqu'au niveau de la texture du mur, du matériau du sol,
de la densité du mobilier, des surfaces qui agissent sur la lumière et des
traces d'usure. Il établit les master references qui assurent la **cohérence de
lieu** tout au long d'une production de film par IA de format long.

## Philosophie

Un espace n'est pas un arrière-plan — c'est un **instrument narratif**. Ce skill :

- **World bible** d'abord — puis per-location, puis per-scene (top-down)
- **Master reference** : un bloc de prompt IA verrouillé pour chaque lieu
  principal — afin de pouvoir produire la même maison même 50 scènes plus tard
- **Design du vécu** : fissures, taches, décoloration au soleil, usure, traces
  de réparation
- **Class-coded design** : chaque matière/couleur dit la classe sociale
- **Coordinated palette** : pensée conjointement avec l'éclairage du DOP et les
  costumes du personnage
- **Period research** : recherche sourcée lorsqu'une exactitude
  historique/culturelle est requise

## À quoi ça sert

| Sortie | Contenu |
|-------|--------|
| **World bible** | Les règles générales du monde du film (époque, classe, architecture, matières) |
| **Color & texture bible** | Palette de couleurs, langage des matières, motifs d'usure |
| **Location dossier** | Un document complet pour chaque lieu principal (verrouillé + variations) |
| **Master reference (AI)** | Le bloc de prompt IA fixe de l'identité d'un lieu |
| **Props inventory** | Objets de plateau, avec leurs fonctions dramatiques |
| **Per-scene plan** | Décoration scène par scène (dressing, props, sources de lumière) |
| **Continuity log** | Contrôle de cohérence de lieu entre les scènes |
| **Period research** | Recherche historique/culturelle sourcée |
| **Notes to DOP / creator-director** | Communication bidirectionnelle |

## Quand il intervient

- Scénario en main, design de monde / lieu / décor nécessaire
- « À quoi doit ressembler ce lieu », « set dressing », « liste de props »
- Référence de lieu cohérente pour la production par IA
- Recherche d'époque (historique, culturelle, régionale)
- Quand `creator-pipeline-supervisor` délègue la phase de design de production

## Flux typique

1. **Briefing** + lecture de `creator-director-vision.md` + DOP visual-language
2. **Tour de questions** : époque, géographie, ton, classe, outils IA
3. **World bible** : les règles générales du monde du film
4. **Color & texture bible** : langage des matières et de la couleur
5. **Major locations** : un dossier pour chaque lieu principal
6. **Master references** : blocs de prompt verrouillés pour la cohérence IA
7. **Per-scene sheets** : set dressing scène par scène + notes de props
8. **Continuity audit** : le même lieu est-il cohérent d'une scène à l'autre ?

## Où il écrit ses sorties

Sous `project/production-design/` (hors cinematography — cela revient au DOP) :

| Fichier | Contenu |
|-------|--------|
| `world-bible.md` | Les règles du monde du film |
| `color-texture-bible.md` | Langage de couleur + matières |
| `locations/{slug}/location-doc.md` | Dossier per-location |
| `locations/{slug}/master-reference.md` | Base prompt IA verrouillé |
| `props/{slug}.md` ou `props-list.md` | Inventaire des props |
| `scenes/scene-{NN}.md` | Plan de design de production scène par scène |
| `continuity-notes.md` | Journal de contrôle de cohérence de lieu |
| `period-research.md` | Recherche d'époque sourcée |
| `notes-to-creator-director.md` | Questions/suggestions au réalisateur |
| `notes-to-creator-cinematographer.md` | Coordination surface/profondeur/lumière avec le DOP |

## Modèle de location dossier (résumé)

```
Location: Demir'in dedesinin köy evi mutfağı
Function in story: Demir'in babayı ilk kez bir mekânda hisseder
Period: 1980'ler doğu Anadolu kırsalı
Architectural style: tek katlı kerpiç, ahşap kiriş tavan, kireçli duvar
Color palette: kireç beyazı, bakır, yanmış toprak, kömür siyahı
Texture: kireç ufalı duvar, ahşap çatlamış, bakır pas yeşili, demir tencere is izi
Walls: kireç boyalı, alt 1m'de toz/duman izi
Floor: ham ahşap, eskimiş
Doors / windows: ahşap kanat pencere, dışarısı çıplak ağaç
Furniture: ahşap masa (4 kişilik), iki sandalye, bakır kapaklı dolap
Decorative: duvarda tek bir solmuş aile fotoğrafı
Daily-use items: bakır kettle, demir tencere, tahta kaşıklar, kil testi
Lived-in level: yıllarca yaşanmış, son 2 hafta dokunulmamış (toz tabakası)
Light-affecting surfaces: kireç (matt, ışık yutar), bakır (kontur), pencere (tek kaynak)
Camera framing points: pencere ışığı kettle'ı tarayan açı; masa ekseni
Continuity anchors: pencere konumu, masa, dolap, fotoğraf — KİLİTLİ
AI master reference prompt: "...same kitchen across all scenes..."
Variations: gündüz, gece, fırtınalı, yeni temizlenmiş (final sahnede)
```

## Master reference (pour la cohérence IA)

Un **bloc de base prompt verrouillé** est écrit pour chaque lieu principal :

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

Ce bloc est répété tel quel dans tous les prompts de scène, avec la variation
spécifique à la scène ajoutée par-dessus.

## Coordination avec les autres skills

- **Cinematographer** :
  - Comment les surfaces réagissent à la lumière (matte, glossy, transparent)
  - Premier plan/plan intermédiaire/arrière-plan pour étager la profondeur
  - La palette de couleurs fonctionne-t-elle avec l'éclairage prévu ?
  - Les miroirs, le verre, les surfaces brillantes posent-ils problème à la caméra ?
- **Director** :
  - Le lieu sert-il le thème central ?
  - Le ton du monde correspond-il à la vision ?
  - Y a-t-il des lieux qui doivent être « signature/iconic » ?
- **Character-designer** :
  - Le costume se lit-il correctement dans la palette du lieu ?
  - Les objets personnels trouvent-ils leur place dans le dressing ?
  - La classe sociale est-elle cohérente à la fois par le costume et par l'espace ?
- **Storyboard / shot-list** : notes des points de cadrage
- **Prompt-engineer** : hand-off de la master reference + prompts de variation

## Reads / writes

- **Reads** : scénario, vision du réalisateur, DOP visual-language, palettes de personnage
- **Writes** : `project/production-design/*` (hors cinematography)

## Solutions orientées production par IA

- Produire de nombreuses scènes avec peu de lieux
- Montrer le même lieu différemment via la variation d'angle/lumière/météo
- Maîtriser la densité du dressing — pour ne pas surcharger l'IA
- Simplifier les espaces complexes avec lesquels l'IA aurait du mal
- Cohérence par des images de référence fixes
- Production précoce de la « master reference »
- Réutiliser les objets de dressing (cohérence du monde)
- Réduire le détail superflu pour faire ressortir l'objet dramatique

## Règles de comportement

| Fait | Ne fait pas |
|-------|--------|
| Conçoit l'espace comme un instrument narratif | Dit « une belle pièce » |
| Lie chaque décision de dressing à l'époque/au personnage/au thème | Fait des choix esthétiques isolés |
| Pose des questions quand l'information manque | Invente en silence |
| Fait des recherches sur les détails culturels et les étiquette | Présente l'interprétation comme un fait |
| Assure la cohérence IA via la master reference | Décrit de zéro à chaque scène |
| Coordonne la palette avec le DOP + les personnages | Décide isolément |
| Clarifie la propriété prop-de-personnage / prop-de-lieu | Entre en conflit avec le character designer |
| Livre un fichier structuré et downstream-readable | Déverse un seul bloc de texte |
| Propose des alternatives pour les lieux à risque pour l'IA | Force un détail impossible à produire |
