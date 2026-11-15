---
title: Before you start
nav_order: 1.5
---

# Before you start

New to the command line? This page takes you from nothing to a first run.
It takes about fifteen minutes, once.

## 1. Install Python

This tool needs **Python 3.10 or later**.

- **Windows:** download Python from [python.org/downloads](https://www.python.org/downloads/)
  and run the installer. On its first screen, tick **Add python.exe to PATH**,
  then click **Install Now**.
- **macOS and Linux:** Python 3 is often there already. Where these pages say
  `python`, type `python3`.

## 2. Get this tool

Open [github.com/Holdi601/3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota), click the
green **Code** button, then **Download ZIP**, and unzip it into a folder of your
choice. If you use git: `git clone https://github.com/Holdi601/3DHeat-Ext-Dota`.

## 3. Get Source2Viewer's command line

Source2Viewer (ValveResourceFormat, MIT licence) reads Dota 2's packed files.
Open its [releases page](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
download the **CLI** build for your system and unzip `Source2Viewer-CLI.exe`
(on macOS and Linux `Source2Viewer-CLI`) into the folder from step 2. That is
enough: the tool looks there. [Finding things: list](list.md) says where else
it looks.

## 4. Open a terminal in that folder

A terminal is a window where you type commands.

- **Windows:** open the folder in Explorer, click into the address bar, type
  `powershell` and press Enter. A blue or black window opens, already in that
  folder.
- **macOS:** open **Terminal**, type `cd ` (with a space), drag the folder into
  the window and press Enter.

`cd` means "change folder": `cd C:\Tools\3DHeat-Ext-Dota` goes to that folder.

## 5. Install the tool

Type this and press Enter:

```bash
python -m pip install -e .
```

You should see, at the end: `Successfully installed heat3d-ext-dota-...`.

## 6. Run it

```bash
heat3d-dota-maps list
```

You should see something like:

```text
Dota 2 at C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota
  dota                         29.0 MB
  ...
Source2Viewer CLI at C:\Tools\3DHeat-Ext-Dota\Source2Viewer-CLI.exe
```

Next: [Building a level: level](level.md).

## How to read the commands on these pages

| You see | It means |
|---|---|
| `<file.glb>` | a placeholder: type your own value instead, without the `< >` |
| `[--detail UNITS]` | optional: leave it out, or type it as shown |
| `# a note` | a comment for you: do not type it |
| `"C:\My Files\x"` | put a path that has spaces in quotes |

## When something goes wrong

| The message | What to do |
|---|---|
| `'python' is not recognized` | Python is not installed, or the PATH box was not ticked: install it again and tick it (or type `py` instead of `python`). |
| `'heat3d-dota-maps' is not recognized` | Run step 5 again in the tool's folder, or type `python -m heat3d_ext_dota` instead of `heat3d-dota-maps`: it does the same. |
| `No module named heat3d_ext_dota` | You are not in the tool's folder, or step 5 failed: `cd` there and run step 5. |
| `Dota 2 not found in any Steam library` | Install Dota 2 through Steam, or give its folder: `--game "D:\Games\Steam\steamapps\common\dota 2 beta"`. |
| `Source2Viewer-CLI not found` | Do step 3, or give its path: `--source2viewer <path to Source2Viewer-CLI.exe>`. |
| anything else | Read the last line of the message, then open an issue on GitHub with it. |

Every command also ends with an **exit status**: 0 means it worked, 2 that
Dota 2, the map or Source2Viewer was not found, 1 that reading failed. To see
it, type `echo $LASTEXITCODE` in PowerShell or `echo $?` on macOS and Linux.
