# kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti
hyttiluokka = input('Anna laivan hyttiluokka ')
if hyttiluokka == 'LUX':
    print ('LUX on parvekkeellinen hytti yläkannella.')
elif hyttiluokka == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hyttiluokka == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hyttiluokka == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka')

