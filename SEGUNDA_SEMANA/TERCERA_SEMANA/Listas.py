# Defino una lista 

frutas = ["Manzana","Pera", "Naranja"]

# Acceso a los elementos de una lista

print(frutas[0])
print(frutas[-1])

# Crear ua lista vacia
mi_lista = []

# Agregar un valor a mi lista
mi_lista.append(10)
mi_lista.append(20)
print(mi_lista)

# Cambiar segundo elemento
frutas[1] = "Uva"
print(frutas)

# Eliminar elementos de una lista

frutas.remove("Uva")
print(frutas)

frutas.pop(0)
print(frutas)

# Slicing
numeros = [1,2,3,4,5]
print(numeros[1:4]) 
print(numeros[:3])
print(numeros[2:])

# Recorrer una lista
frutas = ["Manzana","Pera", "Naranja"]
for fruta in frutas:
    print(fruta)