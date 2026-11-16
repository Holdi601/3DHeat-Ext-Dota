---
title: "Antes de empezar"
nav_order: 1.5
lang: "es"
source: before-you-start.md
source_hash: "8978ef7afccc"
nav_exclude: true
search_exclude: true
---
# Antes de empezar {#before-you-start}

¿Nunca has usado la línea de comandos? Esta página te lleva de cero a una primera ejecución.
Tarda unos quince minutos, una sola vez.

## 1. Instalar Python {#install-python}

Esta herramienta necesita **Python 3.10 o posterior**.

- **Windows:** descarga Python desde [python.org/downloads](https://www.python.org/downloads/)
  y ejecuta el instalador. En su primera pantalla, marca **Add python.exe to PATH**,
  y luego haz clic en **Install Now**.
- **macOS y Linux:** Python 3 suele estar instalado ya. Donde estas páginas dicen
  `python`, escribe `python3`.

## 2. Conseguir esta herramienta {#get-this-tool}

Abre [github.com/Holdi601/3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota), haz clic en el
botón verde **Code** y luego en **Download ZIP**, y descomprímela en una carpeta de tu elección. Si usas git: `git clone https://github.com/Holdi601/3DHeat-Ext-Dota`.

## 3. Conseguir la línea de comandos de Source2Viewer {#get-source2viewers-command-line}

Source2Viewer (ValveResourceFormat, licencia MIT) lee los archivos empaquetados de Dota 2.
Abre su [página de versiones](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
descarga la versión **CLI** para tu sistema y descomprime `Source2Viewer-CLI.exe`
(en macOS y Linux, `Source2Viewer-CLI`) en la carpeta del paso 2. Con eso basta: la herramienta
mira allí. [Encontrar cosas: list](list.md) dice dónde más busca.

## 4. Abrir una terminal en esa carpeta {#open-a-terminal-in-that-folder}

Una terminal es una ventana donde escribes comandos.

- **Windows:** abre la carpeta en el Explorador, haz clic en la barra de direcciones, escribe
  `powershell` y pulsa Intro. Se abre una ventana azul o negra, ya en esa carpeta.
- **macOS:** abre **Terminal**, escribe `cd ` (con un espacio), arrastra la carpeta a
  la ventana y pulsa Intro.

`cd` significa "cambiar de carpeta": `cd C:\Tools\3DHeat-Ext-Dota` va a esa carpeta.

## 5. Instalar la herramienta {#install-the-tool}

Escribe esto y pulsa Intro:

```bash
python -m pip install -e .
```

Al final deberías ver: `Successfully installed heat3d-ext-dota-...`.

## 6. Ejecutarla {#run-it}

```bash
heat3d-dota-maps list
```

Deberías ver algo parecido a:

```text
Dota 2 at C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota
  dota                         29.0 MB
  ...
Source2Viewer CLI at C:\Tools\3DHeat-Ext-Dota\Source2Viewer-CLI.exe
```

Siguiente: [Crear un nivel: level](level.md).

## Cómo leer los comandos de estas páginas {#how-to-read-the-commands-on-these-pages}

| Ves | Significa |
|---|---|
| `<file.glb>` | un marcador: escribe tu propio valor en su lugar, sin los `< >` |
| `[--detail UNITS]` | opcional: déjalo fuera, o escríbelo tal como aparece |
| `# a note` | un comentario para ti: no lo escribas |
| `"C:\My Files\x"` | pon entre comillas una ruta que tenga espacios |

## Cuando algo sale mal {#when-something-goes-wrong}

| El mensaje | Qué hacer |
|---|---|
| `'python' is not recognized` | Python no está instalado, o no se marcó la casilla PATH: instálalo de nuevo y marca la casilla (o escribe `py` en vez de `python`). |
| `'heat3d-dota-maps' is not recognized` | Repite el paso 5 en la carpeta de la herramienta, o escribe `python -m heat3d_ext_dota` en vez de `heat3d-dota-maps`: hace lo mismo. |
| `No module named heat3d_ext_dota` | No estás en la carpeta de la herramienta, o el paso 5 falló: haz `cd` hasta allí y ejecuta el paso 5. |
| `Dota 2 not found in any Steam library` | Instala Dota 2 a través de Steam, o indica su carpeta: `--game "D:\Games\Steam\steamapps\common\dota 2 beta"`. |
| `Source2Viewer-CLI not found` | Haz el paso 3, o indica su ruta: `--source2viewer <ruta a Source2Viewer-CLI.exe>`. |
| cualquier otro | Lee la última línea del mensaje y abre una incidencia en GitHub con ella. |

Cada comando también termina con un **código de salida**: 0 significa que funcionó, 2 que
no se encontró Dota 2, el mapa o Source2Viewer, 1 que la lectura falló. Para verlo,
escribe `echo $LASTEXITCODE` en PowerShell o `echo $?` en macOS y Linux.
