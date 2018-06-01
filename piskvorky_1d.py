import random
from ai_1 import tah
from ai_2 import tah_pocitace

def vyhodnot(pole): #vyhodnocuje pole!

    """
    Vyhleda v poli podminky pro vyhru hrace A nebo B nebo pripadnou remizu
    Pokud vraci False, tak hra pokracuje
    :param pole: (str) pole, kde to zije!
    :return: (str) vrati vyhru, prohru, remizu nebo Velky Spatny
    """
    if "xxx" in pole:
        #print('Vyhral x')
        return "x"
    elif 'ooo' in pole:
        #print('Vyhral o')
        return "o"
    elif "-" not in pole:
        #print("Remiza")
        return "."
    else:
        return False


def piskvorky1D(strategie1, symbol_1, strategie2, symbol_2, delka_pole=20):
    """
    Hra Valka svetu (resp. x vs o)
    :param strategie1: nacteni strategie prvniho hrace, vraci pole s zahranym symbolem
    :param strategie2: nacteni strategie druheho hrace, vraci pole s zahranym symbolem
    :param delka_pole: delka 1D Pyskvorek
    :return: vraci finalni stav po pyskvorovem masakru
    """

    pole = delka_pole*'-'
    stav = False
    while not stav:
        pole = strategie1(pole, symbol_1)
        if vyhodnot(pole) == symbol_1:
            print("Vyhrava: {}".format((symbol_1,'   ', pole)))
            break
        pole = strategie2(pole, symbol_2)
        if vyhodnot(pole) == symbol_2:
            print("Vyhrava: {}".format((symbol_2,'   ', pole)))
            break
        if vyhodnot(pole) == ".":
            print("Remiza:   {}".format(pole))
            break
    stav = vyhodnot(pole)
    return stav

def prehod_symboly(pole):
    nove_pole = []
    for pozice in range(len(pole)):
        if pole[pozice] == 'x':
            nove_pole.append('o')
        elif pole[pozice] == 'o':
            nove_pole.append('x')
        else:
            nove_pole.append('-')
    return ''.join(nove_pole)











