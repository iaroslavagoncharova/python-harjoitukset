#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

number = 1
while number < 1000:
    number = number + 1
    if number % 3 == 0:
        print(number)
print(f'number arvo lopuksi: {number} (ei kuulu tehtävänantoon)')