#EJERCICIO DE CLASE 
def agregar_elemento(lista, elemento):
    lista.append(elemento)


def modificar_elemento(lista, indice, nuevo_valor):
    if indice >= 0 and indice < len(lista):
        lista[indice] = nuevo_valor
    else:
        print("Índice fuera de rango")


def eliminar_elemento(lista, indice):
    if indice >= 0 and indice < len(lista):
        del lista[indice]
    else:
        print("Índice fuera de rango")

mi_lista = ["Manzana", "Banana", "Cereza", "Damasco"]

agregar_elemento(mi_lista, "Uva")

modificar_elemento(mi_lista, 1, "Pera")

eliminar_elemento(mi_lista, 2)

print(mi_lista)
