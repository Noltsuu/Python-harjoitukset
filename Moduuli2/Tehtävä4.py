eka = int(input("Anna eka luku: "))
toka = int(input("Anna toka luku: "))
kolmas  = int(input("Anna kolmas luku: "))
luvut  = [eka, toka, kolmas]

summa = (sum(luvut))
kerto = eka * toka * kolmas
keskiarvo =  sum(luvut) / len(luvut)

print(f"summa: {summa}")
print(f"tulon: {kerto}")
print(f"keskiarvo: {keskiarvo}")