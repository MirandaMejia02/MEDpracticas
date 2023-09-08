# a. Ingresar n datos a una lista.
def ingresar_datos():
    n = int(input("Ingrese el número de datos: "))
    datos = []
    for _ in range(n):
        dato = float(input("Ingrese un dato: "))
        datos.append(dato)
    return datos

# b. Ordenar una lista de menor a mayor (utilizando el algoritmo de ordenación de burbuja).
def ordenar_lista(datos):
    for i in range(len(datos)):
        for j in range(len(datos)-1):
            if datos[j] > datos[j+1]:
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos

# c. Calcular la sumatoria de los datos de una lista.
def sumatoria(datos):
    suma = 0
    for dato in datos:
        suma += dato
    return suma

# d. Calcular la media de los datos.
def media(datos):
    return sumatoria(datos) / len(datos)

# e. Calcular la mediana.
def mediana(datos):
    datos_ordenados = ordenar_lista(datos)
    n = len(datos_ordenados)
    if n % 2 != 0:
        return datos_ordenados[n // 2]
    else:
        return (datos_ordenados[n // 2 - 1] + datos_ordenados[n // 2]) / 2

# f. Calcular la moda.
def moda(datos):
    conteo = {}
    for dato in datos:
        if dato in conteo:
            conteo[dato] += 1
        else:
            conteo[dato] = 1
    moda = max(conteo, key=conteo.get)
    return moda

# g. Calcular la desviación típica o estándar para datos sin agrupar.
def desviacion_estandar(datos):
    promedio = media(datos)
    suma_cuadrados = sum((dato - promedio)**2 for dato in datos)
    desviacion = (suma_cuadrados / (len(datos) - 1))**0.5
    return desviacion
