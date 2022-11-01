vuosi = int(input('Anna vuosi: '))
if vuosi % 4 == 0:
    print('Se on karkausvuosi')
elif vuosi % 100 == 0 and vuosi % 400 == 0:
    print('Se on karkausvuosi')
else:
    print('Se ei ole karkausvuosi')