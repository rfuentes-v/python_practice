def mostrar_menu():
    print("\nGestion de Tareas")
    print("1. Agregar una Tarea")
    print("2. Mostrar todas las Tareas")
    print("3.Buscar una Tarea")
    print("4. Eliminar todas las Tareas")
    print("5. Salir")

def agregar_tarea():
    tarea = input("ingrese la tarea")
    with open("Archivos/Tareas.txt","a") as archivo:
        archivo.write(tarea + "\n")
        print("Tarea agregada")

def mostrar_tareas():
    try:
        with open("Archivos/Tareas.txt","r") as archivo:
            tareas = archivo.readlines()

        if tareas:
            for tarea in tareas:
                print(tarea.strip())
        else:
            print("No hay tareas almacenadas")
    except FileNotFoundError:
        print("El archivo de Tareas no existe")

def buscar_tareas():
    nombre_tarea = input("Ingrese el nombre de la tarea a buscar")
    try:
        with open("Archivos/Tareas.txt","r") as archivo:
            tareas = archivo.readlines()
        
        encontrada = False
        for tarea in tareas:
            if nombre_tarea.lower() in tarea.lower():
                print(f"Tarea encontrada: {tarea.strip()}")
                encontrada =  True

        if not encontrada:
            print("No se encontró la tarea")    

    except FileNotFoundError:
        print("El archivo de tareas no existe")

def eliminar_tareas():
    with open("Archivos/Tareas.txt","w") as archivo:
        pass
    print("Todas las tareas han sido borradas")

while True:
    mostrar_menu():

    opcion = input("Seleccione una opcion")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        buscar_tareas()
    elif opcion == "4":
        eliminar_tareas()
    elif opcion == "5":
        print("Saliendo del progranma")
        break
    else:
        print("Opcion no valida")    
