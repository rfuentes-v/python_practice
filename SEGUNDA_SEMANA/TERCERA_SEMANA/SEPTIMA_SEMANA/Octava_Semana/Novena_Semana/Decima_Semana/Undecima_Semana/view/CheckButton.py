import tkinter as tk

ventana = tk.Tk()
ventana.title("Intereses")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="Selecciona tus intereses:", font=("Arial,12"), bg="lightgray")
etiqueta.pack(pady=10)

interes1 = tk.BooleanVar()
interes2 = tk.BooleanVar()
interes3 = tk.BooleanVar()

check1 = tk.Checkbutton(ventana, text="Leer", variable=interes1, font=("Arial,12"), bg="white")
check1.pack(anchor="w")

check2 = tk.Checkbutton(ventana, text="Viajar", variable=interes2, font=("Arial,12"), bg="white")
check2.pack(anchor="w")

check3 = tk.Checkbutton(ventana, text="Cocinar", variable=interes3, font=("Arial,12"), bg="white")
check3.pack(anchor="w")

def mostrar_intereses():
    seleccion = "Tus intereses son:\n"
    if interes1.get():
        seleccion += "- Leer\n "
    if interes2.get():
        seleccion += "- Viajar\n"
    if interes3.get():
        seleccion += "- Cocinar\n"
    if not any([interes1.get(), interes2.get(), interes3.get()]):
        seleccion = "No seleccionaste ningun interes"

    etiqueta_resultado.config(text=seleccion)    

boton = tk.Button(ventana, text="Mostrar intereses", font=("Arial,12"), command=mostrar_intereses)
boton.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial,12"), bg="white", justify="left")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()


