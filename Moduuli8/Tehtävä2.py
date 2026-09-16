import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Admin",
    database="flight_game"
)

c = yhteys.cursor()

maakoodi = input("Anna maakoodi (esim. FI): ").upper()

sql = """
    SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY type
"""

c.execute(sql, (maakoodi,))

tulokset = c.fetchall()

for tyyppi, maara in tulokset:
    print(f"{tyyppi}: {maara}")

c.close()
yhteys.close()
