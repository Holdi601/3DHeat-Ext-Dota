---
title: "Trovare le cose: list"
nav_order: 2
lang: "it"
source: list.md
source_hash: "a03dec416591"
nav_exclude: true
search_exclude: true
---
# Trovare le cose: `list` {#finding-things-list}

```bash
heat3d-dota-maps list [--game FOLDER] [--source2viewer EXE]
```

stampa dove è installato Dota 2, ogni mappa nella sua cartella `game\dota\maps` con la sua
dimensione, e dove si trova la CLI di Source2Viewer. Eseguilo per primo: quando termina con
`Source2Viewer CLI at ...` e si chiude con 0, [`level`](level.md) ha tutto ciò che gli serve.

```text
Dota 2 at C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota
  dota                         29.0 MB
  dota_winter                  23.7 MB
  ...
Source2Viewer CLI at C:\Tools\3DHeat-Ext-Dota\Source2Viewer-CLI.exe
```

`dota` è la mappa normale; le altre sono versioni precedenti, mappe stagionali ed evento e tutorial
(solo `dota` è stata verificata con i replay).

## Dove viene cercato Dota 2 {#where-dota-2-is-looked-for}

Prima `--game`: la cartella `dota 2 beta` o la sua cartella `game\dota`. Senza di essa,
`steamapps\common\dota 2 beta\game\dota` in ogni libreria Steam: la cartella di Steam stessa (dal
registro, altrimenti `C:\Program Files (x86)\Steam`, `~/.steam/steam` o `~/.local/share/Steam`) e
ogni libreria elencata nel suo `steamapps\libraryfolders.vdf`. Viene usata la prima installazione trovata.

## Dove viene cercata la CLI di Source2Viewer {#where-source2viewers-cli-is-looked-for}

1. `--source2viewer <path>`;
2. la variabile d'ambiente `HEAT3D_SOURCE2VIEWER`;
3. `Source2Viewer-CLI` o `Source2Viewer-CLI.exe` nel `PATH`;
4. `Source2Viewer-CLI.exe` (o `Source2Viewer-CLI`) nella cartella corrente, poi nella
   cartella di questo strumento.

Anche lo strumento CS2 di 3DHeat cerca nei primi tre posti, quindi una sola copia serve a entrambi.
Download: [versioni di ValveResourceFormat](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
la versione **CLI** per il tuo sistema.

## Messaggi e stato di uscita {#messages-and-exit-status}

| Messaggio | Uscita | Significa |
|---|---|---|
| `heat3d-dota-maps: Dota 2 not found in any Steam library: ...` | 2 | installa Dota 2 tramite Steam, oppure indica `--game` |
| `heat3d-dota-maps: <folder> is not a Dota 2 folder ...` | 2 | `--game` punta a un posto senza `game\dota\gameinfo.gi` |
| `heat3d-dota-maps: Source2Viewer-CLI not found: ...` | 2 | le mappe sono comunque elencate; procurati la CLI come sopra |
| `heat3d-dota-maps: --source2viewer <path>: no such file` | 2 | il percorso indicato è sbagliato |
