def contarPalabras(texto):
    palabras = texto.split()
    return len(texto)

texto = input("Escribe una frase: ")
cantidad = contarPalabras(texto)
print("El texto tiene", cantidad, "palabras).")
