from random import randint,choice
from decimal import Decimal

from src.common import DAMAGE_TYPE, player
from src.core.effect import effect_method
from src.utils.attack_utils import attack
from src.core.actor import EffectProperty

def death_judgment(detection_object):
    return detection_object.health <= 0

def all_attacks(attacker, attacked):
    total_attack = 0
    for i in DAMAGE_TYPE:
        total_attack += attack(getattr(attacker, f"{i}_attack",0), getattr(attacked, f"{i}_resistance",0))
    attacked.health -= total_attack
    return total_attack

def effect_attack(effect_object, attacked):
    return effect_method[effect_object.name](attacked,effect_object)

def perform_effect_attack(attacked):
    if attacked is player:
        for i in attacked.status_effects:
            print(f"{i.name}{i.level}使你受到了{effect_attack(i,attacked)}点伤害")
    else:
        for i in attacked.status_effects:
            effect_attack(i,attacked)

def effect_add(addee, effect_key, effect_value):
    addee.status_effects.append(EffectProperty(effect_key, effect_value[3], effect_value[4]))

def perform_effect_add(adder, addee, effect_add_data, adder_team, addee_team):
    effect_list = effect_add_data[adder.name]
    for key, value in effect_list.items():
        if randint(1, 1000) <= Decimal(value[0])*1000:
            for _ in range(value[2]):
                if value[1] == "target":
                    effect_add(effect_addee := addee, key, value)
                elif value[1] == "myself":
                    effect_add(effect_addee := adder, key, value)
                elif value[1] == "enemies":
                    effect_add(effect_addee := choice(list(addee_team.values())), key, value)
                elif value[1] == "allies":
                    effect_add(effect_addee := choice(list(adder_team.values())), key, value)
                else:
                    effect_add(effect_addee := addee, key, value)
                if not hasattr(effect_addee, "name"):  # 判断是否为玩家
                    print(f"你被添加了[{key}]")
                else:
                    print(f"{effect_addee.name}被添加了[{key}]")
