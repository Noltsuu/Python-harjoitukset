import random
lista = []
arpakuutioiden_määrä = int(input("arpakuutioiden määrä: "))
for i in range(arpakuutioiden_määrä):
    tulos = random.randint(1, 6)
    lista.append(tulos) 
print(sum(lista))