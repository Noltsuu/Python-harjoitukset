import random
def noppa():
    lista = []
    tahko = int(input("anna tahkojen määrä: "))
    while True:
        heitto = random.randint(1, tahko)
        lista.append(heitto)
        if heitto == tahko:
            print(lista)
            break
        else:
            continue
noppa()