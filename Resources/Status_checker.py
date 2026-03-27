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

def has_condition(hero, condition):
    what_to_trigger=[]
    for slot in hero["Equipment"]:
        item = hero["Equipment"][slot]
        try:
            for elem in item["Effect"]:
                cond = item["Effect"][elem]
                if isinstance(cond, dict): 
                    if cond["Condition"] == condition:
                        what_to_trigger.append(cond)
        except: pass
    return what_to_trigger

import user
print(has_condition(user.Hero,"AfterCombat"))