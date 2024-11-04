class Vehiculo:
    def __init__(self,marca,modelo,precio_base):
        self.marca = marca
        self.modelo = modelo
        self.precio_base = precio_base

    def calcular_precio(self):
        return self.precio_base

    def __str__(self):
        return f"{self.marca},{self.modelo}"
    
class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio_base,puertas):
        super().__init__(marca, modelo, precio_base)
        self.puertas = puertas

    def calcular_precio(self):
        if self.puertas > 4:
            return self.precio_base * 1.10
        return self.precio_base

    def __str__(self):
        return f"{super().__str__()} Auto con {self.puertas} puertas"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, precio_base, cilindraje):
        super().__init__(marca, modelo, precio_base)
        self.cilindraje = cilindraje

    def calcular_precio(self):
        if self.cilindraje > 500:
            return self.precio_base * 1.08
        
        return self.precio_base             

    def __str__(self):
        return f"{super().__str__()} Motocicleta con {self.cilindraje}"

def mostrar_precio_final(vehiculos):
    for vehiculo in vehiculos:
        print(f"{vehiculo} - Precio final: ${vehiculo.calcular_precio():.2f}")

vehiculos = [
    Auto("Toyota","Corolla",20000,4),
    Auto("Honda","Pilot",30000,6),
    Motocicleta("Yamaha","YZF",15000,600),
    Motocicleta("Kawasaki","Ninja",12000,300)
]
mostrar_precio_final(vehiculos)                    