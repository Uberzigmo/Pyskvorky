from ai_1 import tah
from ai_1 import tah_pocitace as vlada
from ai_2 import tah_pocitace as ondra
from piskvorky_1d import piskvorky1D

ondra_vyhral = []
vlada_vyhral = []
for i in range(100):

    if piskvorky1D(ondra, vlada) == 'o':
        ondra_vyhral.append('o')
    elif piskvorky1D(ondra, vlada) == 'x':
        vlada_vyhral.append('x')
    else:
        ondra_vyhral.append('.')
        vlada_vyhral.append('.')