import os 
class GestorArchivos:
    def __init__(self, archivo="productos.txt"):
        self.archivo = archivo
        
    def guardar_producto(self, producto):
        with open(self.archivo, "a") as file:
            file.write(f"{producto.nombre}, {producto.categoria}, {producto.precio}\n")

    def listar_productos(self):
        if not os.path.exists(self.archivo)
            return []
        with open(self.archivo, "r") as file:
            return [linea.strip() for linea in file.readlines()]

