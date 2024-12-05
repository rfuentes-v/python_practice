# Funcion para mostrar el menu

def mostrar_menu():
    print("\nGestion de Ventas")
    print("1. Registrar una venta")
    print("2. Mostrar todas las ventas")
    print("3. Calcular el total de las ventas")
    print("4. Salir")

def registrar_venta():
    producto = input("Ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el lprecio unitario: "))

    with open("Archivos/Ventas.txt","a") as archivo:
        archivo.write(f"{producto}, {cantidad}, {precio}\n")

    print("Venta registrada")

def mostrar_ventas():
    try:
        with open("Archivos/Ventas.txt","r") as Archivo:
            ventas = Archivo.readlines()

        if ventas:
            for venta in ventas:
                producto, cantidad, precio = venta.strip().split(",")

                print(F"Producto: {producto}, Cantidad: {cantidad}, Precio: {precio}")
        else:
            print("No hay ventas registradas")
    except FileNotFoundError:
        print("El archivo no existe")

def calcular_total_ventas():
        try:
            with open("Archivos/Ventas.txt","r") as Archivo:
                ventas = Archivo.readlines()

            total = 0

            for venta in ventas:
                producto, cantidad, precio = venta.strip().split(",")
                total += int(cantidad) * float(precio)
            print(f"Total de las ventas: ${total:}")
        except FileNotFoundError:
            print("El archivo no existe") 

while True:
    mostrar_menu()

    opcion = input("Seleccione una opcion")

    if opcion == "1":
        registrar_venta()
    elif opcion == "2":
        mostrar_ventas()
    elif opcion == "3":
        calcular_total_ventas()
    elif opcion == "4":
        print("Saliendo del progranma")
        break
    else:
        print("Opcion no valida")               



