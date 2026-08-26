vuosiluvun = int(input("Anna luku vuosi"))
if vuosiluvun % 4 == 0 and vuosiluvun % 400 == 0:
    print("on karkaus vuosi")
else:
    print("ei ole karkaus vuosi")