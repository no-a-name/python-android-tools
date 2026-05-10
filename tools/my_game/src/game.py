import os,time,shutil,random
from pathlib import Path
from src import common as g
from src import ui
from src.utils import save_utils
from src.utils.generate_monsters_utils import generate_monsters
from src.core.battle import death_judgment
from src.utils.input_utils import get_options

def main():
    if not os.path.exists(g.SAVE_PATH / "files/userdata/user_information.dat"):
        print("你应该是第一次进入这个游戏吧")
        time.sleep(2)
        print("\033[2J\033[3J\033[H", end="")
        save_utils.data_initializing()
    save_utils.get_data()
    while True:
        print("\033[2J\033[H\033[3J", end="")
        option = ui.menu()
        if option == 1:
            while True:
                print("\033[2J\033[H\033[3J", end="")
                g.number_of_monsters = 0
                for _ in range(random.randint(1,3)):
                    print(f"你遇到了：{generate_monsters(g.number_of_monsters)}")
                    time.sleep(1)
                time.sleep(2)    
                print("\033[2J\033[H\033[3J", end="")
                while not death_judgment(g.player):
                    ui.battle_ui()
                    for key, value in list(g.monsters_team.items()):
                        if value != "" and value.health <= 0:
                            g.monsters_team[key] = ""
                    if all(x=="" for x in g.monsters_team.values()):
                        g.monsters_team = {}
                        break
                else:
                    shutil.rmtree("/data/data/com.termux/files/home/game_data")
                    print("\033[2J\033[H\033[3J", end="")
                    print("\033[31m你死了！\033[0m")
                    exit()
                print("\033[2J\033[H\033[3J", end="")
                print("你已经击败了所有敌对对象！")
                time.sleep(1)
                print("是否继续：\n1.是\n2.否")
                g.player.backpack["money"] += random.randint(15, 75)
                option = get_options(2)
                if option == 2:
                    break
        elif option == 2:
            ui.backpack()
        elif option == 3:
            ui.shop()
        elif option == 4:
            ui.settings()
        elif option == 5:
            save_utils.storage_data()
            print("\033[2J\033[H\033[3J", end="")
            print("已保存")
            exit()
        else:
            pass