def raiz_n(numero, n):
    if n < 1:
        raise ValueError("El indice de la raiz debes ser un valor positivo. ")
    return numero ** (1/n)

numero = 27
indice = 3

resultado = raiz_n(numero, indice)
print(f"la raiz de {indice}-ésima de {numero} es:  {resultado}")