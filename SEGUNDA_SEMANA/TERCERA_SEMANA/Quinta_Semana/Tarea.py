# Crea una función llamada contar_vocales que reciba una cadena como parámetro y cuente cuántas vocales tiene ese string.


def contar_vocales(string):
    vocales = "aeiou"
    contador = 0

    for letra in string:
        if letra.lower() in vocales:
            contador += 1
            
    return contador

resultado = contar_vocales("Happy Halloween!")
print(f"Número de vocales: {resultado}")

# Crea una función que reciba una frase y reemplace todas las vocales por un asterisco *
def reemplazar_vocales(frase):

    vocales = 'aeiouAEIOU'
    for vocal in vocales:
        frase = frase.replace(vocal, '*')
    return frase

resultado = reemplazar_vocales("Happy Halloween!")
print(resultado)

#  Escribe una función que determine si el carácter ingresado es una letra mayúscula, minúscula o no es una letra.

def determinar_tipo_caracter(caracter):
    if caracter.isupper():
        return "Es una letra mayúscula."
    elif caracter.islower():
        return "Es una letra minúscula."
    elif caracter.isalpha():
        return "Es una letra, pero no es mayúscula ni minúscula."
    else:
        return "No es una letra."


caracter = input("Ingresa un carácter: ")
resultado = determinar_tipo_caracter(caracter)
print(resultado)

# Crea una función que cuente cuántas palabras tiene una frase.

def contar_palabras(frase):

    palabras = frase.split()
    return len(palabras)

frase = "Happy Halloween witches!"
resultado = contar_palabras(frase)
print(f"Número de palabras: {resultado}")

# Crea una función llamada es_contrasena_segura que valide si una contraseña es segura. Para considerarse segura debe:

# Tener al menos 8 caracteres. Contener al menos una letra mayúscula. Contener al menos una letra minúscula. Contener al menos un número.

def es_contrasena_segura(contrasena):

    if len(contrasena) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
    
    return tiene_mayuscula and tiene_minuscula and tiene_numero

contrasena = input("Ingresa una contraseña: ")
if es_contrasena_segura(contrasena):
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura.")
