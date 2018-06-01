import random
from ai_1 import tah
from ai_2 import tah_pocitace

def vyhodnot(pole):
    vyhra_x = "x"
    vyhra_o = "o"


    if "xxx" in pole:
        print("Vyhrava hrac.")
        return vyhra_x
    elif "ooo" in pole:
        print("Vyhrava AI.")
        return vyhra_o
    elif "-" not in pole:
        print("Remiza")
        return False
    else:
        return True

def tah_hrace(pole):
    symbol = 'x'
    try:
        pozice = int(input('Na jakou pozici chces hrat?: '))
    except ValueError:
        return tah_hrace(pole)
    if pole[pozice] == '-':
        return tah(pole, pozice, symbol)
    else:
        print('Na tuhle pozici hrat nelze.')
        return tah_hrace(pole)



def piskvorky1D(strategie1, strategie2):
    pole = 20*'-'
    stav = vyhodnot(pole)
    while stav:
        print("Hraje AI s O")
        pole = strategie1(pole)
        if vyhodnot(pole) == "o":
            print(pole)
            break
        print(pole)
        print("Hraje AI s X")
        pole = strategie2(pole)
        if vyhodnot(pole) == "x":
            print(pole)
            break
        print(pole)
        return vyhodnot(pole)


#print(piskvorky1D(tah_hrace, tah_pocitace))












