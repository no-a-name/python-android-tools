import random
from src.core.actor import MonsterProperty
from src import common as g

def generate_monsters(monsters_quantity):  # 生成怪物
    g.number_of_monsters += 1
    i = random.randint(1, len(g.monsters_data)-1)
    a = g.monsters_data[i].copy()
    a["weapons"] = ""
    del a["story"]
    g.monsters_team[f"monster{g.number_of_monsters}"] = MonsterProperty(**a)
    return g.monsters_data[i]["name"]