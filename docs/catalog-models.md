---
title: Catalogue and models
nav_order: 4
---

# Catalogue and models: `catalog`, `models`

```
heat3d-dota-maps catalog      # heroes, units and items: $HEAT3D_LEVELS/dota/catalog.json
heat3d-dota-maps models       # hero and unit models: $HEAT3D_LEVELS/model-packs/dota/
```

Without `HEAT3D_LEVELS` both write into the current folder; `-o` names
another place. Both need Dota 2 and Source2Viewer's CLI, as `level` does.

**`catalog`** reads the hero scripts (`scripts/npc/heroes/`), the units
(`npc_units.txt`), the items (`items.txt`) and the English names. It writes
each hero with its attribute, attack type, roles, abilities and base numbers,
each unit with its group (creep, neutral, building, summon, ward, courier) and
numbers, and each shop item with its cost. The viewer uses it to name, group
and filter what a match holds.

**`models`** exports each hero (with its default items) and each unit that
has a model, poses it at the first frame of its idle animation, simplifies it
to three levels of detail and writes one `.glb` per unit with a
`model-pack.json` index. The viewer then draws these models in place of its
own figures. `--only axe pudge` builds just those.

Both stay on your machine: the viewer reads them from there, and nothing is
uploaded or shared.
