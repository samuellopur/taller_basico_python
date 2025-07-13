import random

numSecreto = random.randint(1, 10)

numero = int(input("Ingrese un número entre 1 y 10: "))

while numero != numSecreto:
    if numero < numSecreto:
        print("Muy bajo")
    else:
        print("Muy alto")
    numero = int(input("Intenta de nuevo: "))

print("Adivinaste!, el número es", numero)
