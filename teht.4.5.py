#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
#(Oikea käyttäjätunnus on python ja salasana rules).

userID = input('Anna käyttäjätunnuksesi: ')
userPassword = input('Anna salasanasi: ')
ID = 'python'
password = 'rules'
count = 0
while (count < 5) and (userID != ID and userPassword != password) and (userID != ID or userPassword != password):
    count += 1
    print('Yritä uudelleen')
    userID = input('Anna käyttäjätunnuksesi: ')
    userPassword = input('Anna salasanasi: ')
    if userID == ID and userPassword == password:
        break
print('Tervetuloa')




