from flask import Flask, Response
import json
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='EggAkkAnn22',
    autocommit=True
)
app = Flask(__name__)
@app.route('/kentta/<icao>')

def kentta(icao):
    try:
        icao = str(icao)
        sql ="SELECT name, municipality FROM airport WHERE ident = '" + icao + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        for i in tulos:
            nimi = i[0]
            kaupunki = i[1]
        tilakoodi = 200
        vastaus = {
            "ICAO": icao,
            "Name": nimi,
            "Municipality": kaupunki,
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)





