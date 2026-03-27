jaja = {
    "Hat":{
        "Increased_Healing":True,
        "Poison_Resistant":True,
        "Action1":{
            "Heal":{
                "Target":"Self",
                "Amount": 25,
                "Type":"Flat"
            },
            "Effect_Applie":{
                "Target":"All",
                "Amount":25,
                "Duration":5,
                "Type":"Fire"
            },
            "Condition":{
                "Condition_Type":"Multiple",
                "Battle_Start":True,
                "Has_Status":"Fire_Resistant"
            }
        },
        "Action2":{
            "Heal":{
                "Target":"Self",
                "Amount": 25,
                "Type":"MaxHealth"
            },
            "Effect_Remove":{
                "Target":"Self",
                "Type":"Fire",
                "Duration":"All"
            },
            "Condition":{
                "Condition_Type":"Multiple",
                "Times_In_Fight":1,
                "Left":1,
                "HP_below":10,
                "Has_Effect":"Fire"
            }
        }
    }
}

def CondSearch(Equipment):
    for elem in Equipment:
        try:
            I = 1
            while True:
                print(Equipment[elem]["Action"+str(I)])
                I+=1
                print()
                print()


        except: pass

CondSearch(jaja)