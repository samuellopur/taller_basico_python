def validarEsPalindromo(palabra):
    
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

texto = input("Ingresa una palabra: ")
validarEsPalindromo(texto)

