while True:
    print("\n=== MENÚ ===")
    print("1. Calcular el cuadrado de un número")
    print("2. Mostrar números pares entre dos valores")
    print("3. Salir del programa")

    opcion = input("Elige una opción (1, 2 o 3): ")

    if opcion == "1":
        numero = int(input("Ingresa un número: "))
        print("El cuadrado de", numero, "es", numero * numero)

    elif opcion == "2":
        inicio = int(input("Ingresa el primer valor: "))
        fin = int(input("Ingresa el segundo valor: "))
        print("Números pares entre", inicio, "y", fin, ":")
        for num in range(inicio, fin + 1):
            if num % 2 == 0:
                print(num)

    elif opcion == "3":
        print("¡Adiós!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")


