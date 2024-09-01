
import random

number_one = int(input("Input to number: ")) #input recibe un string al momento de que se ingresa un dato
number_dos = random.randint(0, 100)
dateint = int(18)

#print(number_one, number_dos, sep="-----")
#print(type(number_one))

if number_one == number_dos:
    print("Son iguales")
else:
    print("No iguales")

if number_one >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
