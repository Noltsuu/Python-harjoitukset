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


hisi = Hissi(1, 10)
print(f"Hissi on kerroksessa {hisi.nykyinen_kerros}")
hisi.siirry_kerrokseen(5)
print(f"Hissi on kerroksessa {hisi.nykyinen_kerros}")