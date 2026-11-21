"""
Dota 2's catalogue from your own install: heroes, units and items with their
names, roles, attributes and key numbers, in the viewer's catalogue format
(`3dheat-catalog`, version 1).

Read with Source2Viewer's CLI from `pak01_dir.vpk`: `scripts/npc/heroes/*.txt`
(one file per hero), `scripts/npc/npc_units.txt`, `scripts/npc/items.txt` and
the English names in `resource/localization/abilities_english.txt`. Nothing is
written but the catalogue.
"""

from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

from . import kv

FORMAT = "3dheat-catalog"
GAME = "dota"

HERO_NUMBERS = {
    "StatusHealth": "health", "StatusMana": "mana", "ArmorPhysical": "armor", "MagicalResistance": "magicResist",
    "MovementSpeed": "moveSpeed", "MovementTurnRate": "turnRate", "AttackRange": "attackRange",
    "AttackDamageMin": "damageMin", "AttackDamageMax": "damageMax", "AttackRate": "attackRate",
    "AttributeBaseStrength": "strength", "AttributeBaseAgility": "agility", "AttributeBaseIntelligence": "intellect",
    "AttributeStrengthGain": "strengthGain", "AttributeAgilityGain": "agilityGain",
    "AttributeIntelligenceGain": "intellectGain", "VisionDaytimeRange": "visionDay", "VisionNighttimeRange": "visionNight",
    "ModelScale": "modelScale", "Complexity": "complexity",
}
UNIT_NUMBERS = {
    "StatusHealth": "health", "ArmorPhysical": "armor", "MovementSpeed": "moveSpeed", "AttackRange": "attackRange",
    "AttackDamageMin": "damageMin", "AttackDamageMax": "damageMax", "BountyGoldMin": "goldMin",
    "BountyGoldMax": "goldMax", "BountyXP": "xp", "Level": "level", "ModelScale": "modelScale",
}
ATTRIBUTE = {"DOTA_ATTRIBUTE_STRENGTH": "strength", "DOTA_ATTRIBUTE_AGILITY": "agility",
             "DOTA_ATTRIBUTE_INTELLECT": "intellect", "DOTA_ATTRIBUTE_ALL": "universal"}


def _number(text: str | None) -> float | int | None:
    if text is None:
        return None
    try:
        v = float(str(text).split()[0])
    except (ValueError, IndexError):
        return None
    return int(v) if v.is_integer() else round(v, 4)


def _numbers(entry: dict, base: dict, table: dict[str, str]) -> dict:
    out = {}
    for key, name in table.items():
        v = _number(entry.get(key, base.get(key)))
        if v is not None:
            out[name] = v
    return out


def unit_class(uid: str, entry: dict) -> str:
    """A unit's group, from its id and its base class."""
    base = (entry.get("BaseClass") or "").lower()
    for word, group in (("courier", "courier"), ("ward", "ward"), ("tower", "building"), ("barracks", "building"),
                        ("fort", "building"), ("_rax", "building"), ("filler", "building"), ("roshan", "roshan"), ("neutral", "neutral"), ("creep", "creep")):
        if word in uid or word in base:
            return group
    if entry.get("IsSummoned") == "1" or "summon" in uid:
        return "summon"
    return "unit"


