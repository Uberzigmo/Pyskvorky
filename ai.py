import random

# Hloupa strategie pro pocitac123
def tah_pocitace(pole):
    pozice = random.randrange(len(pole))
    symbol = 'o'
    return tah(pole, pozice, symbol)

def tah(pole, pozice, symbol):
    return pole[:pozice] + symbol + pole[pozice+1:]