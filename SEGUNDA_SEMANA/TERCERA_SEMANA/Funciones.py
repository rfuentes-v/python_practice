#Funcion sin parametros
def mostrar_mensaje():
    print("Este es un mensaje simple")

mostrar_mensaje()

#Funcion con parametros
def suma(a,b):
    numeros_sumados = a+b
    print(numeros_sumados)

suma(5,5)

#Funcion con valores de retorno
def multiplicar(x,y):
    resultado = x * y
    return resultado

resultado = multiplicar(1,5)
print(resultado)
