# Monteur Final — `creator-final-cut-editor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · **Français** · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

La compétence qui transforme les sorties de production IA en un **film fini**. La
fin de la pré-production / le début de la post-production. Une fois le matériau
produit, elle gère le flux rough cut → fine cut → final cut → livraison ; elle
trie les erreurs de génération IA, audite la continuité, vérifie l'intégration
audio/musique et produit des masters prêts à livrer.

**Différence avec shot-list-designer** : le shot list conçoit l'intention de
montage AVANT le tournage ; creator-final-cut-editor EXÉCUTE le montage sur le
matériau réel.

## Philosophie

Le final cut n'est **pas un séquençage technique** — c'est la construction d'une
cohérence cinématographique. Cette compétence :

- **Une justification dramatique pour chaque coupe** — « ça rend bien » ne suffit pas
- **Rythme multi-échelle** : à l'intérieur d'un plan, à l'intérieur d'une scène, à l'échelle du film entier
- **Triage des erreurs IA** : quelle erreur casse le montage, laquelle peut être masquée, laquelle peut rester
- **Conception de l'expérience du public** : ce que le spectateur ressent, apprend et retient
- **Discipline de livraison** : YouTube ≠ festival ≠ Instagram ≠ archive
- **Versionnage** : gère séparément les cuts rough/fine/final + festival/social/trailer

## Ce qu'elle fait

| Sortie | Contenu |
|-------|---------|
| **Évaluation du matériau** | Par plan : utilisable / à réviser / à régénérer / à couper |
| **Plan de rough cut** | Premier séquençage brut, liste du matériau manquant |
| **Plan de fine cut** | Points de coupe, durées des plans, silence |
| **Plan de final cut** | Niveau de préparation final + checklist de livraison |
| **Final-check par scène** | Audit détaillé scène par scène |
| **Rapport sur le film entier** | Rapport de final cut pour l'ensemble du film |
| **Rapport d'erreurs IA** | Erreurs de génération + classification par gravité |
| **Audit d'intégration audio** | Retour au sound designer |
| **Notes de color grade** | Directives de correction colorimétrique |
| **EDL** | Edit Decision List lisible par un NLE |
| **Manifeste de versions** | Versions de cut festival/social/trailer |
| **Spécifications de livraison** | Réglages d'export propres à chaque plateforme |
| **Plan de trailer** | Plan de cut teaser/trailer |

## Quand elle entre en jeu

- Les plans vidéo IA ont été produits, le montage commence
- Une planification de rough/fine/final cut est requise
- Un audit des erreurs IA est demandé
- Plusieurs cuts (festival, social, trailer) vont être produits
- Préparation de l'export de livraison
- Lorsque `creator-pipeline-supervisor` délègue la phase de post-production

## Flux typique

1. **Évaluation du matériau** — chaque plan est catégorisé (✅🟡🟠🔴)
2. **Rough cut v01** — ordre narratif, séquence dramatique de base
3. **Fine cut v01** — points de coupe, rythme, silence
4. **Audit d'intégration sonore** — retour à creator-sound-music-designer
5. **Rapport d'erreurs IA** — classification critique/moyen/mineur
6. **Notes de color grade** — si nécessaire
7. **Vérification des sous-titres / titres / graphismes**
8. **Final cut v01** — checklist de préparation
9. **Export de livraison** — version propre à chaque plateforme

## Matrice de triage des erreurs IA

| Gravité | Définition | Action |
|----------|------------|--------|
| 🔴 Critique | Ne peut pas entrer dans le final cut | Régénérer (signaler à creator-prompt-engineer) |
| 🟡 Moyen | Masqué via trim/recadrage/couleur/son | Contournement au montage |
| ✅ Mineur | Ne dérange pas le spectateur | Peut rester |

Vérifiés : déformation du visage, erreurs de mains/doigts, lip-sync, changements
de costume, perte d'accessoires, dérive de lieu, incohérence de direction de
lumière, mouvement de caméra artificiel, scintillement, warping, morphing,
objets qui fondent, effondrement de l'arrière-plan, anachronisme, aspect
plastique.

## Format du final-check par scène

```
Scene 04 — "Mutfak / Cenaze Sonrası"
Target duration: 90s
Current duration: 102s
Dramatic purpose: Demir'in iç dönüşümünün ilk anı
Core emotion: Bastırılmış yas

Shots used: 04.01, 04.02, 04.03, 04.05, 04.06
Shots cut: 04.04 (gereksiz reaction, ritim düşürüyor)
Shots shortened: 04.05 (8s → 5s — wide hold gereksiz uzun)
Shots lengthened: 04.02 (4s → 6s — kettle hold dramatik nefes)
Cut points:
  - 04.01 → 04.02: sound bridge (kettle ıslığı önce)
  - 04.02 → 04.03: hard cut (kettle sessizleşmesi → Demir close)
Transitions:
  - Scene → next: dissolve (sabah ışığına geçiş)
Reaction shot usage: 04.03 (Demir close) — yas kırılma anı
Silence usage: 04.02'de 4 saniye saatin tıkırtısı dışında hiç ses yok
Music usage: YOK — yönetmen direktifi
Ambience / foley notes: kettle, saat tıkırtı, dış rüzgâr çok kısık
Visual continuity notes: ✅ kostüm, ışık yönü, kettle leke pattern hepsi tutarlı
AI error audit:
  - 04.02 kettle buharı warping (🟡 orta) — sound design ile maskelenecek
  - 04.03 Demir göz sol kenar microflicker (🟡 orta) — color grade düzeltir
Color / light notes: 04.05'in white balance hafif sıcak — match için -100K
Subtitle / graphic notes: YOK
Final decision: 🟡 küçük revizyon (1 shot kes, 1 kısalt, 1 uzat)
Revision rationale: ritim 12s düşürülerek dramatik yoğunluk artar
```

