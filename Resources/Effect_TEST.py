import user
import Effects
import DmgCalc
import History
from Effects import EffectsDMG

print(user.effects)

#HP TEST
#print("player hp: ",user.Hero["Hp"])
user.Hero["Hp"] -= EffectsDMG(user.effects,user.Hero)
#print("player hp: ",user.Hero["Hp"])
#print()

#EFFECT APPLIER TEST
#user.effects = Effects.Effect_Applier("Dot","Poison",500,2,user.effects)
#user.effects = Effects.Effect_Applier("Dot","Poipon",500,2,user.effects)
#EFFECT REMOVER TEST
#Effects.Effect_Remover("Poipon",user.effects)
#Effects.Effect_Remover("Poipon",user.effects)
#print()

#SHIELDED EFFECT TEST (Duration 2)
#print(DmgCalc.ShieldedCalc(55,user.effects))
#print()

#EFFECT LEJÁRÁS TEST
user.effects=Effects.Effect_Duration(user.effects)
#print()

#SPEED TEST
#print(DmgCalc.DodgeCalc(user.Hero["Speed"],0,Effects.Effect_checker(user.effects,"Stunned"),Effects.Effect_checker(user.effects,"In_Air")))

#After comabt heal test
#print(DmgCalc.HealCalc(user.Hero,user.effects,"AfterCombat"))

print(user.effects)
print()

for i in range(0,20):
    user.Hero["Hp"] -= EffectsDMG(user.effects,user.Hero)
    user.effects=Effects.Effect_Duration(user.effects)
    print("player hp: ",user.Hero["Hp"])
    print(user.effects)
    input()