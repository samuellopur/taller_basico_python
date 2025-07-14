print("Programa para encontrar los números perfectos entre 1 y 1000")
print()

for num in range(1, 1001):
    suma = 0  
    
    for i in range(1, num):
        if num % i == 0:
            suma += i  

    if suma == num:
        print(num, "es un número perfecto")
