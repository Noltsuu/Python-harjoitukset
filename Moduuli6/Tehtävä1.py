import random

def noppa():
    lista = []
    while True:
        heitto = random.randint(1, 6)
        lista.append(heitto)
        if heitto == 6:
            print(lista)
            break
        else:
            continue
noppa()