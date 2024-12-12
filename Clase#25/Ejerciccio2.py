import tkinter as tk
from tkinter import messagebox

def IMC_calculado():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        imc = peso / (altura ** 2)

        if imc <18.5:
            categoria = "Bajo peso"
        elif 18.5 <= imc < 25:
            categoria  = "Peso normal"
        elif 25 <= imc < 30:
            categoria = "Obesidad"       

        etiqueta_resultado.config(text=f"El IMC es {imc:.2f} - Su categoria es: {categoria}", fg="black")
    except ValueError:

        messagebox.showerror("Error", "Por favor, ingresa un numero valido.")

ventana = tk.Tk()

ventana.title("Calculadora de IMC")

ventana.geometry("400x200")

tk.Label(ventana, text="Su peso en kg").grid(row=0,column=0, padx=10, pady=5)

entry_peso = tk.Entry(ventana)

entry_peso.grid(row=0, column=1, pady=5, padx=10)

tk.Label(ventana, text="Su altura").grid(row=0,column=1, padx=10, pady=5)

entry_altura = tk.Entry(ventana)

entry_altura.grid(row=0, column=1, pady=5, padx=10)

tk.Button(ventana, text="Calculo de IMC", command=IMC_calculado).grid(row=1,column=0,padx=10,pady=5)

etiqueta_resultado = tk.Label(ventana)

etiqueta_resultado.grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()