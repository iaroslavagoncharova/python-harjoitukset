#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
#Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi
# sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
#Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
#Käytä joukkotietorakennetta nimien tallentamiseen.
nimet = set()
nimi = input('Anna nimi: ')
while nimi != ' ':
    if nimi in nimet:
        print('Aiemmin syötetty nimi')
        nimi = input('Anna nimi: ')

    elif nimi not in nimet:
        print('Uusi nimi')
        nimet.add(nimi)
        nimi = input('Anna nimi: ')

    else:
        break

for n in nimet:
    print(n)




