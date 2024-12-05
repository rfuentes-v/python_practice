# Crear o sobreescribir un archivo

with open("Archivos/Ejemplo.txt","w") as archivo:
    archivo.write("Hola Mundo\n")  #\n es un salto de línea
    archivo.write("Programando")

#Leer un archivo existente 
with open("Archivos/Ejemplo.txt","r") as archivo:
    contenido = archivo.read()
    print(contenido)

#    Agregar líneas
with open("Archivos/Ejemplo.txt","a") as archivo:
    archivo.write("\nNueva linea agregada")   

with open("Archivos/Ejemplo.txt","r") as archivo:
    for linea in archivo:
        print(linea.strip()) # elimino los saltos de líneas adicionales

with open("Archivos/Ejemplo.txt","r+") as archivo: # escribir y leer en un archivo
    contenido = archivo.read()
    archivo.write("\nOtra línea agregada")
    print(contenido)

