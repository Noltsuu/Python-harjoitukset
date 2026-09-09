lista = [1, 2, 4, 5, 6, 7, 8, 9, 10]
lista2 = []
def lista_muuntaja(lista,lista2):
    for luku in lista:
        if luku % 2 == 0:
            lista2.append(luku)
    print(f"Alkuperänen: {lista}\nUusi: {lista2}")
lista_muuntaja(lista, lista2)