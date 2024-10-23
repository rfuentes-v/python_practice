def clasificar_edad(edad):
    if edad < 12:
        categoria = "Niño"
    elif 12 <= edad <= 17:
        categoria = "Adolescente"
    elif 18 <= edad <= 64:
        categoria = "Adulto"
    else:
        categoria = "Adulto Mayor"
    
    return categoria
64
edad = int(input("Ingresa la edad: "))
categoria = clasificar_edad(edad)
print(f"La persona con {edad} años es clasificada como: {categoria}")