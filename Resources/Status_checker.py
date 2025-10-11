def has_effect(hero, effect_name):
    for slot in hero["Equipment"]:
        item = hero["Equipment"][slot]
        if isinstance(item, dict):
            effect = item.get("Effect")
            if effect and effect_name in effect:
                return True
    return False

def how_many_effect(hero, effect_name):
    effect_number = 0
    for slot in hero["Equipment"]:
        item = hero["Equipment"][slot]
        if isinstance(item, dict):
            effect = item.get("Effect")
            if effect and effect_name in effect:
                effect_number += 1
    return effect_number


####idk mi ez ˇˇ
def heal_where(hero, effect_name, goal):
    for slot in hero["Equipment"]:
        item = hero["Equipment"][slot]
        if slot == effect_name:
            for healz in hero["Equipment"][effect_name]:
                if healz == hero["Equipment"][effect_name]:
                    print()
