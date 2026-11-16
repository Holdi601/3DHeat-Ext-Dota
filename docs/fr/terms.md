---
title: "Conditions et licence"
nav_order: 8
lang: "fr"
source: terms.md
source_hash: "04ca2f908fa5"
nav_exclude: true
search_exclude: true
---
# Conditions et licence {#terms-and-licence}

## La carte de Valve {#valves-map}

3DHeat Dota n'est ni affilié à Valve ni approuvé par Valve. Dota 2 et les noms et marques
associés appartiennent à leurs propriétaires. Cet outil ne livre rien du jeu et ne
télécharge rien : il lit les fichiers de la copie **que vous** avez installée, sur votre
machine, par Source2Viewer, en dehors du jeu. Il ne modifie rien dans le jeu et ne parle à
aucun serveur. Le niveau qu'il écrit reste sur votre machine, pour le voir dans le
visualiseur 3DHeat.

## Un projet à part {#its-own-project}

Chaque lecteur de jeu est un petit projet à part, avec son propre fichier de licence, ses
propres versions et son propre suivi des tickets : il peut être installé, mis à jour,
maintenu - ou retiré à la demande d'un ayant droit - seul, sans toucher au visualiseur ni
aux autres outils.

Ayants droit : ouvrez un ticket sur
[3DHeat-Ext-Dota/issues](https://github.com/Holdi601/3DHeat-Ext-Dota/issues) - nous
répondons vite et retirons tout ce qui est demandé.

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
