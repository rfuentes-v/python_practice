# Metodo Upper()
texto = "Hola Mundo"
mayusculas = texto.upper()
print(mayusculas)

# Metodo Lower()
minisculas = texto.lower()
print(minisculas)

# Metodo capitalize()
texto = "Hola MUNDO"
capitalizado = texto.capitalize()
print(capitalizado)

# Metodo title()
texto = "bienvenidos al curso de PYTHON"
titulo = texto.title()
print(titulo) 

# https://www.pythoncheatsheet.org/cheatsheet/built-in-functions

# Metodo strip()
texto = "  Hola mundo  "
limpio = texto.strip()
print(limpio)

# Metodo lstrip()
izquierda = texto.lstrip()
print(izquierda) 

# Metodo rstrip()
derecha = texto.rstrip()
print(derecha)

# Metodo replace()
texto = "Python es flexible"
modificar = texto.replace("flexible","genial")
print(texto)
print(modificar) 

# Metodo split()
texto = "Python es genial"
partes = texto.split(" ")
print(partes)

# Metodo join()
palabras = ["Python", "es", "genial"]
frase = " ".join(palabras)
print(frase)

# Metodo find()
texto = "Buscar en esta cadena"
posicion = texto.find("cadena")
print(posicion)

# Metodo startswith()
texto = "Archivo.txt"
print(texto.startswith("A"))

# Metodo endswith()
texto = "documento.pdf"
print(texto.endswith(".pdf"))

# Metodo count()
texto = "banana"
repeticiones = texto.count("a")
print(repeticiones)