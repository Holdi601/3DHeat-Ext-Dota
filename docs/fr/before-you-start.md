---
title: "Avant de commencer"
nav_order: 1.5
lang: "fr"
source: before-you-start.md
source_hash: "8978ef7afccc"
nav_exclude: true
search_exclude: true
---
# Avant de commencer {#before-you-start}

Vous ne connaissez pas la ligne de commande ? Cette page vous mène de zéro
jusqu'à un premier lancement.
Cela prend une quinzaine de minutes, une seule fois.

## 1. Installer Python {#install-python}

Cet outil demande **Python 3.10 ou plus récent**.

- **Windows :** téléchargez Python sur [python.org/downloads](https://www.python.org/downloads/)
  et lancez l'installateur. Sur son premier écran, cochez **Add python.exe to PATH**,
  puis cliquez sur **Install Now**.
- **macOS et Linux :** Python 3 est souvent déjà là. Là où ces pages disent
  `python`, tapez `python3`.

## 2. Obtenir cet outil {#get-this-tool}

Ouvrez [github.com/Holdi601/3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota), cliquez sur
le bouton vert **Code**, puis sur **Download ZIP**, et décompressez-le dans un
dossier de votre choix. Si vous utilisez git : `git clone https://github.com/Holdi601/3DHeat-Ext-Dota`.

## 3. Obtenir la ligne de commande de Source2Viewer {#get-source2viewers-command-line}

Source2Viewer (ValveResourceFormat, licence MIT) lit les fichiers compressés de
Dota 2. Ouvrez sa [page des versions](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
téléchargez la version **CLI** pour votre système et décompressez
`Source2Viewer-CLI.exe` (sur macOS et Linux, `Source2Viewer-CLI`) dans le
dossier de l'étape 2. C'est suffisant : l'outil regarde à cet endroit. [Trouver les choses : list](list.md) dit où
il regarde d'autre.

## 4. Ouvrir un terminal dans ce dossier {#open-a-terminal-in-that-folder}

Un terminal est une fenêtre où vous tapez des commandes.

- **Windows :** ouvrez le dossier dans l'Explorateur, cliquez dans la barre
  d'adresse, tapez `powershell` et appuyez sur Entrée. Une fenêtre bleue ou noire
  s'ouvre, déjà dans ce dossier.
- **macOS :** ouvrez **Terminal**, tapez `cd ` (avec un espace), glissez le
  dossier dans la fenêtre et appuyez sur Entrée.

`cd` veut dire « changer de dossier » : `cd C:\Tools\3DHeat-Ext-Dota` va dans ce dossier.

## 5. Installer l'outil {#install-the-tool}

Tapez ceci et appuyez sur Entrée :

```bash
python -m pip install -e .
```

Vous devez voir, à la fin : `Successfully installed heat3d-ext-dota-...`.

## 6. Le lancer {#run-it}

```bash
heat3d-dota-maps list
```

Vous devez voir quelque chose comme :

```text
Dota 2 at C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota
  dota                         29.0 MB
  ...
Source2Viewer CLI at C:\Tools\3DHeat-Ext-Dota\Source2Viewer-CLI.exe
```

Suite : [Construire un niveau : level](level.md).

## Comment lire les commandes de ces pages {#how-to-read-the-commands-on-these-pages}

| Vous voyez | Cela veut dire |
|---|---|
| `<file.glb>` | un espace réservé : tapez votre propre valeur à la place, sans les `< >` |
| `[--detail UNITS]` | facultatif : omettez-le, ou tapez-le comme indiqué |
| `# a note` | un commentaire pour vous : ne le tapez pas |
| `"C:\My Files\x"` | mettez entre guillemets un chemin qui contient des espaces |

## Quand quelque chose ne va pas {#when-something-goes-wrong}

| Le message | Que faire |
|---|---|
| `'python' is not recognized` | Python n'est pas installé, ou la case PATH n'était pas cochée : réinstallez-le et cochez-la (ou tapez `py` au lieu de `python`). |
| `'heat3d-dota-maps' is not recognized` | Relancez l'étape 5 dans le dossier de l'outil, ou tapez `python -m heat3d_ext_dota` au lieu de `heat3d-dota-maps` : cela fait la même chose. |
| `No module named heat3d_ext_dota` | Vous n'êtes pas dans le dossier de l'outil, ou l'étape 5 a échoué : faites `cd` vers ce dossier et relancez l'étape 5. |
| `Dota 2 not found in any Steam library` | Installez Dota 2 par Steam, ou donnez son dossier : `--game "D:\Games\Steam\steamapps\common\dota 2 beta"`. |
| `Source2Viewer-CLI not found` | Faites l'étape 3, ou donnez son chemin : `--source2viewer <chemin vers Source2Viewer-CLI.exe>`. |
| tout le reste | Lisez la dernière ligne du message, puis ouvrez un ticket (issue) sur GitHub avec cette ligne. |

Chaque commande se termine aussi par un **code de sortie** : 0 veut dire que
cela a marché, 2 que Dota 2, la carte ou Source2Viewer n'a pas été trouvé, 1 que la
lecture a échoué. Pour le voir, tapez `echo $LASTEXITCODE` dans PowerShell, ou
`echo $?` sur macOS et Linux.
