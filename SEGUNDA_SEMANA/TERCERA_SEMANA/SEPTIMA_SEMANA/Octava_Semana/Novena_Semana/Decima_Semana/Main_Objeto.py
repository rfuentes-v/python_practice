from domain.Empleado import empleado

#Creamos instancias (Objetos) de la clase

empleado1 = empleado("Isaac","Programador",300000)
empleado2 = empleado("Bob","Desarrollador",350000)

print(empleado1)
print(empleado2)

empleado1.aumentar_salario(50)
empleado2.aumentar_salario(10)