---
title: "Construire un niveau : level"
nav_order: 3
lang: "fr"
source: level.md
source_hash: "6af25f0a3539"
nav_exclude: true
search_exclude: true
---
# Construire un niveau : `level` {#building-a-level-level}

```bash
heat3d-dota-maps level [<map>] -o <file.glb> [--game FOLDER] [--source2viewer EXE] [--detail UNITS]
```

écrit la carte de Dota 2 comme géométrie de niveau pour le visualiseur 3DHeat : le sol, les
falaises, l'eau, chaque arbre et les bâtiments, dans le repère et les unités où
sont dessinées les [tables de replays Dota 2](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html)
du 3DHeat Watcher. Code :
[`heat3d_ext_dota/dota_map.py`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/heat3d_ext_dota/dota_map.py).

| Option | Rôle |
|---|---|
| `<map>` | le nom de la carte tel que [`list`](list.md) l'affiche (par défaut `dota`, la carte normale), ou le chemin du `.vpk` d'une carte |
| `-o`, `--out FILE` | le `.glb` à écrire (obligatoire) ; son dossier est créé s'il manque |
| `--game FOLDER` | le dossier `dota 2 beta` ou son dossier `game\dota`, quand Dota 2 n'est dans aucune bibliothèque Steam |
| `--source2viewer EXE` | la ligne de commande de Source2Viewer, quand elle n'est pas trouvée toute seule ([list](list.md) dit où elle est cherchée) |
| `--detail UNITS` | la taille, en unités du jeu, des cellules de regroupement des sommets des bâtiments (par défaut 8 ; 0 garde chaque triangle) |

## Le charger dans le visualiseur {#loading-it-in-the-viewer}

Chargez le `.glb` dans le panneau **Arrière-plan / niveau** du visualiseur (**Modèle 3D…**)
sous une table Dota, et la chaleur des héros se pose sur les voies, celle des tours
sur leurs tours. Le visualiseur reconnaît le fichier à ses parties et le garde dans sa
[bibliothèque de niveaux](https://holdi601.github.io/3DHeat/level-library.html) ; à partir de là,
son bouton **Carte de Dota 2** charge cette carte 3D au lieu du dessin d'OpenDota.

Rien du jeu n'est dans cet outil ni téléchargé par lui : la carte sort de votre propre
installation, et le fichier écrit reste sur votre machine ([Conditions](terms.md)).

## Comment elle est faite {#how-it-is-made}

1. **Le maillage de collision.** Source2Viewer exporte depuis `maps/<map>.vpk` le
   fichier `maps/<map>/world_physics.vmdl_c` en glTF. Ses groupes sont nommés
   par surface. Les groupes nommés `clip` (les murs invisibles) ou `sky` sont
   retirés. Les groupes nommés `water`, `slime` ou `window` sont de **l'eau** : la rivière
   et les mares sont `water_slime`, les ruisseaux étroits de la jungle sont
   `window` ; sur un replay, les héros se tiennent 10 à 16 unités sous la première et
   quelques unités sous la seconde. Seules leurs faces orientées vers le haut sont gardées. Le reste est
   le terrain, découpé face par face : une face dont la normale pointe vers le haut
   d'au moins 0,7 (pentes jusqu'à environ 45 degrés) est du **sol**, le reste - les
   faces de falaise, les murs de la carte - est de la **structure**.
2. **Les entités.** Source2Viewer décompile les blocs d'entités de la carte
   (`maps/<map>/entities/*.vents_c`) en texte : des blocs introduits par `====<n>====`,
   une paire `clé valeur` par ligne. Les blocs utilisés sont `default_ents` et chaque
   calque du monde `info_world_layer` qui y apparaît au départ (drapeau de
   spawn 1) - les deux bases. Les calques qui commencent cachés contiennent ce qui apparaît
   quand une base tombe, et sont laissés de côté.
3. **Ce qui est dessiné.** Les arbres (`ent_dota_tree`) et les bâtiments : tours,
   casernes, les Anciens (`npc_dota_fort`), les bâtiments de remplissage (`npc_dota_building`),
   avant-postes, fontaines, sanctuaires de sagesse, bassins de lotus, portes jumelles,
   veilleurs (`npc_dota_lantern`) et réserves d'objets neutres. Les boutiques (un marchand est
   un personnage), le panthéon, les bannières, les lumières et les particules ne le sont pas.
4. **Les modèles.** Chaque modèle nommé par ces entités est exporté depuis
   `game\dota\pak01_dir.vpk` en une seule exécution de Source2Viewer. Les maillages d'un
   modèle qui sont un autre état de la même chose - la souche d'un arbre coupé, le gros plan
   affiché dans l'inspecteur, les gravats - sont laissés de côté d'après leur nom (`stump`,
   `inspector`, `destruction`).
