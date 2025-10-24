import Status_checker
import Effects
import random
import History

def ArmoreCalc(FlatArmore,FlatPen,ArmoreShred,PercentPen):
    FlatArmore-=FlatPen
    PercentArmore = 0
    if FlatArmore<5:
        pass
    else:
        ArmoreShred=(100-ArmoreShred)/100
        FlatArmore=FlatArmore*ArmoreShred
        FlatArmore= int(FlatArmore)
        if FlatArmore < 101:
            PercentArmore=FlatArmore/5
        elif FlatArmore < 201:
            FlatArmore-=100
            PercentArmore=FlatArmore/7
            PercentArmore+=20
        elif FlatArmore < 301:
            FlatArmore-=200
            PercentArmore=FlatArmore/10                
            PercentArmore+=34
        elif FlatArmore < 401:
            FlatArmore-=300
            PercentArmore=FlatArmore/14                
            PercentArmore+=44
        elif FlatArmore < 501:
            FlatArmore-=400
            PercentArmore=FlatArmore/18                
            PercentArmore+=51
        elif FlatArmore < 601:
            FlatArmore-=500
            PercentArmore=FlatArmore/22                
            PercentArmore+=56
        elif FlatArmore < 701:
            FlatArmore-=600
            PercentArmore=FlatArmore/26                
            PercentArmore+=60
        elif FlatArmore < 801:
            FlatArmore-=700
            PercentArmore=FlatArmore/30                
            PercentArmore+=63
        elif FlatArmore < 901:
            FlatArmore-=800
            PercentArmore=FlatArmore/34                
            PercentArmore+=66
        elif FlatArmore < 1001:
            FlatArmore-=900
            PercentArmore=FlatArmore/38                
            PercentArmore+=68
        elif FlatArmore < 2501:
            FlatArmore-=1000
            PercentArmore=FlatArmore/50                
            PercentArmore+=70
        else:
            PercentArmore = 100
    PercentArmore = PercentArmore*(100-PercentPen)/100
    if PercentArmore < 1:
        PercentArmore=0
    return int(round(PercentArmore,0))  #menyi armorja van %ban

def SpeedCalc(Speed,Stunned,In_Air):
    if Stunned:
        return 0
    if In_Air:
        Speed= Speed/2
    return int(round(Speed,0))


def DodgeCalc(Speed,Crit,Stunned,In_Air):
    rand=random.randint(1,10000)
    Speed=SpeedCalc(Speed,Stunned,In_Air)
    Speed -= Crit*0.8
    Speed=int(round(Speed,0))
    DamageAvoided = 0
    if rand < Speed:
        DamageAvoided = 100
    elif rand < Speed*2:
        DamageAvoided = 40
    elif rand < Speed*3:
        DamageAvoided = 25
    elif rand < Speed*4:
        DamageAvoided = 10
    return DamageAvoided #Hány % Sebzés NEM fogja érni



def PoisonClac(Victim,Full_Effects):
    PoisonDMG = Full_Effects["Poison"]["Dmg"]
    if Status_checker.has_effect(Victim,"Poison_Resistant") == True:
        PoisonDMG = int(round(PoisonDMG*0.60,0))
        Effects.Effect_Applier("Dot","Poison",-6,0,Full_Effects)
    if Status_checker.has_effect(Victim,"Poison_Immune") == True or PoisonDMG < 1:
        print("no \033[92mPoison\033[0m damage.")
        return 0
    else:
        print(PoisonDMG,"\033[92mPoison\033[0m damage.")
        return PoisonDMG, Full_Effects
                ###Maga a DMG amit sebezni fog


    ########### Slottonként 1x fogadja el az érzékenységet és ellenállást

def FireClac(Victim,FireDMG):
    Modifier = 10    ##### Base DMG
    Modifier -= Status_checker.how_many_effect(Victim,"Fire_Resistant")
    Modifier += Status_checker.how_many_effect(Victim,"Fire_Vulnerable")
    Modifier = Modifier/10    ###1 az alapértéke, és 10% onként csökenti vagy növeli a damaget
    FireDMG = int(round(FireDMG*Modifier,0))

    if FireDMG < 1:
        print("no \033[31mFire\033[0m damage.")
        return 0
    else:
        print(FireDMG,"\033[31mFire\033[0m damage.")
        return FireDMG   ###Maga a DMG amit sebezni fog
    
    ############################

