def Test_Hero(name):
    Hero={
        "Hp":300,
        "Max_Hp":300,

        "PhysicalAtk":105,
        "PhysicalFlatPen":0,
        "PhysicalPercentPen":0,
        "PhysicalArmore":60,

        "MagicAtk":20,
        "MagicFlatPen":0,
        "MagicPercentPen":0,
        "MagicArmore":70,

        "Mana":200,
        "Max_Mana":200,
        "Speed":95,
        "Crit_Rate":10,
        "Crit_Dmg":55,
        "Name":name,

        "Equipment":{
            "Hat":{
                "Name":"Hat of truth",
                "Effect":{
                    "FutureSight":True
                }
            },

            "Chestplate":{
                "Name":"Criticly important chestplate",
                "Effect":{
                    "MagicCrit":True,
                    "PhysicalCrit":True
                }
            },

            "Pants":{
                "Name":"Cleric pants",
                "Effect":{
                    "Heal":{
                        "AfterCombat":True,
                        "Type":"MissingHealth",
                        "Amount":35
                    }
                }
            },

            "Shoes":{
                "Name":"First strike kicks",
                "Effect":{
                    "StrikeFirst":True
                },
            },

            "Weapon":{
                "Name":"Flimsy sword",
                "Effect":{
                    "PhysicalCrit":True 
                }
            },

            "Backpack_lvl":1,

                "Slot1":{
                    "Type":"Item",
                    "Name":"Potion of healing",
                    "Effect":{
                        "Heal":{
                            "InCombat":True,
                            "Type":"Flat",
                            "Amount":35
                        }
                    }
                },
                "Slot2":None,
                "Slot3":None,
                "Slot4":None,
                "Slot5":None
            }
        
        }
    return Hero

#a=Test_Hero("Fintos")
#print(a)



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


#import user 
#print(has_effect(user.Hero,"Heal_Increase"))
#print(how_many_effect(user.Hero,"Fire_Resistant"))

####idk mi ez ˇˇ
def heal_where(hero, effect_name, goal):
    for slot in hero["Equipment"]:
        item = hero["Equipment"][slot]
        if slot == effect_name:
            for healz in hero["Equipment"][effect_name]:
                if healz == hero["Equipment"][effect_name]:
                    print()

#print(has_effect(a,"Poison_Immune"))

