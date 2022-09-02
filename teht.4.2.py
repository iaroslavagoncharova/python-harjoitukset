#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan
#kunnes käyttäjä antaa negatiivisen tuumamäärän
#Sen jälkeen ohjelma lopettaa toimintansa.
#1 tuuma = 2.54 cm

i = int(input('Anna tuumamäärä: '))
while True:
    i = i*2.54
    print(f'{i} cm')
    i = int(input('Anna tuumamäärä: '))
    if i < 0:
        break
print('Negatiivinen tuumamäärä. Ohjelma lopetti toimitansa')

