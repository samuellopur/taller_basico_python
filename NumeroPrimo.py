print("Número primo")

numero = int(input("Ingrese un número: "))

if numero <= 1:
    print(numero, "No es número primo")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(numero, "No es número primo")
            break
    else:
        print( numero,"Es número primo")