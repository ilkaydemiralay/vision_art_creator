# vision_art_creator

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · **Français** · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

> Un pack de compétences de production cinématographique par IA pour [Claude Code](https://claude.com/claude-code) et [OpenAI Codex](https://github.com/openai/codex).

`vision_art_creator` regroupe **11 compétences `creator-*`** qui couvrent chaque
département d'une production cinématographique — du scénario jusqu'au montage
final — dans un seul dépôt. Installez-le sur n'importe quelle machine avec
`git clone` + `./install.sh`.

> Les compétences sont conçues pour se référencer mutuellement
> (`creator-pipeline-supervisor` orchestre les autres). Il est recommandé de les
> installer toutes ensemble.

---

## Démo : *Before She Leaves*

Une scène de 26 secondes produite avec ce pack et Higgsfield (références Nano Banana Pro, clips Seedance 2.0), et un making-of de 30 secondes qui montre le graphe enregistré : responsables, hashes et validations. Deux agents, Claude Code et OpenAI Codex, ont travaillé à partir des mêmes fichiers de compétences. Toutes les images sont générées par IA.

**Film (26 s)**

https://github.com/user-attachments/assets/1af79d83-494b-403b-96df-cfdf44dabbf1

**Making-of (30 s)**

https://github.com/user-attachments/assets/5db19cde-1c08-42f1-a48a-cd3a4a0a28d8

Fichiers en pleine qualité : [release v1.2.0](https://github.com/ilkaydemiralay/vision_art_creator/releases/tag/v1.2.0)

---

## Installation

```bash
git clone https://github.com/ilkaydemiralay/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

Vous utilisez OpenAI Codex ? Installez dans son répertoire de compétences, puis redémarrez Codex :

```bash
./install.sh --codex   # ~/.agents/skills/
```

`install.sh` crée un **lien symbolique** pour chaque compétence sous
`~/.claude/skills/<skill-name>` qui pointe vers ce dépôt. L'avantage :
pour mettre à jour, un simple `git pull` suffit — aucune réinstallation requise.

### Options

```bash
./install.sh --target /path/to/skills   # installer dans un autre répertoire de compétences
./install.sh --force                    # écraser les noms existants
./uninstall.sh                          # supprimer les liens symboliques
```

`uninstall.sh` ne supprime que les liens symboliques qui pointent vers ce dépôt — il
laisse intacts les liens externes et les répertoires réels (sauf avec `--force`).

### Vérifier

Après l'installation, redémarrez Claude Code et tapez :

```
/creator-pipeline-supervisor
```

Vérifiez que les 11 compétences `creator-*` apparaissent dans la liste des compétences.

---

## Contenu du pack

| Compétence | Résumé |
|---|---|
| `creator-pipeline-supervisor` | Orchestre l'ensemble de la production, séquence les départements, applique la continuité, exécute le contrôle qualité et produit le rapport de préparation à la livraison. |
| `creator-director` | Traduit le scénario en une vision de réalisation unifiée : direction de scène, jeu d'acteur, blocking, contrôle tonal. |
| `creator-screenwriter` | Écriture et révision de scénarios, traitements, loglines, plans de scènes et dialogues. |
| `creator-character-designer` | Conçoit le personnage comme un tout intégré : psychologie, biographie, identité visuelle, costume, accessoires, expressions codées selon FACS. |
| `creator-production-designer` | Construit l'univers du film : décors, plateaux, accessoires, atmosphère d'époque, langage de couleur et de matière, ancrages de continuité. |
| `creator-cinematographer` | Conçoit le langage visuel : lumière, caméra, optique, cadrage, couleur, atmosphère, mouvement. |
| `creator-storyboard-artist` | Visualise les scènes case par case : échelles de plan, angles, blocking, composition, prompts IA. |
| `creator-shot-list-designer` | Transforme les scènes et les storyboards en une shot list technique, découpée en segments produisibles par IA. |
| `creator-sound-music-designer` | L'univers sonore du film : atmosphère, foley, SFX, partition, leitmotivs, plan musical scène par scène, prompts audio IA. |
| `creator-prompt-engineer` | Convertit la production de chaque département en prompts cohérents pour GPT Image 2.0, Nano Banana, Sora, Veo, Runway, Kling, Higgsfield, et plus encore. |
| `creator-final-cut-editor` | Assemble les plans, l'audio, la musique et les graphismes générés par IA en un film terminé : rough cut, fine cut, final cut, triage des erreurs IA, formats de livraison. |

La définition complète de chaque compétence se trouve dans son propre fichier `SKILL.md`.

---

## Comment ça marche

Le pack fonctionne sur un **état partagé basé sur le système de fichiers**. Toutes les
compétences lisent et écrivent dans une arborescence `project/` commune (`bible/`,
`screenplay/`, `characters/`, `storyboards/`, `prompts/`, `cuts/`, `qc/`, …).
`creator-pipeline-supervisor` maintient les fichiers canoniques (les « bibles » du
projet et de la continuité) et audite la production de chaque département par rapport
à ceux-ci.

Le pipeline canonique :

```
0. project bible & vision
1. creator-screenwriter        → screenplay
2. creator-director            → vision, direction sheets, arcs
3-4-5. creator-character-designer + creator-production-designer
        + creator-cinematographer        (run in parallel)
6. creator-storyboard-artist   → panels with prompts
7. creator-shot-list-designer  → shot list + edit plan
8. creator-prompt-engineer     → tool-fit image + video prompts
   → [AI material generation — operator]
9. creator-sound-music-designer → sound + score plan
10. creator-final-cut-editor   → rough → fine → final cut → delivery

Throughout: creator-pipeline-supervisor enforces continuity, runs QC,
manages revision loops, and holds the bibles.
```

La séquence est canonique mais pas rigide : les retours du réalisateur peuvent
relancer le scénariste, et les départements personnage / production / image
s'exécutent généralement en parallèle une fois la vision de réalisation établie.

---

## Mode graphe enregistré (optionnel, expérimental)

Depuis la v1.1.0, le pack inclut un workflow optionnel et vérifiable par machine pour une seule scène. `creator-pipeline-supervisor` peut exécuter la préproduction sous forme de graphe à 12 nœuds : chaque artefact est enregistré avec son hash SHA-256, chaque validation est liée aux entrées exactes qu'elle a examinées, et une révision ne relance que les nœuds concernés.

- Workflow : `workflows/single-scene.v1.json`. Contrat : `skills/creator-pipeline-supervisor/references/graph-workflow.md`.
- Schémas JSON dans `schemas/`, un validateur en lecture seule dans `scripts/validate_graph.py`, des tests dans `tests/`.
- Un pilote textuel complet de 15 secondes et trois plans dans `examples/single-scene/` : v00 s'arrête sur un conflit de design, v01 le résout, v02 change la couleur d'un accessoire.

L'usage normal des skills ne nécessite pas Python. Pour lancer le validateur (Python 3.10+) :

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-graph.txt
.venv/bin/python -m unittest discover -s tests
.venv/bin/python scripts/validate_graph.py validate --manifest path/to/manifest.json
```

Limites : pilote uniquement textuel, rédigé par un seul auteur. Les départements en parallèle, la génération de médias, le montage et les coûts n'ont pas été testés. L'identité des validateurs et les horodatages sont déclarés par l'opérateur, non signés. Les notes de conception et de résultats sont dans `docs/` (en turc).

---

## Mise à jour

```bash
cd ~/projects/vision_art_creator
git pull
```

Comme les compétences sont liées par des liens symboliques, aucune étape
supplémentaire n'est nécessaire.

Consultez [CHANGELOG.md](CHANGELOG.md) pour les changements de chaque version. **v1.1.0 :** `creator-cinematographer` et `creator-storyboard-artist` gardent désormais leurs brouillons de prompts dans leurs propres dossiers ; seul `creator-prompt-engineer` écrit les prompts finaux dans `project/prompts/`.

---

## Développement

1. Modifiez une compétence dans le dépôt (`skills/creator-*/SKILL.md`).
2. Testez la modification dans Claude Code — comme il s'agit d'un lien symbolique,
   elle prend effet immédiatement.
3. Commit + push.

Pour ajouter une nouvelle compétence creator :

```bash
mkdir -p skills/creator-new-skill
# write SKILL.md and README.md
./install.sh   # create the symlink for the new skill
```

---

## Traductions

Ce README et le `README.md` de chaque compétence sont disponibles en 12 langues (voir
le sélecteur de langue en haut). Les fichiers d'instructions `SKILL.md` sont conservés
en anglais à dessein — Claude répond dans la langue de l'utilisateur à l'exécution, et
un jeu d'instructions canonique unique évite les noms de compétences en double.

---

## Licence

[MIT](LICENSE) © 2026 İlkay Demiralay.
