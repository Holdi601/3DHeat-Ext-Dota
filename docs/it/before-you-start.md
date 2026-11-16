---
title: Prima di iniziare
nav_order: 1.5
lang: "it"
source: before-you-start.md
source_hash: "8978ef7afccc"
nav_exclude: true
search_exclude: true
---
# Prima di iniziare {#before-you-start}

Non hai mai usato la riga di comando? Questa pagina ti porta da zero a una prima esecuzione.
Richiede circa quindici minuti, una volta sola.

## 1. Installa Python {#install-python}

Questo strumento richiede **Python 3.10 o successivo**.

- **Windows:** scarica Python da [python.org/downloads](https://www.python.org/downloads/)
  ed esegui il programma di installazione. Nella sua prima schermata spunta **Add python.exe to PATH**,
  poi clicca su **Install Now**.
- **macOS e Linux:** Python 3 spesso c'è già. Dove queste pagine dicono
  `python`, scrivi `python3`.

## 2. Ottieni questo strumento {#get-this-tool}

Apri [github.com/Holdi601/3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota), clicca sul
pulsante verde **Code**, poi su **Download ZIP**, e decomprimilo in una cartella a tua scelta.
Se usi git: `git clone https://github.com/Holdi601/3DHeat-Ext-Dota`.

## 3. Ottieni la riga di comando di Source2Viewer {#get-source2viewers-command-line}

Source2Viewer (ValveResourceFormat, licenza MIT) legge i file compressi di Dota 2.
Apri la sua [pagina delle versioni](https://github.com/ValveResourceFormat/ValveResourceFormat/releases),
scarica la versione **CLI** per il tuo sistema e decomprimi `Source2Viewer-CLI.exe`
(su macOS e Linux `Source2Viewer-CLI`) nella cartella del passo 2. Basta questo: lo strumento
lo cerca lì. [Trovare le cose: list](list.md) dice dove altro lo cerca.

## 4. Apri un terminale in quella cartella {#open-a-terminal-in-that-folder}

Un terminale è una finestra in cui scrivi i comandi.

- **Windows:** apri la cartella in Esplora risorse, clicca nella barra degli indirizzi, scrivi
  `powershell` e premi Invio. Si apre una finestra blu o nera, già in quella cartella.
- **macOS:** apri **Terminale**, scrivi `cd ` (con lo spazio), trascina la cartella nella
  finestra e premi Invio.

`cd` significa "cambia cartella": `cd C:\Tools\3DHeat-Ext-Dota` va in quella cartella.

## 5. Installa lo strumento {#install-the-tool}

Scrivi questo e premi Invio:

```bash
python -m pip install -e .
```

Alla fine dovresti vedere: `Successfully installed heat3d-ext-dota-...`.

## 6. Eseguilo {#run-it}

```bash
heat3d-dota-maps list
```

Dovresti vedere qualcosa del genere:

```text
Dota 2 at C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota
  dota                         29.0 MB
  ...
Source2Viewer CLI at C:\Tools\3DHeat-Ext-Dota\Source2Viewer-CLI.exe
```

Avanti: [Costruire un livello: level](level.md).

## Come leggere i comandi di queste pagine {#how-to-read-the-commands-on-these-pages}

| Vedi | Significa |
|---|---|
| `<file.glb>` | un segnaposto: scrivi invece il tuo valore, senza i `< >` |
| `[--detail UNITS]` | facoltativo: omettilo, oppure scrivilo come mostrato |
| `# a note` | un commento per te: non scriverlo |
| `"C:\My Files\x"` | metti tra virgolette un percorso che contiene spazi |

## Quando qualcosa va storto {#when-something-goes-wrong}

| Il messaggio | Cosa fare |
|---|---|
| `'python' is not recognized` | Python non è installato, oppure non era spuntata la casella PATH: installalo di nuovo e spuntala (o scrivi `py` al posto di `python`). |
| `'heat3d-dota-maps' is not recognized` | Esegui di nuovo il passo 5 nella cartella dello strumento, oppure scrivi `python -m heat3d_ext_dota` al posto di `heat3d-dota-maps`: fa la stessa cosa. |
| `No module named heat3d_ext_dota` | Non sei nella cartella dello strumento, oppure il passo 5 non è riuscito: vai lì con `cd` ed esegui il passo 5. |
| `Dota 2 not found in any Steam library` | Installa Dota 2 tramite Steam, oppure indica la sua cartella: `--game "D:\Games\Steam\steamapps\common\dota 2 beta"`. |
| `Source2Viewer-CLI not found` | Fai il passo 3, oppure indica il suo percorso: `--source2viewer <path to Source2Viewer-CLI.exe>`. |
| qualsiasi altra cosa | Leggi l'ultima riga del messaggio, poi apri una segnalazione su GitHub con quella riga. |

Ogni comando termina anche con uno **stato di uscita**: 0 significa che ha funzionato, 2 che
Dota 2, la mappa o Source2Viewer non sono stati trovati, 1 che la lettura è fallita. Per vederlo,
scrivi `echo $LASTEXITCODE` in PowerShell oppure `echo $?` su macOS e Linux.
