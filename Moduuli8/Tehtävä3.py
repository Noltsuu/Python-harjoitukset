import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Admin",
    database="flight_game"
)

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ").upper()
icao2 = input("Anna toisen lentokentän ICAO-koodi: ").upper()

c = yhteys.cursor()

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
c.execute(sql, (icao1,))
tulos1 = c.fetchone()

c.execute(sql, (icao2,))
tulos2 = c.fetchone()

if tulos1 and tulos2:

    paikka1 = (tulos1[0], tulos1[1])
    paikka2 = (tulos2[0], tulos2[1])

    etaisyys = geodesic(paikka1, paikka2).kilometers

    print(f"Lentokenttien välinen etäisyys on {etaisyys:.2f} km")

else:
    print("Lentokenttää ei löytynyt.")

c.close()
yhteys.close()
