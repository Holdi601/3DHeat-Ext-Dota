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

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn on
a rights holder's request - on its own, without affecting the viewer or the
other tools. The levels this tool writes stay on your machine.

## The standalone program

No Python needed: download the file for your system (Windows, Linux incl. Steam Deck, macOS) from the
[latest release](https://github.com/Holdi601/3DHeat-Ext-Dota/releases/latest), check it against `SHA256SUMS`,
unpack it and start `heat3d-dota-maps`. Its window finds your Dota 2 install, says what is missing (the game,
Source2Viewer-CLI - unzip it next to the program - and disk space), lists the maps that are new or changed since
the last export and exports the ones you pick into the 3DHeat levels folder (`dota/<map>.glb` with its layouts),
writes the catalogue and the model pack, and asks before it updates itself. `heat3d-dota-maps --help` lists its
commands (every command below runs through it too). The 3DHeat app's Extractors panel can install and update it
for you. See the [documentation](https://holdi601.github.io/3DHeat-Ext-Dota/#the-standalone-program-no-python-needed).

The window walks through four steps (find the game, choose, work, done) in the 3DHeat look, dark or light. On Windows the program opens only its window, with no console window; in a terminal it prints as usual, and `heat3d-dota-maps-cli.cmd` in the same folder makes the terminal wait for it and pass on its exit code.

## Quick start for new users

You need: Windows, [Python](https://www.python.org/downloads/) 3.10 or later
("Add python.exe to PATH" ticked in its installer), Dota 2 installed through
Steam, and Source2Viewer's command line (free): from its
[releases](https://github.com/ValveResourceFormat/ValveResourceFormat/releases)
download the **CLI** build for Windows and unzip `Source2Viewer-CLI.exe` into
the folder you will run the commands in. No Git is needed.

1. Install the tool (one line, in PowerShell or a command prompt):

   ```bash
   python -m pip install https://github.com/Holdi601/3DHeat-Ext-Dota/archive/refs/tags/v0.2.0.zip
   ```

2. In the folder with `Source2Viewer-CLI.exe`, check that everything is found,
   then build the map. Dota 2 is found in your Steam libraries by itself
   (else `--game "<...>\steamapps\common\dota 2 beta"`); Source2Viewer
   elsewhere is given with `--source2viewer <path to Source2Viewer-CLI.exe>`:

   ```bash
   heat3d-dota-maps list
   heat3d-dota-maps level -o levels\dota.glb
   ```

3. `list` prints `Dota 2 at ...`, a line per map and `Source2Viewer CLI at ...`.
   The output is one file, `levels\dota.glb` (the normal map: ground, cliffs,
   water, trees, buildings); `level` ends with a line like
   `dota.glb: dota, 700,000 triangles ... 2,400 trees, 70 buildings`.
4. Open it in the [3DHeat viewer](https://github.com/Holdi601/3DHeat#quick-start):
   download the viewer (**Code -> Download ZIP**, unpack) and double-click
   `start.bat`; it offers to install [Node.js](https://nodejs.org/) when it is
   missing and opens Chrome or Edge at `http://127.0.0.1:5273`. There, **Background / level ->
   3D model...** and pick the `.glb`. The viewer keeps it in its level library,
   and its **Dota 2 map** button loads it under a Dota table from then on.

When a new release is out, the tool says so when it starts and offers to
update itself (`python -m heat3d_ext_dota.update` does the same).

## Install from a checkout

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

3DHeat Dota is not affiliated with or endorsed by Valve. Dota 2 and related
names and trademarks belong to their owners. Nothing of the game is in this
repository or downloaded by it; the map comes out of your own install, and the
level it writes stays on your machine ([Terms and
licence](https://holdi601.github.io/3DHeat-Ext-Dota/terms.html)).

Rights holders: open an issue at
[3DHeat-Ext-Dota/issues](https://github.com/Holdi601/3DHeat-Ext-Dota/issues) -
we respond quickly and remove anything on request.

## Tests

```bash
python -m pip install -e .[test]
python -m pytest
```

On made-up data only, with Source2Viewer played by a stand-in.

## Licence

MIT ([`LICENSE`](LICENSE)). Third-party software it uses or runs: [`LICENSES.md`](LICENSES.md).
