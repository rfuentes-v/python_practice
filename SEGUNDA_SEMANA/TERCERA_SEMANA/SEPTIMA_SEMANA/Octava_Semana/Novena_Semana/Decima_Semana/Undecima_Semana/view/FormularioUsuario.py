import tkinter as tk
from tkinter import messagebox # este modulo permite colocar ventanas
                               # para que el usuario vea mensajes 

ventana = tk.Tk()
ventana.title("Registro de usuario")
ventana.geometry("500x500")

ventana.columnconfigure(1, weight=1)


titulo = tk.Label(ventana, text="Formulario de registro:", font=("Arial",12, "bold"))
titulo.grid(row=0,colum=0, sticky="w", columnspan= 2, pady=10)

tk.Label(ventana, text="Nombre: ", font=("Arial,12")).grid(row=1, column=0, sticky="w", padx=10, pady=5)

entrada_nombre = tk.Entry(ventana, font=("Arial",12))
entrada_nombre.grid(row=1, column=1, sticky="ew", padx=10,pady=5)

tk.Label(ventana, text="Correo Electronico: ", font=("Arial,12")).grid(row=1, column=0, sticky="w", padx=10, pady=5)

entrada_correo = tk.Entry(ventana, font=("Arial",12))
entrada_correo.grid(row=2, column=1, sticky="ew", padx=10,pady=5)

tk.Label(ventana, text="Genero: ", font=("Arial",12)).grid(row=3, column=0, sticky="w", padx=10, pady=5)

genero = tk.StringVar(value="")

tk.Radiobutton(ventana, text="Masculino", variable=genero, value="Masculino", font=("Arial",12)).grid(row=3,column=1, sticky="w")
tk.Radiobutton(ventana, text="Femenino", variable=genero, value="Femenino", font=("Arial",12)).grid(row=4,column=1, sticky="w")

tk.Label(ventana, text="Intereses: ", font=("Arial",12)).grid(row=3, column=0, sticky="w", padx=10, pady=5)
intereses = {"Leer": tk.BooleanVar(), "Viajar": tk.BooleanVar(), "Deportes": tk.BooleanVar()}
fila_actual = 5
for interes, var in intereses.items():
    fila_actual += 1
    tk.Checkbutton(ventana, text=interes, variable=var, font=("Arial", 12)).grid(row=fila_actual, colum=1, sticky="w")




