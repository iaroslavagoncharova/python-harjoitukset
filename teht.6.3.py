#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
#ja palauttaa paluuarvonaan vastaavan litramäärän.
#Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
#Muunnos on tehtävä aliohjelmaa hyödyntäen.
#Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def palauta(määrä):
    litrat = glmäärä * 3.785
    return litrat

glmäärä = int(input('Anna gallonamäärä: '))
while True:
    loppumäärä = palauta(glmäärä)
    if loppumäärä <= 0:
        break
    print(f'Litramäärä on {loppumäärä:.2f}')
    glmäärä = int(input('Anna gallonamäärä: '))
