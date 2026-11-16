---
title: Bedingungen und Lizenz
nav_order: 8
lang: "de"
source: terms.md
source_hash: "0c470cb49eea"
nav_exclude: true
search_exclude: true
---
# Bedingungen und Lizenz {#terms-and-licence}

## Valves Karte {#valves-map}

Dota 2 und seine Karte gehören Valve, das dieses Projekt nicht unterstützt. Dieses Werkzeug liefert nichts
vom Spiel mit und lädt nichts herunter: Es liest die Dateien der Kopie, die **du** installiert hast, auf
deinem Rechner, über Source2Viewer, außerhalb des Spiels. Es verändert nichts im Spiel und spricht mit
keinem Server. Das Level, das es schreibt, ist eine Ableitung der Karte von Valve: Es gehört dir zum
Anschauen im 3DHeat-Viewer, nicht zum Teilen oder Veröffentlichen. Die Nutzung des Werkzeugs ist deine
Entscheidung, unter den Bedingungen, die du für Dota 2 und Steam akzeptiert hast.

Deshalb ist es ein eigenes Paket: Wenn Valve je verlangt, dass es verschwindet, geht nur es, und der
Viewer, der Watcher und die anderen Werkzeuge bleiben.

## Source2Viewer {#source2viewer}

Das Lesen der kompilierten Dateien von Source 2 erledigt die Kommandozeile von Source2Viewer
(ValveResourceFormat, MIT-Lizenz,
[github.com/ValveResourceFormat/ValveResourceFormat](https://github.com/ValveResourceFormat/ValveResourceFormat)).
Sie ist nicht Teil dieses Werkzeugs und liegt ihm nicht bei: Du lädst sie selbst herunter, und dieses
Werkzeug startet sie nur. Siehe [`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/LICENSES.md).

## Lizenz und Quellen {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/LICENSE)). Benötigt wird numpy
(BSD-3-Clause); für die Tests pytest (MIT). Für dieses Projekt geschrieben; aus keinem anderen Projekt
wurde Code übernommen.
