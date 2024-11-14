from business.GestorProductos import GestorProductos

class InterfazConsola:
    def __init__(self):
        self.gestor = GestorProductos()

    def mostrar_menu(self):
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Calcular valor total del inventario")
        print("4. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = int(input("Selecccione una opcion: "))
            if opcion == 1:
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad del producto: "))
                self.gestor.agregar_producto(nombre,precio,cantidad)
                print("Producto agregado")
            
            elif opcion == 2:
                self.gestor.listar_productos()
            
            elif opcion == 3:
                self.gestor.calcular_valor_inventario()

            elif opcion == 4:
                print("Saliendo del programa")
                break
            else:
                print("Opcion no valida.Intente de nuevo")

