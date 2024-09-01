
import random

maquina = random.randint(0, 2)

print("Piedra = 0", "Papel = 1", "Tijera = 2", sep="\n")

#Piedra tapa papel
#Tijera corta papel
#Piedra aplasta tijera
usuario = int(input("Escribe un numero: "))

print(maquina)
if usuario == maquina:
    print("Empate")