def read_scripts(tool: Path, pak: Path, work: Path) -> dict[str, str]:
    """The script and localisation files the catalogue needs, as text, by archive path."""
    wanted = ["scripts/npc/heroes/", "scripts/npc/npc_units.txt", "scripts/npc/items.txt",
              "resource/localization/abilities_english.txt"]
    subprocess.run([str(tool), "-i", str(pak), "-f", ",".join(wanted), "-o", str(work)],
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
    return {f.relative_to(work).as_posix(): f.read_text("utf-8", "replace") for f in work.rglob("*.txt")}


def build_catalog(files: dict[str, str], *, game_build: str = "", source: str = "") -> dict:
    names = kv.tokens(files.get("resource/localization/abilities_english.txt", ""))
    items: list[dict] = []
    heroes: dict[str, dict] = {}
    base: dict = {}
    for path, text in sorted(files.items()):
        if not path.startswith("scripts/npc/heroes/"):
            continue
        for hid, entry in (kv.parse(text).get("DOTAHeroes") or {}).items():
            if not isinstance(entry, dict):
                continue
            if hid == "npc_dota_hero_base":
                base = entry
            else:
                heroes[hid] = entry
    for hid, entry in heroes.items():
        if entry.get("Enabled", base.get("Enabled")) == "0" and "HeroID" not in entry:
            continue
        short = hid.removeprefix("npc_dota_hero_")
        name = entry.get("workshop_guide_name") or names.get(hid, "") or short.replace("_", " ").title()
        abilities = [entry[k] for k in sorted((k for k in entry if re.fullmatch(r"Ability\d+", k)), key=lambda k: int(k[7:]))
                     if isinstance(entry[k], str) and entry[k] and not entry[k].startswith(("special_bonus", "generic_hidden"))]
        items.append({
            "id": hid, "key": name, "kind": "hero", "name": name,
            "class": ATTRIBUTE.get(entry.get("AttributePrimary", ""), ""),
            "group": entry.get("AttackCapabilities", "").replace("DOTA_UNIT_CAP_", "").replace("_ATTACK", "").lower(),
            "nation": "", "aliases": [short, name], "roles": [r for r in entry.get("Role", "").split(",") if r],
            "heroId": _number(entry.get("HeroID")), "abilities": abilities,
            "model": f"model-packs/{GAME}/{short}.glb",
            "numbers": _numbers(entry, base, HERO_NUMBERS),
        })
    units = kv.parse(files.get("scripts/npc/npc_units.txt", "")).get("DOTAUnits") or {}
    unit_base = units.get("npc_dota_units_base") or {}
    for uid, entry in units.items():
        if not isinstance(entry, dict) or uid == "npc_dota_units_base":
            continue
        name = names.get(uid.lower(), "") or uid.removeprefix("npc_dota_").replace("_", " ").title()
        items.append({
            "id": uid, "key": name, "kind": "unit", "name": name, "class": unit_class(uid, entry),
            "group": entry.get("BaseClass", ""), "nation": "", "aliases": [uid.removeprefix("npc_dota_")],
            "model": f"model-packs/{GAME}/{uid.removeprefix('npc_dota_')}.glb" if entry.get("Model") else "",
            "numbers": _numbers(entry, unit_base, UNIT_NUMBERS),
        })
    for iid, entry in (kv.parse(files.get("scripts/npc/items.txt", "")).get("DOTAAbilities") or {}).items():
        if not isinstance(entry, dict) or not iid.startswith("item_") or iid.startswith("item_recipe"):
            continue
        name = names.get(f"dota_tooltip_ability_{iid}".lower(), "")
        if not name:
            continue  # unnamed: internal and event items
        numbers = {k: v for k, v in (("cost", _number(entry.get("ItemCost"))), ("id", _number(entry.get("ID")))) if v is not None}
        items.append({
            "id": iid, "key": name, "kind": "item", "name": name,
            "class": "neutral" if entry.get("ItemIsNeutralDrop") == "1" or "ItemIsNeutralActiveDrop" in entry else "shop",
            "group": entry.get("ItemQuality", ""), "nation": "", "aliases": [iid.removeprefix("item_")],
            "model": "", "numbers": numbers,
        })
    return {"format": FORMAT, "version": 1, "game": GAME, "gameBuild": game_build, "source": source, "items": items}


def game_build(folder: Path) -> str:
    """The installed build, from `steam.inf`."""
    inf = folder / "steam.inf"
    if inf.is_file():
        m = re.search(r"ClientVersion=(\d+)", inf.read_text("utf-8", "replace"))
        if m:
            return m.group(1)
    return ""


def write_catalog(folder: Path, tool: Path, out: Path, *, source: str) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        files = read_scripts(tool, folder / "pak01_dir.vpk", Path(tmp))
    if not any(p.startswith("scripts/npc/heroes/") for p in files):
        raise RuntimeError("Source2Viewer read no hero scripts from pak01_dir.vpk")
    catalog = build_catalog(files, game_build=game_build(folder), source=source)
    import json

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(catalog, indent=1, ensure_ascii=False), encoding="utf-8")
    return catalog