def CorruptionClac(Victim,Full_Effects):
    from Effects import Effect_checker
    CorruptionDMG = Full_Effects["Corruption"]["Dmg"]
    if Effect_checker(Full_Effects,"Corruption_Touched"):
        multiplier = (Full_Effects["Corruption_Touched"]["Amount"]*0.15)+1
        CorruptionDMG = int(round(CorruptionDMG*multiplier,0))

    if Status_checker.has_effect(Victim,"Corruption_Resistant") == True:
        CorruptionDMG = int(round(CorruptionDMG*0.95,0))
        Effects.Effect_Applier("Dot","Corruption",-40,0,Full_Effects)
    if CorruptionDMG < 1:
        print("no \033[35mCorruption\033[0m damage.")
        return 0
    else:
        print(CorruptionDMG,"\033[35mCorruption\033[0m damage.")
        Effects.Effect_Applier("Buff","Corruption_Touched",200,1,Full_Effects)
        return CorruptionDMG  ###Maga a DMG amit sebezni fog
    
def HealMultCalc(Victim,Full_Effects):
    Multiplier = 100
    if Status_checker.how_many_effect(Victim,"Accelerated_Healing") >0:
        Multiplier += 6 + ((Status_checker.how_many_effect(Victim,"Accelerated_Healing"))*4)
    #####################
    if Status_checker.how_many_effect(Victim,"Deceleration_Healing") >0:
        Multiplier -= 6 + ((Status_checker.how_many_effect(Victim,"Deceleration_Healing"))*4)
    #####################
    if Effects.Effect_checker(Full_Effects,"Heal_Increase") == True:
        Multiplier += 35
    if Effects.Effect_checker(Full_Effects,"Heal_Decrease") == True:
        Multiplier -= 35
    return Multiplier  #a heal szorzoját adja vissza de 100 al elkell osztani

###look
def HealCalc(Victim,Full_Effects,Condition):
    maxh = 0
    missingh = 0
    flath = 0
    for elem in Victim["Equipment"]:
        try:
            if Victim["Equipment"][elem]["Effect"]["Heal"]["Condition"] == Condition and Victim["Equipment"][elem]["Type"] != "Item":
                if Victim["Equipment"][elem]["Effect"]["Heal"]["Type"] == "MaxHealth":
                    maxh += Victim["Equipment"][elem]["Effect"]["Heal"]["Amount"]
                elif Victim["Equipment"][elem]["Effect"]["Heal"]["Type"] == "MissingHealth":
                    missingh += Victim["Equipment"][elem]["Effect"]["Heal"]["Amount"]
                elif Victim["Equipment"][elem]["Effect"]["Heal"]["Type"] == "Flat":
                    flath += Victim["Equipment"][elem]["Effect"]["Heal"]["Amount"]
                else:
                    print("Debug: healing Type error")
        except:
            pass
    maxh= Victim["Max_Hp"]*(maxh/100)
    missingh = ((((((Victim["Hp"]/Victim["Max_Hp"])*100)-100)*-1)/100)*Victim["Max_Hp"])*(missingh/100)
    flath += maxh + missingh
    flath = flath * (HealMultCalc(Victim,Full_Effects)/100)
    return int(round(flath,0))

    
def RegenCalc(Victim,Full_Effects):
    HealDMG = Full_Effects["Regen"]["Dmg"]*(HealMultCalc(Victim,Full_Effects)/100)
    HealDMG = int(round(HealDMG,0))
    if HealDMG < 1:
        print("Nothing.")
    else:
        print(HealDMG,"\033[32mHealth\033[0m.")
    return HealDMG

def ShieldedCalc(Dmg,Full_Effects):
    if Effects.Effect_checker(Full_Effects,"Shielded"):
        Remaining_shield = Full_Effects["Shielded"]["Amount"] - Dmg
        if Remaining_shield < 1:
            _ = Dmg - Full_Effects["Shielded"]["Amount"]
            Effects.Effect_Remover("Shielded",Full_Effects)
            return _  #A Sebzést NEM védte ki teljesen de részét blokkolta
        else:
            Effects.Effect_Applier("Buff","Shielded",0,-Dmg,Full_Effects)
            return 0 #a sebzést teljesen kivédte a pajzs
    else: return Dmg  # Nem volt pajzsa a felhasználónak

