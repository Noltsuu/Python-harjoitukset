gallon_l = 3.785

def bensiinin():
    while True:
        gallon = float(input("anna gallon: "))
        if gallon <= -0:
            break
        else:
            litra = gallon_l * gallon
            print(litra)
            continue
bensiinin()