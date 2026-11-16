---
title: Home
nav_order: 1
lang: "it"
source: index.md
source_hash: "3e8858fb1b90"
nav_exclude: true
search_exclude: true
permalink: /it/
---
# 3DHeat Dota {#dheat-dota}

**Che cos'è?** Questo strumento trasforma la mappa di Dota 2, letta dalla **tua installazione**,
in un livello 3D - un modello della mappa sopra cui puoi volare - per il visualizzatore
[3DHeat](https://github.com/Holdi601/3DHeat)
([documentazione](https://holdi601.github.io/3DHeat/)): il suolo, le scogliere, il fiume, ogni albero e gli edifici.

**Perché usarlo?** Per vedere le partite di Dota 2 - le tabelle dei replay che il
[3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html)
scrive - sulla mappa del gioco stesso in 3D, invece che su un disegno piatto.

**Esempio:** `heat3d-dota-maps level -o levels/dota.glb` -> `levels/dota.glb`,
nelle unità e negli assi delle tabelle Dota del Watcher: nessun posizionamento o ridimensionamento
nel visualizzatore.

**Un progetto a sé:** Ogni lettore di un gioco è un piccolo progetto a sé, con il proprio file di
licenza, i propri rilasci e il proprio tracker delle issue, così può essere installato, aggiornato,
mantenuto - o ritirato su richiesta di un titolare dei diritti - da solo, senza toccare il
visualizzatore o gli altri strumenti.

## Avvio rapido {#quick-start}

Non hai mai usato la riga di comando? Leggi prima [Prima di iniziare](before-you-start.md).
Ti servono Python 3.10 o successivo, Dota 2 installato tramite Steam e la riga di comando di
Source2Viewer (un download gratuito con licenza MIT, vedi
[Trovare le cose: list](list.md)). Esegui questi comandi nella cartella in cui hai clonato o
decompresso lo strumento:

```bash
python -m pip install -e .                  # installa il comando heat3d-dota-maps
heat3d-dota-maps list                       # dove si trovano Dota 2 e Source2Viewer, le mappe installate
heat3d-dota-maps level -o levels/dota.glb   # la mappa normale come livello
```

Da `list` dovresti vedere `Dota 2 at ...`, una riga per mappa e `Source2Viewer CLI at ...`;
`level` termina con una riga del tipo
`levels/dota.glb: dota, 700,000 triangles ... 2,400 trees, 70 buildings`.
Poi carica `levels/dota.glb` nel pannello **Sfondo / livello** del visualizzatore, con
**Modello 3D…**: il visualizzatore lo conserva nella sua libreria dei livelli, e il suo pulsante
**Mappa di Dota 2** lo carica da quel momento in poi ([Costruire un livello](level.md#loading-it-in-the-viewer)).

Il livello è costruito dai file del gioco e resta **sul tuo computer** ([Termini](terms.md)).

## Pagine {#pages}

| Pagina | Cosa contiene |
|---|---|
| [Prima di iniziare](before-you-start.md) | Python, Source2Viewer, un terminale, una prima esecuzione |
| [Trovare le cose: list](list.md) | dove vengono trovati Dota 2 e la CLI di Source2Viewer, cosa stampa `list` |
| [Costruire un livello: level](level.md) | ogni opzione, come è fatto il livello, le sue parti, come è stato verificato |
| [Termini e licenza](terms.md) | la mappa di Valve, la licenza di Source2Viewer, questo strumento come progetto a sé |
| [Riferimento dei comandi](../cli-reference.md) | ogni opzione, generata dal codice |
| [Manutenzione di questa documentazione](maintaining.md) | la lista di controllo per ogni rilascio |

## Collegamenti {#related}

- Il visualizzatore 3DHeat: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentazione su [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Le tabelle dei replay di Dota 2 sotto cui si collocano questi livelli: il
  [3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html).
- Le mappe di Counter-Strike 2 con la stessa CLI di Source2Viewer:
  [3DHeat CS2](https://holdi601.github.io/3DHeat-CS2/).

## Gli strumenti 3DHeat {#the-3dheat-tools}

| Strumento | Cosa fa | Codice | Documentazione |
|---|---|---|---|
| visualizzatore 3DHeat | mostra i dati: mappe di calore, analisi di gara, revisione delle partite | [3DHeat](https://github.com/Holdi601/3DHeat) | [documentazione](https://holdi601.github.io/3DHeat/) |
| GameFiles | livelli e percorsi dai file propri di un gioco | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [documentazione](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | telemetria dei giri, e livelli ricostruiti dal video di gioco | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [documentazione](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin per Unreal Editor: un livello come un unico `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [documentazione](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | demo e mappe di Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [documentazione](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | registra ciò che i giochi pubblicano mentre giochi | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [documentazione](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | replay di War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [documentazione](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | replay di World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [documentazione](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | replay di World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [documentazione](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | demo dei server di Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | mappe di DCS World come livelli 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [documentazione](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | mappe di IL-2 Sturmovik come livelli 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [documentazione](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | la mappa di Dota 2 come livello 3D | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | replay di Dota 2 | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [documentazione](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | replay di League of Legends e VALORANT (ciò che contengono in chiaro) | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | percorsi, gare e auto di Forza dalla tua installazione | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | livelli di Battlefield (Frostbite) come livelli 3D | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | percorsi di BeamNG.drive | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [documentazione](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | tappe di Assetto Corsa Rally come percorsi | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [documentazione](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | mondi di Arma Reforger (Enfusion) come livelli 3D | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | replay di partite di Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [documentazione](https://holdi601.github.io/3DHeat-Ext-R6/) |
