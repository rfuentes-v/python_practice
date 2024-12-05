class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def __str__(self):
         return f"{self.titulo}, de {self.autor} ({self.anio_publicacion})"
    
       