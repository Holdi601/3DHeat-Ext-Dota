"""
The standalone app's description of this tool (app/spec.py): the Dota 2
install it reads, Source2Viewer-CLI as the check before a map can be exported,
the install's maps (new ones after a game update are found by app/manifest.py),
and the catalogue and the model pack as tasks.
`python -m heat3d_ext_dota.standalone_spec` runs the app from a checkout; the
release executables run the same.
"""

from __future__ import annotations

from pathlib import Path

from . import __version__
from .app import paths
from .app.spec import Check, GameSpec, MapSource, Spec, Task, game_folders

#: The install's folder name in a Steam library.
STEAM_FOLDER = "dota 2 beta"


def _as_root(p: Path) -> Path | None:
    """The install's top folder from it, its `game` or its `game/dota` folder."""
    for r in (p, p.parent, p.parent.parent):
        if (r / "game" / "dota" / "gameinfo.gi").is_file():
            return r
    return None


def _find(given: str | None) -> Path | None:
    if given:
        return _as_root(Path(given).expanduser())
    from .steam import steam_libraries

    for c in [*paths.steam_game_dirs(STEAM_FOLDER), *(common / STEAM_FOLDER for common in steam_libraries())]:
        root = _as_root(c)
        if root is not None:
            return root
    return None


def _maps(game: Path) -> list[MapSource]:
    from .dota_map import maps

    return [MapSource(p.stem, p.stem, [p]) for p in maps(game / "game" / "dota")]


def _extract(game: Path, m: MapSource, out: Path, log) -> list[Path]:
    from . import dota_map, layouts

    out.mkdir(parents=True, exist_ok=True)
    level = out / f"{m.id}.glb"
    log(dota_map.export_map(m.id, level, game=str(game), say=log))
    # Towers, barracks, fountains and spawns beside it; a map without them is not an error.
    try:
        log(layouts.export_layouts(m.id, out, game=str(game), tool_name=f"heat3d-dota-maps {__version__}", say=log))
    except (OSError, RuntimeError, ValueError) as e:
        log(f"{m.id}: no layouts ({e})")
    return [p for p in (level, out / f"{m.id}.layouts.json") if p.is_file()]


def _build(game: Path) -> str | None:
    from .catalog import game_build

    return game_build(game / "game" / "dota") or None


def _checks(found: dict, levels: Path) -> list[Check]:
    from .dota_map import SOURCE2VIEWER_URL, find_source2viewer

    try:
        detail, ok = str(find_source2viewer()), True
    except FileNotFoundError:
        detail, ok = (f"not found; every export needs it. Download its command-line build for this system from "
                      f"{SOURCE2VIEWER_URL} and unzip it next to this program, put it on PATH, or set "
                      "HEAT3D_SOURCE2VIEWER to it."), False
    return [Check("source2viewer", "Source2Viewer-CLI (reads the maps of your own Dota 2 install)", ok, detail)]


def _game_args() -> list[str]:
    game = game_folders(SPEC).get("dota")
    return ["--game", str(game)] if game else []


SPEC = Spec(
    id="heat3d-dota-maps",
    name="3DHeat Dota maps",
    repo="Holdi601/3DHeat-Ext-Dota",
    version=__version__,
    tools={"heat3d-dota-maps": "heat3d_ext_dota.cli:main"},
    default_tool="heat3d-dota-maps",
    description="Dota 2's map from your own install as a 3DHeat level",
    module="heat3d_ext_dota.standalone_spec",
    games=[GameSpec(
        key="dota", label="Dota 2", find=_find, subdir="dota", build=_build,
        maps=_maps, extract=_extract,
        existing_outputs=lambda out, m: [out / f"{m.id}.glb"],
        output_version="0.2.0",
        platforms=("windows-x64", "linux-x64", "macos-arm64"),
    )],
    checks=_checks,
    tasks=[
        Task(
            "catalog", "Heroes, units and items catalogue", [],
            lambda v, levels: ["heat3d-dota-maps", "catalog", *_game_args()],
            help="catalog.json in the levels folder's dota folder, from your install",
        ),
        Task(
            "models", "Hero and unit models (local model pack)", [],
            lambda v, levels: ["heat3d-dota-maps", "models", *_game_args()],
            help="a model pack in the levels folder, from your install; it stays on this machine",
        ),
    ],
    min_free_gb=2.0,
    notice="Not affiliated with or endorsed by Valve Corporation.",
)

if __name__ == "__main__":
    from . import update
    from .app.entry import main

    raise SystemExit(main(SPEC, apply_source=update.apply))
