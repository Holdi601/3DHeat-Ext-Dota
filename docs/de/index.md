---
title: Startseite
nav_order: 1
lang: "de"
source: index.md
source_hash: "3e8858fb1b90"
nav_exclude: true
search_exclude: true
permalink: /de/
---
# 3DHeat Dota {#dheat-dota}

**Was ist das?** Dieses Werkzeug macht aus der Dota-2-Karte, gelesen aus **deiner eigenen Installation**,
ein 3D-Level – ein Modell der Karte, über das du fliegen kannst – für den
[3DHeat](https://github.com/Holdi601/3DHeat)-Viewer
([Dokumentation](https://holdi601.github.io/3DHeat/)): den Boden, die Klippen, den Fluss, jeden Baum
und die Gebäude.

**Wozu brauche ich das?** Um Dota-2-Matches – die Replay-Tabellen, die der
[3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html) schreibt – auf der
Karte des Spiels in 3D zu sehen, statt auf einer flachen Zeichnung.

**Beispiel:** `heat3d-dota-maps level -o levels/dota.glb` -> `levels/dota.glb`, in den Einheiten und
Achsen der Dota-Tabellen des Watchers: kein Platzieren oder Skalieren im Viewer nötig.

**Ein eigenes Projekt:** Jeder Spiel-Leser ist ein eigenes kleines Projekt mit eigener Lizenzdatei,
eigenen Releases und eigenem Issue-Tracker. So lässt er sich für sich allein installieren,
aktualisieren, pflegen – oder auf Wunsch eines Rechteinhabers zurückziehen –, ohne den Viewer oder
die anderen Werkzeuge zu berühren.

## Schnellstart {#quick-start}

Neu bei der Kommandozeile? Lies zuerst [Bevor du anfängst](before-you-start.md).
Du brauchst Python 3.10 oder neuer, Dota 2, installiert über Steam, und die Kommandozeile von
Source2Viewer (ein kostenloser Download unter der MIT-Lizenz, siehe
[Dinge finden: list](list.md)). Führe diese Befehle in dem Ordner aus, den du geklont oder entpackt hast:

```bash
python -m pip install -e .                  # installs the heat3d-dota-maps command
heat3d-dota-maps list                       # where Dota 2 and Source2Viewer are, the maps installed
heat3d-dota-maps level -o levels/dota.glb   # the normal map as a level
```

Du solltest `Dota 2 at ...`, eine Zeile pro Karte und `Source2Viewer CLI at ...` aus `list` sehen;
`level` endet mit einer Zeile wie
`levels/dota.glb: dota, 700,000 triangles ... 2,400 trees, 70 buildings`.
Lade danach `levels/dota.glb` im Viewer im Panel **Hintergrund / Level** mit **3D-Modell…**: Der Viewer
behält es in seiner Level-Bibliothek, und sein Button **Dota-2-Karte** lädt es von da an
([Ein Level bauen](level.md#loading-it-in-the-viewer)).

Das Level wird aus den Dateien des Spiels gebaut und bleibt **auf deinem Rechner**
([Bedingungen](terms.md)).

## Seiten {#pages}

| Seite | Was sie behandelt |
|---|---|
| [Bevor du anfängst](before-you-start.md) | Python, Source2Viewer, ein Terminal, ein erster Lauf |
| [Dinge finden: list](list.md) | wo Dota 2 und die Kommandozeile von Source2Viewer gefunden werden, was `list` ausgibt |
| [Ein Level bauen: level](level.md) | jede Option, wie das Level entsteht, seine Teile, wie es geprüft wurde |
| [Bedingungen und Lizenz](terms.md) | Valves Karte, die Lizenz von Source2Viewer, dieses Werkzeug als eigenes Projekt |
| [Befehlsreferenz](../cli-reference.md) | jede Option, aus dem Code erzeugt |
| [Diese Dokumentation pflegen](maintaining.md) | die Checkliste für Releases |

## Verwandtes {#related}

- Der 3DHeat-Viewer: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  Dokumentation unter [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Die Dota-2-Replay-Tabellen, unter denen diese Level stehen: der
  [3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html).
- Counter-Strike-2-Karten über dieselbe Source2Viewer-Kommandozeile:
  [3DHeat CS2](https://holdi601.github.io/3DHeat-CS2/).

## Die 3DHeat-Werkzeuge {#the-3dheat-tools}

| Werkzeug | Was es tut | Code | Dokumentation |
|---|---|---|---|
| 3DHeat-Viewer | zeigt die Daten: Heatmaps, Rennanalyse, Match-Auswertung | [3DHeat](https://github.com/Holdi601/3DHeat) | [Dokumentation](https://holdi601.github.io/3DHeat/) |
| GameFiles | Level und Strecken aus den eigenen Dateien eines Spiels | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [Dokumentation](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | Runden-Telemetrie und Level, die aus Spielvideos nachgebaut werden | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [Dokumentation](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | ein Unreal-Editor-Plugin: ein Level als eine `.glb`-Datei | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [Dokumentation](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Counter-Strike-2-Demos und Karten | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [Dokumentation](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | zeichnet auf, was Spiele veröffentlichen, während du spielst | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [Dokumentation](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | War-Thunder-Replays | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | World-of-Tanks-Replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | World-of-Warships-Replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | Squad-Server-Demos | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | DCS-World-Karten als 3D-Level | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | IL-2-Sturmovik-Karten als 3D-Level | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | die Dota-2-Karte als 3D-Level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | Dota-2-Replays | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | League-of-Legends- und VALORANT-Replays (was sie unverschlüsselt enthalten) | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | Forza-Strecken, Rennen und Autos aus deiner eigenen Installation | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | Battlefield-Level (Frostbite) als 3D-Level | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | BeamNG.drive-Strecken | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | Assetto-Corsa-Rally-Etappen als Strecken | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | Arma-Reforger-Welten (Enfusion) als 3D-Level | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | Rainbow-Six-Siege-Match-Replays | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [Dokumentation](https://holdi601.github.io/3DHeat-Ext-R6/) |
