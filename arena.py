import random
from ai_ondra import tah_pocitace as ai1
from ai_vlada import tah_pocitace as ai2

from piskvorky_1d import piskvorky1D

def gong(pocet_her):
    pocet_her = int(pocet_her/2)
    ondra_vyhral = []
    vlada_vyhral = []

    for i in range(pocet_her):
        """
        Porovna vysledek jedne hry a rozsiri prislusneho pole
        ondra_vyhral nebo vlada_vyhral
        o pozici s vyhernim nebo remizovym symbolem
        (Pro jistotu si Ondra vzal "o" protoze v nahodne strategii vyhraje temer vzdy :) )
        """
        vysledek = piskvorky1D(ai1,'o',ai2,'x')
        if vysledek == "o":
            ondra_vyhral.append("o")
            print("Vyhral Ondra")
        elif vysledek == "x":
            vlada_vyhral.append("x")
            print("Vyhral Vlada")
        elif vysledek == ".":
            ondra_vyhral.append("/")
            vlada_vyhral.append("/")
            print("Remiza")


        vysledek = piskvorky1D(ai2, 'x', ai1, 'o')
        if vysledek == "o":
            ondra_vyhral.append("o")
            print("Vyhral Ondra")
        elif vysledek == "x":
            vlada_vyhral.append("x")
            print("Vyhral Vlada")
        # elif vysledek == ".":
        #     ondra_vyhral.append("/")
        #     vlada_vyhral.append("/")

    print("Ondrovo skore: {}".format((len(ondra_vyhral))))
    print("Vladovo skore: {}".format((len(vlada_vyhral))))

gong(10000)