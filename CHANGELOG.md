# Changelog

## 0.4.0

- Its own icon: the 3DHeat cube with a text badge for its game (letters in 3DHeat's colours), as the
  program, window, taskbar and docs icon.
- A new window: the 3DHeat look in dark and light (follows the system, switchable), the logo and
  icon, sharp at any display scaling. Four steps: find the game (each requirement with its fix),
  choose (maps ticked when there is something to do, filters, search; jobs with their fields
  inline), work (progress, time left, cancel), done (open in 3DHeat, open the output folder, and
  for a failure what went wrong and what to do, copy details, report a problem).
- No console window on Windows: the program is a window program. From a terminal it still prints
  as before; `heat3d-dota-maps-cli.cmd` beside it waits for it in a terminal and passes its exit code.
- The update offer in the same look: Update now / Later / Skip this version, and "Update
  automatically" from the dialog.
- CI draws every page and dialog of the window (on Linux under a virtual display) and checks the
  Windows build is a window program.

## 0.3.0

- A standalone program for Windows, Linux and macOS (no Python needed), built by CI with a `SHA256SUMS` file.
  Without arguments it opens a window: what is found and what is missing (install, Source2Viewer-CLI, disk space),
  the levels folder, the install's maps as new / changed by a game update / exported by an older version / up to
  date, export of the picked ones one at a time (`dota/<map>.glb` and its layouts), the catalogue, the model pack,
  and updates.
- Each exported map is recorded in `<levels>/dota/.heat3d-extract.json` (extractor version, game build, size and
  SHA-256 of its `.vpk`), so maps a game update adds are found and only those exported: `status --json`,
  `extract --new` / `--changed` / `--outdated` / `<map>...`, `--progress-json`.
- Updates ask first (update now / later / skip this version) unless automatic updates were chosen
  (`--auto-update`, the window's checkbox, or `HEAT3D_AUTO_UPDATE=1`).
- The install is also found in Steam libraries on Linux (native, flatpak, Steam Deck) and macOS; Source2Viewer-CLI
  also next to the standalone program.

## 0.2.0

- `layouts`: towers, barracks, ancients, fountains, outposts, shrines and the heroes', couriers', creeps' and
  neutrals' spawns as `<map>.layouts.json` beside the level. Docs: [Level](docs/level.md#towers-bases-and-spawns-layouts).
- `catalog`: heroes, units and items with names, roles, abilities and numbers
  (`catalog.json`, format `3dheat-catalog`).
- `models`: hero and unit models as a local model pack for the viewer, posed
  at their idle, three levels of detail (`model-pack.json` + one `.glb` each).

## 0.1.0

- First version, moved out of the 3DHeat Watcher (its `dota-map` command now
  runs this tool): the Dota 2 map from your own install as a 3DHeat level -
  ground, cliffs, water, trees and buildings in the Watcher's Dota tables'
  frame, read through Source2Viewer's CLI. `list` says where Dota 2 and
  Source2Viewer are and which maps are installed; Source2Viewer is also found
  unzipped in the current folder or this tool's folder.
- Installs with one pip line from the release zip, no Git needed; a pip install knows its version and updates itself with pip when a newer release is out.
- README: a quick start for new users.

## Docs

Where each feature is documented
([holdi601.github.io/3DHeat-Ext-Dota](https://holdi601.github.io/3DHeat-Ext-Dota/)):

| Feature | Page |
|---|---|
| Installing, Source2Viewer, a first run | [Before you start](docs/before-you-start.md) |
| Finding the install and the CLI (`list`, `--game`, `--source2viewer`, `HEAT3D_SOURCE2VIEWER`) | [Finding things: list](docs/list.md) |
| Building a level (`level` and its options), its parts, how it was checked, loading it in the viewer | [Building a level: level](docs/level.md) |
| Valve's map, Source2Viewer's licence | [Terms and licence](docs/terms.md) |
| Every option and part name, generated | [Command reference](docs/cli-reference.md) |
| Release checklist for the docs | [Maintaining these docs](docs/maintaining.md) |
