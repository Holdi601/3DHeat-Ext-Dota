# Changelog

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
