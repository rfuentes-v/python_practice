def calcular_precio_envio(peso):
    if peso <= 2:
        costo = 5
    if peso <= 5:
        costo = 10
    else:
        costo = 15
    return costo

peso = float(input("Ingresa el peso del paquete en kg: "))
costo_envio = calcular_precio_envio(peso)
print(f"El costo del envío para un paquete de {peso} kg es: ${costo_envio}")