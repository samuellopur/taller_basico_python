def sumarListaNum(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

lista = [2, 5, 7, 10]
resultado = sumarListaNum(lista)
print("La suma de los números es:", resultado)
