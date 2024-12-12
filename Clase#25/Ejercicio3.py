import tkinter as tk
from tkinter import messagebox
import random

def comprobar_numero():
    try:
        intento = int(entry_numero.get())
        if intento < numero_magico:
            etiqueta_resultado.config(text="El numero es mayor.", fg="blue")
        elif intento > numero_magico:
            etiqueta_resultado.config(text="El numero es menor.", fg="blue")
        else:
            etiqueta_resultado.config(text="Numero correcto.", fg="green")
    except ValueError:

        messagebox.showerror("Error", "Por favor, ingresa un numero valido.")
        
def reiniciar_juego():
    global numero_magico
    numero_magico = random.randint(1,100) 

    entry_numero.delete(0,tk.END)

numero_magico = random.randint(1,100)                 

ventana = tk.Tk()
ventana.title("Encuentra el numero magico")
ventana.geometry("400x200")

tk.Label(ventana, text = "Adivina un numero entre 1 y 100").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(ventana, text="Tu intento:").grid(row=1, column=0, padx=10, pady=5)

entry_numero = tk.Entry(ventana)

entry_numero.grid(row=1, column=1, padx=10, pady=5)

tk.Button(ventana, text="Comprobar", command=comprobar_numero).grid(row=2, column=0, pady=10)
tk.Button(ventana, text="Reiniciar", command=reiniciar_juego).grid(row=2, column=1, pady=10)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()

