lista = []
lista2 = []
import random
def lista_gen(lista):
    for _ in range(10):
        x = random.randint(1, 100)
        r = random.randint(1, x)
        lista.append(r)
lista_gen(lista)
def lista_muuntaja(lista,lista2):
    for luku in lista:
        if luku % 2 == 0:
            lista2.append(luku)
    print(f"Alkuperänen: {lista}\nUusi: {lista2}")
lista_muuntaja(lista, lista2)