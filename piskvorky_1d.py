import random
from ai_1 import tah
from ai_2 import tah_pocitace

def vyhodnot(pole): #vyhodnocuje pole!
    if 'xxx' in pole:
        print('Vyhral x')
        return False
    elif 'ooo' in pole:
        print('Vyhral o')
        return False
    else:
        return True


def tah_hrace(pole):
    symbol = 'x'
    try:
        pozice = 2
        # pozice = int(input('Na jakou pozici chces hrat?: '))
    except ValueError:
        return tah_hrace(pole)
    if pole[pozice] == '-':
        return tah(pole, pozice, symbol)
    else:
        print('Na tuhle pozici hrat nelze.')
        return tah_hrace(pole)



def piskvorky1D(delka_pole=20):
    pole = delka_pole*'-'
    stav = vyhodnot(pole)
    while stav:
        pole = tah_hrace(pole)
        print(pole)
        stav = vyhodnot(pole)

        pole = tah_pocitace(pole)
        print(pole)
        stav = vyhodnot(pole)

piskvorky1D()












