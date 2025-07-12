print ("Tabla de multipicar")

num = int(input("Ingrese un número para generar tabla: "))

print (f"Tabla del {num}")

for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result}")


