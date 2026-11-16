---
title: "Costruire un livello: level"
nav_order: 3
lang: "it"
source: level.md
source_hash: "6af25f0a3539"
nav_exclude: true
search_exclude: true
---
# Costruire un livello: `level` {#building-a-level-level}

```bash
heat3d-dota-maps level [<map>] -o <file.glb> [--game FOLDER] [--source2viewer EXE] [--detail UNITS]
```

scrive la mappa di Dota 2 come geometria di livello per il visualizzatore 3DHeat: il suolo, le
scogliere, l'acqua, ogni albero e gli edifici, nel sistema di riferimento e nelle unità in cui sono
disegnate le [tabelle dei replay di Dota 2](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html)
del 3DHeat Watcher. Codice:
[`heat3d_ext_dota/dota_map.py`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/heat3d_ext_dota/dota_map.py).

| Opzione | Fa |
|---|---|
| `<map>` | il nome della mappa come lo stampa [`list`](list.md) (predefinito `dota`, la mappa normale), oppure il percorso del `.vpk` di una mappa |
| `-o`, `--out FILE` | il `.glb` da scrivere (obbligatorio); la sua cartella viene creata se manca |
| `--game FOLDER` | la cartella `dota 2 beta` o la sua cartella `game\dota`, quando Dota 2 non è in nessuna libreria Steam |
| `--source2viewer EXE` | la CLI di Source2Viewer, quando non viene trovata da sola ([list](list.md) dice dove la cerca) |
| `--detail UNITS` | la cella di raggruppamento dei vertici degli edifici in unità di gioco (predefinito 8; 0 mantiene ogni triangolo) |

## Caricarlo nel visualizzatore {#loading-it-in-the-viewer}

