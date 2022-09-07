#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
#Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
#Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
#kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
import math
def yksikköhinta1(halkaisija, hinta):
        a = (halkaisija * 0.0001) ** 2 / 4 * math.pi
        hinta1 = pizzan_hinta1 / a
        return hinta1

halkaisija1 = int(input('Anna ekan pizzan halkaisija: '))
pizzan_hinta1 = int(input('Anna ekan pizzan hinta: '))
#halkaisija2 = int(input('Anna tokan pizzan halkaisija: '))
#pizzan_hinta2 = int(input('Anna tokan pizzan hinta'))
loppuhinta1 = yksikköhinta1(halkaisija1, pizzan_hinta1)
print(f'Eka pizza maksaa {loppuhinta1:.2f} euroa/neliömetri')