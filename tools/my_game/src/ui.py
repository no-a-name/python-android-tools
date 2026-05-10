import time
from decimal import Decimal
from src import common as g
from src.utils.input_utils import get_options
from src.core.battle import all_attacks,perform_effect_attack,perform_effect_add

def menu():
    """
    显示游戏主菜单，等待玩家选择操作
    
    Returns:
        int: 玩家选择的选项(1~5)
    
    Note:
    调用时会清屏
    """
    print("\033[2J\033[H\033[3J", end="")
    print("\033[33m不知道叫什么的游戏\033[0m")
    print("\033[31m主菜单\033[0m")
    print("1.开始游戏")
    print("2.查看背包")
    print("3.商店")
    print("4.设置")
    print("5.保存并退出")
    return get_options(5)
    
def settings():
    """
    打印设置，支持查看和修改按键配置
    
    Note:
        调用时会清屏
        函数内部使用 while 循环，直到用户选择退出才会返回
        修改按键时会检测冲突，重复的按键不会被保存
    """
    while True:
        print("\033[2J\033[H\033[3J", end="")
        print("\033[31m设置\033[0m")
        print(f"游戏难度：{g.game_difficulty}")
        print("1.按键设置")
        print("2.开发人员名单")
        print("\033[31m3.退出设置\033[0m")
        
        option = get_options(3)
        
        if option == 3:
            break
        elif option == 2:
            print("\033[2J\033[3J\033[H", end="")
            print("制作人Producer: q_q_w_e_t_i_qe")
            print("策划Designer: q_q_w_e_t_i_qe 人空之类")
            #print("美术设计Artist：")
            print("程序编写Programmer: q_q_w_e_t_i_qe")
            print("测试人员Tester: 人空之类 红钧子好吃")
            print("TA是干什么的来着: 没钱螃蟹")
            print("还有来当吉祥物的: 馒馒不吃噜_")
            print("什么时候有的这个人: 玐龟啦啦啦")
            input()
        elif option == 1:
            while True:
                print("\033[2J\033[3J\033[H", end="")
                print(f"1.查看介绍：{g.view_introductions}")
                print(f"2.打开背包：{g.open_backpack}")
                print(f"3.攻击：{g.attack_key}")
                print(f"4.使用道具：{g.use_props}")
                print(f"5.退出：{g.return_next}")
                print("\033[31m6.退出设置\033[0m")
                
                option = get_options(6)
                
                if option == 6:
                    break
                old_trigger_key = list(g.trigger_key.values())  # 保存原本的触发键数据
                trigger_key = old_trigger_key.copy()
                trigger_key[option-1] = input(f"将{option}的触发键改为：")
                if len(trigger_key) != len(set(trigger_key)):  # 防止触发键重复导致一个按键触发多个功能
                    trigger_key = old_trigger_key
                
                g.trigger_key = {
                    "view_introductions": trigger_key[0],
                    "open_backpack": trigger_key[1],
                    "attack_key": trigger_key[2],
                    "use_props": trigger_key[3],
                    "return_next": trigger_key[4]
                }
                for key, value in g.trigger_key.items():
                    setattr(g, key, value)
        else:
            pass
            
def view_introduction(view_object):
    """
    查看对象的信息（用于战斗过程中）
    
    清屏后打印对象的生命值、攻击力、武器和状态效果。
    生命值根据百分比显示不同颜色：
        - >75%：绿色
        - 25%~75%：黄色
        - <25%：红色
    
    Args:
        view_object: 要查看的对象，需包含以下属性：
            name (str): 对象名称
            health (Decimal): 当前生命值
            health_max (Decimal): 生命值上限
            physical_attack (int): 物理攻击力
            water_attack (int): 水属性攻击力
            ice_attack (int): 冰属性攻击力
            fire_attack (int): 火属性攻击力
            electric_attack (int): 电属性攻击力
            weapons (str): 所持武器名称，为空字符串表示无武器
            status_effect (str): 状态效果描述
    
    Raises:
        不抛出异常，若对象缺少必要属性，会捕获并打印错误信息
    
    Note:
        函数会阻塞，等待用户按回车键继续
    """
    print("\033[2J\033[H\033[3J", end="")
    
    try:
        print(view_object.name)
        
        if view_object.health <= view_object.health_max and view_object.health >= view_object.health_max*Decimal("0.75"):
            print(f"生命值：\033[38;2;68;255;136m{view_object.health}\033[0m / \033[38;2;128;128;128m{view_object.health_max}\033[0m")
        elif view_object.health < view_object.health_max*Decimal("0.75") and view_object.health > view_object.health_max*Decimal("0.25"):
            print(f"生命值：\033[38;2;255;204;68m{view_object.health}\033[0m / \033[38;2;128;128;128m{view_object.health_max}\033[0m")
        elif view_object.health <= view_object.health_max*Decimal("0.25"):
            print(f"生命值：\033[38;2;255;51;68m{view_object.health}\033[0m / \033[38;2;128;128;128m{view_object.health_max}\033[0m")
        else:
            pass
        print(f"攻击力：{view_object.physical_attack + view_object.water_attack + view_object.ice_attack + view_object.fire_attack + view_object.electric_attack}")    
        if not view_object.weapons == "":
            print(f"持有武器：{view_object.weapons}")    
        print(f"状态效果:{view_object.status_effects}")
    except Exception as e:
        print(f"查看对象出错: {e}")
    input()
    
