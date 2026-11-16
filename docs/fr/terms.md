---
title: "Conditions et licence"
nav_order: 8
lang: "fr"
source: terms.md
source_hash: "0c470cb49eea"
nav_exclude: true
search_exclude: true
---
# Conditions et licence {#terms-and-licence}

## La carte de Valve {#valves-map}

Dota 2 et sa carte appartiennent à Valve, qui ne cautionne pas ce projet. Cet outil ne
livre rien du jeu et ne télécharge rien : il lit les fichiers de la copie
**que vous** avez installée, sur votre machine, par Source2Viewer, en dehors du
jeu. Il ne modifie rien dans le jeu et ne parle à aucun serveur. Le niveau qu'il
écrit est une œuvre dérivée de la carte de Valve : il est à vous pour le voir dans le visualiseur 3DHeat, pas pour le partager ou le publier. Utiliser l'outil est votre
décision, selon les conditions que vous avez acceptées pour Dota 2 et Steam.

C'est pourquoi c'est un paquet séparé : si Valve demande un jour qu'il disparaisse, il
disparaît seul, et le visualiseur, le Watcher et les autres outils restent.

## Source2Viewer {#source2viewer}

La lecture des fichiers compilés de Source 2 est faite par la ligne de commande de Source2Viewer
(ValveResourceFormat, licence MIT,
[github.com/ValveResourceFormat/ValveResourceFormat](https://github.com/ValveResourceFormat/ValveResourceFormat)).
Elle ne fait pas partie de cet outil et n'y est pas incluse : vous la téléchargez
vous-même, et cet outil se contente de la lancer. Voir
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/LICENSES.md).

## Licence et sources {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/LICENSE)). Demande numpy
(BSD-3-Clause) ; les tests demandent pytest (MIT). Écrit pour ce projet ; aucun code
n'a été pris à un autre projet.
