import tkinter as tk
from tkinter import messagebox

def celsius_a_fahrenheit():
    try:
        celsius = float(entry_temperatura.get())
        fahrenheit = celsius * 9/5 + 32

        etiqueta_resultado.config(text=f"{celsius} °C = {fahrenheit} °F", fg="black")
    except ValueError:

        messagebox.showerror("Error", "Por favor, ingresa un numero valido.")

def fahrenheit_a_celsius():
    try:
        fahrenheit = float(entry_temperatura.get())
        celsius = (fahrenheit - 32) * 5/9

        etiqueta_resultado.config(text=f"{fahrenheit} °F = {celsius:.2f} °C", fg="black")
    except ValueError:

        messagebox.showerror("Error", "Por favor, ingresa un numero valido.")

ventana = tk.Tk()

ventana.title("Convertidor de temperaturas")

ventana.geometry("400x200")

tk.Label(ventana, text="Temperatura").grid(row=0,column=0, padx=10, pady=5)

entry_temperatura = tk.Entry(ventana)

entry_temperatura.grid(row=0, column=1, pady=5, padx=10)


tk.Button(ventana, text="Celsius a Farenheit", command=celsius_a_fahrenheit).grid(row=1,column=0,padx=10,pady=5)
tk.Button(ventana, text="Farenheit a celsius", command=fahrenheit_a_celsius).grid(row=1,column=1,padx=10,pady=5)

etiqueta_resultado = tk.Label(ventana)

etiqueta_resultado.grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()