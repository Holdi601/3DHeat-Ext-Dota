"""
The map's layout for the viewer (`<map>.layouts.json`, beside its level): towers, barracks, the ancients,
outposts, shrines, the lotus pools and twin gates, Roshan's and the runes' spawns as objectives; the fountains as
each side's base; where heroes, couriers and the lane creeps start, and the neutral camps, as spawns. All from the
map's entity lumps (`dota_map.entities_of`), in the level's frame: game units (X, Z, -Y), as the level is written.

Sides: Radiant (the game's team 2) is team 1, Dire (team 3) team 2.
"""

from __future__ import annotations

import json
import re
import tempfile
from pathlib import Path
from typing import Any, Callable

from . import dota_map

FORMAT = "3dheat-layouts"
TEAMS = {"2": 1, "3": 2}
TEAM_NAMES = {"1": "Radiant", "2": "Dire"}

#: Entity class -> (layout kind, objective type or spawn, what it is called).
OBJECTIVES = {
    "npc_dota_tower": ("objective", "tower", "Tower"),
    "npc_dota_barracks": ("objective", "barracks", "Barracks"),
    "npc_dota_fort": ("objective", "ancient", "Ancient"),
    "npc_dota_watch_tower": ("objective", "outpost", "Outpost"),
    "npc_dota_xp_fountain": ("objective", "shrine", "Wisdom shrine"),
    "npc_dota_lotus_pool": ("objective", "lotus_pool", "Lotus pool"),
    "npc_dota_unit_twin_gate": ("objective", "twin_gate", "Twin gate"),
    "npc_dota_roshan_spawner": ("objective", "roshan", "Roshan"),
    "npc_dota_miniboss_spawner": ("objective", "tormentor", "Tormentor"),
    "dota_item_rune_spawner_powerup": ("objective", "rune", "Power rune"),
    "dota_item_rune_spawner_bounty": ("objective", "rune", "Bounty rune"),
    "ent_dota_fountain": ("base", "fountain", "Fountain"),
}
SPAWNS = {
    "info_player_start_goodguys": ("spawn", "Heroes", "hero"),
    "info_player_start_badguys": ("spawn", "Heroes", "hero"),
    "npc_dota_neutral_spawner": ("vehicle_spawn", "Neutral camp", "neutrals"),
}
_COURIER = re.compile(r"^info_courier_spawn_(radiant|dire)")
_LANE = re.compile(r"^npc_dota_spawner_(good|bad)_(top|mid|bot)$")
_NAME = re.compile(r"(tower\d)_(top|mid|bot)|(melee|range)_rax_(top|mid|bot)|rax_(melee|range)_(top|mid|bot)")


def _key(e: dota_map.Entity, k: str) -> str:
    return dota_map._text(e.keys.get(k, ""))


def _team(e: dota_map.Entity, cls: str) -> int | None:
    t = TEAMS.get(_key(e, "teamnumber"))
    if t is None:
        low = cls + " " + _key(e, "targetname").lower()
        t = 1 if re.search(r"good|radiant", low) else 2 if re.search(r"bad|dire", low) else None
    return t


def _pos(e: dota_map.Entity) -> list[float]:
    x, y, z = e.origin
    return [round(x, 1), round(z, 1), round(-y, 1)]


def layout(entities: list[dota_map.Entity], level: str, tool: str) -> dict[str, Any]:
    objectives: list[dict[str, Any]] = []
    spawns: list[dict[str, Any]] = []
    for e in entities:
        cls = e.classname
        if cls in OBJECTIVES:
            typ, kind, name = OBJECTIVES[cls]
            target = _key(e, "targetname").replace("[PR#]", "")
            m = _NAME.search(target)
            label = name
            if m and kind == "tower":
                label = f"Tower {m.group(1)[-1]} {m.group(2)}"
            elif m and kind == "barracks":
                label = f"{(m.group(3) or m.group(5)).capitalize()} barracks {m.group(4) or m.group(6)}"
            obj = {"type": typ, "kind": kind, "name": label, "team": _team(e, cls), "position": _pos(e),
                   "entity": cls, **({"targetname": target} if target else {})}
            if kind in ("roshan", "rune", "tormentor", "lotus_pool", "twin_gate"):
                obj["team"] = None
            objectives.append(obj)
        elif cls in SPAWNS:
            typ, base, vehicle = SPAWNS[cls]
            spawns.append({"type": typ, "team": None if vehicle == "neutrals" else _team(e, cls), "base": base,
                           "vehicle": vehicle, "position": _pos(e)})
        elif _COURIER.match(cls):
            spawns.append({"type": "vehicle_spawn", "team": 1 if "radiant" in cls else 2, "base": "Courier",
                           "vehicle": "courier", "position": _pos(e)})
        else:
            m = _LANE.match(cls)
            if m:
                spawns.append({"type": "vehicle_spawn", "team": 1 if m.group(1) == "good" else 2,
                               "base": f"Creeps {m.group(2)}", "vehicle": "creeps", "position": _pos(e)})
    return {"format": FORMAT, "version": 1, "game": "dota", "level": level, "source": tool, "units": "game units",
            "up": "y", "coordinates": "the level's frame: game units (X, Z, -Y)", "teams": TEAM_NAMES,
            "layouts": [{"id": "default", "name": "All Pick", "mode": "default",
                         "aliases": ["all_pick", "ranked", "turbo", "captains_mode"],
                         "objectives": objectives, "zones": [], "spawns": spawns}]}


def export_layouts(name: str, out: str | Path, game: str | None = None, source2viewer: str | None = None,
                   tool_name: str = "", say: Callable[[str], None] = lambda _: None) -> str:
    """Writes the map's layouts to `out` (a .json, or a folder for `<map>.layouts.json`); returns what it holds."""
    folder = dota_map.game_folder(game)
    vpk = dota_map.find_vpk(name, folder)
    tool = dota_map.find_source2viewer(source2viewer)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        say(f"reading {vpk.name}: entities")
        dota_map._run(tool, vpk, [f"maps/{vpk.stem}/entities/"], tmp / "entities", extensions="vents_c")
        lumps = {f.stem: f.read_text(encoding="utf-8", errors="replace") for f in (tmp / "entities").rglob("*.vents")}
    if "default_ents" not in lumps:
        raise RuntimeError(f"{vpk.stem} has no entity lump Source2Viewer could read")
    target = Path(out)
    level = target.name[: -len(".layouts.json")] if target.name.endswith(".layouts.json") else vpk.stem
    if not target.name.endswith(".json"):
        target = target / f"{level}.layouts.json"
    doc = layout(dota_map.entities_of(lumps), level, tool_name)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(doc, indent=1), encoding="utf-8")
    lay = doc["layouts"][0]
    return f"{target}: {len(lay['objectives'])} objectives, {len(lay['spawns'])} spawns"
