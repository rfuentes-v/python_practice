class Estudiante:
    #Constructor que inicializa los atributos
    def __init__(self,nombre,edad,nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    #Metodo para mostrar informacion
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}")

    def es_aprobado(self):
        if self.nota >= 60:
            print(f"Resultado: {self.nombre} ha aprobado el curso")
        else:
            print(f"Resultado: {self.nombre} ha reprobado el curso")

estudiante1 = Estudiante("Isaac",23,90) #Instancia de una clase 
estudiante2 = Estudiante("Ana",30,50)
estudiante3 = Estudiante("Carlos",22,80)

#Mostrar informacion de los estudiantes
estudiante1.mostrar_informacion()
estudiante1.es_aprobado()

estudiante2.es_aprobado()