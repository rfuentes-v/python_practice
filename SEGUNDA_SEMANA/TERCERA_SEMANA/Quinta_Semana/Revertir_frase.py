#  Crea un funcion en python que reciba la frase "Hola Mundo" e imprima esa frase en orden inverso

def revertir_frase(frase):
    frase_inversa = frase[::-1]
    print(frase_inversa)

# Llamamos a la función con la frase "Hola Mundo" para revertirla 
revertir_frase("Hola Mundo")

# Otra forma de resolverlo 

def invertir_frase(frase):
    frase_invertida = ""
    palabra_actual = ""
    for caracter in frase:
        if caracter != " ":
            palabra_actual = caracter + palabra_actual
        else: 
            frase_invertida += palabra_actual + " "
            palabra_actual = ""
    frase_invertida += palabra_actual
    print(f"Frase invertida: {frase_invertida}")

invertir_frase("Hola mundo")    