5. **Les bâtiments** sont le maillage propre de leur modèle, allégé par **regroupement
   de sommets** : chaque point se déplace vers la moyenne des points de son cube de taille
   `--detail` (par défaut 8 unités, environ un tiers de la largeur d'un héros), et les triangles
   qui s'effondrent ou se répètent disparaissent. 0 garde chaque triangle.
6. **Les arbres** sont le contour de chaque modèle sous forme de petit solide tourné : sa hauteur en cinq
   bandes, chacune un anneau à six côtés aussi large que la plupart des points du modèle à cette
   hauteur (le 90e percentile de leur distance à l'axe du tronc), fermé en bas et pointu en
   haut - 60 triangles, la hauteur et la largeur réelles du modèle. Un pin sort en cône, un chêne en
   boule sur un tronc. Les vrais maillages pèseraient environ dix fois plus sur plus de 2 000 arbres.
7. **Placés** comme le jeu les place : mis à l'échelle par `scales`, tournés par `angles`
   (tangage, lacet, roulis de Source en degrés), déplacés vers `origin`.
8. **Dans le repère du visualiseur.** Source2Viewer écrit du glTF en mètres, Y vers le haut :
   (Y, Z, X) du jeu multiplié par 0,0254. C'est annulé, et chaque point est écrit
   (X, Z, -Y) du jeu : Y vers le haut, le Y du jeu inversé - le repère dans lequel les
   tables Dota sont dessinées grâce à leurs indices `heat3d` (`up: z`, `flipY: true`, échelle 1).
   Une rotation, pas un miroir.

## Le fichier {#the-file}

Un glTF 2.0 binaire comme celui de l'outil 3DHeat CS2 (voir sa page sur l'export des cartes) : un
nœud et un maillage par partie à la racine, sans transformations, à ombrage plat (un sommet
par coin de triangle portant la normale de son triangle), indices `uint32`, sans
matériaux, textures ni UV, `asset.generator` `heat3d_ext_dota`, unités du jeu.

| Partie | Contenu |
|---|---|
| `ground:terrain` | le sol où l'on peut marcher |
| `structure:terrain` | les faces de falaise et les murs de la carte |
| `water:water_slime`, `water:window` | la rivière et les mares ; les ruisseaux de la jungle |
| `structure:tree` | chaque arbre debout au départ |
| `structure:tower`, `structure:barracks`, `structure:ancient`, `structure:filler`, `structure:outpost`, `structure:fountain`, `structure:shrine`, `structure:lotus_pool`, `structure:twin_gate`, `structure:watcher`, `structure:neutral_stash` | les bâtiments, par genre |

Le préfixe `ground:` / `structure:` / `water:` est la façon dont tous les exporteurs de
niveaux 3DHeat disent au visualiseur ce qu'est une partie ; elle les croit sur parole. Comme les
unités sont celles du jeu (environ un pouce chacune), un autre visualiseur glTF montre la carte
environ 39 fois trop grande ; dans 3DHeat, elle se trouve exactement sous la table.

Ce qu'il affiche, sur un exemple d'exécution (les chiffres dépendent de la version de la carte) :

```text
reading dota.vpk: collision mesh and entities
reading 30 models from pak01_dir.vpk
dota.glb: dota, 700,000 triangles (230,000 ground) in 16 parts; 2,400 trees, 70 buildings
```

Les deux premières lignes vont dans le flux d'erreurs, la dernière dans la sortie. Un modèle que
Source2Viewer n'a pas trouvé est laissé de côté et nommé à la fin de la dernière ligne
(`; 1 model(s) not found, left out: ...`). Les erreurs affichent `heat3d-dota-maps: <pourquoi>` : Dota 2, la carte ou Source2Viewer
introuvable sortent avec le code 2, un échec de Source2Viewer avec le code 1.

## Comment elle a été vérifiée {#how-it-was-checked}

Sur le replay d'un match public converti par le 3DHeat Watcher (patch 7.40) et la carte du
jeu installé :

- chaque échantillon de position d'un héros pointe tout droit vers la face de sol la plus haute
  à au plus 64 unités au-dessus de ses pieds, trouve du sol, la hauteur médiane au-dessus est de
  0 unité, et 99,5 % sont à moins de 16 unités ; avec la carte en miroir (Y non
  inversé), seule environ la moitié trouve du sol, et les autres flottent ou s'enfoncent
  de la hauteur d'une falaise ;
- les 22 tours, 12 casernes, 2 Anciens, 14 bâtiments de remplissage, 2 avant-postes, 2 fontaines
  et 10 veilleurs que la table des unités du replay place se tiennent sur les entités de la
  carte du même genre, à 0,02 unité près, horizontalement et en hauteur ;
- le pied de chaque arbre est sur le sol.

Les tests ([`tests/test_dota_map.py`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/tests/test_dota_map.py)) vérifient le lecteur des blocs, les repères, la
découpe du terrain, les contours d'arbres et le regroupement, le placement, et l'export complet
avec Source2Viewer remplacé par un simulacre - sur des données inventées seulement.

## Ce qu'il ne fait pas {#what-it-does-not-do}

- Pas de textures ni de couleurs : le visualiseur ombre le niveau à sa façon.
- Pas d'arbres coupés ni de bâtiments détruits pendant un match : la carte telle qu'elle commence.
- Les parties événementielles et les cartes personnalisées ne sont pas testées ; leurs classes d'entités peuvent différer.
- Les accessoires qui ne servent qu'à décorer (rochers, clôtures, bannières) n'y figurent que
  dans la mesure où ils font partie du maillage de collision.
