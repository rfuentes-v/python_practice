class empleado:
    def __init__(self,nombre,puesto,salario): # Construye el objeto 
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
    
    def __str__(self):  # Muestra la información del objeto 
        return f"Empleado: {self.nombre}, Puesto: {self.puesto}, Salario: {self.salario}"
    
    def aumentar_salario(self,porcentaje):
        self.salario += self.salario * (porcentaje /100)
        print (f"Nuevo salario de {self.nombre}: ${self.salario}")
    
