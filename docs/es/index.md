---
title: Inicio
nav_order: 1
lang: "es"
source: index.md
source_hash: "3e8858fb1b90"
nav_exclude: true
search_exclude: true
permalink: /es/
---
# 3DHeat Dota {#dheat-dota}

**¿Qué es?** Esta herramienta convierte el mapa de Dota 2, leído de **tu propia instalación**,
en un nivel 3D: un modelo del mapa sobre el que puedes volar. Es para el visor
[3DHeat](https://github.com/Holdi601/3DHeat)
([documentación](https://holdi601.github.io/3DHeat/)): el suelo, los acantilados,
el río, cada árbol y los edificios.

**¿Para qué la usaría?** Para ver partidas de Dota 2 (las tablas de repeticiones que
escribe el [3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html))
sobre el mapa propio del juego, en 3D, en vez de un dibujo plano.

**Ejemplo:** `heat3d-dota-maps level -o levels/dota.glb` -> `levels/dota.glb`,
en las unidades y ejes de las tablas de Dota del Watcher: sin colocar ni escalar nada en
el visor.

**Un proyecto propio:** Cada lector de un juego es un pequeño proyecto propio, con su propio archivo de licencia, sus versiones y su gestor de incidencias, así que puede instalarse, actualizarse, mantenerse (o retirarse a petición de un titular de derechos) por sí solo, sin afectar al visor ni a las demás herramientas.

## Inicio rápido {#quick-start}

¿Nunca has usado la línea de comandos? Lee primero [Antes de empezar](before-you-start.md).
Necesitas Python 3.10 o posterior, Dota 2 instalado a través de Steam y
la línea de comandos de Source2Viewer (una descarga gratuita con licencia MIT, ver
[Encontrar cosas: list](list.md)). Ejecuta estos comandos en la carpeta que clonaste o descomprimiste:

```bash
python -m pip install -e .                  # instala el comando heat3d-dota-maps
heat3d-dota-maps list                       # dónde están Dota 2 y Source2Viewer, los mapas instalados
heat3d-dota-maps level -o levels/dota.glb   # el mapa normal como nivel
```

Deberías ver `Dota 2 at ...`, una línea por mapa y `Source2Viewer CLI at ...`
al ejecutar `list`; `level` termina con una línea como
`levels/dota.glb: dota, 700,000 triangles ... 2,400 trees, 70 buildings`.
Después carga `levels/dota.glb` en el panel **Fondo / nivel** del visor con
**Modelo 3D…**: el visor lo guarda en su biblioteca de niveles, y su botón **Mapa de Dota 2**
lo carga desde entonces ([Crear un nivel](level.md#cargarlo-en-el-visor)).

El nivel se crea a partir de los archivos del juego y se queda **en tu equipo** ([Condiciones](terms.md)).

## Páginas {#pages}

| Página | Qué contiene |
|---|---|
| [Antes de empezar](before-you-start.md) | Python, Source2Viewer, una terminal, una primera ejecución |
| [Encontrar cosas: list](list.md) | dónde se encuentran Dota 2 y la línea de comandos de Source2Viewer, qué muestra `list` |
| [Crear un nivel: level](level.md) | cada opción, cómo se crea el nivel, sus partes, cómo se comprobó |
| [Condiciones y licencia](terms.md) | el mapa de Valve, la licencia de Source2Viewer, esta herramienta como proyecto propio |
| [Referencia de comandos](../cli-reference.md) | cada opción, generada desde el código |
| [Mantener estos documentos](maintaining.md) | la lista de comprobación de cada versión |

## Relacionado {#related}

- El visor 3DHeat: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentación en [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Las tablas de repeticiones de Dota 2 en las que se sitúan estos niveles: el
  [3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html).
- Mapas de Counter-Strike 2 con la misma línea de comandos de Source2Viewer:
  [3DHeat CS2](https://holdi601.github.io/3DHeat-CS2/).

## Las herramientas de 3DHeat {#the-3dheat-tools}

| Herramienta | Qué hace | Código | Documentación |
|---|---|---|---|
| visor 3DHeat | muestra los datos: mapas de calor, análisis de carreras, revisión de partidas | [3DHeat](https://github.com/Holdi601/3DHeat) | [documentación](https://holdi601.github.io/3DHeat/) |
| GameFiles | niveles y circuitos a partir de los archivos propios de un juego | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [documentación](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | telemetría de vueltas, y niveles reconstruidos a partir de vídeo de juego | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [documentación](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin del editor de Unreal: un nivel como un solo `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [documentación](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | demos y mapas de Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [documentación](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | registra lo que los juegos publican mientras juegas | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [documentación](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | repeticiones de War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [documentación](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | repeticiones de World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [documentación](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | repeticiones de World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [documentación](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | demos de servidores de Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [documentación](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | mapas de DCS World como niveles 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [documentación](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | mapas de IL-2 Sturmovik como niveles 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [documentación](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | el mapa de Dota 2 como nivel 3D | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [documentación](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | repeticiones de Dota 2 | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [documentación](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | repeticiones de League of Legends y VALORANT (lo que contienen sin cifrar) | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [documentación](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | circuitos, carreras y coches de Forza a partir de tu propia instalación | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [documentación](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | niveles de Battlefield (Frostbite) como niveles 3D | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [documentación](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | circuitos de BeamNG.drive | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [documentación](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | tramos de Assetto Corsa Rally como circuitos | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [documentación](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | mundos de Arma Reforger (Enfusion) como niveles 3D | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [documentación](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | repeticiones de partidas de Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [documentación](https://holdi601.github.io/3DHeat-Ext-R6/) |
