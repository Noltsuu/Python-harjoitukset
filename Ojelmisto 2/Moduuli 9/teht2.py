class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyttää(self,nopeudenmuutos):
        self.tämänhetkinen_nopeus = self.tämänhetkinen_nopeus + nopeudenmuutos

        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0


auto1 = Auto("abc-123", 142)

print(f"Tämän hetkinen nopeus: {auto1.tämänhetkinen_nopeus}")
auto1.kiihdyttää(30)
print(f"Tämän hetkinen nopeus: {auto1.tämänhetkinen_nopeus}")
auto1.kiihdyttää(70)
print(f"Tämän hetkinen nopeus: {auto1.tämänhetkinen_nopeus}")
auto1.kiihdyttää(50)
print(f"Tämän hetkinen nopeus: {auto1.tämänhetkinen_nopeus}")
auto1.kiihdyttää(-200)
print(f"Tämän hetkinen nopeus: {auto1.tämänhetkinen_nopeus}")
