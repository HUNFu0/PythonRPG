import random
import Enemys
import user
import Effects




def combat(selection_name):
    enemy_function = getattr(Enemys, selection_name)
    enemy = enemy_function()
    move=enemy_attack_select(enemy["Moves"])
    print(move)
    next_move(move,selection_name)

    print(user.Hero["Hp"])
    print(Effects.Effect_checker(user_effects,"Poison"))


def enemy_attack_select(movelist):
    #print(movelist)
    #print(len(movelist))
    weight_sum=0
    for i in movelist:
        weight_sum+=movelist[i]["Weight"]
    rand=random.randint(1,weight_sum)
    #print(rand)
    for i in movelist:
        if movelist[i]["Weight"] >= rand and movelist[i]["Weight"] != 0:
            move= i
            break
        else:
            rand-=movelist[i]["Weight"]
    return move
        
def next_move(move,enemy):
    if enemy == "Giant_Cockroach":
        if move=="Bite":
            print("asd")
        if move=="Jump":
            print("das")


user_effects = [["Poison",20,10]]
enemy_effects = []
combat("Giant_Cockroach")