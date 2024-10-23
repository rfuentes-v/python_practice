# Sintaxis de una tupla es:

mi_tupla = (1,2,3,"hola",True)

# Acceso a los elementos de una tupla

mi_tupla = (10,20,30)
print(mi_tupla[0])
print(mi_tupla[1])

# Segundo ejemplo

frutas = ("Manzana", "Fresa", "Uva")
print(frutas[0])
print(frutas[1])

# Inmutabilidad de las tuplas

#frutas[0] = "Pera"

# Metodos count() e index()
print(frutas.count("Manzana"))
print(frutas.index("Fresa"))

# Desempaquetado
tupla = (1,2,3)
a,b,c = tupla
print(a)
print(b)
print(c)
