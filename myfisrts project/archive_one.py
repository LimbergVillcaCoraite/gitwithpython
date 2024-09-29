menu = 0

while (menu != 20):
    numero = int(input("Ingresa un numero: "))
    rest = numero % 2 #5 / 2 = 1
    if (rest == 0):
        print("Es par")
    else:
        print("Es impar")
    menu = int(input("Press: 20->exit and Press: 21->continue: "))
    

