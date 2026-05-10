import pickle
#(probability, enemies/target/allies/myself, count(int), level, duration)

monsters_effect_add_data = {
    "史莱姆": {
        "stun": ("0.01", "target", 1, 1, 1)
    },
    "水史莱姆": {
        "wet": ("0.45", "enemies", 2, 1, 3)
    },
    "冰史莱姆": {
        "freeze": ("0.1", "target", 1, 1, 1),
        "stun": ("0.02", "target", 1, 1, 1),
        "instant_health": ("0.7", "myself", 1, 2, 0),
        "regeneration": ("0.15", "allies", 2, 1, 2)
    },
    "火史莱姆": {
        "burn": ("0.12", "target", 1, 2, 2),
        "stun": ("0.01", "target", 1, 1, 1)
    },
    "电史莱姆": {
        "numb": ("0.3", "target", 1, 2, 1)
    },
}

with open("/storage/emulated/0/monsters_effect_add_data.dat", 'wb') as f:
    pickle.dump(monsters_effect_add_data, f)