from ai_1 import tah
from ai_vlada import tah_pocitace as vlada
from ai_ondra import tah_pocitace as ondra
from piskvorky_1d import piskvorky1D

ondra_vyhral = []
vlada_vyhral = []
for i in range(100):

    if piskvorky1D(ondra, vlada) == 'o':
        ondra.append('o')
    elif piskvorky1D(ondra, vlada) == 'x':
        vlada.append('x')
    else:
        ondra.append('.')
        vlada.append('.')