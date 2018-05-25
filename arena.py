#from ai_1 import tah
#from ai_vlada import tah_pocitace as vlada
#from ai_ondra import tah_pocitace as ondra

from ai_1 import tah_pocitace as ai1
from ai_2 import tah_pocitace as ai2

from piskvorky_1d import piskvorky1D

ondra_vyhral = []
vlada_vyhral = []

for i in range(100):

    if piskvorky1D(ai1, ai2) == 'o':
        ondra_vyhral.append('o')
    elif piskvorky1D(ai1, ai2) == 'x':
        vlada_vyhral.append('x')
    else:
        ondra_vyhral.append('.')
        vlada_vyhral.append('.')