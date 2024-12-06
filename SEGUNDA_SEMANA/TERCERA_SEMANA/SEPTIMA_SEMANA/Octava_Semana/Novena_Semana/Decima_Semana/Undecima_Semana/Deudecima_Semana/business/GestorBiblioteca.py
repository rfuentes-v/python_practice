from domain.Libro import Libro
from data.GestorArchivos import GestorArchivos

class GestorBiblioteca:
    def __init__(self):
        self.libros = []
        self.gestor_archivos = GestorArchivos()

    def agregrar_libro(self, titulo, autor, anio_publicacion):
        self.gestor_archivos(titulo, autor, anio_publicacion)

    def listar_libros(self):
        lineas = self.gestor_archivos.listar_libros()
        if not lineas:
            print("No hay libros en la biblioteca")
            return
        print("\nLista de libros en la biblioteca") 
        for linea in lineas:
            print(linea)
            titulo, autor, anio = linea.strip().split(",")
            print(f"{titulo}, de {autor} ({anio})")

    def buscar_libro(self, titulo=""):
        for libro in self.libros:
            if titulo.lower() == libro.titulo.lower():
                print("El libro fue encontrado")
                return
            else:
                print("El libro no fue encontrado")
                

                



        