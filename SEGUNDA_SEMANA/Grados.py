def convertir_temperatura(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = convertir_temperatura(celsius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")