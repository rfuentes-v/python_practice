from domain.Libro import Libro

class GestorBiblioteca:
    def __init__(self):
        self.libros = []

    def agregrar_libro(self, titulo, autor, anio_publicacion):
        libro = Libro(titulo, autor, anio_publicacion)
        self.libros.append(libro)
        print("Libro agregado: {libro}")


    def listar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca")
        else:
            print("\nLista de libros en la biblioteca") 
            for libro in self.libros:
                print(libro)

    def buscar_libro(self, titulo=""):
        for libro in self.libros:
            if titulo.lower() == libro.titulo.lower():
                print("El libro fue encontrado")
                return
            else:
                print("El libro no fue encontrado")

                



        