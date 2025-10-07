import Resources.launguage_select as launguage_select
import Resources.Enemys as Enemy
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


lang=launguage_select.lang()
clear()
input()
clear()
input()
a=Enemy.Giant_Cockroach()
print(a["Hp"])
