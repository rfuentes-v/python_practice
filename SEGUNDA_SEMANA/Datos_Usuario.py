#Solicitar nombre al usuario

nombre = input("Digite su nombre")
print("El nombre ingresado es " +nombre) # aqui se concatena el texto con la variable nombre

#Ejemple sumar dos números ingresados por el usuario
numero1 = input("Ingrese el primer numero")
numero2 = input("Ingrese el segundo numero")

#Convertimos las entradas a numeros
numero1 = int(numero1)
numero2 = int(numero2)

#Calculamos la suma
suma = numero1 + numero2
print("La suma de los numeros es: "+str(suma))