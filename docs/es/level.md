---
title: "Crear un nivel: level"
nav_order: 3
lang: "es"
source: level.md
source_hash: "6af25f0a3539"
nav_exclude: true
search_exclude: true
---
# Crear un nivel: `level` {#building-a-level-level}

```bash
heat3d-dota-maps level [<map>] -o <file.glb> [--game FOLDER] [--source2viewer EXE] [--detail UNITS]
```

escribe el mapa de Dota 2 como geometría de nivel para el visor 3DHeat: el suelo, los
acantilados, el agua, cada árbol y los edificios, en el marco y las unidades en que se dibujan las
[tablas de repeticiones de Dota 2](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html)
del 3DHeat Watcher. Código:
[`heat3d_ext_dota/dota_map.py`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/heat3d_ext_dota/dota_map.py).

| Opción | Hace |
|---|---|
| `<map>` | el nombre del mapa tal como lo muestra [`list`](list.md) (por defecto `dota`, el mapa normal), o la ruta al `.vpk` de un mapa |
| `-o`, `--out FILE` | el `.glb` a escribir (obligatorio); su carpeta se crea si no existe |
| `--game FOLDER` | la carpeta `dota 2 beta` o su carpeta `game\dota`, cuando Dota 2 no está en ninguna biblioteca de Steam |
| `--source2viewer EXE` | la CLI de Source2Viewer, cuando no se encuentra por sí sola ([list](list.md) dice dónde busca) |
| `--detail UNITS` | el tamaño de celda de la agrupación de vértices de los edificios, en unidades del juego (por defecto 8; 0 conserva cada triángulo) |

## Cargarlo en el visor {#loading-it-in-the-viewer}

