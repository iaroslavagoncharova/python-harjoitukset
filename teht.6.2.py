#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
#Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heitäNoppaa(tahkot):
    luku = random.randint(1, tahkot)
    return luku

tahkoLKM = int(input('Kuinka monta tahkoa? '))
while True:
    silmäluku = heitäNoppaa(tahkoLKM)
    print(silmäluku)
    if silmäluku == tahkoLKM:
        break
