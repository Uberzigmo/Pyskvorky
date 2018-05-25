import random

# Hloupa strategie pro pocitac

# To bude brnkacka vyhrat :) ..
# Teda doufam, snad neni random lepsi nez ja

# !!!!!!!!!!!
# Je tu malo vykricniku

def tah_pocitace(pole):
    """

    :param pole: (str) pole, kde se ma hrat
    :return: (str) zmenene pole
    """
    pozice = random.randrange(len(pole))
    symbol = 'o'
    if pole[pozice] == '-':
        return tah(pole, pozice, symbol)
    else:
        tah_pocitace(pole)

def tah(pole, pozice, symbol):
    """
    Vymeni znak na dane pozici v poli za symbol.
    :param pole: (list) aktualni hraci pole
    :param pozice: (int) kterou pozici zamenit
    :param symbol: (str) jakym znakem nahradit znak na pozici
    :return: None
    """
    return pole[:pozice] + symbol + pole[pozice+1:]