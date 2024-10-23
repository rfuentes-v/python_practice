#Crea una función en python que cuente cuantas vocales tiene una palabra ingresada por el usuario 

def contar_vocales(palabra):
    vocales = "aeiou"
    contador = 0
    #El .lower hace que no importa si entro mayusculas o minusculas igual las va a contar
    for letra in palabra:
        if letra.lower() in vocales:
            contador += 1
            
    return contador

# Fuera de la funcion
palabra = input("Ingresa una palabra: ")
cantidad_vocales = contar_vocales(palabra)
print(f"La cantidad de vocales en la palabra '{palabra}' es: {cantidad_vocales}")

def contar_vocales(palabra):
    contador_vocales = 0
    for letra in palabra:
        if letra.lower() in "aeiou":
            contador_vocales += 1
    print(f"La palabra '{palabra}' tiene {contador_vocales} vocales")

contar_vocales("Hola")         