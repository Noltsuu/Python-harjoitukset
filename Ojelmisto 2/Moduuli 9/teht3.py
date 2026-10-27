class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyttää(self, nopeudenmuutos):
        self.tämänhetkinen_nopeus += nopeudenmuutos

        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tuntimäärä


auto1 = Auto("abc-123", 142)

auto1.kiihdyttää(60)
auto1.kulje(1.5)

print(f"Kuljettu matka: {auto1.kuljettu_matka} km")