class Auto:
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El auto {self.marca}{self.modelo} de color {self.color} ha arrancado")

    def no_arranco(self):
        print(f"El auto {self.marca}{self.modelo} de color {self.color} no ha arrancado")

def ejecutar_auto():
    marca = input("Ingresa la marca del auto")
    modelo = input("Ingresa el modelo del auto")
    color = input("Ingresa el color del auto")

    # Creacion de un objetoauto
    auto = Auto(marca,modelo,color)

    # Preguntamos al usuario si desea arrancar el auto
    respuesta = input("Quieres arrancar el auto?").lower()
    if respuesta == "si":
        auto.arrancar()
    elif respuesta == "no":
        auto.no_arranco()
    else:
        print("Respuesta no válida")

auto1 = Auto("Toyota","Corolla","Negro")
print(auto1.marca)                          
            

