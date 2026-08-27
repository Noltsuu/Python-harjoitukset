lista = []
while True:
    syöte = input("anna luku: ")
    if syöte =="":
        print(f"maximi: {max(lista)} minimi: {min(lista)}"); break
    else:
        lista.append(int(syöte)); print(lista)