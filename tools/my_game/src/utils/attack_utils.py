def attack(attacker_attack, attacked_resistance):  # 攻击
    damage = round(attacker_attack*(1-attacked_resistance), 2)
    return damage