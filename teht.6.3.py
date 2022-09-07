#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
#ja palauttaa paluuarvonaan vastaavan litramäärän.
#Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
#Muunnos on tehtävä aliohjelmaa hyödyntäen.


def palauta(määrä):
    litrat = glmäärä * 3.785
    return litrat

glmäärä = int(input('Anna gallonamäärä: '))
loppumäärä = palauta(glmäärä)
print(f'Litramäärä on {loppumäärä:.2f}')