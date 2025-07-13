print ("Calculo área de un triangulo")

def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))

resultado = calcularAreaTriangulo(base, altura)
print("El área del triángulo es:", resultado)