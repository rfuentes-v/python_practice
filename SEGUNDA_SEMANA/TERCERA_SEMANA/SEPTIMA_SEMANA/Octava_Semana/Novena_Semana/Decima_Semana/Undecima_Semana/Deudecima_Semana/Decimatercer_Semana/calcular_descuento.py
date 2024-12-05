import tkinter as tk
from tkinter import messagebox

def calcular_descuento():
    try:
        precio_original = float(entrada_precio.get())
        descuento = float(entrada_descuento.get())

        #Validar porcentaje de descuento
        if descuento < 0 or descuento > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100")
        
        #Calcular precio final

        precio_final = precio_original * (1 - descuento/100)

        etiqueta_resultado.config(text=f"Precio final ${precio_final}", fg="green")

    except ValueError as e:
        etiqueta_resultado.config(text=f"Error: {str(e)}", fg="red")

    except Exception:
        etiqueta_resultado.config(text=f"Error: Por favor ingresa valores validos", fg="red")  


ventana = tk.Tk()

ventana.title("Calculadora de descuento")

ventana.geometry("400x300")

#Etiquetas de titulo
etiqueta_titulo = tk.Label(ventana, text="Calculadora de Descuento")
etiqueta_titulo.grid(row=0, column=0,pady=10)

#Etiqueta y cuadro de texto para el precio original
etiqueta_precio = tk.Label(ventana,text ="Precio")
etiqueta_precio.grid(row=1, column=0, padx=10, pady=5)

entrada_precio = tk.Entry(ventana)
entrada_precio.grid(row=1, column=1, padx=10, pady=5)

#Etiqueta y cuadro de texto para porcentaje 
etiqueta_descuento = tk.Label(ventana,text ="Descuento")
etiqueta_descuento.grid(row=2, column=0, padx=10, pady=5)

entrada_descuento = tk.Entry(ventana)
entrada_descuento.grid(row=2, column=1, padx=10, pady=5)

#Boton para calcular
boton_calcular = tk.Button(ventana, text="Calcular")
boton_calcular.grid(row=3, column=0, columnspan=2, pady=10)

etiqueta_resultado = tk.Label(ventana)
etiqueta_resultado.grid(row=4, column=0, columnspan=2)


