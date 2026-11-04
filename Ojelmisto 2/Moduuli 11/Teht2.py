import random

class Auto:
    def __init__(self, rekari, h_nopeus):
        self.rekari = rekari
        self.h_nopeus = h_nopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus = self.nopeus + muutos

        if self.nopeus > self.h_nopeus:
            self.nopeus = self.h_nopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka = self.matka + self.nopeus * aika

class Sähkö(Auto):
    def __init__(self, rekari, h_nopeus, kw):
        super().__init__(rekari, h_nopeus)
        self.akku = kw

class bensa(Auto):
    def __init__(self, rekari, h_nopeus, koko):
        super().__init__(rekari, h_nopeus)
        self.tankin_koko = koko

        
bensa_auto = bensa("ACD-123", 165, 32.3)
sähköauto = Sähkö("ABC-15", 180 , 52.5)   

sähköauto.kiihdytä(100)
bensa_auto.kiihdytä(120)

sähköauto.kulje(3)
bensa_auto.kulje(3)

print(f"{sähköauto.rekari}: matkamittarilukemat {sähköauto.matka} km")
print(f"{bensa_auto.rekari}: matkamittarilukemat {bensa_auto.matka} km")