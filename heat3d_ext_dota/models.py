"""
Dota 2's hero and unit models from your own install, as a local model pack for the 3DHeat viewer.

Each hero (its `Model` in `scripts/npc/heroes/*.txt`, with the default items `items_game.txt` gives it) and each
unit of `npc_units.txt` with a model is exported by Source2Viewer's CLI to glTF with its idle animation, posed at
the idle's first frame (the skin applied here), scaled by its `ModelScale`, welded and simplified to three levels of
detail, and written as one `.glb` per unit plus `model-pack.json` (layout in `modelpack.py`). The pack is for this
machine only.
"""

from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path
from typing import Callable

import numpy as np

from . import glb, kv, modelpack
from .catalog import GAME, game_build, read_scripts, unit_class

#: Triangles per level of detail: heroes and units are small on a Dota map, and there are many.
BUDGETS = (6000, 1800, 500)
BUILDING_BUDGETS = (9000, 2500, 700)
IDLE = re.compile(r"^(idle|idle_anim|idle1|idle_loop|ACT_DOTA_IDLE)$", re.I)
#: Models that are nothing to draw.
SKIP_MODEL = re.compile(r"development/|invisiblebox|dummy|/empty", re.I)


def _trs(node: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return (np.array(node.get("translation", [0, 0, 0]), float), np.array(node.get("rotation", [0, 0, 0, 1]), float),
            np.array(node.get("scale", [1, 1, 1]), float))


def _matrix(t: np.ndarray, r: np.ndarray, s: np.ndarray) -> np.ndarray:
    x, y, z, w = r / (np.linalg.norm(r) or 1)
    m = np.eye(4)
    m[:3, :3] = np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
        [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
        [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)],
    ]) * s
    m[:3, 3] = t
    return m


def posed(doc: dict, blob: bytes, *, pose: dict[str, np.ndarray] | None = None) -> tuple[list[tuple[np.ndarray, np.ndarray]], dict[str, np.ndarray]]:
    """
    Every mesh of a glTF export in its idle pose (the first frame of the idle animation, else the bind pose), in
    glTF metres. `pose` gives joints' world matrices by name (a hero's, for its items); returns the meshes and this
    file's joint matrices by name.
    """
    nodes = doc.get("nodes", [])
    local = [list(_trs(n)) for n in nodes]
    for n_i, n in enumerate(nodes):
        if "matrix" in n:
            m = np.array(n["matrix"], float).reshape(4, 4).T
            local[n_i] = [m[:3, 3], None, m]
    anims = doc.get("animations", [])
    anim = next((a for a in anims if IDLE.match(a.get("name", ""))), None) or next(
        (a for a in anims if "idle" in a.get("name", "").lower()), None)
    if anim:
        for ch in anim.get("channels", []):
            target = ch.get("target", {})
            node, path = target.get("node"), target.get("path")
            if node is None or path not in ("translation", "rotation", "scale"):
                continue
            out = glb._accessor(doc, blob, anim["samplers"][ch["sampler"]]["output"])
            if len(out) and local[node][1] is not None:
                local[node][{"translation": 0, "rotation": 1, "scale": 2}[path]] = np.asarray(out[0], float)
    parent = {c: i for i, n in enumerate(nodes) for c in n.get("children", [])}
    world: dict[int, np.ndarray] = {}

    def world_of(i: int) -> np.ndarray:
        if i not in world:
            t, r, s = local[i]
            m = s if r is None else _matrix(t, r, s)
            world[i] = world_of(parent[i]) @ m if i in parent else m
        return world[i]

    joints_by_name = {nodes[i].get("name", ""): world_of(i) for i in range(len(nodes))}
    meshes = []
    for i, n in enumerate(nodes):
        if "mesh" not in n:
            continue
        skin = doc["skins"][n["skin"]] if "skin" in n and doc.get("skins") else None
        if pose is not None and (skin is None or not any(nodes[j].get("name", "") in pose for j in skin["joints"])):
            continue  # an item on a skeleton of its own (placed by attachment, not bones): left out
        if skin is not None:
            ibm = glb._accessor(doc, blob, skin["inverseBindMatrices"]).reshape(-1, 4, 4).transpose(0, 2, 1)
            mats = []
            for j, ji in enumerate(skin["joints"]):
                name = nodes[ji].get("name", "")
                w = pose[name] if pose is not None and name in pose else world_of(ji)
                mats.append(w @ ibm[j])
            mats = np.stack(mats)
        for prim in doc["meshes"][n["mesh"]]["primitives"]:
            if prim.get("mode", 4) != 4 or "indices" not in prim:
                continue
            p = glb._accessor(doc, blob, prim["attributes"]["POSITION"]).astype(float)
            t = glb._accessor(doc, blob, prim["indices"]).reshape(-1, 3).astype(np.int64)
            if skin is not None and "JOINTS_0" in prim["attributes"]:
                js = glb._accessor(doc, blob, prim["attributes"]["JOINTS_0"]).astype(np.int64)
                raw = glb._accessor(doc, blob, prim["attributes"]["WEIGHTS_0"])
                ws = raw.astype(float)
                if raw.dtype.kind in "iu":
                    ws = ws / np.iinfo(raw.dtype).max
                ws = ws / np.maximum(ws.sum(1, keepdims=True), 1e-9)
                h = np.c_[p, np.ones(len(p))]
                out = np.zeros((len(p), 4))
                for k in range(js.shape[1]):
                    out += ws[:, k:k + 1] * np.einsum("nij,nj->ni", mats[js[:, k]], h)
                p = out[:, :3]
            else:
                m = world_of(i)
                p = p @ m[:3, :3].T + m[:3, 3]
            meshes.append((p, t))
    return meshes, joints_by_name


