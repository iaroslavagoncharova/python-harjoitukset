# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
def palauta_summa(summa1):
    loppusumma = 0
    for n in summa1:
        loppusumma += n
    return loppusumma


lista = [1, 2, 4, 18, 29, 14, 48]
summa = palauta_summa(lista)
print(summa)
