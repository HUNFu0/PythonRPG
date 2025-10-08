def EffectsDMG(Full_Effects,Victim):
    import DmgCalc
    Total = 0
    if Effect_checker(Full_Effects,"Poison") == True:
        print("You take ",end="")
        Total+=DmgCalc.PoisonClac(Victim,Full_Effects["Poison"]["Dmg"])
    
    if Effect_checker(Full_Effects,"Fire") == True:
        print("You take ",end="")
        Total+=DmgCalc.FireClac(Victim,Full_Effects["Fire"]["Dmg"])
    
    if Effect_checker(Full_Effects,"Corruption") == True:
        print("You take ",end="")
        Total+=DmgCalc.CorruptionClac(Victim,Full_Effects)
    
    if Effect_checker(Full_Effects, "Regen") == True:
        print("You heal ", end="")
        Total-=DmgCalc.RegenCalc(Victim,Full_Effects)
    return Total

def Effect_Duration(Full_Effects,Victim):
    index=[]
    for elem in Full_Effects:
        Full_Effects[elem]["Duration"] -= 1
        if Full_Effects[elem]["Duration"] < 1: index.append(elem)
    while len(index)>0:
        del Full_Effects[index[0]]
        index.pop(0)
    return Full_Effects
    
def Effect_Applier(Type,Name,Duration,Amount,Full_Effects):
    if Type=="Dot": 
        if Effect_checker(Full_Effects,Name):
            Full_Effects[Name]["Duration"] += Duration
            Full_Effects[Name]["Dmg"] += Amount
        else:
            Full_Effects={
                Name:{
                    "Duration":Duration,
                    "Dmg":Amount
                }
            }
    elif Type=="Buff":
        if Effect_checker(Full_Effects,Name):
            Full_Effects[Name]["Duration"] += Duration
            Full_Effects[Name]["Amount"] += Amount
        else:
            Full_Effects={
                Name:{
                    "Duration":Duration,
                    "Amount":Amount
                }
            }
    elif Type=="Status":
        if Effect_checker(Full_Effects,Name):
            Full_Effects[Name]["Duration"]+=Duration
        else:
            Full_Effects={
                Name:{
                    "Duration":Duration
                }
            }


        



    
def Effect_checker(Full_Effects,Effect):
    if Effect in Full_Effects:
        return True
    return False




#a=[["Poison",20,10],["Fire",4,45],["Corruption",2,80],["Fragile",2,80],["Shielded",2,80]]
#Effects(a)
#Pl=[["HP",500],["FlatAtk",100],["FlatPen",0],["PercentPen",0],["FlatArmore",100]]


#print(Effect_checker(user_effects,"Fire"))