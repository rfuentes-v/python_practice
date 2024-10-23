#Crea una funcion en python que reciba un numero entero ingresado por el usuario y calcule la suma de todos sus digitos##

def suma_digitos(numero):
    suma = 0
    for digito in numero:
        suma += int(digito)
    print(f"La suma de los digitos es {suma}")

#En esta cso puse los numeros como una cadena de texto
suma_digitos("1234")         