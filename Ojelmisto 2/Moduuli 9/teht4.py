import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.tämänhetkinen_nopeus += muutos

        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, tunti):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunti


autot = []

for i in range(1, 11):
    auto = Auto("ABC-" + str(i), random.randint(100, 200))
    autot.append(auto)

kilpailu_jatkuu = True

while kilpailu_jatkuu:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_jatkuu = False

print("Rekisteri Huippunopeus Nykyinen nopeus Matka")

for auto in autot:
    print(auto.rekisteritunnus, " ",
          auto.huippunopeus, " ",
          auto.tämänhetkinen_nopeus, " ",
          auto.kuljettu_matka)