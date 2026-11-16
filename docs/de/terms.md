---
title: Bedingungen und Lizenz
nav_order: 8
lang: "de"
source: terms.md
source_hash: "04ca2f908fa5"
nav_exclude: true
search_exclude: true
---
# Bedingungen und Lizenz {#terms-and-licence}

## Valves Karte {#valves-map}

3DHeat Dota ist weder mit Valve verbunden noch von Valve unterstützt. Dota 2 und zugehörige Namen
und Marken gehören ihren Inhabern. Dieses Werkzeug liefert nichts vom Spiel mit und lädt nichts
herunter: Es liest die Dateien der Kopie, die **du** installiert hast, auf deinem Rechner, über
Source2Viewer, außerhalb des Spiels. Es verändert nichts im Spiel und spricht mit keinem Server. Das
Level, das es schreibt, bleibt auf deinem Rechner, zum Anschauen im 3DHeat-Viewer.

## Ein eigenes Projekt {#its-own-project}

Jeder Spiel-Leser ist ein eigenes kleines Projekt mit eigener Lizenzdatei, eigenen Releases und
eigenem Issue-Tracker. So lässt er sich für sich allein installieren, aktualisieren, pflegen – oder
auf Wunsch eines Rechteinhabers zurückziehen –, ohne den Viewer oder die anderen Werkzeuge zu
berühren.

Rechteinhaber: Eröffnet ein Issue unter
[3DHeat-Ext-Dota/issues](https://github.com/Holdi601/3DHeat-Ext-Dota/issues) – wir antworten schnell
und entfernen auf Wunsch alles.

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
