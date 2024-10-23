# Ejemplo de una excepcion de división por cero (ZeroDivisionError)

def dividir_numeros(a,b):

    try:
        resultado = a/b

        print(f"El resultado es {resultado}")
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")
dividir_numeros(5,0)    
print("Hola")

# Ejemplo de multiples excepciones

def manejar_excepciones(a,b):

    try:
        resultado = a/b

        print(f"El resultado es {resultado}")
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")
    except TypeError:
        print("Error: Los tipos de datos no son compatibles para la operación")

manejar_excepciones(10,2) # Funciona correctamente 
manejar_excepciones(10,0) # Maneja ZeroDivisionError
manejar_excepciones(10,"dos") # Maneja TypeError

# Ejemplo de excepciones con Finally 
def ejemplo_else_finally(a,b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    else:
        print(f"El resultado es {resultado}")
    finally:
        print("Esto se ejecuta siempre, sin importar que ocurra")

ejemplo_else_finally(10,2) # Se ejecuta el bloque else y finally
ejemplo_else_finally(10,0) # Se ejecuta el bloque except y finally    

# Ejemplo creando una excepcion propia con la  palabra reservada raise 

def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    elif edad < 18:
        raise ValueError("Eres menor de edad, no puedes acceder")
    else:
        print("Eres mayor de edad, puedes acceder")

try:
    edad_usuario = int(input("Ingrese su edad:"))
    verificar_edad(edad_usuario)
except ValueError as e:
    print(f"Error: {e}")            


