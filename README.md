# 3DHeat Dota: the Dota 2 map as a 3D level

**What is it?** This tool turns the Dota 2 map, read from your own Dota 2
install, into a 3D model you can fly over in the
[3DHeat](https://github.com/Holdi601/3DHeat) viewer: the ground, the cliffs,
the river, every tree and the buildings.

**Why would I use it?** To see Dota 2 matches - the replay tables the
[3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html)
writes - on the game's own map in 3D, instead of a flat drawing.

**Example:** `heat3d-dota-maps level -o levels/dota.glb` -> `levels/dota.glb`,
in the units and axes of the Watcher's Dota tables.

**Documentation:** [holdi601.github.io/3DHeat-Ext-Dota](https://holdi601.github.io/3DHeat-Ext-Dota/), a page per
command with step-by-step use and example output. Part of
[3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)).

This tool is kept outside the 3DHeat tools on purpose: it reads Valve's game
files. If it ever has to go, nothing else goes with it. The levels it writes
stay on your machine.

## Install

New to the command line? Read [Before you start](https://holdi601.github.io/3DHeat-Ext-Dota/before-you-start.html) first.

1. Install Python 3.10 or later, and Dota 2 through Steam.
2. `git clone https://github.com/Holdi601/3DHeat-Ext-Dota` (or download the
   ZIP) and open a terminal in that folder.
3. Download Source2Viewer's command line (ValveResourceFormat, MIT): the **CLI**
   build for your system from its
   [releases](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
   and unzip `Source2Viewer-CLI.exe` into this folder (or put it on `PATH`, or
   set `HEAT3D_SOURCE2VIEWER` to it).
4. Install the command and check that everything is found:

```bash
python -m pip install -e .        # installs the heat3d-dota-maps command
heat3d-dota-maps list             # where Dota 2 and Source2Viewer are, the maps installed
```

You should see `Dota 2 at ...`, a line per map, and `Source2Viewer CLI at ...`.

## Commands

| Command | Does | Page |
|---|---|---|
| `list [--game FOLDER] [--source2viewer EXE]` | where Dota 2 and Source2Viewer's CLI are, and the maps installed | [list](https://holdi601.github.io/3DHeat-Ext-Dota/list.html) |
| `level [map] -o <file.glb>` | the map as a `.glb` level: ground, cliffs, water, trees, buildings | [level](https://holdi601.github.io/3DHeat-Ext-Dota/level.html) |

```bash
heat3d-dota-maps level -o levels/dota.glb                # the normal map
heat3d-dota-maps level dota -o levels/dota.glb --detail 0  # buildings with every triangle
```

| `level` option | Does |
|---|---|
| `-o`, `--out FILE` | the `.glb` to write (required) |
| `--game FOLDER` | the `dota 2 beta` folder, when Dota 2 is in no Steam library (also for `list`) |
| `--source2viewer EXE` | Source2Viewer's CLI, when it is not found on its own (also for `list`) |
| `--detail UNITS` | the buildings' vertex clustering cell in game units (default 8; 0 keeps every triangle) |

Exit status: 0 done; 1 reading failed; 2 Dota 2, the map or Source2Viewer not
found (the message says which, and what to do). Every option, as the program
prints it: [Command reference](https://holdi601.github.io/3DHeat-Ext-Dota/cli-reference.html).

## What comes out, and loading it

One glTF binary: a node per part, named `ground:terrain`, `structure:terrain`
(cliffs), `water:<surface>`, `structure:tree` and `structure:<building kind>`,
in the game's units with the Watcher's Dota tables' axes. Load it in the
viewer's **Background / level** panel with **3D model…** under a Dota table: the
viewer recognises the map by its parts, keeps it in its level library, and its
**Dota 2 map** button loads it from then on.
[The level, part by part](https://holdi601.github.io/3DHeat-Ext-Dota/level.html).

The 3DHeat Watcher's `dota-map` command runs this tool when it is installed,
so `python -m heat3d_watch dota-map -o dota.glb` does the same.

## Terms

Dota 2 and its map belong to Valve, who do not endorse this project. Nothing of
the game is in this repository or downloaded by it; the map comes out of your
own install, and the level it writes is yours to view, not to share
([Terms and licence](https://holdi601.github.io/3DHeat-Ext-Dota/terms.html)).

## Tests

```bash
python -m pip install -e .[test]
python -m pytest
```

On made-up data only, with Source2Viewer played by a stand-in.

## Licence

MIT ([`LICENSE`](LICENSE)). Third-party software it uses or runs: [`LICENSES.md`](LICENSES.md).
