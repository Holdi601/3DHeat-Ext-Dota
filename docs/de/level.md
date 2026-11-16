---
title: "Ein Level bauen: level"
nav_order: 3
lang: "de"
source: level.md
source_hash: "cf6d9414a203"
nav_exclude: true
search_exclude: true
---
# Ein Level bauen: `level` {#building-a-level-level}

```bash
heat3d-dota-maps level [<map>] -o <file.glb> [--game FOLDER] [--source2viewer EXE] [--detail UNITS]
```

schreibt die Dota-2-Karte als Leveldaten für den 3DHeat-Viewer: den Boden, die Klippen, das Wasser,
jeden Baum und die Gebäude, im Koordinatensystem und in den Einheiten, in denen die
[Dota-2-Replay-Tabellen](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html)
des 3DHeat Watcher gezeichnet werden. Code:
[`heat3d_ext_dota/dota_map.py`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/heat3d_ext_dota/dota_map.py).

| Option | Tut |
|---|---|
| `<map>` | der Name der Karte, so wie [`list`](list.md) ihn ausgibt (Standard `dota`, die normale Karte), oder der Pfad zur `.vpk` einer Karte |
| `-o`, `--out FILE` | die zu schreibende `.glb` (erforderlich); ihr Ordner wird angelegt, falls er fehlt |
| `--game FOLDER` | der Ordner `dota 2 beta` oder sein Ordner `game\dota`, wenn Dota 2 in keiner Steam-Bibliothek liegt |
| `--source2viewer EXE` | die Kommandozeile von Source2Viewer, wenn sie nicht von selbst gefunden wird ([list](list.md) sagt, wo gesucht wird) |
| `--detail UNITS` | die Zellgröße der Vertex-Zusammenfassung der Gebäude in Spieleinheiten (Standard 8; 0 behält jedes Dreieck) |

## Im Viewer laden {#loading-it-in-the-viewer}

