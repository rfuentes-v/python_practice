import os

class GestorArchivos:
    def __init__(self, archivo="Archivo/Biblioteca.txt"):
        self.archivo = archivo
    def agregar_libro(self,titulo,autor,anio_publicacion):
        with open (self.archivo, "a")  as archivo:
            archivo.write(f"{titulo}, {autor}, {anio_publicacion}\n")
        print("El libro fue guardado")    

    def listar_libros(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, "r") as archivo:
            return archivo.readlines()
        



        