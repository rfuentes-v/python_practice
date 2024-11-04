class Empleado:
    def trabajar(self):
        raise NotImplementedError ("Este método debe ser implementado por la subclase")

class Desarrollador(Empleado):
    def trabajar(self):
        return "Desarrollando código y solucionando errores"

class Diseñador(Empleado):
    def trabajar(self):
        return "Diseñando interfaces y creando gráficos"

empleado1 = Desarrollador()
empleado2 = Diseñador()

def realizar_trabajo(empleado):
    print(empleado.trabajar())

realizar_trabajo(empleado1)
realizar_trabajo(empleado2)