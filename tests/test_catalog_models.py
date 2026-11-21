import json

import numpy as np

from heat3d_ext_dota import catalog, kv, modelpack, models

HERO = '''"DOTAHeroes"
{
	"npc_dota_hero_base" { "ModelScale" "1" "StatusHealth" "120" }
	"npc_dota_hero_axe"
	{
		"Model"		"models/heroes/axe/axe.vmdl"
		"HeroID"	"2"
		"workshop_guide_name"	"Axe"
		"AttributePrimary"	"DOTA_ATTRIBUTE_STRENGTH"
		"AttackCapabilities"	"DOTA_UNIT_CAP_MELEE_ATTACK"
		"Role"	"Initiator,Durable"
		"Ability1"	"axe_berserkers_call"
		"Ability10"	"special_bonus_unique_axe"
		"MovementSpeed"	"310"	// comment
		[$WIN32]
	}
}'''
LOC = '\ufeff"lang" { "Language" "English" "Tokens" { "DOTA_Tooltip_Ability_item_blink" "Blink Dagger" '\
      '"npc_dota_creep_badguys_melee" "Melee Creep" } }'
UNITS = '"DOTAUnits" { "Version" "1" "npc_dota_creep_badguys_melee" { "Model" "models/creeps/x.vmdl" "BaseClass" "npc_dota_creep_lane" } }'
ITEMS = '"DOTAAbilities" { "Version" "1" "item_blink" { "ItemCost" "2250" "ID" "1" } "item_recipe_x" { } }'


def files():
    return {"scripts/npc/heroes/npc_dota_hero_axe.txt": HERO, "scripts/npc/npc_units.txt": UNITS,
            "scripts/npc/items.txt": ITEMS, "resource/localization/abilities_english.txt": LOC}


def test_kv_and_tokens():
    tree = kv.parse(HERO)
    assert tree["DOTAHeroes"]["npc_dota_hero_axe"]["MovementSpeed"] == "310"
    assert kv.tokens(LOC)["npc_dota_creep_badguys_melee"] == "Melee Creep"


def test_catalog_heroes_units_items():
    c = catalog.build_catalog(files())
    by = {i["id"]: i for i in c["items"]}
    axe = by["npc_dota_hero_axe"]
    assert (axe["name"], axe["class"], axe["group"]) == ("Axe", "strength", "melee")
    assert axe["abilities"] == ["axe_berserkers_call"] and axe["numbers"]["moveSpeed"] == 310
    assert axe["numbers"]["health"] == 120  # from the base hero
    assert by["npc_dota_creep_badguys_melee"]["name"] == "Melee Creep"
    assert by["npc_dota_creep_badguys_melee"]["class"] == "creep"
    assert by["item_blink"]["name"] == "Blink Dagger" and by["item_blink"]["numbers"]["cost"] == 2250
    assert "item_recipe_x" not in by


def test_collect_and_items_on_body():
    wanted = models.collect(files(), "")
    assert [w["id"] for w in wanted] == ["axe", "creep_badguys_melee"]
    lo, hi = np.array([-0.5, 0, -0.5]), np.array([0.5, 2, 0.5])
    assert models._held(np.array([[0.2, 1.0, 0], [0.4, 1.6, 0.1]]), lo, hi)
    assert not models._held(np.array([[0.0, 0.0, 0], [1.2, 0.1, 0.1]]), lo, hi)  # lying on the ground


def test_figure_frame_and_pack(tmp_path):
    # glTF +Z (the model's front) is the figure's +x; glTF +X (its left) is the figure's -z.
    assert np.allclose(models.to_figure(np.array([[1.0, 2.0, 3.0]]), 2.0), [[6.0, 4.0, -2.0]])
    v = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]], float)
    f = np.array([[0, 1, 2], [0, 2, 3], [4, 2, 3]])
    built = modelpack.build_lods({"hull": (v, f)}, (100, 50, 20))
    assert len(built.lods[0].parts["hull"][0]) == 4  # the seam vertex welded
    modelpack.write_unit_glb(tmp_path / "u.glb", built, {"unit": "u"}, {"source": "t"})
    entry = modelpack.unit_entry("u", built, kind="hero", domain="person", name="U", source_key="k")
    modelpack.write_index(tmp_path, "dota", "1", "t", {"u": entry})
    pack = json.loads((tmp_path / "model-pack.json").read_text())
    assert pack["format"] == "3dheat-model-pack" and pack["units"]["u"]["file"] == "u.glb"
    assert (tmp_path / "u.glb").read_bytes()[:4] == b"glTF"
