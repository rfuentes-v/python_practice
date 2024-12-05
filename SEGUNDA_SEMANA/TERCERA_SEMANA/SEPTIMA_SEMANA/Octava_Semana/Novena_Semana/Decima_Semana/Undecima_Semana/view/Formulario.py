import tkinter as tk

ventana = tk.Tk()
ventana.title("Formulario basico")
ventana.geometry("400x400")

etiqueta_nombre = tk.Label(ventana, text="Nombre:", font=("Arial,12"), bg="lightgray")
etiqueta_nombre.pack(pady=5)

entrada_nombre  = tk.Entry(ventana, font=("Arial,12"))
entrada_nombre.pack(pady=5)

etiqueta_mensaje = tk.Label(ventana, text="Mensaje:", font=("Arial,12"), bg="lightgray")
etiqueta_mensaje.pack(pady=5)

entrada_mensaje  = tk.Entry(ventana, font=("Arial,12"))
entrada_mensaje.pack(pady=5)

def enviar():
    nombre = entrada_nombre.get()
    mensaje = entrada_mensaje.get()

    if nombre and mensaje:
        cuadro_texto.insert(tk.END, f"{nombre} dice: {mensaje}\n")
    else:
         cuadro_texto.insert(tk.END, "Por favor llene ambos campos.\n")

boton_enviar = tk.Button(ventana, text="Enviar", font=("Arial,12"), command=enviar)
boton_enviar.pack(pady=10)   

cuadro_texto = tk.Text(ventana, height=10, font=("Arial,12")) #height indica la cantidad de lineas que se van a ver 
cuadro_texto.pack(pady=5)

ventana.mainloop()