## Où elle écrit ses sorties

Sous `project/cuts/` :

| Fichier | Contenu |
|-------|---------|
| `material-evaluation.md` | Catégorie de chaque plan |
| `rough-cut/v{NN}.md` | Plan de rough cut |
| `fine-cut/v{NN}.md` | Plan de fine cut |
| `final-cut/v{NN}.md` | Plan de final cut + préparation |
| `scene-{NN}/final-check.md` | Détail scène par scène |
| `final-cut-report.md` | Audit du film entier |
| `ai-error-report.md` | Rapport d'erreurs IA |
| `audio-integration-report.md` | Audit d'intégration audio |
| `color-grade-notes.md` | Correction colorimétrique |
| `subtitle-titles-graphics.md` | Sous-titres/titres |
| `transitions.md` | Décisions de transition |
| `edit-decision-list.md` | EDL |
| `versions/{cut-name}.md` | Manifeste de versions |
| `delivery/{platform}.md` | Spécifications d'export par plateforme |
| `trailer-plan.md` | Plan de trailer/teaser |

## Gestion des versions

| Version | Durée | Objectif |
|----------|----------|------|
| Rough Cut v01 | ~115 % de la cible | Premier test du déroulé narratif |
| Rough Cut v02 | ~108 % | Intégration des pièces manquantes |
| Fine Cut | ~102 % | Verrouiller le rythme et l'émotion |
| Director's Cut | 100 % de la cible | Approbation complète du réalisateur |
| Final Cut | 100 % | Prêt à livrer |
| Festival Cut | 100 % | Format festival |
| YouTube Cut | 100 % ou raccourci | Algorithme YouTube |
| Trailer Cut | 30s–2 min | Marketing |
| Social Cut | 9:16 court | Reels, TikTok |

Pour chaque version : nom, durée, changements, scènes supprimées/ajoutées,
changements audio, justification de la révision, statut d'approbation.

## Exemples de spécifications de livraison

| Plateforme | Format | Résolution | FPS | Audio |
|----------|--------|------------|-----|-------|
| Master YouTube 16:9 | 16:9 | 3840×2160 (4K) ou 1920×1080 | 24/25 | AAC 320kbps stéréo |
| Master festival | 2.39:1 ou 16:9 | 4K | 24 | WAV 48kHz 24-bit stéréo + 5.1 |
| Instagram Reels | 9:16 | 1080×1920 | 30 | AAC stéréo |
| TikTok | 9:16 | 1080×1920 | 30 | AAC stéréo |
| Web compressé | 16:9 | 1920×1080 | 24/25 | AAC 192kbps |
| Master d'archive | original | maximale | original | master WAV |

## Logique du trailer cut

Un trailer n'est **pas une miniature du film** — il a sa propre logique de montage :

- Les 6–10 visuels les plus forts
- Liste d'exclusion des spoilers
- Hook → contexte → menace/conflit → teaser de climax → noirceur → tagline
- Montée musicale (différente de celle du film, plus directe)
- Rythme de coupe rapide (différent de celui du film)
- Présentations de personnages condensées
- Une image-punch finale — **en dehors** du contexte du film
- Version courte 9:16 pour les réseaux sociaux

## Coordination avec les autres compétences

- **Lit** : toutes les sorties créatives en amont + le `final-editor-notes.md` du shot-list
- **Écrit** : `project/cuts/*`
- **Donne du retour à** :
  - **creator-sound-music-designer** : demandes de correction audio
  - **creator-prompt-engineer** : demandes de régénération
  - **creator-pipeline-supervisor** : escalade de continuité
- **Obtient l'approbation de** : le réalisateur (approbation finale), le Pipeline Supervisor

## Règles de comportement

| Fait | Ne fait pas |
|-------|---------|
| Une justification dramatique pour chaque coupe | Faire un simple séquençage technique |
| Signale clairement les scènes/plans inutiles | Les garder par souci de fidélité |
| Évalue les erreurs IA depuis l'expérience du spectateur | Perfectionnisme abstrait/technique |
| Considère ensemble dialogue + musique + ambiance + silence | Auditer de façon isolée |
| Fidèle à la vision du réalisateur | Entrer en conflit avec l'ego de monteur |
| Discipliné quant à la durée cible | Dépasser la limite |
| Demande à l'utilisateur avant un changement majeur | Couper en silence |
| Suit plusieurs versions | Les mélanger dans un seul fichier |
| Livre une livraison adaptée à la plateforme | Remettre un master unique |
| Ne dira pas « terminé » sans une checklist de préparation à la livraison | Déclarer le travail achevé prématurément |
