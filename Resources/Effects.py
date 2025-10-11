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
    Total=int(round(Total,0))
    return Total

def Effect_Duration(Full_Effects):
    index=[]
    for elem in Full_Effects:
        Full_Effects[elem]["Duration"] -= 1
        if Full_Effects[elem]["Duration"] < 1: index.append(elem)
    while len(index)>0:
        del Full_Effects[index[0]]
        index.pop(0)
    return Full_Effects
    
    
def Effect_checker(Full_Effects,Effect):
    if Effect in Full_Effects:
        return True
    return False


def Effect_Applier(Type,Name,Duration,Amount,Full_Effects):
    if Type=="Dot": 
        if Effect_checker(Full_Effects,Name):
            Full_Effects[Name]["Duration"] += Duration
            Full_Effects[Name]["Dmg"] += Amount
        else:
            Full_Effects[Name]={
                "Duration":Duration,
                "Dmg":Amount
                }
            
    elif Type=="Buff":
        if Effect_checker(Full_Effects,Name):
            Full_Effects[Name]["Duration"] += Duration
            Full_Effects[Name]["Amount"] += Amount
        else:
            Full_Effects[Name]={
                    "Duration":Duration,
                    "Amount":Amount
            }
            
    elif Type=="Status":
        if Effect_checker(Full_Effects,Name):
            Full_Effects[Name]["Duration"]+=Duration
        else:
            Full_Effects[Name]={
                    "Duration":Duration
            }

    else:
        print("Error, itt egy effectet kellett volna kapnod")
    return Full_Effects

def Effect_Remover(Effect,Full_Effects):
    del Full_Effects[Effect]
    return Full_Effects