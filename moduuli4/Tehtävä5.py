Salsana = "123"
käytäjätunnus = "123"
Väärät_tiedot = 0


while True:
    print("---------------------------")
    k = input("käytäjätunnus: ")
    s = input("salsana: ")
    if Väärät_tiedot == 5:
        print("liian monta yritystä")
        break

    else:
        if k == käytäjätunnus and s == Salsana:
            print("Tervetuloa")
            print("---------------------------")
            break
        else:
            print("Pääsy evätty")
            Väärät_tiedot += 1
            print("---------------------------")
        