def shop():  # 临时
    """商店"""
    while True:
        print("\033[2J\033[H\033[3J", end="")
        print("\033[31m商店\033[0m")
        print("1.medicine：10")
        print("\033[31m2.退出商店\033[0m")
        option = get_options(2)
        if option == 1:
            if g.player.backpack["money"] >= 10:
                g.player.backpack["money"] -= 10
                if "medicine" in g.player.backpack:
                    g.player.backpack["medicine"] += 1
                else:
                    g.player.backpack["medicine"] = 1
            else:
                print("\033[31m你没有那么多钱！\033[0m")
                print("\033[1A\033[2K\033[G",end="")
        if option == 2:
            break
            
def backpack():
    """背包"""
    while True:
        print("\033[2J\033[H\033[3J", end="")
        for i in range(len(g.player.backpack)):
            print(f"{i+1}.{list(g.player.backpack.keys())[i]}：{g.player.backpack[list(g.player.backpack.keys())[i]]}")
        option = get_options([g.view_introductions,g.use_props,g.return_next])
        if option == g.view_introductions:
            print(f"你查看对象的序号是：{get_options(len(g.player.backpack))}")
        elif option == g.use_props:
            print(f"你使用对象的序号是：")
            option = get_options(len(g.player.backpack))
            if "medicine" in g.player.backpack:
                if option == list(g.player.backpack.keys()).index("medicine")+1:
                    g.player.backpack["medicine"] -= 1
                    if g.player.backpack["medicine"] == 0:
                        del g.player.backpack["medicine"]
                    g.player.health += 35
                    print("你恢复了35点血量")
                    time.sleep(1.2)
        elif option == g.return_next:
            break
        if g.player.health > 100:
            g.player.health = 100
            
def battle_ui():
    """
    显示战斗界面，处理玩家回合操作
    
    显示玩家和敌方阵营的角色名称和生命值，玩家操作时能调用打开背包、查看对象信息、攻击对象的功能
    
    Note:
        调用时会清屏
        怪物对象的值为""代表已死亡
        玩家和怪物行动时会触发状态效果
        函数内部使用 while 循环阻塞等待用户输入
        怪物自动攻击后会暂停等待玩家按键
    """
    print("\033[2J\033[H\033[3J", end="")
    
    print(f"You:\n{g.user_name}\n血量：{g.player.health}")
    
    print("Enemy:")
    for i in range(len(g.monsters_team)):
        if g.monsters_team[f"monster{i+1}"] != "":  # 避免显示已死亡的怪物
            print(f"{i+1}.{g.monsters_team[f"monster{i+1}"].name}\n血量：{g.monsters_team[f"monster{i+1}"].health}")
    
    keys_list = [
        g.view_introductions,
        g.open_backpack,
        g.attack_key
        ]  # 玩家可调用的功能触发键
    
    def get_alive_monster_index(team):
        """获取玩家选择的存活怪物序号"""
        option = get_options(len(team))
        while team[f"monster{option}"] == "":
            print("\033[31m请输入正确的选项序号！\033[0m", end="")
            print("\033[1A\033[2K\033[G", end="")
            option = get_options(len(team))
        return option
    
    operator = get_options(keys_list)
    
    if operator == g.view_introductions:
        print(f"你查看对象的序号是：")
        
        option = get_alive_monster_index(g.monsters_team)
        
        view_introduction(g.monsters_team[f"monster{option}"])
    elif operator == g.open_backpack:
        backpack()
    elif operator == g.attack_key:
        print(f"你攻击对象的序号是：")
        
        option = get_alive_monster_index(g.monsters_team)
        
        print(f"你对{g.monsters_team[f"monster{option}"].name}{option}造成了{all_attacks(g.player,g.monsters_team[f"monster{option}"])}点伤害")
        input()
        
        print("\033[2A\033[2K\033[1A\033[2K", end="")
        if g.player.status_effects:
            print("\033[s",end="")
            perform_effect_attack(g.player)
            input()
            print("\033[u\033[J\033[1A")
        
        for key,value in g.monsters_team.items():
            if value != "":
                print(f"{value.name}对你造成了{all_attacks(value,g.player)}点伤害")
                
                perform_effect_add(value, g.player, g.monsters_effect_add_data, g.monsters_team, [g.player])
                
                if value.status_effects:
                    perform_effect_attack(value)
            time.sleep(1)
        input()
    else:
        pass                 