---
title: "Dinge finden: list"
nav_order: 2
lang: "de"
source: list.md
source_hash: "a03dec416591"
nav_exclude: true
search_exclude: true
---
# Dinge finden: `list` {#finding-things-list}

```bash
heat3d-dota-maps list [--game FOLDER] [--source2viewer EXE]
```

gibt aus, wo Dota 2 installiert ist, jede Karte in ihrem Ordner `game\dota\maps` mit ihrer Größe, und wo
die Kommandozeile von Source2Viewer liegt. Führe es zuerst aus: Wenn es mit `Source2Viewer CLI at ...`
endet und mit 0 beendet wird, hat [`level`](level.md) alles, was es braucht.

```text
Dota 2 at C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota
  dota                         29.0 MB
  dota_winter                  23.7 MB
  ...
Source2Viewer CLI at C:\Tools\3DHeat-Ext-Dota\Source2Viewer-CLI.exe
```

`dota` ist die normale Karte; die anderen sind ältere Versionen, saisonale und Event-Karten sowie
Tutorials (nur `dota` wurde an Replays geprüft).

## Wo Dota 2 gesucht wird {#where-dota-2-is-looked-for}

Zuerst `--game`: der Ordner `dota 2 beta` oder sein Ordner `game\dota`. Ohne diese Option
`steamapps\common\dota 2 beta\game\dota` in jeder Steam-Bibliothek: Steams eigener Ordner (aus der
Registry, sonst `C:\Program Files (x86)\Steam`, `~/.steam/steam` oder `~/.local/share/Steam`) und jede
Bibliothek, die ihre `steamapps\libraryfolders.vdf` auflistet. Die erste gefundene Installation wird
genommen.

## Wo die Kommandozeile von Source2Viewer gesucht wird {#where-source2viewers-cli-is-looked-for}

1. `--source2viewer <path>`;
2. die Umgebungsvariable `HEAT3D_SOURCE2VIEWER`;
3. `Source2Viewer-CLI` oder `Source2Viewer-CLI.exe` im `PATH`;
4. `Source2Viewer-CLI.exe` (oder `Source2Viewer-CLI`) im aktuellen Ordner, dann im Ordner dieses Werkzeugs.

Das 3DHeat-CS2-Werkzeug sucht ebenfalls an den ersten drei Stellen, so reicht eine Kopie für beide.
Download: [ValveResourceFormat-Releases](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
der **CLI**-Build für dein System.

## Meldungen und Exit-Status {#messages-and-exit-status}

| Meldung | Exit | Bedeutet |
|---|---|---|
| `heat3d-dota-maps: Dota 2 not found in any Steam library: ...` | 2 | installiere Dota 2 über Steam, oder gib `--game` an |
| `heat3d-dota-maps: <folder> is not a Dota 2 folder ...` | 2 | `--game` zeigt auf einen Ort ohne `game\dota\gameinfo.gi` |
| `heat3d-dota-maps: Source2Viewer-CLI not found: ...` | 2 | die Karten werden trotzdem aufgelistet; besorge die CLI wie oben |
| `heat3d-dota-maps: --source2viewer <path>: no such file` | 2 | der angegebene Pfad ist falsch |
