#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

userInput = int(input('Anna kokonaisluku: '))
luku = userInput
if luku % 1 == 0 and luku % luku == 0:
    print('Se on alkuluku')
else:
    print('Se ei ole alkuluku')