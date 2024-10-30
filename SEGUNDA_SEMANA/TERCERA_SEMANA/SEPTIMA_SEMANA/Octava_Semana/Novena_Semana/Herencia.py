class Vehiculo:
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def describir(self):
        return f"Vehículo de marca {self.marca}, modelo {self.modelo}, color {self.color}"    
        
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color, num_puertas):
        super().__init__(marca, modelo, color)
        self.puertas = num_puertas

    def describir(self):
        descripcion = super().describir()
        return f"{descripcion} Tiene {self.puertas} puertas"  

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, color, cilindraje):
        super().__init__(marca, modelo, color)
        self.cilindraje = cilindraje

    def describir(self):
        descripcion = super().describir()
        return f"{descripcion} Tiene {self.cilindraje} cc"    


auto = Automovil("Toyota","Corolla","Negro",4)
print(auto.describir())

moto = Motocicleta("Yamaha", "YZF", "Negro", 600)
print(moto.describir())