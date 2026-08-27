import random
while True:
    vastus = random.randint(1, 10)
    arvaus = int(input("Arvaa luku: "))

    if vastus == arvaus:
        print("Sait oikein")
        break
    elif vastus < arvaus:
        print("arvaus liian suuri")
    elif vastus > arvaus:
        print("arvaus liian pieni")