class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Kerros: {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Kerros: {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohdekerros):
    
        if kohdekerros > self.ylin_kerros or kohdekerros < self.alin_kerros:
            return

        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylös()

        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissit):
        self.alin = alin
        self.ylin = ylin
        self.hissit = hissit
        self.hissit = []


        for i in range(hissit):
            self.hissit.append(Hissi(alin, ylin))


    def aja_hissiä(self, Hissi_N, kerros):
            if 1 <= Hissi_N <= len(self.hissit):
                print(f" Hissi numero: {Hissi_N} hissi on matkalla kerokkseen: {kerros}")
                self.hissit[Hissi_N - 1].siirry_kerrokseen(kerros)
               
talo = Talo(1, 10, 3)

talo.aja_hissiä(1, 7)

talo.aja_hissiä(2, 4)

