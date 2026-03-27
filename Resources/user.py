
Hero={
    "Hp":300,
    "Max_Hp":3000,

    "PhysicalAtk":105,
    "PhysicalFlatPen":0,
    "PhysicalArmoreShred":0,
    "PhysicalPercentPen":0,
    "PhysicalArmore":60,

    "MagicAtk":20,
    "MagicFlatPen":0,
    "MagicArmoreShred":0,
    "MagicPercentPen":0,
    "MagicArmore":70,

    "Mana":200,
    "Max_Mana":200,
    "Speed":95,
    "Omnivamp":0,
    "Crit_Rate":10,
    "Crit_Dmg":55,
    "Name": input("gie me yo name"),

    "Equipment":{
        "Hat":{
            "Type":"Armore",
            "Name":"Hat of truth",
            "Effect":{
                "FutureSight":True,
            }
        },

        "Chestplate":{
            "Type":"Armore",
            "Name":"Criticly important chestplate",
            "Effect":{
                "MagicCrit":True,
                "PhysicalCrit":True,
            }
        },

        "Pants":{
            "Type":"Armore",
            "Name":"Bence pants",
            "Effect":{
                "Accelerated_Healing":True,
                "Heal":{
                    "Condition":"AfterCombat" and "BeforeCombat",
                    "Type":"MissingHealth",
                    "Amount":30
                }
            }
        },

        "Shoes":{
            "Type":"Armore",
            "Name":"First strike kicks",
            "Effect":{
                "StrikeFirst":True
            },
        },

        "Weapon":{
            "Type":"Weapon",
            "Name":"Flimsy sword",
            "Effect":{
                "PhysicalCrit":True,
                "Fire_Resistant":True,
            }
        },

        #"Backpack_lvl":1,
        "Slot1":{
            "Type":"Item",
            "Name":"Potion of healing",
            "Effect":{
                #"Poison_Immune":True,
                "Poison_Resistant":True,
                #"Corruption_Resistant":True,
                #"Fire_Resistant":True,
                #"Fire_Vulnerable":True,
                #"Accelerated_Healing":True,
                #"Deceleration_Healing":True,
                "Heal":{
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

effects={
    "Poison":{
        "Duration":2000,
        "Dmg":10
    },
    "Fire":{
        "Duration":400,
        "Dmg":45
    },
    "Corruption":{
        "Duration":200,
        "Dmg":70
    },
    "Corruption_Touched":{
        "Duration":200,
        "Amount":1
    },
    
    "Regen":{
        "Duration":200,
        "Dmg":45
    },
    "Shielded":{
        "Duration":200,
        "Amount":50
    },
    #"Heal_Increase":{
    #    "Duration":200
    #},
    #"In_Air":{
    #    "Duration":200
    #},
    #"Stunned":{
    #    "Duration":200
    #},
    #"Heal_Decrease":{
    #    "Duration":200
    #}
}