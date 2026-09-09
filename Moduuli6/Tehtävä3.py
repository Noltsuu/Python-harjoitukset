def bensiinin(gallon_l):
    while True:
        gallon = float(input("anna gallon: "))
        if gallon <= -0:
            break
        else:
            litra = gallon_l * gallon
            print(litra)
            continue
bensiinin(3.785)