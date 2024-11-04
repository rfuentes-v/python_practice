class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau" 

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"

class Pajaro(Animal):
    def hacer_sonido(self):
        return "Pio pio"

def reproducir_sonido(animal):
    print(animal.hacer_sonido())

mi_perro = Perro()
mi_gato = Gato()
mi_pajaro = Pajaro()

reproducir_sonido(mi_perro)
reproducir_sonido(mi_gato)
reproducir_sonido(mi_pajaro)