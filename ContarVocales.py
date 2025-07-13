print("Contar vocales ")
cadena = str(input("Ingrese una palabra: "))
vocales = "aeiou"
contVocales = 0

for letra in cadena.lower():
    if letra in vocales:
        contVocales+= 1

print("Se encontró ", contVocales, " vocales")
