# Ejemplo de un diccionario 
# Vemos en el ejemplo 3 llaves/clave con distintos valores 

persona = {"Nombre": "Juan", "Edad":"30", "Ciudad":"San José"}
paises = {"Costa Rica":"San Jose", "Francia":"Paris", "España":"Madrid"}

# Accesso a un valor por su clave
print(persona["Nombre"])
print(persona["Edad"])

# Uso de get para evitar errores si la clave no existe 

print(persona.get("Pais", "Clave no encontrada"))

# Cambiar valores de un diccionario / son mutables

persona["Edad"] = 31
print(persona)

# Añadir elementos de un diccionario

persona["Profesión"] = "Programador"
print(persona)

# Aquí estamos eliminando valores

persona.pop("Ciudad")
print(persona)

# Funcion del para eliminar valores

del persona["Edad"]
print(persona)

# Recorrer un diccionario

for clave in persona:
    print(clave)

# Iterar sobre claves y valores  

for clave,valor in persona.items():
    print(f"{clave}:{valor}")

# Metodo update() actualiza el diccionario

persona.update({"Nombre":"Carlos", "Profesión":"Secretario"}) 
print(persona) 

# Metodo keys() devuelve todas las llaves, values() e items()
print(persona.keys())
print(persona.values())
print(persona.items())

equipo = {
    "Portero": {"Nombre":"Manuel", "Edad":30},
    "Delantero": {"Nombre":"Isaac", "Edad":23}
}
# Acceder a un valor en un diccionario anidado
print(equipo["Delantero"]["Nombre"])

# Comparación entre dicionarios
dic1 = {"a":1,"b":2}
dic2 = {"a":1,"b":2}
print(dic1 == dic2)