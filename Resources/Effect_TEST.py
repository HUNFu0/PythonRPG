import user
import Effects
from Effects import EffectsDMG

print(user.effects)

#HP TEST
print("player hp: ",user.Hero["Hp"])
user.Hero["Hp"] -= EffectsDMG(user.effects,user.Hero)
print("player hp: ",user.Hero["Hp"])
print()

#EFFECT APPLIER TEST
user.effects = Effects.Effect_Applier("Dot","Poison",500,2,user.effects)
user.effects = Effects.Effect_Applier("Dot","Poipon",500,2,user.effects)
#EFFECT REMOVER TEST
Effects.Effect_Remover("Poipon",user.effects)
print()

#SHIELDED EFFECT TEST (Duration 2)
import DmgCalc
print(DmgCalc.ShieldedCalc(50,user.effects))
print()

#EFFECT LEJÁRÁS TEST
user.effects=Effects.Effect_Duration(user.effects)
print()

print(user.effects)

