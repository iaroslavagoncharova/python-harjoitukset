import math
le = (float)(input('Anna leiviskät: '))
na = (float) (input ('Anna naulat: '))
lu = (float) (input ('Anna luodit: '))
grammat = 20 * 32 * 13.3 * le + 32 * 13.3 * na + 13.3 * lu
kilot = math.floor(grammat/1000)
print(f'Massa nykymittojen mukaan:\n {kilot} kilogrammaa')


