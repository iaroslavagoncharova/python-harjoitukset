import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='EggAkkAnn22',
         autocommit=True
         )


def haku(icao):
    sql = 'select latitude_deg, longirude_deg from airport where gps_code="'+icao+'"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        return tulos[0]
    else:
        print('Lentokenttää ei löydy')

locations =[]
for i in range(2):
    icao = input(f'Syötä {i+1}. lentokentän ICAO-koodi: ')
    locations.append(haku(icao))
print(locations)

gap = distance.distance(locations[0], locations[1]).km
print(gap)
print(type(gap))

print(f'Lentokenttien välinen etäisyys on {gap:.2f} km.')

