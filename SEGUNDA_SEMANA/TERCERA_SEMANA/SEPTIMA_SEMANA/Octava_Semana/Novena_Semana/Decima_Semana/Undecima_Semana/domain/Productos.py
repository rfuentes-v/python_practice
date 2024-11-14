class Producto:
    def __init__(self, nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio 
        self.cantidad = cantidad
        
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}"
    
    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
    

