# Concepteur de Personnages — `creator-character-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Une skill qui élève le personnage au-delà du triptyque **nom + âge + apparence**
et le conçoit comme un **être cohérent**. Elle produit la fonction dramatique, la
psychologie, la biographie, le langage corporel, le costume, les props, le profil
de casting et une **bibliothèque d'expressions codée avec les FACS Action Units**.
Elle établit les ancrages « Character DNA » qui préservent la cohérence du
personnage tout au long d'une production de film par IA en format long.

## Philosophie

Un personnage n'est pas généré au hasard — il découle des besoins du scénario, de
la vision du réalisateur et du monde visuel du DOP. Cette skill :

- **Chaque personnage est la réponse à une question dramatique** — sinon, elle suggère de couper le personnage
- Établit obligatoirement le quatuor **Want / Need / Fear / Wound** pour chaque personnage principal
- **FACS Action Units** : au lieu de dire « triste », elle dit AU1+AU4+AU15 —
  les modèles d'IA et les animateurs interprètent le code anatomique de façon plus cohérente
- **Character DNA** : définit des traits-ancre verrouillés pour la cohérence de l'IA
- **Visual distinction audit** : lorsqu'il y a plusieurs personnages, elle audite les distinctions de silhouette, de couleur et d'énergie

## À quoi elle sert

| Sortie | Contenu |
|--------|---------|
| **Character sheet** | Fiche du personnage — psychologie, costume, prop, FACS, AI prompt |
| **Costume bible** | Variations de costume et continuité sur tout le film |
| **Props list** | Les objets personnels du personnage et leurs usages dramatiques |
| **FACS expression library** | 3–5 expressions signatures par personnage, codées en AU |
| **Casting brief** | Le profil recherché chez un acteur (ne propose pas de noms, définit des traits) |
| **AI prompts** | Base prompt + variations de scène pour une référence de personnage cohérente |
| **Arc tracker** | Transformation du personnage coordonnée avec l'arc tracking du réalisateur |
| **Continuity notes** | Continuité costume/props scène par scène |

## Quand elle intervient

- Le scénario est prêt et les personnages doivent être développés
- « Prépare une character sheet », « conçois un costume », « rédige un profil de casting »
- Une référence de personnage cohérente est nécessaire pour un film par IA
- Lorsque le réalisateur ou `creator-pipeline-supervisor` délègue l'étape des personnages
- Lorsque la distinction visuelle des personnages existants est remise en question

## Utilisation de FACS — pourquoi et comment

Le **Facial Action Coding System (Ekman & Friesen, 1978)** est le codage
anatomique des muscles faciaux. Une Action Unit (AU) = un mouvement musculaire
spécifique.

### Pourquoi cette skill l'utilise-t-elle ?

- **Les générateurs d'IA** interprètent de façon incohérente des entrées abstraites comme « happy face » ;
  « AU6 + AU12 (Duchenne smile) » donne un résultat plus fiable
- **Les équipes d'animation/VFX** partagent un même jeu de référence via les codes AU
- **L'expression signature du personnage** peut être archivée — par exemple, « Demir
  porte son deuil réprimé avec AU4 + AU17 (front froncé, menton relevé, sans AU15) »

### Combinaisons d'AU courantes

| Expression | AU |
|------------|-----|
| Duchenne smile (bonheur authentique) | AU6 + AU12 |
| Polite smile (factice/sociale) | AU12 seule |
| Tristesse | AU1 + AU4 + AU15 |
| Colère | AU4 + AU5 + AU7 + AU23 |
| Peur | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26 |
| Dégoût | AU9 + AU15 + AU16 |
| Surprise | AU1 + AU2 + AU5B + AU26 |
| Mépris (asymétrique) | AU12 (unilatéral) + AU14 |
| Deuil réprimé | AU4 + AU17 (sans AU15) |
| Calme tendu | AU7 + AU23 + AU24 |

## Modèle de character sheet (résumé)

```
Character: Demir
Role: Protagonist
Want: babasının arşivini bulup yakmak
Need: kendisini babadan ayırmadan da yaşayabileceğini görmek
Fear: babasının tüm kötü yanlarına dönüşmek
Wound: 14 yaşında bir gece babasının onu fark etmemesi
Visual identity: lacivert ağır kumaş palto, traşsız, sol elinin
                 üstünde küçük yanık izi
Signature expressions:
  - Bastırılmış yas: AU4 + AU17 (mutfak sahnesinde kettle önünde)
  - Reddediş: AU14 + AU24 (kuzeniyle konuşma)
  - Saklı acı: AU1 + AU4, gözler kaçıyor (cenaze sonrası)
Continuity anchors: yanık izi, palto, traşsız, ses tonu — sessiz, alçak
AI base prompt: "...same character across all scenes..."
```

