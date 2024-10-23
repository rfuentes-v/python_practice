def verificar_numero(numero):
    if numero > 0:
        print("El número es positivo.")
    else:
        print("El número es negativo.")

# Solicitar al usuario que ingrese un número
numero = float(input("Por favor, ingresa un número: "))
verificar_numero(numero)