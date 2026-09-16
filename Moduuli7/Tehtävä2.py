nimet = set()
def nimeet(nimet):
    while True:
        nimi = input("Anna nimi: ")
        if nimi == "":
            print("----------------------\nOhjelmma loppuu!")
            print(*nimet, sep="\n")
            break

        else:
            if nimi in nimet:
                print("Aiemmin syötetty nimi")
                continue
            else:
                print("Uusi nimi")
                nimet.add(nimi)
nimeet(nimet)