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


def piskvorky1D(strategie1, strategie2, delka_pole=20):
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
        pole = strategie1(pole)
        if vyhodnot(pole) == "o":
            print("Vyhrava 'o':   {}".format(pole))
            break
        pole = strategie2(pole)
        if vyhodnot(pole) == "x":
            print("Vyhrava 'x':   {}".format(pole))
            break
        if vyhodnot(pole) == ".":
            print("Remiza:   {}".format(pole))
            break
    stav = vyhodnot(pole)
    return stav












