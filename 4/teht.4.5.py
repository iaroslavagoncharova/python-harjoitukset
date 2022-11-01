#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
#(Oikea käyttäjätunnus on python ja salasana rules).

userID = input('Anna käyttäjätunnuksesi: ')
userPassword = input('Anna salasanasi: ')
count = 0
while (count < 4) and (userID != 'python' and userPassword != 'rules') or (userID != 'python' or userPassword != 'rules'):
    count += 1
    print('Yritä uudelleen')
    userID = input('Anna käyttäjätunnuksesi: ')
    userPassword = input('Anna salasanasi: ')
    if (userID == 'python' and userPassword == 'rules') or count >= 4:
        break
if userID == 'python' and userPassword == 'rules':
    print('Tervetuloa')
else:
    print('Pääsy evätty')


