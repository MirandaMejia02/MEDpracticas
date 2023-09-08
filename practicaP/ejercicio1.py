def suma(*args):
    total = 0
    for num in  args:
        total +=  num
    return total
    
resultado1 = suma(1,2,3,4,5)
resultado2 = suma(10,20,30,40,50,60)

print(f"la suma es:{resultado1}")
print(f"la suma es:{resultado2}")