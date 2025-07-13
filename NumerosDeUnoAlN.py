print("Números del 1 a N")
print()

numero = int(input("Ingrese un número : "))
contador = 1

if numero <= 0:
    print("Error, ingrese un número positivo")
else:
    while  contador  <= numero:
        print(contador)
        contador += 1 
    
