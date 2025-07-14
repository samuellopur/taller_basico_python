def contar_letras(palabra):
   
    frecuencia_letras = {}
    for letra in palabra:
        if letra in frecuencia_letras:
            frecuencia_letras[letra] += 1
        else:
            frecuencia_letras[letra] = 1
    return frecuencia_letras

palabra_usuario = input("Ingrese una palabra: ")
resultados = contar_letras(palabra_usuario)

for letra, cantidad in resultados.items():
    print(f"La letra '{letra}' aparece {cantidad} veces.")