Carga el `.glb` en el panel **Fondo / nivel** del visor (**Modelo 3D…**)
bajo una tabla de Dota y el calor de los héroes queda sobre los carriles, las torres sobre sus
torres. El visor reconoce el archivo por sus partes y lo guarda en su
[biblioteca de niveles](https://holdi601.github.io/3DHeat/level-library.html); desde entonces
su botón **Mapa de Dota 2** carga este mapa 3D en lugar del dibujo de OpenDota.

Esta herramienta no contiene nada del juego ni lo descarga: el mapa sale de tu propia instalación, y el archivo que escribe se queda en tu equipo ([Condiciones](terms.md)).

## Cómo se crea {#how-it-is-made}

1. **La malla de colisión.** Source2Viewer exporta de `maps/<map>.vpk` el
   `maps/<map>/world_physics.vmdl_c` del mapa como glTF. Sus grupos
   llevan nombre según la superficie. Se descartan los grupos llamados `clip` (los muros invisibles) o `sky`. Los grupos llamados `water`, `slime` o `window` son **agua**: el río
   y los estanques son `water_slime`, los arroyos estrechos de la jungla son
   `window`; en una repetición, los héroes están entre 10 y 16 unidades bajo el primero y unas
   pocas unidades bajo el segundo. Solo se conservan sus caras superiores. Lo demás es el
   terreno, dividido cara por cara: una cara cuya normal apunta hacia arriba al menos 0.7
   (pendientes de hasta unos 45 grados) es **suelo**; el resto (caras de acantilado, los
   muros del mapa) es **estructura**.
2. **Las entidades.** Source2Viewer descompila los bloques de entidades del mapa
   (`maps/<map>/entities/*.vents_c`) a texto: bloques con cabecera `====<n>====`, una
   `clave valor` por línea. Se usan los bloques `default_ents` y cada capa de mundo
   (una entidad `info_world_layer`) que se muestra al inicio (indicador de aparición 1): las
   capas de las dos bases. Se dejan fuera las capas que empiezan ocultas, que contienen lo que aparece cuando cae una base.
3. **Qué se dibuja.** Los árboles (`ent_dota_tree`) y los edificios: torres,
   cuarteles, los antiguos (`npc_dota_fort`), los edificios de relleno (`npc_dota_building`),
   puestos avanzados, fuentes, santuarios de sabiduría, estanques de loto, puertas gemelas, vigías
   (`npc_dota_lantern`) y los almacenes de objetos neutrales. No se dibujan las tiendas (un tendero es un
   personaje), el salón de la fama, las pancartas, las luces ni las partículas.
4. **Los modelos.** Cada modelo que nombran estas entidades se exporta de
   `game\dota\pak01_dir.vpk` en una sola ejecución de Source2Viewer. Las mallas de un modelo que son
   otro estado de la misma cosa (el tocón de un árbol talado, el primer plano que se muestra
   en el inspector, los escombros) se dejan fuera por su nombre (`stump`, `inspector`,
   `destruction`).
5. **Los edificios** son la malla propia de su modelo, aligerada por **agrupación de vértices**:
   cada punto se mueve a la media de los puntos dentro de su cubo de tamaño `--detail`
   (por defecto 8 unidades, un tercio aproximadamente del ancho de un héroe), y desaparecen los triángulos que se colapsan o se repiten. 0 conserva cada triángulo.
6. **Los árboles** son el contorno de cada modelo como un sólido bajo de revolución: su altura en cinco
   bandas, cada una un anillo de seis lados tan ancho como la mayoría de los puntos del modelo a esa
   altura (el percentil 90 de su distancia al eje del tronco), cerrado por abajo y acabado en punta
   por arriba: 60 triángulos, la altura y el ancho reales del modelo. Un pino sale como un cono, un roble como una bola sobre un tronco. Las mallas reales pesarían unas diez veces más en los más de 2.000 árboles.
7. **Colocados** como los pone el juego: escalados por `scales`, girados por `angles`
   (cabeceo, guiñada y alabeo de Source en grados), movidos a `origin`.
8. **Al marco del visor.** Source2Viewer escribe glTF en metros, con Y hacia arriba: (Y, Z, X) del
   juego por 0.0254. Eso se deshace, y cada punto se escribe como (X, Z, -Y) del
   juego: Y hacia arriba, con la Y del juego invertida; es el marco en que se dibujan las tablas de Dota mediante sus pistas `heat3d` (`up: z`, `flipY: true`, escala 1).
   Es una rotación, no un espejo.

## El archivo {#the-file}

Un binario glTF 2.0 como el de la herramienta 3DHeat CS2 (ver su página de exportación de mapas): un
nodo y una malla por parte en la raíz, sin transformaciones, con sombreado plano (un vértice
por esquina de triángulo que lleva la normal de su triángulo), índices `uint32`, sin
materiales, texturas ni UV, `asset.generator` `heat3d_ext_dota`, unidades del juego.

| Parte | Qué es |
|---|---|
| `ground:terrain` | el suelo por el que se puede caminar |
| `structure:terrain` | caras de acantilado y los muros del mapa |
| `water:water_slime`, `water:window` | el río y los estanques; los arroyos de la jungla |
| `structure:tree` | cada árbol que está en pie al inicio |
| `structure:tower`, `structure:barracks`, `structure:ancient`, `structure:filler`, `structure:outpost`, `structure:fountain`, `structure:shrine`, `structure:lotus_pool`, `structure:twin_gate`, `structure:watcher`, `structure:neutral_stash` | los edificios, por tipo |

El prefijo `ground:` / `structure:` / `water:` es la forma en que todos los exportadores de niveles 3DHeat
indican al visor qué es cada parte; el visor les cree. Como las unidades son las del juego (unas
2,5 cm cada una), otro visor de glTF muestra el mapa unas 39 veces más grande; en 3DHeat queda
exactamente bajo la tabla.

Lo que imprime, en una ejecución de ejemplo (los números dependen de la versión del mapa):

```text
reading dota.vpk: collision mesh and entities
reading 30 models from pak01_dir.vpk
dota.glb: dota, 700,000 triangles (230,000 ground) in 16 parts; 2,400 trees, 70 buildings
```

Las dos primeras líneas van al flujo de errores, la última a la salida. Un modelo que Source2Viewer
no encontró se deja fuera y se nombra al final de la última línea
(`; 1 model(s) not found, left out: ...`). Los errores imprimen `heat3d-dota-maps: <motivo>`: Dota 2, el mapa o Source2Viewer no encontrados salen con código 2; si Source2Viewer falla, con código 1.

## Cómo se comprobó {#how-it-was-checked}

Con una repetición de una partida pública convertida por el 3DHeat Watcher (parche 7.40) y el mapa del
juego instalado:

- cada muestra de posición de héroe mira hacia abajo y encuentra suelo en la cara más alta
  a no más de 64 unidades sobre sus pies; la altura media sobre él es
  0 unidades, y el 99,5 % están a 16 unidades; con el mapa reflejado (Y sin invertir) solo
  unas la mitad encuentran suelo, y el resto flota o se hunde la altura de un acantilado;
- las 22 torres, 12 cuarteles, 2 antiguos, 14 edificios de relleno, 2 puestos avanzados, 2 fuentes
  y 10 vigías que coloca la tabla de unidades de la repetición están sobre las entidades del mapa del mismo
  tipo, con un error de 0,02 unidades como máximo, en horizontal y en altura;
- el pie de cada árbol está sobre el suelo.

Las pruebas ([`tests/test_dota_map.py`](https://github.com/Holdi601/3DHeat-Ext-Dota/blob/main/tests/test_dota_map.py)) comprueban el lector de bloques, los marcos, la división del terreno, los contornos y la agrupación de árboles, la colocación y la exportación completa con Source2Viewer sustituido por un doble: solo con datos inventados.

## Lo que no hace {#what-it-does-not-do}

- Sin texturas ni colores: el visor sombrea el nivel a su manera.
- Sin árboles talados ni edificios destruidos durante una partida: el mapa tal como empieza.
- Los mapas de eventos y personalizados no están probados; sus clases de entidades pueden ser distintas.
- Los elementos que solo decoran (rocas, vallas, pancartas) están en él solo en la medida en que forman parte de la malla de colisión.
