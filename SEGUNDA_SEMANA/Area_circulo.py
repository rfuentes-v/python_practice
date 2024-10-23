def calcular_area_circulo(radio):
    PI = 3.1416
    area = PI * radio ** 2
    return area
radio = 7  # Puede cambiar este valor por cualquier otro para el radio 
area = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area}")