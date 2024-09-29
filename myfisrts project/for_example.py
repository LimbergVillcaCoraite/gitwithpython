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

    while (numer_to != 11):
        if numer_to < 11 and numer_to > 0:
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
        
        numer_to = int(input(print("Ingresa un numero")))
    
except:
    print("EL valor ingresado no es valido")
