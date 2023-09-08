# Obtener el valor de n
n = int(input("Ingrese el valor de n: "))

# Visualizar los n primeros números en forma descendente
print(f"Los primeros {n} números en forma descendente son:")
for numero in range(n, 0, -1):
    print(numero)   