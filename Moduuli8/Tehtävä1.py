import mysql.connector

icao = input("Anna lentoaseman ICAO-koodi: ")

yhteys = mysql.connector.connect(
    host="localhost",
    database="flight_game",
    user="Admin",
    password="Admin"
)

c = yhteys.cursor()

sql = """
SELECT name, municipality
FROM airport
WHERE ident = %s
"""

c.execute(sql, (icao,))

tulos = c.fetchone()

if tulos:
    print("Lentokenttä:", tulos[0])
    print("Sijaintikunta:", tulos[1])
else:
    print("ICAO-koodia vastaavaa lentokenttää ei löytynyt.")

c.close()
yhteys.close()
