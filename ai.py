import random

# Hloupa strategie pro pocitac
# To bude brnkacka vyhrat :) ..
# Uz si brousim klavesnici!

def tah_pocitace(pole):
    pozice = random.randrange(len(pole))
    symbol = 'o'
    return tah(pole, pozice, symbol)

def tah(pole, pozice, symbol):
    return pole[:pozice] + symbol + pole[pozice+1:]