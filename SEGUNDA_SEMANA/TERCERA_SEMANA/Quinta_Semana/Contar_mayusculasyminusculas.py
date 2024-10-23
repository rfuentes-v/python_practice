#Crea un funcion en python que cuente cuantas letras mayusculas y minisculas hay en una palabra ingresada por el usuario

def contar_mayusculas_minusculas(palabra):
    mayusculas = 0
    minisculas = 0
    for letra in palabra:
        if letra.isupper():
            mayusculas += 1
        elif letra.lower():
            minisculas += 1
    print(f"En la palabra '{palabra}' hay {mayusculas} mayusculas y {minisculas} minusculas")

contar_mayusculas_minusculas("Hola Mundo")              
