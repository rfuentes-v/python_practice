from business.GestorBiblioteca import GestorBiblioteca

class InterfazConsola:
    def __init__(self):
        self.gestor = GestorBiblioteca

    def mostrar_menu(self):
        print("\nMenu de Biblioteca")
        print("1. Agregar un libro")
        print("2. Listar todos los libros")
        print("3. Buscar un libro por titulo")
        print("4. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                titulo = input("Ingrese el titulo del libro: ")
                autor = input("Ingrese el nombre del autor")
                anio_publicacion = int(input("Ingrese el año de publicacion"))

                self.gestor.agregrar_libro(titulo, autor,anio_publicacion)
            elif opcion == "2":
                self.gestor.listar_libros()
            elif opcion == "3":
                tituloBuscado = input("Ingrese el titulo: ")
                self.gestor.buscar_libro(tituloBuscado)
            elif opcion == "4":
                print("Saliendo del progranma")
                break
            else:
                print("Opcion no valida")      

