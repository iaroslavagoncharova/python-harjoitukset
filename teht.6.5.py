#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista
#paitsi että siitä on karsittu pois kaikki parittomat luvut.
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
#ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def poista_luvut(kokonaisluvut):
    for k in kokonaisluvut[0:6]:
        if k % 2 == 0:
            pass
        else:
            kokonaisluvut.remove(k)
    return kokonaisluvut


lista = [11, 28, 44, 13, 29, 21]
toinen_lista = lista.copy()
toinen_lista = poista_luvut(toinen_lista)
print(toinen_lista)
print(lista)