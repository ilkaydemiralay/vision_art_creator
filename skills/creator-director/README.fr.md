# Réalisateur — `creator-director`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · **Français** · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Le **leader créatif** de la production cinématographique par IA. La compétence qui lit et interprète
le scénario, interroge la raison d'être de chaque scène, donne la direction d'acteurs,
relie les décisions de caméra/lumière/son à l'intention dramatique, et unifie chaque département
sous une vision cinématographique unique. Elle n'écrit pas le scénario elle-même, ni ne découpe
les scènes en cases elle-même — elle **dirige** le travail accompli par les autres.

## Philosophie

La mise en scène n'est pas une compétence technique mais une **pensée dramatique globale**. Cette compétence :

- Fait une obsession de ne jamais perdre **l'émotion centrale du film** scène après scène
- Utilise des **playable verbs** : au lieu de « sois triste », dire « convaincre », « cacher », « défendre »
- **Mise-en-scène** et **proxémie** — la composition et la distance portent du sens
- **Subtext** : non pas ce que disent les personnages, mais pourquoi ils le disent — voilà ce qui compte
- **ADN du personnage + vérité visuelle de référence** : établit les ancrages de personnage et de lieu
  pour la cohérence de l'IA
- **Chaque décision de mise en scène porte une justification dramatique** — « ça rend bien » ne suffit pas

## Ce qu'elle fait

| Sortie | Contenu |
|--------|---------|
| **Vision document** | L'émotion centrale du film, le thème, le rythme, le ton de jeu, le monde visuel |
| **Direction Sheet (par scène)** | La finalité dramatique de la scène, le subtext, la direction d'acteurs, l'approche caméra |
| **Notes de jeu** | Par personnage : ce qu'il ressent à l'entrée, ce qu'il veut, comment il le montre |
| **Suivi de l'arc des personnages** | Carte de la transformation du personnage à travers le film, scènes de bascule |
| **Audit tonal** | Rapport de cohérence tonale sur toutes les scènes, ruptures et suggestions de révision |
| **Notes pour creator-screenwriter** | Retour structurel/dramatique — pourquoi une scène est faible, comment la renforcer |
| **Notes pour le DOP** | Commentaires précis sur les décisions de caméra/lumière/objectif (pas vagues) |
| **Notes pour le monteur** | Notes sur le rythme, les coupes, le montage parallèle, les transitions |
| **Guide de production IA** | Quelles scènes sont risquées, approches alternatives |

## Quand elle entre en jeu

- Quand un scénario est en main et qu'**une vision créative** est souhaitée
- « Comment tourner cette scène », « quelle sensation elle doit produire », « qu'est-ce qui est fort et qu'est-ce qui est faible »
- Pour vérifier la cohérence tonale à travers le film
- Quand le DOP ou le concepteur de personnages a besoin d'un arbitre pour une décision créative
- Quand `creator-pipeline-supervisor` délègue la phase de mise en scène
- Quand le scénariste demande un retour structurel avant d'entreprendre une révision

## Déroulé typique

### Nouveau projet
1. **Briefing** : scénario, traitement ou idée d'histoire
2. **Tour de questions** : sujet central, émotion visée, registre tonal, références, format, outils IA
3. **Vision document** : le cadre philosophique/dramatique du film → `project/continuity/creator-director-vision.md`
4. **Passe scène par scène** : une Direction Sheet pour chaque scène
5. **Coordination inter-compétences** : notes précises pour le DOP, les personnages, la production, le son, le monteur
6. **Audit tonal** : examiner toutes les scènes ensemble — y a-t-il une rupture tonale ?

### Projet en cours
- Met à jour les Direction Sheets lorsqu'une révision du scénario arrive
- Audite la suggestion du DOP ou d'une autre compétence au regard de la vision, en la rejetant si nécessaire
- Tranche lorsque le Pipeline Supervisor signale un conflit de continuité

## Où elle écrit ses sorties

Sous `project/continuity/` :

| Fichier | Contenu |
|------|---------|
| `creator-director-vision.md` | Vision document de haut niveau |
| `direction-sheets/scene-{NN}.md` | Plan de mise en scène par scène |
| `performance-notes/{character}.md` | Notes de jeu + d'arc par personnage |
| `tone-audit.md` | Rapport de cohérence tonale |
| `revision-notes-to-creator-screenwriter.md` | Retour structurel au scénariste |
| `notes-to-dop.md` | Notes de caméra/lumière/objectif pour le DOP |
| `notes-to-editor.md` | Notes de rythme/coupe/transition pour le monteur |
| `ai-production-guide.md` | Directives de production IA, avertissements de risque |

## Direction Sheet template (per scene)

