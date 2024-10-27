class Libro:
    def __init__(self,titulo,autor,precio,cantidad):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        print(f"Información del libro")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad disponible: {self.cantidad}")

    def vender_libro(self,cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida # Esto es para disminuir la cantidad del libro
            print(f"Se han vendido {cantidad_vendida} copias de {self.titulo}")
            print(f"Quedan {self.cantidad} copias en inventario")
        else:
            print(f"No hay suficientes copias de {self.titulo} en inventario para vender {cantidad_vendida}")

Libros = []
for i in range(3):
    print(f"Ingrese los datos del libro {i+1}")
    titulo = input("titulo")
    autor = input("Autor") 
    precio = float(input("Precio"))
    cantidad = int(input("Cantidad"))

    mi_libro = Libro(titulo,autor,precio,cantidad)
    Libros.append(mi_libro)

while True:
    titulo_buscar = input("Ingresa el titulo del libro que deseas vender(o 'salir' para terminar):")
    if titulo_buscar.lower() == "salir":
        break
    # Buscar el libro por titulo
    for libro in Libros:
        if libro.titulo.lower() == titulo_buscar.lower():
            libro_encontrado = libro
            break
    if libro_encontrado: 
        cantidad_vender = int(input(f"Cuantos ejemplares deseas vender de {libro_encontrado.titulo}"))

        libro_encontrado.vender_libro(cantidad_vender)
    else:
        print(f"No se encontro un libro con el titulo {titulo_buscar}")           


