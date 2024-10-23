def calcular_descuento(precio, porcentaje_descuento):
    # Calcular el monto del descuento
    descuento = (precio * porcentaje_descuento) / 100
    # Calcular el precio final después de aplicar el descuento
    precio_final = precio - descuento
    # Mostrar el precio final
    print(f"El precio final después de aplicar el descuento es: ${precio_final:.2f}")

precio = float(input("Ingresa el precio del producto: $"))
porcentaje_descuento = float(input("Ingresa el porcentaje de descuento: "))
calcular_descuento(precio, porcentaje_descuento)