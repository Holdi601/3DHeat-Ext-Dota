---
title: Command reference
nav_order: 90
---

# Command reference

Generated from the code by `tools/gen_docs_reference.py`: do not edit by hand.
The other pages explain each command step by step.

## `heat3d-dota-maps`

```text
usage: heat3d-dota-maps [-h] [--version] {list,level,catalog,models} ...

Dota 2's map from your own install into a 3DHeat level

positional arguments:
  {list,level,catalog,models}
    list                where Dota 2 and Source2Viewer's CLI are, and the maps
                        installed
    level               the map as a level (.glb) under the Dota replay tables
    catalog             heroes, units and items with names, roles and numbers
                        (catalog.json)
    models              hero and unit models as a local model pack for the viewer

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
```

## `list`

```text
usage: heat3d-dota-maps list [-h] [--game GAME] [--source2viewer SOURCE2VIEWER]

options:
  -h, --help            show this help message and exit
  --game GAME           the Dota 2 folder, `dota 2 beta` or its game/dota (default:
                        found in your Steam libraries)
  --source2viewer SOURCE2VIEWER
                        Source2Viewer-CLI's path (default: HEAT3D_SOURCE2VIEWER, PATH,
                        then the current folder and this tool's)
```

## `level`

```text
usage: heat3d-dota-maps level [-h] -o OUT [--game GAME]
                              [--source2viewer SOURCE2VIEWER] [--detail DETAIL]
                              [map]

positional arguments:
  map                   the map's name as list prints it (default: dota) or the path
                        to its .vpk

options:
  -h, --help            show this help message and exit
  -o, --out OUT         the .glb to write
  --game GAME           the Dota 2 folder, `dota 2 beta` or its game/dota (default:
                        found in your Steam libraries)
  --source2viewer SOURCE2VIEWER
                        Source2Viewer-CLI's path (default: HEAT3D_SOURCE2VIEWER, PATH,
                        then the current folder and this tool's)
  --detail DETAIL       buildings' vertex clustering cell in game units (default 8; 0
                        keeps every triangle)
```

## `catalog`

```text
usage: heat3d-dota-maps catalog [-h] [-o OUT] [--game GAME]
                                [--source2viewer SOURCE2VIEWER]

options:
  -h, --help            show this help message and exit
  -o, --out OUT         the file to write (default $HEAT3D_LEVELS/dota/catalog.json,
                        else ./catalog.json)
  --game GAME           the Dota 2 folder, `dota 2 beta` or its game/dota (default:
                        found in your Steam libraries)
  --source2viewer SOURCE2VIEWER
                        Source2Viewer-CLI's path (default: HEAT3D_SOURCE2VIEWER, PATH,
                        then the current folder and this tool's)
```

## `models`

```text
usage: heat3d-dota-maps models [-h] [-o OUT] [--only ONLY [ONLY ...]] [--game GAME]
                               [--source2viewer SOURCE2VIEWER]

options:
  -h, --help            show this help message and exit
  -o, --out OUT         the folder to write (default $HEAT3D_LEVELS/model-packs/dota,
                        else ./dota)
  --only ONLY [ONLY ...]
                        just the heroes or units whose id contains these
  --game GAME           the Dota 2 folder, `dota 2 beta` or its game/dota (default:
                        found in your Steam libraries)
  --source2viewer SOURCE2VIEWER
                        Source2Viewer-CLI's path (default: HEAT3D_SOURCE2VIEWER, PATH,
                        then the current folder and this tool's)
```

## Output

### `.glb` parts

`ground:terrain`, `structure:terrain`, `water:<surface>` (one per water surface of the collision mesh), `structure:tree` (ent_dota_tree), and per building class: `structure:tower` (npc_dota_tower), `structure:barracks` (npc_dota_barracks), `structure:ancient` (npc_dota_fort), `structure:filler` (npc_dota_building), `structure:outpost` (npc_dota_watch_tower), `structure:fountain` (ent_dota_fountain), `structure:shrine` (npc_dota_xp_fountain), `structure:lotus_pool` (npc_dota_lotus_pool), `structure:twin_gate` (npc_dota_unit_twin_gate), `structure:watcher` (npc_dota_lantern), `structure:neutral_stash` (ent_dota_neutral_item_stash).

`asset.generator`: `heat3d_ext_dota`.
