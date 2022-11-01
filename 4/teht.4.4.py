import random
userInput = int(input('Anna arvaus: '))
i = random.randint(1, 10)
while userInput != i:
    if userInput > i:
        print('Liian suuri arvaus')
        userInput = int(input('Anna arvaus: '))
    if userInput < i:
        print('Liian pieni arvaus')
        userInput = int(input('Anna arvaus: '))
    if userInput == i:
        break
print('Oikein')
