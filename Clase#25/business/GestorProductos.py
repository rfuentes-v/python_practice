from data.GestorArchivos import GestorArchivos
from domain.Producto import Producto


class GestorProductos:
    def __init__(self):
        self.gestor_archivos = GestorArchivos()

    def agregar_producto(self, nombre, categoria, precio):
        if not nombre or not categoria or precio <= 0:
            raise ValueError("Datos invalidos")
        producto = Producto(nombre, categoria, precio)

        self.gestor_archivos.guardar_producto(producto)


    def obtener_productos(self):
        lineas = self.gestor_archivos.listar_productos()
        productos = []
        for linea in lineas:
            nombre, categoria, precio = linea.split(",")
            productos.append(Producto(nombre,categoria,float(precio)))
        return productos    
