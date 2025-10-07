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

def DodgeCalc(Speed,Crit):
    import random
    rand=random.randint(1,10000)
    Speed-=int(round(Crit*0.8,0))
    print(Speed)
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



def PoisonClac(Victim,PoisonDMG):
    import Status_checker
    if Status_checker.has_effect(Victim,"Poison_Immune") == True:
        print("no \033[92mPoison\033[0m damage.")
        return 0
    elif Status_checker.has_effect(Victim,"Poison_Resistant") == True:
        PoisonDMG = int(round(PoisonDMG*0.60,0))
        if PoisonDMG < 1:
            print("no \033[92mPoison\033[0m damage.")
            return 0
        else:
            print(PoisonDMG,"\033[92mPoison\033[0m damage.")
            return PoisonDMG
    else:
        print(PoisonDMG,"\033[92mPoison\033[0m damage.")
        return PoisonDMG
                ###Maga a DMG amit sebezni fog



    ########### Slottonként 1x fogadja el az érzékenységet és ellenállást

def FireClac(Victim,FireDMG):
    import Status_checker
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
    import Status_checker
    from Effects import Effect_checker
    CorruptionDMG = Full_Effects["Corruption"]["Dmg"]
    if Effect_checker(Full_Effects,"Corruption_Touched"):
        multiplier = (Full_Effects["Corruption_Touched"]["Amount"]*0.15)+1
        CorruptionDMG = int(round(CorruptionDMG*multiplier,0))

    if Status_checker.has_effect(Victim,"Corruption_Resistant") == True:
        CorruptionDMG = int(round(CorruptionDMG*0.75,0))
        if CorruptionDMG < 1:
            print("no \033[35mCorruption\033[0m damage.")
            return 0
        else:
            print(CorruptionDMG,"\033[35mCorruption\033[0m damage.")
            return CorruptionDMG
    else:
        print(CorruptionDMG,"\033[35mCorruption\033[0m damage.")
        return CorruptionDMG  ###Maga a DMG amit sebezni fog
    
def HealMultCalc(Victim,Full_Effects):
    import Status_checker
    import Effects
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
    
def RegenCalc(Victim,Full_Effects):
    HealDMG = Full_Effects["Regen"]["Heal"]*(HealMultCalc(Victim,Full_Effects)/100)
    HealDMG = int(round(HealDMG,0))
    if HealDMG < 1:
        print("Nothing.")
    else:
        print(HealDMG,"\033[32mHealth\033[0m.")
    return HealDMG


#print(DodgeCalc(400,0))
#print(ArmoreCalc(1500,25,60,8))

