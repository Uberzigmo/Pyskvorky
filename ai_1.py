import random

# Hloupa strategie pro pocitac

# To bude brnkacka vyhrat :) ..
# Teda doufam, snad neni random lepsi nez ja

# !!!!!!!!!!!


def tah_pocitace(pole):
    """

    :param pole: (str) pole, kde se ma hrat
    :return: (str) zmenene pole
    """

    symbol = 'o'
    while True:
        pozice = random.randrange(len(pole))
        if pole[pozice] is '-':
            return tah(pole, pozice, symbol)



def tah(pole, pozice, symbol):
    """
    Vymeni znak na dane pozici v poli za symbol.
    :param pole: (list) aktualni hraci pole
    :param pozice: (int) kterou pozici zamenit
    :param symbol: (str) jakym znakem nahradit znak na pozici
    :return: None
    """
    return pole[:pozice] + symbol + pole[pozice+1:]

