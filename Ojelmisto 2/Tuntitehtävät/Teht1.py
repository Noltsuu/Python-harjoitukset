class Lentokone:
    def __init__(self ,nimi, bensam, nykyinenbensa):
        self.nimi = nimi
        self.bensam = bensam
        self.nykyinenbensa =  nykyinenbensa

class Lenttokenttä:
    def __init__(self,nimi):
        self.nimi = nimi
        self.koneet = []
    def Lisää_kone(self,kone):
        self.koneet.append(kone)
        print(f"kone listätty{kone.nimi}")

helsinki = Lenttokenttä("helsiki vantaa")
kone = Lentokone("test", 100, 100)
print(f"Koneen nimi: {kone.nimi}\nMaximi bensa: {kone.bensam}\nNykyinen bensa: {kone.nykyinenbensa}")
