History = []

def add(Target,Type,Amount):
    History.insert(0,[Target,Type,Amount])

'''
add("Game","Combat",1)
add("Game","Turn",1)
add("Buzi","Hit",50)
add("Buzi","heal",30)
add("Hero","shield",90)
add("Game","Turn",2)
add("Buzi","Hit",50)
add("Buzi","Death",1)
add("Game","Combat",2)
add("Game","Turn",2)
'''

def View(History,Lenght):
    if len(History) < Lenght:
        for i in range(0,len(History)):
            if History[i][0]=="Game": print() 
            print(History[i][0],History[i][1],History[i][2])
    else:
        for i in range(0,Lenght):
            if History[i][0]=="Game": print() 
            print(History[i][0],History[i][1],History[i][2])

#View(History,900)