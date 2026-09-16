import math
eka = int(input("Anna pizzan halkaisia: "))
eka_h = int(input("Anna pizzan hinta: "))
toka = int(input("Anna pizzan halkaisia: "))
toka_h = int(input("Anna pizzan hinta: "))

def Pizza_laskuri(halkaisija, hinta):
    a = halkaisija / 100
    b = a / 2
    c = math.pi * b * b
    vastaus = hinta / c
    hinta / c
    return vastaus
pizza1 = Pizza_laskuri(eka, eka_h)
pizza2 = Pizza_laskuri(toka, toka_h)

if pizza1 < pizza2:
    print(f"eka pizza on isompi: {pizza1:.2f}€/m²")

elif pizza1 > pizza2:
    print(f"toka pizza on isompi: {pizza2:.2f}€/m²")