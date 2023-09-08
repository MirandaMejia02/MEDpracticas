# Ingresar 5 números
numeros = []
for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Ordenar los números de forma ascendente (usando Bubble Sort)
for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Mostrar los números ordenados
print("Los números ordenados de forma ascendente son:")
for numero in numeros:
    print(numero)