def menu():
    print("Bienvenido a la calculadora de conversiones")
    print("1. Convertir metros a kilómetros")
    print("2. Convertir kilogramos a libras")
    print("3. Convertir litros a mililitros")
    print("4. Convertir Celsius a Fahrenheit")
    print("5. Salir")

def convertir_metros_a_kilometros(metros):
    return metros / 1000

def convertir_kilogramos_a_libras(kilogramos):
    return kilogramos * 2.20462

def convertir_litros_a_mililitros(litros):
    return litros * 1000

def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

while True:
    menu()

    try:
        opcion = input("Elige una opción (1-5): ")
    
        if opcion == '1':
            metros = float(input("Introduce el valor en metros: "))
            resultado = convertir_metros_a_kilometros(metros)
            print(f"{metros} metros son {resultado} kilómetros.")
    
        elif opcion == '2':
            kilogramos = float(input("Introduce el valor en kilogramos: "))
            resultado = convertir_kilogramos_a_libras(kilogramos)
            print(f"{kilogramos} kilogramos son {resultado} libras.")
    
        elif opcion == '3':

            litros = float(input("Introduce el valor en litros: "))
            resultado = convertir_litros_a_mililitros(litros)
            print(f"{litros} litros son {resultado} mililitros.")
    
        elif opcion == '4':
            celsius = float(input("Introduce el valor en Celsius: "))
            resultado = convertir_celsius_a_fahrenheit(celsius)
            print(f"{celsius} Celsius son {resultado} Fahrenheit.")
    
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
        break

    except ValueError:
            print("Error: Por favor, introduce un número válido.")
    except ZeroDivisionError:
            print("Error: División por cero no permitida.")
    
else:
        print("Error: Opción no válida. Por favor, elige una opción entre 1 y 5.")
