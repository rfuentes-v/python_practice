class Perro:
    def __init__(self,nombre,raza,edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Informacion del perro")
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")

    def ladrar(self):
        print(f"{self.nombre} esta ladrando")

nombre = input("Ingrese el nomber del perro")
raza = input("Ingrese la raza del perro")
edad = input("Ingrese la edad del perro")

mi_perro = Perro(nombre,raza,edad)
mi_perro.mostrar_informacion()
mi_perro.ladrar
   