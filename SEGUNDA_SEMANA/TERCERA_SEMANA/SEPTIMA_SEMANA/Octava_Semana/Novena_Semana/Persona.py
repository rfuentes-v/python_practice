class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def mostrar_informacion(self):
        print(f"Nombre : {self.nombre}, Edad: {self.edad}, Nacionalidad {self.nacionalidad}")

    def es_mayor_de_edad(self):
        return self.edad >= 18
    
    def actualizar_nacionalidad(self, nueva_nacionalidad):
        self.nacionalidad = nueva_nacionalidad

nombre = input("Ingrese el nombre de la persona")
edad = int(input("Ingrese la edad de la persona"))
nacionalidad = input("Ingrese la nacionalidad de la persona")

# Para crear un objeto debo llamar al nombre de la clase y los parentesis
persona = Persona(nombre,edad,nacionalidad)
persona.mostrar_informacion()

if persona.es_mayor_de_edad():
    print(f"{persona.nombre} es mayor de edad")
else:
    print(f"{persona.nombre} es menor de edad")

nueva_nacionalidad = input("Ingrese la nueva nacionalidad: ")

if nueva_nacionalidad:
    persona.actualizar_nacionalidad(nueva_nacionalidad)
    persona.mostrar_informacion()
else:
    print("No ingreso nada")    