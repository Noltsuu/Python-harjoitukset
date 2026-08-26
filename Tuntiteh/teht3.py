vuosiluku = int(input("anna vuose luku: "))

if vuosiluku:
    if vuosiluku % 4 == 0:
        print("oli olympiavuosi")
    else:
        print("ei ollut olympiavuosi")