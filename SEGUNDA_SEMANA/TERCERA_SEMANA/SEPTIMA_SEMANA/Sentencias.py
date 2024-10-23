# Ejemplo sentencia Continue / En este ejemplo se va a saltar el 5 
# El Continue siempre se usa utilizando una condición 

for numero in range(1,11):

    if numero == 5:
        continue
    print(numero)

def contar_letras(frase):
    contador = 0
    for letra in frase:
        if letra == " ":
            continue
        contador += 1
    return contador
print(contar_letras("Hola  Mundo"))    

# Ejemplo de sentencia Pass

for numero in range(1,10):
    pass

def funcion_no_implementada():
    pass

# Ejemplo de sentencia Else con for
# Buscamos un numero par dentro de una lista, si lo encontramos imprimimos un mensaje

numeros = [1,3,2,7,9]

for numero in numeros:
    if numero%2==0:
        print(f"Encontre un numero par: {numero}")
        break
else:
    print("No se encontraron numeros pares")

# Ejemplo de sentencia Else con While

contador = 5
while contador > 0:
    print(f"Cuenta regresiva: {contador}")
    contador -= 1
else:
    print("Finalizado")      

