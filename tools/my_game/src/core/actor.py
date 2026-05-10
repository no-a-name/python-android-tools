from decimal import Decimal

class PlayerProperty:
    def __init__(self,health,health_max,physical_attack,water_attack,ice_attack,fire_attack,electric_attack,physical_resistance,water_resistance,ice_resistance,fire_resistance,electric_resistance,backpack,status_effects,can_attack,can_operate):
        self.health = Decimal(health)
        self.health_max = Decimal(health_max)
        self.physical_attack = Decimal(physical_attack)
        self.water_attack = Decimal(water_attack)
        self.ice_attack = Decimal(ice_attack)
        self.fire_attack = Decimal(fire_attack)
        self.electric_attack = Decimal(electric_attack)
        self.physical_resistance = Decimal(physical_resistance)
        self.water_resistance = Decimal(water_resistance)
        self.ice_resistance = Decimal(ice_resistance)
        self.fire_resistance = Decimal(fire_resistance)
        self.electric_resistance = Decimal(electric_resistance)
        self.backpack = backpack
        self.status_effects = status_effects
        self.can_attack = can_attack
        self.can_operate = can_operate
        
class MonsterProperty:
    def __init__(self,name,health,physical_attack,water_attack,ice_attack,fire_attack,electric_attack,physical_resistance,water_resistance,ice_resistance,fire_resistance,electric_resistance,weapons,introduction):
        self.name = name
        self.introduction = introduction
        self.health = Decimal(health)
        self.health_max = Decimal(health)
        self.physical_attack = Decimal(physical_attack)
        self.water_attack = Decimal(water_attack)
        self.ice_attack = Decimal(ice_attack)
        self.fire_attack = Decimal(fire_attack)
        self.electric_attack = Decimal(electric_attack)
        self.physical_resistance = Decimal(physical_resistance)
        self.water_resistance = Decimal(water_resistance)
        self.ice_resistance = Decimal(ice_resistance)
        self.fire_resistance = Decimal(fire_resistance)
        self.electric_resistance = Decimal(electric_resistance)
        self.weapons = weapons
        self.status_effects = []
        self.can_attack = True
        self.can_operate = True

class EffectProperty:
    def __init__(self,name,level,duration):
        self.name = name
        self.level = level
        self.duration = duration