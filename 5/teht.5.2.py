#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
numbers = []
readingnumbers = True
while readingnumbers:
    strInput = input('Anna luku:')
    if strInput == ' ':
        readingnumbers = False
    else:
        numbers.append(int(strInput))
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(numbers[0:5])
for number in numbers[0:5]:
    print(number)