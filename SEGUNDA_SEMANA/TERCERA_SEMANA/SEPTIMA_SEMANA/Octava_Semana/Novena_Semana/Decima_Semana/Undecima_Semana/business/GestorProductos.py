from domain.Productos import Producto

class GestorProductos:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self,nombre,precio,cantidad):
        producto = Producto(nombre,precio,cantidad)
        self.productos.append(producto)

    def listar_productos(self):
        for producto in self.productos:
            print(producto)

    def calcular_valor_inventario(self):
        total = 0
        for producto in self.productos:
            total += producto.calcular_valor_total()
        print(f"Valor total del inventario: ${total}")
        

        

