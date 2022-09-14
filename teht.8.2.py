import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='EggAkkAnn22',
         autocommit=True
         )


def löytä_lentoasemat(maakoodi):
    sql = 'SELECT _type, count(*) FROM airport'
    sql += ' WHERE iso_country="'+maakoodi+'"'
    sql += ' group by _type'
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f'Koodilla {maakoodi} löytyy{rivi[1]}, {rivi[0]}')
    else:
        print(f'Koodilla {maakoodi} ei löytyy mitään')
    return

maakoodi = input('Anna maakoodi: ')
löytä_lentoasemat(maakoodi)