Carica il `.glb` nel pannello **Sfondo / livello** del visualizzatore (**Modello 3D…**) sotto una
tabella di Dota e il calore degli eroi si posa sulle corsie, le torri sulle torri della mappa. Il visualizzatore
riconosce il file dalle sue parti e lo conserva nella sua [libreria dei livelli](https://holdi601.github.io/3DHeat/level-library.html);
da quel momento il suo pulsante **Mappa di Dota 2** carica questa mappa 3D invece del disegno di OpenDota.

Nulla del gioco è contenuto in questo strumento né viene scaricato da esso: la mappa proviene dalla
tua installazione, e il file che scrive resta sul tuo computer ([Termini](terms.md)).

## Come è fatto {#how-it-is-made}

1. **La maglia di collisione.** Source2Viewer esporta da `maps/<map>.vpk` la
   `maps/<map>/world_physics.vmdl_c` della mappa in glTF. I suoi gruppi hanno nomi che indicano la superficie.
   I gruppi chiamati `clip` (i muri invisibili) o `sky` vengono eliminati. I gruppi chiamati `water`, `slime` o
   `window` sono **acqua**: il fiume e gli stagni sono `water_slime`, i ruscelli stretti nella giungla sono
   `window`; in un replay, gli eroi stanno 10-16 unità sotto i primi e poche unità sotto i secondi. Vengono
   tenute solo le loro facce superiori. Tutto il resto è il terreno, diviso faccia per faccia: una faccia la
   cui normale punta verso l'alto di almeno 0.7 (pendii fino a circa 45 gradi) è **suolo**, le altre - le
   facce delle scogliere, i muri della mappa - sono **struttura**.
2. **Le entità.** Source2Viewer decompila i blocchi di entità della mappa
   (`maps/<map>/entities/*.vents_c`) in testo: blocchi introdotti da `====<n>====`, una coppia `chiave valore`
   per riga. I blocchi usati sono `default_ents` e ogni livello di mondo (`info_world_layer`) che vi compare
   all'inizio (flag di spawn 1) - i livelli delle due basi. I livelli che iniziano nascosti contengono ciò che
   appare quando una base cade e vengono esclusi.
3. **Cosa viene disegnato.** Gli alberi (`ent_dota_tree`) e gli edifici: torri, caserme, gli antichi
   (`npc_dota_fort`), i riempitivi (`npc_dota_building`), gli avamposti, le fontane, i santuari della saggezza,
   gli stagni di loto, i cancelli gemelli, le vedette (`npc_dota_lantern`) e i depositi di oggetti neutrali.
   Negozi (un negoziante è un personaggio), la sala della fama, gli stendardi, le luci e le particelle non vengono disegnati.
4. **I modelli.** Ogni modello nominato da queste entità viene esportato da
   `game\dota\pak01_dir.vpk` in una sola esecuzione di Source2Viewer. Le mesh di un modello che sono
   un altro stato della stessa cosa - il ceppo di un albero abbattuto, il primo piano mostrato nell'ispettore,
   le macerie - vengono escluse per nome (`stump`, `inspector`, `destruction`).
5. **Gli edifici** sono la mesh stessa del loro modello, sfoltita per **raggruppamento dei vertici**:
   ogni punto si sposta nella media dei punti del suo cubo di dimensione `--detail` (predefinito 8 unità,
   circa un terzo della larghezza di un eroe), e i triangoli che collassano o si ripetono vengono eliminati.
   0 mantiene ogni triangolo.
6. **Gli alberi** sono il contorno di ogni modello come un solido basso e tornito: la sua altezza in cinque
   fasce, ognuna un anello di sei lati largo quanto la maggior parte dei punti del modello a quell'altezza
   (il 90° percentile della loro distanza dall'asse del tronco), chiuso in basso e a punta in alto - 60
   triangoli, l'altezza e la larghezza vere del modello. Un pino esce come un cono, una quercia come una
   palla su un fusto. Le mesh reali peserebbero circa dieci volte di più su oltre 2.000 alberi.
7. **Collocati** come li colloca il gioco: scalati da `scales`, ruotati da `angles` (beccheggio, imbardata e
   rollio di Source in gradi), spostati in `origin`.
8. **Nel sistema di riferimento del visualizzatore.** Source2Viewer scrive il glTF in metri, Y verso l'alto:
   (Y, Z, X) del gioco per 0.0254. Questo viene annullato, e ogni punto viene scritto come (X, Z, -Y) del gioco:
   Y verso l'alto, con la Y del gioco negata - il sistema in cui le tabelle Dota sono disegnate tramite i loro
   suggerimenti `heat3d` (`up: z`, `flipY: true`, scala 1). Una rotazione, non uno specchio.

## Il file {#the-file}

Un binario glTF 2.0 come quello dello strumento CS2 di 3DHeat (vedi la sua pagina sull'esportazione delle mappe):
un nodo e una mesh per parte alla radice, nessuna trasformazione, ombreggiatura piatta (un vertice per angolo di
triangolo che porta la normale del suo triangolo), indici `uint32`, nessun materiale, texture o UV,
`asset.generator` `heat3d_ext_dota`, unità quelle del gioco.

| Parte | Cosa |
|---|---|
| `ground:terrain` | il suolo calpestabile |
| `structure:terrain` | le facce delle scogliere e i muri della mappa |
| `water:water_slime`, `water:window` | il fiume e gli stagni; i ruscelli della giungla |
| `structure:tree` | ogni albero presente all'inizio |
| `structure:tower`, `structure:barracks`, `structure:ancient`, `structure:filler`, `structure:outpost`, `structure:fountain`, `structure:shrine`, `structure:lotus_pool`, `structure:twin_gate`, `structure:watcher`, `structure:neutral_stash` | gli edifici, per tipo |

Il prefisso `ground:` / `structure:` / `water:` è il modo in cui tutti gli esportatori di livelli 3DHeat
dicono al visualizzatore che cos'è una parte; il visualizzatore gli crede sulla parola. Poiché le unità
sono quelle del gioco (circa un pollice ciascuna), un altro visualizzatore glTF mostra la mappa circa 39
volte più grande; in 3DHeat si trova esattamente sotto la tabella.

Cosa stampa, in un'esecuzione di esempio (i numeri dipendono dalla versione della mappa):

```text
reading dota.vpk: collision mesh and entities
reading 30 models from pak01_dir.vpk
dota.glb: dota, 700,000 triangles (230,000 ground) in 16 parts; 2,400 trees, 70 buildings
```

Le prime due righe vanno al flusso degli errori, l'ultima all'output. Un modello che Source2Viewer non
riesce a trovare viene escluso e nominato alla fine dell'ultima riga (`; 1 model(s) not found, left out: ...`).
Gli errori stampano `heat3d-dota-maps: <perché>`: Dota 2, la mappa o Source2Viewer non trovati escono con
codice 2, Source2Viewer che fallisce con codice 1.

## Come è stato verificato {#how-it-was-checked}

Su un replay di una partita pubblica convertito dal 3DHeat Watcher (patch 7.40) e sulla mappa del gioco installato:

- ogni campione di posizione di un eroe, guardando dritto in giù, trova suolo nella faccia più alta che si trova
  al massimo 64 unità sopra i suoi piedi; l'altezza mediana sopra di esso è 0 unità, e il 99,5 % è entro 16 unità;
  con la mappa specchiata (Y non negata) solo circa la metà trova suolo e il resto galleggia o affonda di
  un'altezza di scogliera;
- le 22 torri, 12 caserme, 2 antichi, 14 riempitivi, 2 avamposti, 2 fontane e 10 vedette che la tabella delle
  unità del replay colloca stanno sulle entità della mappa dello stesso tipo, con uno scarto di 0,02 unità o
  meno, in orizzontale e in altezza;
- il piede di ogni albero è sul suolo.

I test ([`tests/test_dota_map.py`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/tests/test_dota_map.py))
verificano il lettore delle entità, i sistemi di riferimento, la divisione del terreno, i contorni degli alberi e
il raggruppamento, il posizionamento e l'intera esportazione con Source2Viewer sostituito da una controfigura - solo
su dati inventati.

## Cosa non fa {#what-it-does-not-do}

- Nessuna texture né colore: il visualizzatore ombreggia il livello a modo suo.
- Nessun albero abbattuto né edificio distrutto durante una partita: la mappa com'è all'inizio.
- Le mappe evento e personalizzate non sono verificate; le loro classi di entità possono essere diverse.
- Gli oggetti che servono solo a decorare (rocce, recinzioni, stendardi) sono nel livello solo nella misura in cui
  fanno parte della maglia di collisione.
