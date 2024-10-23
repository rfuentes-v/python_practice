# Diccionario inicial con varias personas 

personas = {
    70323902: {"Nombre":"Juan", "Edad":"25", "Ciudad":"San Jose"},
    10293202: {"Nombre":"Ana", "Edad":"30", "Ciudad":"San Jose"},
    30302032: {"Nombre":"Luis", "Edad":"22", "Ciudad":"Heredia"}
}
def agregar_persona(diccionario):
    id = int(input("Ingrese la cedula:"))
    nombre = input("Ingrese el nombre:")
    edad =int(input("Ingrese la edad:"))
    ciudad = input("Ingrese la ciudad:")

    nueva_persona = {"Nombre":nombre, "Edad":edad, "Ciudad":ciudad}

    diccionario[id] = nueva_persona
    print (f"Persona agregada exitosamente con id {id}")

agregar_persona(personas)

for id_persona, datos in personas.items():
    print(f"ID {id_persona}, Nombre {datos['Nombre']}, Edad {datos['Edad']}, Ciudad {datos['Ciudad']}")