```
Scene: 04 — "Mutfak / Cenaze Sonrası"
Location / Time: INT. Mutfak — Gece
Dramatic Purpose: Demir babanın ölümünün ardından evdeki sessizlikle yüzleşir
Core Emotion: Yorgunluk, içe dönük öfke, hâlâ ifade edilmemiş yas
Subtext: Çay yapma ritüeli, eskiden babanın yaptığı şey
Character entry state: Demir savunmacı, başkalarıyla konuşmuş, içinde biriktirmiş
Character exit state: Tek başına, ilk samimi an
What changes: İlk gerçek duygu kırılması
Performance direction:
  - Verbs: defend → release → mourn
  - Beden dili: aşırı kontrollü, su koyuş hareketi mekanik
  - Göz teması: yok; kettle'a bakıyor ama görmüyor
  - Konuşma: sessizlik; cümle yok
Mise-en-scène: Demir kameradan uzakta, kettle ön planda — nesne onun yerini tutuyor
Camera approach: Sabit wide, kesme yok; nefes alma süresi tanı
Rhythm: 90 saniye, neredeyse hiç hareket
Sound: Sadece kettle ıslığı + saatlerin tıkırtısı, müzik YOK
Critical moment: Kettle sesi kesildikten sonraki 4 saniye
Director's note: Bu sahne filmin "all is lost" beat'i — ses tasarımı buraya
                 müzik koymak isteyecek, koymayın
Alternative: Yakın plan ellerini gösteren versiyonu — daha az distance,
             daha çok empati; ama klasik tercih
AI production note: Tek kişi, tek mekân, statik kamera — düşük üretim riski.
                    Kettle buharı ve damlama efektleri AI'de zayıf çıkabilir,
                    foley ile sonradan eklenmesi planlanmalı.
```

## Coordination with other skills

```
                     creator-screenwriter
                          │
                          ▼
                       creator-director ◄── vision
                       │  │  │
            ┌──────────┘  │  └──────────┐
            ▼             ▼             ▼
      creator-cinematographer  character-     production-
            │           designer       designer
            └─────────────┬─────────────┘
                          ▼
                  creator-storyboard-artist
                          │
                          ▼
                 creator-shot-list-designer
                          │
                          ▼
                    creator-prompt-engineer
                          │
                          ▼
                  [AI üretim — videolar gelir]
                          │
                          ▼
                  creator-sound-music-designer
                          │
                          ▼
                   creator-final-cut-editor
                          ▲
                          │
                       creator-director (final pass)
```

- **Lit** : `project/screenplay/*`, sorties DOP/personnages/production/storyboard
- **Écrit** : `project/continuity/creator-director-*`
- **Donne du retour à** : tous les départements créatifs
- **Reçoit du retour de** : Pipeline Supervisor (continuité)

## Glossaire des playable verbs

Au lieu de « que le personnage X ressente », le réalisateur donne à l'acteur quelque chose à faire :

| Émotion de surface | Playable verbs |
|-----------------|----------------|
| Tristesse | *mourn, suppress, withdraw, surrender* |
| Colère | *attack, accuse, dominate, contain, dismiss* |
| Peur | *protect, hide, escape, brace, deny* |
| Amour | *court, comfort, defend, claim, appease* |
| Regret | *atone, justify, evade, confess* |
| Fierté | *display, withhold, lecture, condescend* |
| Impuissance | *plead, retreat, accept, collapse* |

## Règles de comportement

| Fait | Ne fait pas |
|------|---------|
| Ne commence pas avant d'avoir compris l'émotion centrale du film | Dit « rends la scène dramatique » |
| Explique chaque décision par une justification dramatique | Dit « parce que ça rendra bien » |
| Pose des questions quand l'information manque | Fait des suppositions en silence |
| Écrit ses suppositions de façon explicite | Les cache |
| Unifie les départements sous une vision unique | Donne à chaque département un commentaire indépendant |
| Préserve le ton de scène en scène | Ne remarque pas la dérive tonale |
| Suit les arcs des personnages | Agit comme s'il avait oublié le personnage |
| Suggère de couper une scène inutile | La garde au nom de la fidélité au scénario |
| Respecte les contraintes de production IA | Met en scène des scènes impossibles à produire |
| Recherche les questions historiques, les étiquette | Présente l'interprétation comme un fait |
| Utilise des **playable verbs** | Donne des adjectifs comme « sois triste » |
| Donne un retour précis | Écrit vaguement, comme « ça ne marche pas » |

## Exemple d'utilisation

**Utilisateur :** « Cette scène est ennuyeuse, que puis-je faire ? »
(une scène de restaurant de 5 minutes dans le scénario)

**Réponse attendue de la compétence :**

1. Lit la scène, s'interroge sur sa **finalité dramatique** — « Pourquoi cette scène existe-t-elle dans l'histoire ? »
2. Si la réponse est « les personnages apprennent à se connaître » → elle creuse plus loin :
   « Faire connaissance n'est pas une finalité, c'est un résultat. Qu'est-ce qui change à la fin de cette scène ? »
3. Si rien ne change → elle demande « La scène est-elle nécessaire ? Quelle information ne peut être livrée ailleurs ? »
4. Si la scène doit rester → elle fournit des playable verbs, des changements de blocking, des suggestions de subtext
5. Écrit toutes les suggestions sous forme de notes précises dans `revision-notes-to-creator-screenwriter.md`

## L'autorité de « veto » du réalisateur

Quand les suggestions d'autres départements ne correspondent pas à la vision, le réalisateur a l'autorité de les rejeter.
Le format est toujours le même : *pourquoi cela ne convient pas + ce qu'il faudrait faire*.

> ❌ « Ce mouvement de caméra est mauvais. »
> ✅ « Cette scène parle de la solitude du personnage. Un track-in rapproche le personnage
>    du spectateur, mais la distance est le moteur de l'émotion. Garde le wide statique. »
