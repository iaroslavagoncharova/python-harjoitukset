#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
#Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
#Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
#kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
import math
def yksikköhinta1(halkaisija, hinta):
        a = (halkaisija / 2)** 2 * math.pi
        hinta1 = hinta / a
        return hinta1

def yksikköhinta2(halkaisija, hinta):
        a = (halkaisija / 2) ** 2 * math.pi
        hinta2 = hinta / a
        return hinta2

halkaisija1 = int(input('Anna ekan pizzan halkaisija: '))
pizzan_hinta1 = int(input('Anna ekan pizzan hinta: '))
halkaisija2 = int(input('Anna tokan pizzan halkaisija: '))
pizzan_hinta2 = int(input('Anna tokan pizzan hinta: '))
loppuhinta1 = yksikköhinta1(halkaisija1, pizzan_hinta1)
loppuhinta2 = yksikköhinta2(halkaisija2, pizzan_hinta2)
if loppuhinta1 > loppuhinta2:
        print('Toka pizza on edullisempi')
elif loppuhinta2 > loppuhinta1:
        print('Eka pizza on edullisempi')
