import random
from ai_1 import tah
from ai_2 import tah_pocitace

def vyhodnot(pole): #vyhodnocuje pole!
    if 'xxx' in pole:
        print('Vyhral x')
        return 'x'
    elif 'ooo' in pole:
        print('Vyhral o')
        return 'o'
    else:
        return False


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



def piskvorky1D(strategie1, strategie2, delka_pole=20):
    pole = delka_pole*'-'
    stav = vyhodnot(pole)
    while not stav:
        pole = strategie1(pole)
        print(pole)
        stav = vyhodnot(pole)

        pole = strategie2(pole)
        print(pole)
        stav = vyhodnot(pole)
    return stav


# print(piskvorky1D(tah_hrace, tah_pocitace))












