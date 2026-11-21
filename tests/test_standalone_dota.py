"""The standalone spec on a synthetic Dota 2 install (tiny fake files, no game data)."""

from __future__ import annotations

import dataclasses
import json
from pathlib import Path

import pytest

from heat3d_ext_dota import dota_map, layouts, standalone_spec as S
from heat3d_ext_dota.app import entry


@pytest.fixture(autouse=True)
def _isolated(tmp_path, monkeypatch):
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "appdata"))
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "appdata"))
    monkeypatch.setenv("HEAT3D_LEVELS", str(tmp_path / "levels"))
    monkeypatch.setenv("HEAT3D_NO_UPDATE", "1")


def install(tmp_path: Path) -> Path:
    root = tmp_path / "dota 2 beta"
    dota = root / "game" / "dota"
    (dota / "maps").mkdir(parents=True)
    (dota / "gameinfo.gi").write_text("x")
    (dota / "steam.inf").write_text("ClientVersion=6123\n")
    for name in ("dota", "hero_demo_main"):
        (dota / "maps" / f"{name}.vpk").write_bytes(name.encode())
    return root


@pytest.fixture
def no_source2viewer(monkeypatch):
    """The exports without Source2Viewer: each writes a placeholder."""

    def level(name, out, game=None, say=print, **kw):
        assert dota_map.game_folder(game).name == "dota"
        Path(out).write_bytes(b"glb " + name.encode())
        return f"{out}: {name}"

    def lay(name, out, game=None, **kw):
        (Path(out) / f"{name}.layouts.json").write_text("{}")
        return name

    monkeypatch.setattr(dota_map, "export_map", level)
    monkeypatch.setattr(layouts, "export_layouts", lay)


def test_find_maps_build(tmp_path):
    root = install(tmp_path)
    assert S._find(str(root)) == root
    assert S._find(str(root / "game" / "dota")) == root
    assert S._find(str(tmp_path / "nowhere")) is None
    assert [m.id for m in S._maps(root)] == ["dota", "hero_demo_main"]
    assert S._build(root) == "6123"


def test_install_that_gains_a_map(tmp_path, no_source2viewer, capsys):
    root = install(tmp_path)
    g = dataclasses.replace(S.SPEC.games[0], find=lambda given: root)
    spec = dataclasses.replace(S.SPEC, games=[g])

    def status():
        entry.main(spec, ["status", "--json"])
        game = json.loads(capsys.readouterr().out)["games"][0]
        return game, {m["id"]: m["state"] for m in game["maps"]}

    game, states = status()
    assert game["found"] and game["build"] == "6123" and set(states.values()) == {"new"}
    assert entry.main(spec, ["extract", "--new", "--progress-json"]) == 0
    capsys.readouterr()
    man = json.loads((tmp_path / "levels" / "dota" / ".heat3d-extract.json").read_text())
    assert man["entries"]["dota"]["outputs"] == ["dota/dota.glb", "dota/dota.layouts.json"]
    assert "game/dota/maps/dota.vpk" in man["entries"]["dota"]["sources"]

    # A game update brings a map: it is the only new one.
    (root / "game" / "dota" / "maps" / "dota_new.vpk").write_bytes(b"n")
    _, states = status()
    assert states == {"dota": "current", "hero_demo_main": "current", "dota_new": "new"}


def test_tasks_and_tools():
    assert S.SPEC.version == (Path(__file__).resolve().parents[1] / "VERSION").read_text().strip()
    assert [t.id for t in S.SPEC.tasks] == ["catalog", "models"]
    assert entry.run_tool(S.SPEC, "heat3d-dota-maps", ["--help"]) == 0
