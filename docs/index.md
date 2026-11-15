---
title: Home
nav_order: 1
---

# 3DHeat Dota

**What is it?** This tool turns the Dota 2 map, read from **your own install**,
into a 3D level - a model of the map you can fly over - for the
[3DHeat](https://github.com/Holdi601/3DHeat) viewer
([documentation](https://holdi601.github.io/3DHeat/)): the ground, the cliffs,
the river, every tree and the buildings.

**Why would I use it?** To see Dota 2 matches - the replay tables the
[3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html)
writes - on the game's own map in 3D, instead of a flat drawing.

**Example:** `heat3d-dota-maps level -o levels/dota.glb` -> `levels/dota.glb`,
in the units and axes of the Watcher's Dota tables: no placing or scaling in
the viewer.

## Quick start

New to the command line? Read [Before you start](before-you-start.md) first.
You need Python 3.10 or later, Dota 2 installed through Steam, and
Source2Viewer's command line (a free, MIT-licensed download, see
[Finding things: list](list.md)). Run these in the folder you cloned or unzipped:

```bash
python -m pip install -e .                  # installs the heat3d-dota-maps command
heat3d-dota-maps list                       # where Dota 2 and Source2Viewer are, the maps installed
heat3d-dota-maps level -o levels/dota.glb   # the normal map as a level
```

You should see `Dota 2 at ...`, a line per map, and `Source2Viewer CLI at ...`
from `list`; `level` ends with a line like
`levels/dota.glb: dota, 700,000 triangles ... 2,400 trees, 70 buildings`.
Then load `levels/dota.glb` in the viewer's **Background / level** panel with
**3D model…**: the viewer keeps it in its level library, and its **Dota 2 map**
button loads it from then on ([Building a level](level.md#loading-it-in-the-viewer)).

The level is built from the game's files: it stays **on your machine**, to
view, not to share or publish ([Terms](terms.md)).

## Pages

| Page | What it covers |
|---|---|
| [Before you start](before-you-start.md) | Python, Source2Viewer, a terminal, a first run |
| [Finding things: list](list.md) | where Dota 2 and Source2Viewer's CLI are found, what `list` prints |
| [Building a level: level](level.md) | every option, how the level is made, its parts, how it was checked |
| [Terms and licence](terms.md) | Valve's map, Source2Viewer's licence, why this is a separate package |
| [Command reference](cli-reference.md) | every option, generated from the code |
| [Maintaining these docs](maintaining.md) | the release checklist |

## Related

- The 3DHeat viewer: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentation at [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- The Dota 2 replay tables these levels sit under: the
  [3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html).
- Counter-Strike 2 maps through the same Source2Viewer CLI:
  [3DHeat CS2](https://holdi601.github.io/3DHeat-CS2/).

## The 3DHeat tools

| Tool | What it does | Code | Docs |
|---|---|---|---|
| 3DHeat viewer | shows the data: heatmaps, race analysis, match review | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | levels and courses from a game's own files | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | lap telemetry, and levels rebuilt from gameplay video | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | an Unreal Editor plugin: a level as one `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Counter-Strike 2 demos and maps | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | records what games publish while you play | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | War Thunder replays | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | World of Tanks replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | World of Warships replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | Squad server demos | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | DCS World maps as 3D levels | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | IL-2 Sturmovik maps as 3D levels | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | the Dota 2 map as a 3D level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | Dota 2 replays | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | League of Legends and VALORANT replays (what they carry unencrypted) | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | Forza courses, races and cars from your own install | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [docs](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | Battlefield levels (Frostbite) as 3D levels | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [docs](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | BeamNG.drive courses | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [docs](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | Assetto Corsa Rally stages as courses | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [docs](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | Arma Reforger worlds (Enfusion) as 3D levels | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [docs](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
