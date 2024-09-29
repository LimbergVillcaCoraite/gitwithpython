# for es un ciclo que se ejecuta un determinado numero de veces

try:
    numer_to = int(input("Ingresa un numero: "))

    # 0 -> 1
    # 1 -> 2
    # 2 -> 3
    # 3 -> 4
    # 4 -> 5

# Tablas de multiplicar del 1 al numero ingresado por el usuario, ademas el usuario no debe ingresar
# numeros mayores 10

    if numer_to < 11:
        for j in range (1, numer_to + 1, 1):
            print("------------------")
            for i in range(1, 11, 1):
                if i == 10:
                    print("|", j, " * ", i, "  = ", i * j)
                else:
                    print("|", j, " * ", i, "  =  ", i * j)
            print("------------------")
    else:
        print("EL numero no es valido")
except:
    print("EL valor ingresado no es valido")

# input = 11
# error, es un numero no permitido

# input = 2
# 1, 2

# input = 5
# 1, 2, 3, 4, 5
