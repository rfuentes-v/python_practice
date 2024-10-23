#Condicionales if
#Ejemplo #1

edad = 3

if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")    

#Ejemplo #2
numero = int(input("Ingrese un numero"))

if numero > 10:
    print("El numero es mayor a 10")

#Numeros pares o impares
numero = int(input("Ingrese un numero"))

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")


def pares_impares(numero):
    modulo = numero & 2
    if modulo == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
numero = int(input("Ingrese un numero"))
pares_impares(numero)        

def verificar_numero(numero):
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")