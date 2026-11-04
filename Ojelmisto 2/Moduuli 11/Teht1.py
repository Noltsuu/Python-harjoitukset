class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, smaara):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.smaara = smaara

    def tulosta_tiedot(self):
        print(f"kirja: {self.nimi}")
        print(f"kirjailija: {self.kirjoittaja}")
        print(f"sivumäärä: {self.smaara}\n")


class Lehti(Julkaisu):
    def __init__(self, nimi, Päätoi):
        self.nimi = nimi
        self.Päätoi = Päätoi

    def tulosta_tiedot(self):
        print(f"kirja: {self.nimi}")
        print(f"päätoimittaja: {self.Päätoi}\n")


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_numero_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti_numero_6.tulosta_tiedot()