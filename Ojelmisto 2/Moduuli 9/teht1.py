class Auto:
    def __init__(self, rekisteritunnus, top):
        self.rekisteritunnus = rekisteritunnus
        self.top = top
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

auto1 = Auto("abc-123", 142)
print(f"Rekisteri Tunnus: {auto1.rekisteritunnus}\nHuippunopeus: {auto1.top}\nHuippu nopeus: {auto1.tämänhetkinen_nopeus}\nTänhetkinen nopeus:{auto1.kuljettu_matka}")

