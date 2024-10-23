def contar_letras(palabra,letra_a_contar):
    contador = 0

    for caracter in palabra:
        if caracter.lower() == letra_a_contar.lower():  #Ignorar mayusculas y minusculas
            contador += 1
            
    return contador

# Aqui pedimos los datos al usuario
palabra = input("Ingresa una palabra: ")
letra_a_contar = input("Ingresa la letra a contar: ")

cantidad = contar_letras(palabra, letra_a_contar)
print(f"La letra '{letra_a_contar}' aparece {cantidad} veces en la palabra '{palabra}'.") 

# Otra forma de hacerlo
def contar_letras(palabra,letra_a_contar):
    contador = 0

    for letra in palabra:
        if letra == letra_a_contar:
            contador += 1
    print(f"La letra '{letra_a_contar}' aparece {contador} veces en la palabra {palabra}")

contar_letras("Holaaa", "a")    