from decimal import Decimal
from src.utils.attack_utils import attack
import random
# object, effect_object
def burn(obj, e_obj):  # 燃烧
    total_damage = 0
    e_obj.duration -= 1
    if e_obj.duration <= 0 and e_obj.level >= 1:
        e_obj.level -= 1-e_obj.duration
        e_obj.duration = 1
    if e_obj.level <= 5:
        damage = attack(e_obj.level*Decimal("1.5") + 2, obj.fire_resistance)
        total_damage += damage
        obj.health -= damage
    else:
        damage = attack(e_obj.level + Decimal("4.5"), obj.fire_resistance)
        total_damage += damage
        obj.health -= damage
    return total_damage, "damage"
  
def freeze(obj, e_obj):  # 冻结
    e_obj.duration -= 1
    if random.randint(1,100) <= e_obj.level*10:
        e_obj.duration += 1
    obj.can_attack = False
    if e_obj.duration <= 0:
        obj.can_attack = True
    return None, None

def instant_health(obj, e_obj):  # 瞬间治疗
    total_treatment = 0
    e_obj.duration = 0
    treatment = random.randint(e_obj.level*5, 4 + e_obj.level**2)
    total_treatment += treatment
    obj.health += treatment
    return total_treatment, "treatment"

def regeneration(obj, e_obj):  # 生命恢复
    total_treatment = 0
    e_obj.duration -= 1
    treatment = e_obj.level*Decimal("2.5")
    total_treatment += treatment
    obj.health += treatment
    return total_treatment, "treatment"

def stun(obj, e_obj):  # 眩晕
    e_obj.level = 1
    e_obj.duration -= 1
    obj.can_attack = False
    if e_obj.duration <= 0:
        obj.can_attack = True
    return None, None

def numb(obj, e_obj):  # 麻痹
    e_obj.duration -= 1
    total_damage = 0
    if random.randint(1,100) <= e_obj.level*10:
        damage = attack(Decimal(random.randint(100,225))/100, obj.electric_resistance)
        total_damage += damage
        obj.health -= damage
    obj.can_attack = False
    obj.can_operate = False
    if e_obj.duration <= 0:
        obj.can_operate = True
        obj.can_attack = True
    return total_damage, "damage"

def poisoned(obj, e_obj):  # 中毒
    total_damage = 0
    e_obj.duration -= 1
    if random.randint(1,10000) <= 5:
        damage = round(Decimal("0.15")*obj.health,2)
        total_damage += damage
        obj.health -= damage
    damage = e_obj.level*2 + 2
    total_damage += damage
    obj.health -= damage
    return total_damage, "damage"

def tetanus(obj, e_obj):  # 破伤风
    total_damage = 0
    e_obj.duration -= 1
    damage = round(30*Decimal("1.15")**e_obj.level/obj.health,2)
    total_damage += damage
    obj.health -= damage
    if damage <= Decimal("1.75"):
        e_obj.duration += 1
    if damage > 22:
        e_obj.level -= 1
    return total_damage, "damage"

def wet(obj, e_obj):  # 潮湿
    e_obj.duration -= 1
    if random.randint(1,100) <= ((e_obj.level*(1 - obj.water_resistance)*4)/obj.health)*100:
      e_obj.duration += 1
    return None, None

effect_method = {
    "burn": burn,
    "freeze": freeze,
    "instant_health": instant_health,
    "regeneration": regeneration,
    "stun": stun,
    "numb": numb,
    "poisoned": poisoned,
    "tetanus": tetanus,
    "wet": wet
}