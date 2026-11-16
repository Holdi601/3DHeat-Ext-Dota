---
title: Bevor du anfängst
nav_order: 1.5
lang: "de"
source: before-you-start.md
source_hash: "8978ef7afccc"
nav_exclude: true
search_exclude: true
---
# Bevor du anfängst {#before-you-start}

Neu bei der Kommandozeile? Diese Seite führt dich von null bis zum ersten Lauf.
Es dauert einmalig etwa fünfzehn Minuten.

## 1. Python installieren {#install-python}

Dieses Werkzeug braucht **Python 3.10 oder neuer**.

- **Windows:** Lade Python von [python.org/downloads](https://www.python.org/downloads/)
  herunter und starte den Installer. Setze auf dem ersten Bildschirm das Häkchen bei
  **Add python.exe to PATH** und klicke dann auf **Install Now**.
- **macOS und Linux:** Python 3 ist oft schon vorhanden. Wo diese Seiten
  `python` schreiben, tippe `python3`.

## 2. Dieses Werkzeug holen {#get-this-tool}

Öffne [github.com/Holdi601/3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota), klicke auf den
grünen Button **Code** und dann auf **Download ZIP**. Entpacke das Archiv in einen Ordner deiner
Wahl. Wenn du git benutzt: `git clone https://github.com/Holdi601/3DHeat-Ext-Dota`.

## 3. Die Kommandozeile von Source2Viewer holen {#get-source2viewers-command-line}

Source2Viewer (ValveResourceFormat, MIT-Lizenz) liest die gepackten Dateien von Dota 2.
Öffne die [Release-Seite](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
lade den **CLI**-Build für dein System herunter und entpacke `Source2Viewer-CLI.exe`
(unter macOS und Linux `Source2Viewer-CLI`) in den Ordner aus Schritt 2. Das reicht:
Das Werkzeug schaut dort nach. [Dinge finden: list](list.md) sagt, wo es sonst noch sucht.

## 4. Ein Terminal in diesem Ordner öffnen {#open-a-terminal-in-that-folder}

Ein Terminal ist ein Fenster, in das du Befehle tippst.

- **Windows:** Öffne den Ordner im Explorer, klicke in die Adresszeile, tippe
  `powershell` und drücke Enter. Ein blaues oder schwarzes Fenster öffnet sich, schon im
  richtigen Ordner.
- **macOS:** Öffne **Terminal**, tippe `cd ` (mit Leerzeichen), ziehe den Ordner in das
  Fenster und drücke Enter.

`cd` heißt „Ordner wechseln“: `cd C:\Tools\3DHeat-Ext-Dota` geht in diesen Ordner.

## 5. Das Werkzeug installieren {#install-the-tool}

Tippe das und drücke Enter:

```bash
python -m pip install -e .
```

Am Ende solltest du sehen: `Successfully installed heat3d-ext-dota-...`.

## 6. Ausführen {#run-it}

```bash
heat3d-dota-maps list
```

Du solltest etwa so etwas sehen:

```text
Dota 2 at C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota
  dota                         29.0 MB
  ...
Source2Viewer CLI at C:\Tools\3DHeat-Ext-Dota\Source2Viewer-CLI.exe
```

Weiter: [Ein Level bauen: level](level.md).

## So liest du die Befehle auf diesen Seiten {#how-to-read-the-commands-on-these-pages}

| Du siehst | Das bedeutet |
|---|---|
| `<file.glb>` | ein Platzhalter: Tippe stattdessen deinen eigenen Wert, ohne die `< >` |
| `[--detail UNITS]` | optional: Lass es weg, oder tippe es wie gezeigt |
| `# a note` | ein Kommentar für dich: nicht eintippen |
| `"C:\My Files\x"` | ein Pfad mit Leerzeichen kommt in Anführungszeichen |

## Wenn etwas schiefgeht {#when-something-goes-wrong}

| Die Meldung | Was zu tun ist |
|---|---|
| `'python' is not recognized` | Python ist nicht installiert, oder das Kästchen PATH war nicht angehakt: Installiere es neu und hake es an (oder tippe `py` statt `python`). |
| `'heat3d-dota-maps' is not recognized` | Führe Schritt 5 im Ordner des Werkzeugs noch einmal aus, oder tippe `python -m heat3d_ext_dota` statt `heat3d-dota-maps`: Das tut dasselbe. |
| `No module named heat3d_ext_dota` | Du bist nicht im Ordner des Werkzeugs, oder Schritt 5 ist fehlgeschlagen: Wechsle mit `cd` dorthin und führe Schritt 5 aus. |
| `Dota 2 not found in any Steam library` | Installiere Dota 2 über Steam, oder gib seinen Ordner an: `--game "D:\Games\Steam\steamapps\common\dota 2 beta"`. |
| `Source2Viewer-CLI not found` | Mache Schritt 3, oder gib seinen Pfad an: `--source2viewer <path to Source2Viewer-CLI.exe>`. |
| alles andere | Lies die letzte Zeile der Meldung und eröffne damit ein Issue auf GitHub. |

Jeder Befehl endet außerdem mit einem **Exit-Status**: 0 heißt, es hat geklappt; 2 heißt, dass
Dota 2, die Karte oder Source2Viewer nicht gefunden wurde; 1 heißt, das Lesen ist fehlgeschlagen.
Um ihn zu sehen, tippe `echo $LASTEXITCODE` in PowerShell oder `echo $?` unter macOS und Linux.
