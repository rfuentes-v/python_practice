# Ejercicio 2
#Crea una función en python que reciba dos números e imprima todos los números pares en ese rango, al final debe indicar cuantos números pares se indicaron

def contar_pares(inicio, fin):
    contador_pares = 0
    for i in range(inicio,fin):
        if i % 2 == 0:
            contador_pares += 1
            print(f"{i} es un numero par")
    print(f"Hay {contador_pares} numeros pares entre {inicio} y {fin}")

contar_pares(1,21)    


