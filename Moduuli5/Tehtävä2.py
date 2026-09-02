lista = []
while True:
    syöte = input("anna luku: ")
    if syöte == "":
        break
    else:
        lista.append(syöte)
lista.sort(reverse=True)
for a in lista[:5]:
    print(a)