Lade die `.glb` im Viewer im Panel **Hintergrund / Level** (**3D-Modell…**) unter einer
Dota-Tabelle, dann liegt die Hitze der Helden auf den Lanes, die Türme auf ihren Türmen. Der
Viewer erkennt die Datei an ihren Teilen und behält sie in seiner
[Level-Bibliothek](https://holdi601.github.io/3DHeat/level-library.html). Von da an lädt sein Button
**Dota-2-Karte** statt der Zeichnung von OpenDota diese 3D-Karte.

Nichts vom Spiel steckt in diesem Werkzeug, und es lädt nichts herunter: Die Karte stammt aus deiner
eigenen Installation, und die Datei, die es schreibt, gehört dir zum Behalten, nicht zum Teilen – die
Karte gehört Valve ([Bedingungen](terms.md)).

## So entsteht sie {#how-it-is-made}

1. **Das Kollisionsnetz.** Source2Viewer exportiert `maps/<map>/world_physics.vmdl_c` aus
   `maps/<map>.vpk` als glTF. Seine Gruppen sind nach Oberfläche benannt. Gruppen namens `clip`
   (die unsichtbaren Wände) oder `sky` werden weggelassen. Gruppen namens `water`, `slime` oder `window`
   sind **Wasser**: der Fluss und die Teiche sind `water_slime`, die schmalen Bäche durch den Dschungel
   sind `window`; bei einem Replay stehen Helden 10 bis 16 Einheiten unter dem ersten und ein paar
   Einheiten unter dem zweiten. Nur ihre nach oben weisenden Flächen bleiben. Alles andere ist das
   Gelände, Fläche für Fläche aufgeteilt: Eine Fläche, deren Normale mindestens um 0,7 nach oben zeigt
   (Hänge bis etwa 45 Grad), ist **Boden**; der Rest – Klippenwände, die Mauern der Karte – ist
   **Struktur**.
2. **Die Entitäten.** Source2Viewer dekompiliert die Entitäts-Blöcke der Karte
   (`maps/<map>/entities/*.vents_c`) in Text: Blöcke mit dem Kopf `====<n>====`, je eine Zeile
   `key value`. Verwendet werden die Block `default_ents` und jede Weltebene, eine
   `info_world_layer`-Entität dort, die zu Beginn sichtbar ist (Spawn-Flag 1) – die Ebenen der beiden
   Basen. Die Ebenen, die versteckt starten, enthalten, was erscheint, wenn eine Basis fällt, und
   werden weggelassen.
3. **Was gezeichnet wird.** Bäume (`ent_dota_tree`) und die Gebäude: Türme, Kasernen, die Ancients
   (`npc_dota_fort`), die Füllbauten (`npc_dota_building`), Außenposten, Brunnen, die Weisheitsschreine,
   Lotusteiche, Zwillingstore, Wächter (`npc_dota_lantern`) und die neutralen Item-Lager. Läden (ein
   Ladenbesitzer ist eine Figur), die Ruhmeshalle, Banner, Lichter und Partikel nicht.
4. **Die Modelle.** Jedes Modell, das diese Entitäten nennen, wird in einem Lauf von Source2Viewer aus
   `game\dota\pak01_dir.vpk` exportiert. Teile eines Modells, die nur ein anderer Zustand derselben Sache
   sind – der Baumstumpf nach dem Fällen, die Nahansicht im Inspektor, Schutt –, werden nach Namen
   weggelassen (`stump`, `inspector`, `destruction`).
5. **Gebäude** sind ihr eigenes Netz des Modells, ausgedünnt durch **Vertex-Zusammenfassung**: Jeder
   Punkt wandert zum Mittelwert der Punkte in seinem Würfel der Größe `--detail` (Standard 8 Einheiten,
   etwa ein Drittel der Breite eines Helden), und Dreiecke, die zusammenfallen oder sich wiederholen,
   verschwinden. 0 behält jedes Dreieck.
6. **Bäume** sind der Umriss jedes Modells als niedriger gedrehter Körper: seine Höhe in fünf Bändern,
   jedes ein sechseckiger Ring so breit wie der größte Teil der Punkte des Modells in dieser Höhe (das
   90. Perzentil ihres Abstands von der Achse des Stamms), unten geschlossen und oben spitz zulaufend –
   60 Dreiecke, mit der wahren Höhe und Breite des Modells. Eine Kiefer wird ein Kegel, eine Eiche eine
   Kugel auf einem Stiel. Bei über 2.000 Bäumen wögen die echten Netze etwa zehnmal so viel.
7. **Platziert**, wie das Spiel sie platziert: skaliert mit `scales`, gedreht mit `angles` (Pitch, Yaw,
   Roll von Source in Grad), an `origin` verschoben.
8. **In das Koordinatensystem des Viewers.** Source2Viewer schreibt glTF in Metern, Y nach oben: (Y, Z, X)
   des Spiels mal 0,0254. Das wird rückgängig gemacht, und jeder Punkt wird als (X, Z, -Y) des Spiels
   geschrieben: Y nach oben, das Y des Spiels negiert – das Koordinatensystem, in dem die Dota-Tabellen
   über ihre `heat3d`-Hinweise gezeichnet werden (`up: z`, `flipY: true`, Skalierung 1). Eine Drehung,
   keine Spiegelung.

## Die Datei {#the-file}

Eine glTF-2.0-Binärdatei wie die des 3DHeat-CS2-Werkzeugs (siehe dessen Seite zum Karten-Export): je ein
Knoten und ein Netz pro Teil auf oberster Ebene, ohne Transformationen, flachschattiert (ein Eckpunkt pro
Dreiecksecke mit der Normale des Dreiecks), `uint32`-Indizes, ohne Materialien, Texturen oder UVs,
`asset.generator` `heat3d_ext_dota`, Einheiten des Spiels.

| Teil | Was |
|---|---|
| `ground:terrain` | der begehbare Boden |
| `structure:terrain` | Klippenwände und die Mauern der Karte |
| `water:water_slime`, `water:window` | der Fluss und die Teiche; die Dschungelbäche |
| `structure:tree` | jeder Baum, der zu Beginn steht |
| `structure:tower`, `structure:barracks`, `structure:ancient`, `structure:filler`, `structure:outpost`, `structure:fountain`, `structure:shrine`, `structure:lotus_pool`, `structure:twin_gate`, `structure:watcher`, `structure:neutral_stash` | die Gebäude, nach Art |

Das Präfix `ground:` / `structure:` / `water:` ist die Art, wie alle 3DHeat-Level-Exporter dem Viewer
sagen, was ein Teil ist; der Viewer glaubt es ihnen. Weil die Einheiten die des Spiels sind (je etwa ein
Zoll), zeigt ein anderer glTF-Betrachter die Karte etwa 39-mal zu groß; im 3DHeat liegt sie genau unter
der Tabelle.

Was es auf einem Beispiellauf ausgibt (die Zahlen hängen von der Version der Karte ab):

```text
reading dota.vpk: collision mesh and entities
reading 30 models from pak01_dir.vpk
dota.glb: dota, 700,000 triangles (230,000 ground) in 16 parts; 2,400 trees, 70 buildings
```

Die ersten beiden Zeilen gehen auf die Fehlerausgabe, die letzte auf die Ausgabe. Ein Modell, das
Source2Viewer nicht finden konnte, wird weggelassen und am Ende der letzten Zeile genannt
(`; 1 model(s) not found, left out: ...`). Fehler zeigen `heat3d-dota-maps: <why>`. Wenn Dota 2, die Karte oder Source2Viewer nicht gefunden wird, endet das Werkzeug mit Exit-Code 2; ein Fehlschlag von Source2Viewer endet mit Code 1.

## So wurde sie geprüft {#how-it-was-checked}

An einem öffentlichen Match-Replay, konvertiert vom 3DHeat Watcher (Patch 7.40), und der Karte der
installierten Spielversion:

- jede Position eines Helden wird von oben gesehen, und die höchste Bodenfläche höchstens 64 Einheiten über
  seinen Füßen findet Boden; die mittlere Höhe darüber beträgt 0 Einheiten, und 99,5 % liegen innerhalb
  von 16 Einheiten; mit gespiegelter Karte (Y nicht negiert) finden nur etwa die Hälfte Boden, der Rest
  schwebt oder sinkt um die Höhe einer Klippe;
- die 22 Türme, 12 Kasernen, 2 Ancients, 14 Füllbauten, 2 Außenposten, 2 Brunnen und 10 Wächter, die die
  Einheitentabelle des Replays platziert, stehen auf den Entitäten der Karte derselben Art, auf 0,02
  Einheiten genau, waagerecht und in der Höhe;
- der Fuß jedes Baums steht auf dem Boden.

Die Tests ([`tests/test_dota_map.py`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/tests/test_dota_map.py))
prüfen den Entitäten-Leser, die Koordinatensysteme, die Aufteilung des Geländes, die Baumumrisse und die
Zusammenfassung, die Platzierung und den ganzen Export mit einem Stellvertreter für Source2Viewer – nur mit
erfundenen Daten.

## Was es nicht tut {#what-it-does-not-do}

- Keine Texturen und Farben: Der Viewer schattiert das Level auf seine eigene Weise.
- Keine gefällten Bäume und keine zerstörten Gebäude während eines Matches: die Karte, wie sie beginnt.
- Event- und Custom-Karten sind ungetestet; ihre Entitätsklassen können abweichen.
- Die Requisiten, die nur schmücken (Felsen, Zäune, Banner), sind nur insoweit darin, wie sie Teil des
  Kollisionsnetzes sind.
