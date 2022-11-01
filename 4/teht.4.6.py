import random
inside = 0
i = 0
n = int(input('Anna pisteiden määrä:'))

while i< 0:
    x = random.uniform (-1,1)
    y = random.uniform (-1,1)
    if x**2 + y**2 <=1:
        inside +=1
    i+=1

pi = 4 * inside / n
print(f'pi on {pi}')
