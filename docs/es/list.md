---
title: "Encontrar cosas: list"
nav_order: 2
lang: "es"
source: list.md
source_hash: "a03dec416591"
nav_exclude: true
search_exclude: true
---
# Encontrar cosas: `list` {#finding-things-list}

```bash
heat3d-dota-maps list [--game FOLDER] [--source2viewer EXE]
```

muestra dónde está instalado Dota 2, cada mapa en su carpeta `game\dota\maps` con
su tamaño, y dónde está la línea de comandos de Source2Viewer. Ejecútalo primero: cuando termina con
`Source2Viewer CLI at ...` y sale con 0, [`level`](level.md) tiene todo lo que necesita.

```text
Dota 2 at C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota
  dota                         29.0 MB
  dota_winter                  23.7 MB
  ...
Source2Viewer CLI at C:\Tools\3DHeat-Ext-Dota\Source2Viewer-CLI.exe
```

`dota` es el mapa normal; los demás son versiones antiguas, mapas de temporada y de eventos
y tutoriales (solo `dota` se comprobó con repeticiones).

## Dónde se busca Dota 2 {#where-dota-2-is-looked-for}

Primero `--game`: la carpeta `dota 2 beta` o su carpeta `game\dota`. Sin él,
`steamapps\common\dota 2 beta\game\dota` en cada biblioteca de Steam: la carpeta propia de Steam
(desde el registro, si no `C:\Program Files (x86)\Steam`,
`~/.steam/steam` o `~/.local/share/Steam`) y cada biblioteca que
figura en su `steamapps\libraryfolders.vdf`. Se usa la primera instalación encontrada.

## Dónde se busca la línea de comandos de Source2Viewer {#where-source2viewers-cli-is-looked-for}

1. `--source2viewer <ruta>`;
2. la variable de entorno `HEAT3D_SOURCE2VIEWER`;
3. `Source2Viewer-CLI` o `Source2Viewer-CLI.exe` en `PATH`;
4. `Source2Viewer-CLI.exe` (o `Source2Viewer-CLI`) en la carpeta actual, y luego
   en la carpeta propia de esta herramienta.

La herramienta de 3DHeat CS2 también busca en los tres primeros lugares, así que una sola copia sirve
para las dos. Descarga: [versiones de ValveResourceFormat](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
la versión **CLI** para tu sistema.

## Mensajes y código de salida {#messages-and-exit-status}

| Mensaje | Salida | Significa |
|---|---|---|
| `heat3d-dota-maps: Dota 2 not found in any Steam library: ...` | 2 | instala Dota 2 a través de Steam, o indica `--game` |
| `heat3d-dota-maps: <folder> is not a Dota 2 folder ...` | 2 | `--game` apunta a un sitio sin `game\dota\gameinfo.gi` |
| `heat3d-dota-maps: Source2Viewer-CLI not found: ...` | 2 | los mapas se siguen listando; consigue la CLI como se indicó arriba |
| `heat3d-dota-maps: --source2viewer <path>: no such file` | 2 | la ruta indicada es incorrecta |
