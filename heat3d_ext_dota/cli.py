"""
heat3d-dota-maps list                  where Dota 2 and Source2Viewer's CLI are, and the maps installed
heat3d-dota-maps level [map] -o <file> the map as a 3DHeat level (.glb): ground, cliffs, water, trees, buildings

Exit status: 0 done, 1 failed, 2 nothing to read (no Dota 2 install, no such map,
no Source2Viewer CLI).
"""

from __future__ import annotations

import argparse
import sys

from . import __version__
from . import dota_map


def cmd_list(args) -> int:
    try:
        folder = dota_map.game_folder(args.game)
    except FileNotFoundError as e:
        print(f"heat3d-dota-maps: {e}", file=sys.stderr)
        return 2
    print(f"Dota 2 at {folder}")
    for vpk in dota_map.maps(folder):
        print(f"  {vpk.stem:24s} {vpk.stat().st_size / 1e6:8.1f} MB")
    try:
        print(f"Source2Viewer CLI at {dota_map.find_source2viewer(args.source2viewer)}")
    except FileNotFoundError as e:
        print(f"heat3d-dota-maps: {e}", file=sys.stderr)
        return 2
    return 0


def cmd_level(args) -> int:
    try:
        line = dota_map.export_map(args.map, args.out, game=args.game, source2viewer=args.source2viewer,
                                   detail=args.detail, say=lambda text: print(text, file=sys.stderr))
    except FileNotFoundError as e:
        print(f"heat3d-dota-maps: {e}", file=sys.stderr)
        return 2
    except (OSError, RuntimeError, ValueError) as e:
        print(f"heat3d-dota-maps: {e}", file=sys.stderr)
        return 1
    print(line)
    return 0


def main(argv: list[str] | None = None) -> int:
    try:
        import heat3d_update

        heat3d_update.startup("heat3d_ext_dota")
    except Exception:  # an update check never stops an export
        pass
    ap = argparse.ArgumentParser(prog="heat3d-dota-maps", description="Dota 2's map from your own install into a 3DHeat level")
    ap.add_argument("--version", action="version", version=__version__)
    sub = ap.add_subparsers(dest="command", required=True)

    def where(p):
        p.add_argument("--game", help="the Dota 2 folder, `dota 2 beta` or its game/dota (default: found in your Steam libraries)")
        p.add_argument("--source2viewer", help="Source2Viewer-CLI's path (default: HEAT3D_SOURCE2VIEWER, PATH, then the current folder and this tool's)")

    p = sub.add_parser("list", help="where Dota 2 and Source2Viewer's CLI are, and the maps installed")
    where(p)
    p.set_defaults(run=cmd_list)

    p = sub.add_parser("level", help="the map as a level (.glb) under the Dota replay tables")
    p.add_argument("map", nargs="?", default="dota", help="the map's name as list prints it (default: dota) or the path to its .vpk")
    p.add_argument("-o", "--out", required=True, help="the .glb to write")
    where(p)
    p.add_argument("--detail", type=float, default=8.0,
                   help="buildings' vertex clustering cell in game units (default 8; 0 keeps every triangle)")
    p.set_defaults(run=cmd_level)

    args = ap.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main())
