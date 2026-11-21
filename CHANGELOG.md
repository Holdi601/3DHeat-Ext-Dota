# Changelog

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