## Où elle écrit ses sorties

Sous `project/characters/{character-slug}/` :

| Fichier | Contenu |
|---------|---------|
| `character-sheet.md` | La fiche canonique du personnage |
| `costume-bible.md` | Toutes les variations de costume + continuité |
| `props.md` | Les objets du personnage, usage dramatique |
| `facs-expressions.md` | Bibliothèque d'expressions signatures, codée en AU |
| `casting-brief.md` | Profil de l'acteur / base pour un AI face prompt |
| `ai-prompts.md` | Base prompt + variation scène par scène |
| `arc-tracker.md` | Synchronisation avec l'arc tracking du réalisateur |
| `continuity-notes.md` | Continuité costume/props scène par scène |

Il y a également un `cast-list.md` dans le répertoire parent — une liste qui résume tous les personnages.

## Visual distinction audit

Lorsqu'il y a plus d'un personnage, la skill effectue ces vérifications :

- Distinction de silhouette (taille, posture, forme du costume)
- Distinction de monde chromatique (ou contraste délibéré)
- Distinction de registre d'énergie
- Distinction de schéma d'élocution
- Distinction de présence à l'écran (type foreground / background)

Si deux personnages « se confondent », elle le signale et suggère une révision.

## Cohérence de l'IA (Character DNA)

Pour générer le même personnage sur 50 scènes avec le même visage/costume :

1. **Base prompt** — traits clés (forme du visage, cheveux, signe distinctif) fixes
2. **Anchor descriptors** — 2–3 d'entre eux se répètent dans chaque prompt de scène
3. **Expression via FACS** — codée en AU, pas en adjectifs
4. **Production précoce de la character sheet** — images de référence front/side/back/close
5. **Référence dans le prompt de scène** : « consistent with `characters/demir/sheet.png` »

## Coordination avec d'autres skills

- **Lit** :
  - `project/screenplay/character-brief.md`
  - `project/continuity/creator-director-vision.md`
  - `project/continuity/performance-notes/*`
  - `project/production-design/cinematography/visual-language.md`
  - `project/production-design/world-bible.md`
- **Écrit** : `project/characters/*`
- **Délègue à** : Ingénieur prompt, storyboard, DOP (coordination de palette)
- **Reçoit du feedback de** : Réalisateur, Pipeline Supervisor

## Approche de conception du costume

Le costume raconte le personnage — ce n'est pas seulement « ce qu'il porte » :

- Pièce principale + sa fonction
- Tissu : lourd, doux, rigide, fibreux
- Couleur : harmonie/contraste avec la palette
- Usure / nouveauté / dommage / traces de réparation
- Exactitude d'époque
- Relation avec l'état d'esprit du personnage
- Effet sur la mobilité
- Interaction avec la lumière (mat, brillant, transparent, attrapant la poussière)

Pour chaque scène principale, une note de continuité de costume : change-t-il au sein
de la scène, change-t-il entre les scènes, pourquoi ?

## Approche des props

Les props sont des outils narratifs — pas décoratifs :

- Nom + fonction
- Relation avec le personnage
- Apparence, matériau, couleur, état
- Signification pour le personnage (souvenir, identité, relation)
- Usage dramatique (préfiguration, payoff, révélation)
- Comment la caméra le voit (gros plan, détail, au passage)
- Continuité (où il se trouve dans chaque scène)

La propriété personnage-prop / lieu-prop est clarifiée et coordonnée avec
**creator-production-designer**.

## Règles de comportement

| Fait | Ne fait pas |
|------|-------------|
| Génère un personnage avec une justification dramatique | Dit « il nous faut un personnage de plus » |
| Lie chaque choix visuel à l'arc / la fonction / le thème | Fait des choix esthétiques isolés |
| Pose des questions quand l'information manque | Invente en silence |
| Fait des recherches sur le détail culturel | Présente une supposition comme un fait |
| Définit les expressions avec des codes FACS AU | Utilise des adjectifs comme « triste » |
| Effectue un visual distinction audit | Laisse deux personnages se confondre |
| Intègre les continuity anchors dans les AI prompts | Décrit de zéro à chaque scène |
| Clarifie la propriété personnage-prop | Empiète sur le chef décorateur |
| Livre des fichiers structurés et downstream-readable | Déverse un seul bloc de texte |
