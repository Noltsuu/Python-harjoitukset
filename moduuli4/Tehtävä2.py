tuuma = 2.54


while True:
    T = int(input("anna tuumat: "))
    tulos = T * tuuma
    if tulos <= 0:
        break
    elif tulos:
        print(f"{tulos}cm")