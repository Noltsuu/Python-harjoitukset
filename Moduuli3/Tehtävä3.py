sukupuoli = input("mikä on suku puoli: ")
while True:
    if sukupuoli == "Mies":
        hemoglobiiniarvon  = int(input("hemoglobiiniarvon: "))
        if  hemoglobiiniarvon in range(134, 192):
            print("hemoglobiiniarvon on normaali")
        elif hemoglobiiniarvon <= 134:
            print("hemoglobiiniarvon on alhainen")
        elif hemoglobiiniarvon >= 192:
            print("hemoglobiiniarvon on Koekea")
    else:
        hemoglobiiniarvon  = int(input("hemoglobiiniarvon: "))
        if  hemoglobiiniarvon in range(117,175):
            print("hemoglobiiniarvon on normaali")
        elif hemoglobiiniarvon <= 134:
            print("hemoglobiiniarvon on alhainen")
        elif hemoglobiiniarvon >= 192:
            print("hemoglobiiniarvon on Koekea")
                

    