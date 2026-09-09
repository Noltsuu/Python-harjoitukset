Asemat = {
     
}

while True:
    print("1 = uus lentoasema")
    print("2 = hakea lentoasema tiedot")
    print("3 = Lopeta")
    valinta = input("")

    if valinta == "1":
        ICAO = input("Anna ICAO-koodin: ")
        Nimi = input("Anna Lento aseman nime: ")
        if ICAO != "" and Nimi != "":
             Asemat[ICAO] = Nimi
             print("Talenettu")
        else:
            print("VIRHE!")
    elif valinta == "2":
        etsi = input("Syötä ICAO-koodin: ")
        if etsi in Asemat:
            print(f"ICAO-Koodia {etsi} vastaava lentoasema on: {Asemat[etsi]}")
        else:
            print("ICAO-Koodia vastaavaa lentoasemaa ei löytynty")
    elif valinta == "3":
            print("Ohjelma loppuu.")
            break