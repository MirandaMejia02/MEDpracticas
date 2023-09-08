def division(a, b):
  try:
    resultado = a / b
    print(f"El resultado de la división es {resultado}")
  except ZeroDivisionError:
    print("La división entre cero no está definida")
    
division(10, 2)
division(5, 0) 