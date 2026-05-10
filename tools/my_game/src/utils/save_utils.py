"""
对游戏数据处理
"""

import os, pickle
from decimal import Decimal
from pathlib import Path
from src import common as g
from src.version import __version__
from src.core.actor import PlayerProperty
from src.utils.input_utils import get_options

monsters_static_data = (Path(__file__).parent.parent / "data" / "monsters_data.dat")
monsters_effect_add_static_data = (Path(__file__).parent.parent / "data" / "monsters_effect_add_data.dat")

def data_initializing():  # 初始化新用户的数据
    user_name = input("你的名字是：")
    print("\033[2J\033[3J\033[H", end="")
    print("请锁定一个难度\n1.简单\n2.普通\n3.困难")
    game_difficulty = get_options(3)
    print("\033[2J\033[3J\033[H", end="")
    user_information = {
        "user_name": user_name,
        "user_version": __version__
    }
    game_settings = {
        "game_difficulty": game_difficulty
    }
    trigger_key = {
        "view_introductions": "Q",
        "open_backpack": "E",
        "attack_key": "A",
        "use_props": "U",
        "return_next": "R"
    }  
    player_property = {
        "health": "100",
        "health_max": "100",
        "physical_attack": "10",
        "water_attack": "0",
        "ice_attack": "0",
        "fire_attack": "0",
        "electric_attack": "0",
        "physical_resistance": "0",
        "water_resistance": "0",
        "ice_resistance": "-0.05",
        "fire_resistance": "-0.15",
        "electric_resistance": "-0.05",
        "status_effects": [],
        "can_attack": True,
        "can_operate": True,
        "backpack": {
            "money": 50
        }
    }
    # 询问信息并存储进字典
    os.makedirs(g.SAVE_PATH / "cache")
    os.makedirs(g.SAVE_PATH / "files/userdata")
    with open(g.SAVE_PATH / "files/userdata/user_information.dat", "wb") as file:
        pickle.dump(user_information, file)
    with open(g.SAVE_PATH / "files/game_settings.dat", "wb") as file:
        pickle.dump(game_settings, file)
    with open(g.SAVE_PATH / "files/trigger_key.dat", "wb") as file:
        pickle.dump(trigger_key, file)
    with open(g.SAVE_PATH / "files/userdata/player_property.dat", "wb") as file:
        pickle.dump(player_property, file)  
    # 存储信息

def get_data():  # 载入数据
    global player,trigger_key,user_information,monsters_data,monsters_effect_add_static_data
    with open(g.SAVE_PATH / "files/userdata/user_information.dat", "rb") as file:
        user_information = pickle.load(file)
    with open(g.SAVE_PATH / "files/game_settings.dat", "rb") as file:
        g.game_settings = pickle.load(file)
    game_difficulty = g.game_settings["game_difficulty"]
    with open(g.SAVE_PATH / "files/trigger_key.dat", "rb") as file:
        g.trigger_key = pickle.load(file) 
    with open(g.SAVE_PATH / "files/userdata/player_property.dat", "rb") as file:
        g.player = PlayerProperty(**pickle.load(file))
    # 获取玩家信息
    
    with open(monsters_static_data, "rb") as file:
        g.monsters_data = pickle.load(file)
    with open(monsters_effect_add_static_data, "rb") as file:
        g.monsters_effect_add_data = pickle.load(file)
    # 获取怪物信息
    
    g.user_name = user_information["user_name"]
    
    for key, value in g.trigger_key.items():
        setattr(g, key, value)
    # 修改全局变量
            
def storage_data():  # 存储数据
    player_property = {
        "health": g.player.health,
        "health_max": g.player.health_max,
        "physical_attack": g.player.physical_attack,
        "water_attack": g.player.water_attack,
        "ice_attack": g.player.ice_attack,
        "fire_attack": g.player.fire_attack,
        "electric_attack": g.player.electric_attack,
        "physical_resistance": g.player.physical_resistance,
        "water_resistance": g.player.water_resistance,
        "ice_resistance": g.player.ice_resistance,
        "fire_resistance": g.player.fire_resistance,
        "electric_resistance": g.player.electric_resistance,
        "status_effects": g.player.status_effects,
        "can_attack": g.player.can_attack,
        "can_operate": g.player.can_operate,
        "backpack": g.player.backpack
    }
    with open(g.SAVE_PATH / "files/trigger_key.dat", "wb") as file:
        pickle.dump(g.trigger_key, file)
    with open(g.SAVE_PATH / "files/userdata/player_property.dat", "wb") as file:
        pickle.dump(player_property, file)  