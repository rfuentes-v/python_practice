# Funcion para sumar los valores 

def suma(a,b):
    return a + b

# Funcion para restar dos valores 

def resta(a,b):
    return a - b

# Funcion para multiplicar dos numeros
def multiplicacion(a,b):
    return a * b

# Funcion para dividir dos numeros
def division(a,b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a/b

# Fubcion para mostrar menu de opciones
def menu():
    print("Menu de la calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir") 

# Funcion principal que ejecuta el programa de la claculadora
def ejecutar_calculadora():

    while True:  # Bucle infinito hasta que se elija la opcion de salir
        menu()
        try:
            # Solicita al usuario que elija una opcion del menu
            opcion = int(input("Seleccione una opcion (1-5):"))
            if opcion == 5:
                print("Saliendo del programa...")
                break
            if opcion < 1 or opcion > 5:
                print("Ingrese un numero valido")
                continue
            # Solicita los dos numeros para realizar la operacion
            num1 = float(input("Ingrese el primer numero"))
            num2 = float(input("Ingrese el segundo numero"))

            if opcion == 1:
                resultado = suma(num1,num2) # Realiza la suma
                print(f"El resultado de la suma es: {resultado}")
            elif opcion == 2:
                resultado = resta(num1,num2) # Realiza la resta
                print(f"El resultado de la resta es: {resultado}")
            elif opcion == 3:
                resultado = multiplicacion(num1,num2) # Realiza la multiplicacion
                print(f"El resultado de la multiplicacion es: {resultado}")
            elif opcion == 4:
                resultado = division(num1,num2) # Realiza la division
                print(f"El resultado de la division es: {resultado}")
            # Primer posible error es capturar errores de tipo ValuError, como cuando se ingresa valor no numerico
        except ValueError:
            print("Error: Ingresar un valor valido")
            # Captura el error de division por cero cuando se intenta dividir por cero
        except ZeroDivisionError as e:
            print(f"Error; {e}")
        except Exception as e:
            # Captura cualquier otro error inesperado
            print(f"Ocurrio un error inesperado: {e}")        

# Llamada a la funcion 
ejecutar_calculadora()


