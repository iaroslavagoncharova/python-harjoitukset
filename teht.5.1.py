
#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan
#Käytä for-toistorakennetta.
import random

dices_num = int(input('Anna arpakuutioiden määrä'))
summa = 0

for dn in range(0, dices_num):
    n=random.randint(1,6)
    summa += n
print(summa)
#
# for määrä in summa:
#
#
# summa.append()
# for n in summa:
#     summa+=n
#     print(summa)