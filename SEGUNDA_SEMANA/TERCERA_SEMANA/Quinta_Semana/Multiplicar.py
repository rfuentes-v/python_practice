# Ejercicio 1
#Crea una función en python que reciba un numero como argumento e imprima la tabla de multiplicar del numero, desde 1 hasta 10 
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Aqui ingresamos el numero que queremos multiplicar (6)(5) o el numero que quiera
tabla_multiplicar(6)