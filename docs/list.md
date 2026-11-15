---
title: "Finding things: list"
nav_order: 2
---

# Finding things: `list`

```bash
heat3d-dota-maps list [--game FOLDER] [--source2viewer EXE]
```

prints where Dota 2 is installed, each map in its `game\dota\maps` folder with
its size, and where Source2Viewer's CLI is. Run it first: when it ends with
`Source2Viewer CLI at ...` and exits with 0, [`level`](level.md) has all it needs.

```text
Dota 2 at C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota
  dota                         29.0 MB
  dota_winter                  23.7 MB
  ...
Source2Viewer CLI at C:\Tools\3DHeat-Ext-Dota\Source2Viewer-CLI.exe
```

`dota` is the normal map; the others are older versions, seasonal and event
maps and tutorials (only `dota` was checked against replays).

## Where Dota 2 is looked for

`--game` first: the `dota 2 beta` folder or its `game\dota` folder. Without it,
`steamapps\common\dota 2 beta\game\dota` in every Steam library: Steam's own
folder (from the registry, else `C:\Program Files (x86)\Steam`,
`~/.steam/steam` or `~/.local/share/Steam`) and each library its
`steamapps\libraryfolders.vdf` lists. The first install found is used.

## Where Source2Viewer's CLI is looked for

1. `--source2viewer <path>`;
2. the `HEAT3D_SOURCE2VIEWER` environment variable;
3. `Source2Viewer-CLI` or `Source2Viewer-CLI.exe` on `PATH`;
4. `Source2Viewer-CLI.exe` (or `Source2Viewer-CLI`) in the current folder, then
   in this tool's own folder.

The 3DHeat CS2 tool looks in the first three places too, so one copy serves
both. Download: [ValveResourceFormat releases](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
the **CLI** build for your system.

## Messages and exit status

| Message | Exit | Means |
|---|---|---|
| `heat3d-dota-maps: Dota 2 not found in any Steam library: ...` | 2 | install Dota 2 through Steam, or pass `--game` |
| `heat3d-dota-maps: <folder> is not a Dota 2 folder ...` | 2 | `--game` points somewhere without `game\dota\gameinfo.gi` |
| `heat3d-dota-maps: Source2Viewer-CLI not found: ...` | 2 | the maps are still listed; get the CLI as above |
| `heat3d-dota-maps: --source2viewer <path>: no such file` | 2 | the path given is wrong |
