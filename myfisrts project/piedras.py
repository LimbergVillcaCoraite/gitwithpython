
import random

maquina = random.randint(0, 2)

print("Piedra = 0", "Papel = 1", "Tijera = 2", sep="\n")

#Piedra tapa papel
#Tijera corta papel
#Piedra aplasta tijera

print(maquina)
try:
    usuario = int(input("Escribe un numero: "))
    if usuario > 2:
        print("Este es un numero no valido")
    else:
        if usuario == maquina:
            print("Empate")
        else:
            if usuario == 0:
                if maquina == 1:
                    print("Perdiste")
                else:
                    print("Ganaste")
            if usuario == 1:
                if maquina == 0:
                    print("Ganaste")
                else:
                    print("Perdiste")
            if usuario == 2:
                if maquina == 0:
                    print("Perdiste")
                else:
                    print("Ganaste")
except:
    print("No es un numero")


