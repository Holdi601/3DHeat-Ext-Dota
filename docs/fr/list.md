---
title: "Trouver les choses : list"
nav_order: 2
lang: "fr"
source: list.md
source_hash: "a03dec416591"
nav_exclude: true
search_exclude: true
---
# Trouver les choses : `list` {#finding-things-list}

```bash
heat3d-dota-maps list [--game FOLDER] [--source2viewer EXE]
```

affiche où Dota 2 est installé, chaque carte dans son dossier `game\dota\maps` avec
sa taille, et où se trouve la ligne de commande de Source2Viewer. Lancez-la d'abord : quand elle se termine par
`Source2Viewer CLI at ...` et sort avec le code 0, [`level`](level.md) a tout ce qu'il lui faut.

```text
Dota 2 at C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota
  dota                         29.0 MB
  dota_winter                  23.7 MB
  ...
Source2Viewer CLI at C:\Tools\3DHeat-Ext-Dota\Source2Viewer-CLI.exe
```

`dota` est la carte normale ; les autres sont des versions plus anciennes, des cartes
saisonnières et d'événements, et des tutoriels (seule `dota` a été vérifiée avec des replays).

## Où l'on cherche Dota 2 {#where-dota-2-is-looked-for}

D'abord `--game` : le dossier `dota 2 beta` ou son dossier `game\dota`. Sans lui,
`steamapps\common\dota 2 beta\game\dota` dans chaque bibliothèque Steam : le dossier propre
de Steam (depuis le registre, sinon `C:\Program Files (x86)\Steam`,
`~/.steam/steam` ou `~/.local/share/Steam`) et chaque bibliothèque que son
`steamapps\libraryfolders.vdf` liste. La première installation trouvée est utilisée.

## Où l'on cherche la ligne de commande de Source2Viewer {#where-source2viewers-cli-is-looked-for}

1. `--source2viewer <chemin>` ;
2. la variable d'environnement `HEAT3D_SOURCE2VIEWER` ;
3. `Source2Viewer-CLI` ou `Source2Viewer-CLI.exe` dans le `PATH` ;
4. `Source2Viewer-CLI.exe` (ou `Source2Viewer-CLI`) dans le dossier courant, puis
   dans le dossier propre à cet outil.

L'outil 3DHeat CS2 cherche aussi aux trois premiers endroits, donc une seule copie sert
aux deux. Téléchargement : [versions de ValveResourceFormat](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
la version **CLI** pour votre système.

## Messages et code de sortie {#messages-and-exit-status}

| Message | Code | Signification |
|---|---|---|
| `heat3d-dota-maps: Dota 2 not found in any Steam library: ...` | 2 | installez Dota 2 par Steam, ou donnez `--game` |
| `heat3d-dota-maps: <folder> is not a Dota 2 folder ...` | 2 | `--game` pointe vers un endroit sans `game\dota\gameinfo.gi` |
| `heat3d-dota-maps: Source2Viewer-CLI not found: ...` | 2 | les cartes sont tout de même listées ; obtenez la CLI comme indiqué plus haut |
| `heat3d-dota-maps: --source2viewer <path>: no such file` | 2 | le chemin donné est faux |