def to_figure(gl: np.ndarray, scale: float) -> np.ndarray:
    """glTF metres (Y up, the model facing +Z) -> the figure frame (x forward, y up, z right)."""
    return np.stack([gl[:, 2], gl[:, 1], -gl[:, 0]], axis=1) * scale


def default_items(items_game: str) -> dict[str, list[str]]:
    """Each hero's default item models (`prefab default_item`), by hero id."""
    out: dict[str, list[str]] = {}
    slots: set[tuple[str, str]] = set()
    items = (kv.parse(items_game).get("items_game") or {}).get("items") or {}
    for entry in items.values():
        if not isinstance(entry, dict) or entry.get("prefab") != "default_item":
            continue
        model = entry.get("model_player")
        heroes = entry.get("used_by_heroes")
        if not model or not isinstance(heroes, dict):
            continue
        for hero in heroes:
            # The first default of each slot, the hero's own look (not a persona's).
            slot = (hero, entry.get("item_slot", "weapon"))
            if slot in slots or "persona" in slot[1]:
                continue
            slots.add(slot)
            out.setdefault(hero, []).append(model)
    return out


def _vmdl_c(model: str) -> str:
    return model[:-5] + ".vmdl_c" if model.endswith(".vmdl") else model + "_c"


def export(tool: Path, pak: Path, models: list[str], out: Path) -> None:
    """Source2Viewer exporting `models` (with their idle animations) to `out` as .glb, in batches."""
    for k in range(0, len(models), 40):
        batch = models[k:k + 40]
        subprocess.run([str(tool), "-i", str(pak), "-d", "-f", ",".join(_vmdl_c(m) for m in batch), "-o", str(out),
                        "--gltf_export_format", "glb", "--gltf_export_animations",
                        "--gltf_animation_list", "idle,idle_anim,idle1,idle_loop"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")


def _held(p: np.ndarray, lo: np.ndarray, hi: np.ndarray) -> bool:
    """
    Whether an item's posed mesh is on the body: not lying flat on the ground or off to the side, as an item does
    whose bones the game moves by attachment rather than animation.
    """
    if not len(p):
        return False
    size = hi - lo
    c = (p.min(0) + p.max(0)) / 2
    low = p[:, 1].max() < lo[1] + 0.15 * size[1] or p[:, 1].min() < lo[1] - 0.05 * size[1]
    flat = low or (p[:, 1].max() - p[:, 1].min() < 0.12 * size[1] and p[:, 1].min() < lo[1] + 0.08 * size[1])
    aside = np.any(np.abs(c[[0, 2]] - (lo[[0, 2]] + hi[[0, 2]]) / 2) > 0.6 * size[[0, 2]] + 0.1)
    return not (flat or aside)


def _glb_of(out: Path, model: str) -> Path:
    return out / Path(model).with_suffix(".glb")


def collect(files: dict[str, str], items_game: str) -> list[dict]:
    """What to build: each hero and model-bearing unit, with its model, items, scale and names."""
    wanted: list[dict] = []
    defaults = default_items(items_game) if items_game else {}
    base: dict = {}
    heroes: dict[str, dict] = {}
    for path, text in sorted(files.items()):
        if path.startswith("scripts/npc/heroes/"):
            for hid, entry in (kv.parse(text).get("DOTAHeroes") or {}).items():
                if isinstance(entry, dict):
                    (heroes.__setitem__(hid, entry) if hid != "npc_dota_hero_base" else base.update(entry))
    names = kv.tokens(files.get("resource/localization/abilities_english.txt", ""))
    for hid, entry in heroes.items():
        model = entry.get("Model")
        if not model or "HeroID" not in entry:
            continue
        short = hid.removeprefix("npc_dota_hero_")
        name = entry.get("workshop_guide_name") or short.replace("_", " ").title()
        wanted.append({"id": short, "model": model, "items": defaults.get(hid, []), "kind": "hero",
                       "scale": float(entry.get("ModelScale", base.get("ModelScale", 1)) or 1),
                       "name": name, "aliases": [hid, name], "type": "hero"})
    units = kv.parse(files.get("scripts/npc/npc_units.txt", "")).get("DOTAUnits") or {}
    seen = set()
    for uid, entry in units.items():
        if not isinstance(entry, dict) or uid == "npc_dota_units_base":
            continue
        model = entry.get("Model")
        if not model or SKIP_MODEL.search(model):
            continue
        short = uid.removeprefix("npc_dota_")
        if short in seen:
            continue
        seen.add(short)
        name = names.get(uid.lower(), "") or short.replace("_", " ").title()
        wanted.append({"id": short, "model": model, "items": [], "kind": unit_class(uid, entry),
                       "scale": float(entry.get("ModelScale", 1) or 1), "name": name,
                       "aliases": [uid], "type": unit_class(uid, entry)})
    return wanted


def write_pack(folder: Path, tool: Path, out_dir: Path, *, source: str, only: list[str] | None = None,
               say: Callable[[str], None] = print) -> dict:
    pak = folder / "pak01_dir.vpk"
    build = game_build(folder)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        files = read_scripts(tool, pak, tmp / "scripts")
        subprocess.run([str(tool), "-i", str(pak), "-f", "scripts/items/items_game.txt", "-o", str(tmp / "ig")],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
        # One file asked for: Source2Viewer writes it at the output path itself.
        ig = tmp / "ig" if (tmp / "ig").is_file() else tmp / "ig" / "scripts" / "items" / "items_game.txt"
        wanted = collect(files, ig.read_text("utf-8", "replace") if ig.exists() else "")
        if only:
            wanted = [w for w in wanted if any(o.lower() in w["id"] or o.lower() == w["name"].lower() for o in only)]
        models = sorted({m for w in wanted for m in [w["model"], *w["items"]]})
        say(f"exporting {len(models)} models for {len(wanted)} heroes and units")
        export(tool, pak, models, tmp / "m")
        units: dict[str, dict] = {}
        failed = []
        for w in wanted:
            path = _glb_of(tmp / "m", w["model"])
            if not path.exists():
                failed.append(w["id"])
                continue
            meshes, pose = posed(*glb.read(path))
            body = np.concatenate([p for p, t in meshes if len(t)]) if meshes else np.zeros((1, 3))
            lo, hi = body.min(0), body.max(0)
            for item in w["items"]:
                ip = _glb_of(tmp / "m", item)
                if ip.exists():
                    meshes += [m for m in posed(*glb.read(ip), pose=pose)[0] if _held(m[0], lo, hi)]
            meshes = [(p, t) for p, t in meshes if len(t)]
            if not meshes:
                failed.append(w["id"])
                continue
            offs = np.cumsum([0] + [len(p) for p, _ in meshes])
            v = to_figure(np.concatenate([p for p, _ in meshes]), w["scale"])
            f = np.concatenate([t + offs[i] for i, (_, t) in enumerate(meshes)])
            built = modelpack.build_lods({"hull": (v, f)}, BUILDING_BUDGETS if w["kind"] == "building" else BUDGETS)
            key = f"{w['model']}|{','.join(w['items'])}|{w['scale']}|{build}"
            asset = {"source": source, "version": 1, "game": GAME, "gameBuild": build, "unit": w["id"], "scale": 1}
            meta = {"unit": w["id"], "kind": w["kind"], "domain": "person",
                    "anchor": "ground", "pivots": {}}
            modelpack.write_unit_glb(out_dir / f"{w['id']}.glb", built, meta, asset)
            units[w["id"]] = modelpack.unit_entry(
                w["id"], built, kind=w["kind"], domain=meta["domain"], name=w["name"], aliases=w["aliases"],
                type_word=w["type"], source_key=key, model=w["model"], items=w["items"], modelScale=w["scale"])
    if units:
        modelpack.write_index(out_dir, GAME, build, source, units)
    return {"units": units, "failed": failed}
