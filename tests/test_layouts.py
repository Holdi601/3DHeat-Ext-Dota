"""The map's layout (layouts.py) from entities."""

from heat3d_ext_dota import layouts
from heat3d_ext_dota.dota_map import Entity


def test_buildings_and_spawns_by_side_in_the_levels_frame():
    ents = [
        Entity("npc_dota_tower", origin=(100.0, 200.0, 128.0),
               keys={"teamnumber": '"2"', "targetname": '"[PR#]dota_goodguys_tower1_mid"'}),
        Entity("ent_dota_fountain", origin=(7000.0, 6500.0, 380.0), keys={"teamnumber": '"3"'}),
        Entity("npc_dota_spawner_bad_top", origin=(1.0, 2.0, 3.0)),
        Entity("info_player_start_goodguys", origin=(-6500.0, -6500.0, 384.0)),
        Entity("npc_dota_roshan_spawner", origin=(2830.0, -2740.0, 64.0)),
        Entity("ent_dota_tree", origin=(0.0, 0.0, 0.0)),
    ]
    lay = layouts.layout(ents, "dota", "test")["layouts"][0]
    tower, fountain, roshan = lay["objectives"]
    assert (tower["name"], tower["team"], tower["position"]) == ("Tower 1 mid", 1, [100.0, 128.0, -200.0])
    assert (fountain["type"], fountain["team"]) == ("base", 2)
    assert roshan["team"] is None
    assert [(s["base"], s["team"]) for s in lay["spawns"]] == [("Creeps top", 2), ("Heroes", 1)]
