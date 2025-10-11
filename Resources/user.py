
Hero={
    "Hp":300,
    "Max_Hp":300,

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
    "Crit_Rate":10,
    "Crit_Dmg":55,
    "Name":"name",

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
            "Name":"Bence pants",
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
                "PhysicalCrit":True,
                "Fire_Resistant":True,
            }
        },

        "Backpack_lvl":1,

            "Slot1":{
                "Type":"Item",
                "Name":"Potion of healing",
                "Effect":{
                    #"Poison_Immune":True,
                    #"Poison_Resistant":True,
                    #"Corruption_Resistant":True,
                    #"Fire_Resistant":True,
                    #"Fire_Vulnerable":True,
                    #"Accelerated_Healing":True,
                    #"Deceleration_Healing":True,

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

effects={
    "Poison":{
        "Duration":20,
        "Dmg":10
    },
    "Fire":{
        "Duration":4,
        "Dmg":45
    },
    "Corruption":{
        "Duration":2,
        "Dmg":70
    },
    "Corruption_Touched":{
        "Duration":2,
        "Amount":1
    },
    
    "Regen":{
        "Duration":2,
        "Dmg":45
    },
    "Shielded":{
        "Duration":2,
        "Amount":51
    },
    "Heal_Increase":{
        "Duration":2
    },
    #"Heal_Decrease":{
    #    "Duration":2
    #}
}
