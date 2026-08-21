leiviskä = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

tulosnaulat = leiviskä * 20 + naula
tulosluoti = tulosnaulat * 32 + luoti
tulosgramma = tulosluoti * 13.3

kg = tulosgramma // 1000
gr = tulosgramma % 1000

print(f"{int(kg)} kilogrammaa ja {round(gr)} grammaa.")