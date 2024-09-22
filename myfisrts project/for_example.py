# for es un ciclo que se ejecuta un determinado numero de veces

try:
    numer_to = int(input("Ingresa un numero: "))

    numer_to = numer_to

    # 0 -> 1
    # 1 -> 2
    # 2 -> 3
    # 3 -> 4
    # 4 -> 5

# Tablas de multiplicar del 1 al numero ingresado por el usuario, ademas el usuario no debe ingresar
# numeros mayores 10

    for i in range(1, 11, 1):
        print(i, "*", numer_to, "=", i * numer_to)
except:
    print("EL valor ingresado no es valido")

# input = 11
# error, es un numero no permitido

# input = 2
# 1, 2

# input = 5
# 1, 2, 3, 4, 5