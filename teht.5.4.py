#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
#(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen
#Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
#käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

cities = []
# count = 0
# while count < 5:
#    strInput = int(input('Anna kaupungin nimi: '))
#     count += 1
#     cities.append(strInput)
# else:
#     print(cities[0:5])

for i in range(5):
    strInput = input('Anna kaupungin nimi: ')
    cities.append(strInput)

for city in cities:
    print(city)
