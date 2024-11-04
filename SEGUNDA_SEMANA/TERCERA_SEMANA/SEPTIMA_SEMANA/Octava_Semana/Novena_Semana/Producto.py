# Clase base 'Producto' que representa un producto genérico en una tienda
class Producto:
    # Constructor de la clase Producto
    def __init__(self, nombre, precio, cantidad):
        # Atributo 'nombre' del producto
        self.nombre = nombre
        # Atributo 'precio' del producto
        self.precio = precio
        # Atributo 'cantidad' en inventario del producto
        self.cantidad = cantidad

    # Método para mostrar la información del producto
    def mostrar_informacion(self):
        # Retorna la información del producto en un formato de cadena
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}"
    
    # Método de prueba que imprime "Prueba"
    def test(self):
        print("Prueba")

# Clase 'Electronico' que hereda de la clase Producto
class Electronico(Producto):
    # Constructor de la clase 'Electronico'
    def __init__(self, nombre, precio, cantidad, garantia):
        # Llama al constructor de la clase base (Producto) usando super()
        super().__init__(nombre, precio, cantidad)
        # Atributo 'garantia' específico para productos electrónicos
        self.garantia = garantia
    
    # Sobrescribe el método mostrar_informacion para incluir la garantía
    def mostrar_informacion(self):
        # Llama al método mostrar_informacion de la clase base (Producto)
        informacion_basica = super().mostrar_informacion()
        # Agrega la garantía al mensaje
        return f"{informacion_basica}, Garantía: {self.garantia} años"

# Clase 'Ropa' que también hereda de la clase Producto
class Ropa(Producto):
    # Constructor de la clase 'Ropa'
    def __init__(self, nombre, precio, cantidad, talla):
        # Llama al constructor de la clase base (Producto) usando super()
        super().__init__(nombre, precio, cantidad)
        # Atributo 'talla' específico para productos de ropa
        self.talla = talla
    
    # Sobrescribe el método mostrar_informacion para incluir la talla
    def mostrar_informacion(self):
        # Llama al método mostrar_informacion de la clase base (Producto)
        informacion_basica = super().mostrar_informacion()
        # Agrega la talla al mensaje
        return f"{informacion_basica}, Talla: {self.talla}"

# Creación de una instancia de la clase Electronico
producto_electronico = Electronico("Laptop", 1000, 5, 2)

# Creación de una instancia de la clase Ropa
producto_ropa = Ropa("Camisa", 20, 15, "M")

# Imprime la información del producto electrónico llamando al método sobrescrito mostrar_informacion
print(producto_electronico.mostrar_informacion())

# Imprime la información del producto de ropa llamando al método sobrescrito mostrar_informacion
print(producto_ropa.mostrar_informacion())

# Llama al método test de la clase Producto para cada instancia
producto_ropa.test()
producto_electronico.test()