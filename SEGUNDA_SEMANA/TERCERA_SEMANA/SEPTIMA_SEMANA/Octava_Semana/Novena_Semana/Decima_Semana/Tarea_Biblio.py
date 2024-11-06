class Material:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    # Método para mostrar información general del material
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.año_publicacion}")

# Subclase de Material para Libros
class Libro(Material):
    def __init__(self, titulo, autor, año_publicacion, num_paginas):
        super().__init__(titulo, autor, año_publicacion)
        self.num_paginas = num_paginas

    # Sobrescribe el método mostrar_informacion para incluir el número de páginas
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de Páginas: {self.num_paginas}")

# Subclase de Material para Revistas
class Revista(Material):
    def __init__(self, titulo, autor, año_publicacion, numero):
        super().__init__(titulo, autor, año_publicacion)
        self.numero = numero

    # Sobrescribe el método mostrar_informacion para incluir el número de edición
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de Edición: {self.numero}")

# Subclase de Material para Audiolibros
class Audiolibro(Material):
    def __init__(self, titulo, autor, año_publicacion, duracion):
        super().__init__(titulo, autor, año_publicacion)
        self.duracion = duracion

    # Sobrescribe el método mostrar_informacion para incluir la duración
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Duración: {self.duracion} horas")

# Función para mostrar la información de cada material
def mostrar_materiales(materiales):
    for material in materiales:
        print("Información del material:")
        material.mostrar_informacion()
        print("-" * 30)  # Línea divisoria para separar cada material

# Creación de objetos de cada tipo de material
libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 417)
revista = Revista("National Geographic", "National Geographic Society", 2021, 5)
audiolibro = Audiolibro("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2011, 15.5)

# Lista de materiales
materiales = [libro, revista, audiolibro]

# Llamada a la función que mostrará la información de cada material
mostrar_materiales(materiales)

