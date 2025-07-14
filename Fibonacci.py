print("Calcular el mayor de tres números")
print()

def generar_Fibonacci(n):
    # Lista para guardar secuencia
    secuencia = []

    for i in range(n):
        if i == 0:
            secuencia.append(0)  # Primer número siempre es 0
        elif i == 1:
            secuencia.append(1)  # Segundo número siempre es 1
        else:
            # Tercer número sumamos los dos anteriores
            nuevo_numero = secuencia[i - 1] + secuencia[i - 2]
            secuencia.append(nuevo_numero)
    return secuencia

# Uso:
numero = int(input("¿Cuántos números de Fibonacci quieres ver? "))
resultado = generar_Fibonacci(numero)
print("Secuencia de Fibonacci:")
print(resultado)

