# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
gender = input('Sukupuolesi (nainen/mies)? ')
hg_value = int(input('Hemoglobiinisi (g/l)? '))

if gender == 'nainen':
    #testataan naisen ohjearvot
    if not (5 < hg_value < 300):
        print('Virheellinen hg-arvo')
    if hg_value < 117:
        print('Hemoglobiiniarvo on alhainen')
    elif hg_value < 175:
        print('Hemoglobiiniarvo on normaali')
    else:
        print('Hemoglobiiniarvo on korkea')
elif gender == 'mies':
    #testataan miehen arvot
    if not (5 < hg_value < 300):
        print('Virheellinen hg-arvo')
    if hg_value < 134:
        print('Hemoglobiiniarvo on alhainen')
    elif hg_value < 195:
        print('Hemoglobiiniarvo on normaali')
    else:
        print('Hemoglobiiniarvo on korkea')


