# Diccionario con multiples personas y datos

personas = {

    1:{"Nombre":"Juan", "Edad":25, "Ciudad":"Madrid"},
    2:{"Nombre":"Ana", "Edad":30, "Ciudad":"Barcelona"},
    3:{"Nombre":"Luis", "Edad":22, "Ciudad":"Valencia"}

}
# Acceder a una oersona específica
persona_id_2 = personas[2]
#print(f"Nombre: {persona_id_2["Nombre"]}, Edad: {persona_id_2["Edad"]}")

# Imprimir todas las personas del diccionario

for id_persona,datos in personas.items():

   # print(f"ID: {id_persona}, Nombre: {datos['Nombre']}, Edad: {datos['Edad']}")

# Buscar elementos en un diccionario(una persona por su nombre)
    nombre_buscado= "Ana"

    if datos["Nombre"] == nombre_buscado:
        print("Persona encontrada")
        print(id_persona)
        print(datos["Edad"])

