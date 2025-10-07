def lang():
    import time

    print("\033[34m"+"Please select the language you would like to use. \n"+"\033[31m"+"Kérlek válaszd "+"\033[37m"+"ki milyen nyelvet"+"\033[32m"+" szeretnél használni."+"\033[0m")
    print("1. English")
    print("2. Magyar")
    Supported_Languages = {
        "1": 'Resources.Etext',
        "English": 'Resources.Etext',
        "2": 'Resources.Mtext',
        "Magyar": 'Resources.Mtext',
        "Cat":'Resources.Ctext',
        "Cica":'Resources.Ctext'
    }

    Language_select = None
    while Language_select not in Supported_Languages:
        Language_select = input().strip().capitalize()
        if Language_select in Supported_Languages:
            break
        else:
            print("\033[31;1;4m"+"Incorrect sellection. \nNem választott nyelvet."+"\033[0m")

    Nyelv = __import__(Supported_Languages[Language_select], fromlist=[''])
    Nyelv.finalased_select()
    try:
        Nyelv.anti_cat()
        time.sleep(3)
        Nyelv.cat_img()
    except:
        pass
    input()
    return Nyelv

#a=lang()

def talk(lang):
    lang.text()

def intro(lang):
    lang.intro()

#talk(a)