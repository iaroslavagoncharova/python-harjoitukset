#Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
asemat = {}

while True:
    print('1 - syötä uusi')
    print('2 - hae')
    print('3 - lopeta')
    syöttäminen = int(input('Valitse: '))
    if syöttäminen == 1:
        koodi = input('Anna ICAO-koodi: ')
        nimi = input('Anna lentoaseman nimi: ')
        asemat[koodi] = nimi
    elif syöttäminen == 2:
        haku = input('Anna lentoaseman ICAO-koodi: ')
        if haku in asemat:
            print(asemat[haku])
    else:
        break
print('Ohjelma on loppunut')




