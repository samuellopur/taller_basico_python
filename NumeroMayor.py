print("Calcular el mayor de tres números")
print("")

def calcularNroMayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
    

num1 = float(input("Ingresa número 1: "))
num2 = float(input("Ingresa número 2: "))
num3 = float(input("Ingresa número 3: "))

mayor = calcularNroMayor(num1, num2, num3)
print("El mayor número es:", mayor)

