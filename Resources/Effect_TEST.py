
user_effects = {
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
    #"Corruption_Touched":{
    #    "Duration":2,
    #    "Amount":2
    #},
    "Regen":{
        "Duration":2,
        "Heal":45
    },
    #"Heal_Increase":{
    #    "Duration":2
    #},
    #"Heal_Decrease":{
    #    "Duration":2
    #}
}


import user
import Effects
from Effects import EffectsDMG
#print("player hp: ",user.Hero["Hp"])
user.Hero["Hp"] -= EffectsDMG(user_effects,user.Hero)
#print("player hp: ",user.Hero["Hp"])
#print(user_effects)
user_effects=Effects.Effect_Duration(user_effects,user.Hero)
#print(user_effects)
