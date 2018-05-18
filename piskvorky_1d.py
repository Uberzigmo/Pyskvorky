# retezec = "Caute, tady Zuza \n a zdravi vas!"
# print(retezec)
#
# print("cago\n!!")
#
# print(r'C:\Users\zpiskoro\Desktop\pyladies_vol_2\ukoly')
#
#
# retezec = 'cokolada'
# print(retezec[2:6])
#
# print(retezec.upper())


# def zamen(retezec, pozice, znak):
#     novy_retezec = retezec[:pozice] + znak + retezec[pozice+1:]
#     return novy_retezec

import random
from ai import tah
from ai import tah_pocitace

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
    try:
        pozice = int(input('Na jakou pozici chces hrat?: '))
    except ValueError:
        pozice = random.randrange(0,len(pole))

    symbol = 'x'
    return tah(pole,pozice,symbol)

def piskvorky1D():
    pole = '---------'
    stav = vyhodnot(pole)
    while stav:
        pole = tah_hrace(pole)
        print(pole)
        stav = vyhodnot(pole)

        pole = tah_pocitace(pole)
        print(pole)
        stav = vyhodnot(pole)

piskvorky1D()












