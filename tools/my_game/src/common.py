from decimal import Decimal
from pathlib import Path

# 游戏常量
DAMAGE_TYPE = ("physical","water","ice","fire","electric")

player = None
user_name = ""
game_settings = {}
game_difficulty = 1
trigger_key = {}

# 触发键
view_introductions = "Q"
open_backpack = "E"
attack_key = "A"
use_props = "U"
return_next = "R"

# 战斗时调用
number_of_monsters = 0
monsters_team = {}
monsters_data = []
monsters_effect_add_data = []

SAVE_PATH = Path("/data/data/com.termux/files/home/game_data")
