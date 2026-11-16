---
title: "Accueil"
nav_order: 1
lang: "fr"
source: index.md
source_hash: "a1d480a07830"
nav_exclude: true
search_exclude: true
permalink: /fr/
---
# 3DHeat Dota {#dheat-dota}

**Qu'est-ce que c'est ?** Cet outil transforme la carte de Dota 2, lue dans
**votre propre installation**, en un niveau 3D : un modèle de la carte au-dessus
duquel vous pouvez voler, pour le visualiseur [3DHeat](https://github.com/Holdi601/3DHeat)
([documentation](https://holdi601.github.io/3DHeat/)) : le sol, les falaises,
la rivière, chaque arbre et les bâtiments.

**À quoi cela sert-il ?** À voir des parties de Dota 2 - les tables de replays
que le [3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html)
écrit - sur la carte du jeu, en 3D, au lieu d'un dessin à plat.

**Exemple :** `heat3d-dota-maps level -o levels/dota.glb` -> `levels/dota.glb`,
dans les unités et les axes des tables Dota du Watcher : rien à placer ni à
mettre à l'échelle dans le visualiseur.

## Démarrage rapide {#quick-start}

Vous ne connaissez pas la ligne de commande ? Lisez d'abord [Avant de commencer](before-you-start.md).
Il vous faut Python 3.10 ou plus récent, Dota 2 installé par Steam, et la
ligne de commande de Source2Viewer (un téléchargement gratuit sous licence MIT, voir
[Trouver les choses : list](list.md)). Lancez ces commandes dans le dossier où vous avez cloné ou décompressé l'outil :

```bash
python -m pip install -e .                  # installe la commande heat3d-dota-maps
heat3d-dota-maps list                       # où sont Dota 2 et Source2Viewer, les cartes installées
heat3d-dota-maps level -o levels/dota.glb   # la carte normale comme niveau
```

Avec `list`, vous devez voir `Dota 2 at ...`, une ligne par carte, et `Source2Viewer CLI at ...` ;
`level` se termine par une ligne comme
`levels/dota.glb: dota, 700,000 triangles ... 2,400 trees, 70 buildings`.
Chargez ensuite `levels/dota.glb` dans le panneau **Arrière-plan / niveau** du visualiseur, avec **Modèle 3D…** : le visualiseur le garde dans sa bibliothèque
de niveaux, et son bouton **Carte de Dota 2** le charge à partir de là ([Construire un niveau](level.md#loading-it-in-the-viewer)).

Le niveau est construit à partir des fichiers du jeu : il reste **sur votre
machine**, pour le voir, pas pour le partager ou le publier ([Conditions](terms.md)).

## Pages {#pages}

| Page | Ce qu'elle couvre |
|---|---|
| [Avant de commencer](before-you-start.md) | Python, Source2Viewer, un terminal, un premier lancement |
| [Trouver les choses : list](list.md) | où sont trouvés Dota 2 et la ligne de commande de Source2Viewer, ce qu'affiche `list` |
| [Construire un niveau : level](level.md) | chaque option, comment le niveau est fait, ses parties, comment il a été vérifié |
| [Conditions et licence](terms.md) | la carte de Valve, la licence de Source2Viewer, pourquoi c'est un paquet séparé |
| [Référence des commandes](../cli-reference.md) | chaque option, générée à partir du code |
| [Maintenance de ces documents](maintaining.md) | la liste de contrôle des versions |

## Liens utiles {#related}

- Le visualiseur 3DHeat : [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentation sur [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Les tables de replays Dota 2 sous lesquelles ces niveaux se placent : le
  [3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html).
- Les cartes de Counter-Strike 2 avec la même ligne de commande Source2Viewer :
  [3DHeat CS2](https://holdi601.github.io/3DHeat-CS2/).

## Les outils 3DHeat {#the-3dheat-tools}

| Outil | Ce qu'il fait | Code | Documentation |
|---|---|---|---|
| visualiseur 3DHeat | montre les données : cartes de chaleur, analyse de course, revue de match | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | niveaux et parcours tirés des fichiers d'un jeu | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | télémétrie de tours, et niveaux reconstruits à partir de vidéos de jeu | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin pour l'éditeur Unreal : un niveau en un seul `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | démos et cartes de Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | enregistre ce que les jeux publient pendant que vous jouez | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | replays de War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | replays de World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | replays de World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | démos de serveurs Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | cartes de DCS World en niveaux 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | cartes d'IL-2 Sturmovik en niveaux 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | la carte de Dota 2 en niveau 3D | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | replays de Dota 2 | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | replays de League of Legends et VALORANT (ce qu'ils contiennent sans chiffrement) | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | parcours, courses et voitures de Forza tirés de votre propre installation | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [docs](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | niveaux de Battlefield (Frostbite) en niveaux 3D | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [docs](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | parcours de BeamNG.drive | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [docs](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | étapes d'Assetto Corsa Rally en parcours | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [docs](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | mondes d'Arma Reforger (Enfusion) en niveaux 3D | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [docs](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | replays de matchs de Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [docs](https://holdi601.github.io/3DHeat-Ext-R6/) |
