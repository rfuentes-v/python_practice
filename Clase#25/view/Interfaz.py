import tkinter as tk
from tkinter import messagebox
from business.GestorProductos import GestorProductos

class Interfaz:
    def __init__(self):
        self.gestor = GestorProductos()
        self.ventana = tk.Tk()
        self.ventana.title("Registro de Productos")
        self.ventana.geometry("500x500")
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.ventana, text="Nombre del producto").grid(row=0,column=0,padx=10,pady=5)
        self.entrada_nombre = tk.Entry(self.ventana)
        self.entrada_nombre.grid(row=0,column=1,padx=10,pady=5)

        tk.Label(self.ventana, text="Categoria").grid(row=1,column=0,padx=10,pady=5)
        self.entrada_categoria = tk.Entry(self.ventana)
        self.entrada_categoria.grid(row=1,column=1,padx=10,pady=5)

        tk.Label(self.ventana, text="Precio").grid(row=2,column=0,padx=10,pady=5)
        self.entrada_precio = tk.Entry(self.ventana)
        self.entrada_precio.grid(row=2,column=1,padx=10,pady=5)

        tk.Button(self.ventana, text="Agregar producto",command=self.agregar_productos).grid(row=3,column=0,columnspan=2,pady=5)
        tk.Button(self.ventana, text="Listar productos",command=self.listar_productos).grid(row=4,column=0,columnspan=2,pady=5)

        self.texto_productos = tk.Text(self.ventana,height=15,width=50)

        self.texto_productos.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

    def agregar_productos(self):
        try:
            nombre = self.entrada_nombre.get()
            categoria = self.entrada_categoria.get()
            precio = float(self.entrada_precio.get())

            self.gestor.agregar_producto(nombre,categoria,precio)

            messagebox.showinfo("Exito", "Producto agregado")

            self.entrada_nombre.delete(0,tk.END)
            self.entrada_categoria.delete(0,tk.END)
            self.entrada_precio.delete(0,tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def listar_productos(self):
        productos = self.gestor.obtener_productos()

        self.texto_productos.delete("1.0",tk.END)
        if productos:
            for producto in productos:
                self.texto_productos.insert(tk.END,f"{producto}\n")
        else:
            self.texto_productos.insert(tk.END,"No hay productos registrados")

    def iniciar(self):
        self.ventana.mainloop()                            




