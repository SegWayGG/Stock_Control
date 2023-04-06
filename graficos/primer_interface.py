import tkinter as tk
from tkinter import *
# Creamos la ventana
root = Tk()
root.title("Stock")
root.geometry("450x250")


# Creamos un frame para los widgets
mi_frame = Frame()
mi_frame.pack()

"""
mi_frame.config(bg="red")
mi_frame.config(width="100", height="100")
"""

"""
# Creamos las etiquetas y los cuadros de texto para agregar un producto
nombre_label = tk.Label(mi_frame, text="Nombre del producto")
nombre_label.grid(row=0, column=0, sticky="w")
nombre_entry = tk.Entry(mi_frame)
nombre_entry.grid(row=0, column=1)

precio_label = tk.Label(mi_frame, text="Precio del producto")
precio_label.grid(row=1, column=0, sticky="w")
precio_entry = tk.Entry(mi_frame)
precio_entry.grid(row=1, column=1)

cantidad_label = tk.Label(mi_frame, text="Cantidad del producto")
cantidad_label.grid(row=2, column=0, sticky="w")
cantidad_entry = tk.Entry(mi_frame)
cantidad_entry.grid(row=2, column=1)

# Creamos el botón para agregar un producto
def agregar_producto_click():
    agregar_producto(nombre_entry.get(), float(precio_entry.get()), int(cantidad_entry.get()))
    nombre_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)
    cantidad_entry.delete(0, tk.END)

agregar_producto_button = tk.Button(mi_frame, text="Agregar producto", command=agregar_producto_click)
agregar_producto_button.grid(row=3, column=0)

# Creamos las etiquetas y los cuadros de texto para actualizar la cantidad de un producto
id_label = tk.Label(mi_frame, text="ID del producto a actualizar")
id_label.grid(row=4, column=0, sticky="w")
id_entry = tk.Entry(mi_frame)
id_entry.grid(row=4, column=1)
cantidad_label = tk.Label(mi_frame, text="Nueva cantidad del producto")
cantidad_label.grid(row=5, column=0, sticky="w")
cantidad_entry = tk.Entry(mi_frame)
cantidad_entry.grid(row=5, column=1)

# Creamos el botón para actualizar la cantidad de un producto
def actualizar_cantidad_click():
    actualizar_cantidad(int(id_entry.get()), int(cantidad_entry.get()))
    id_entry.delete(0, tk.END)
    cantidad_entry.delete(0, tk.END)

actualizar_cantidad_button = tk.Button(mi_frame, text="Actualizar cantidad", command=actualizar_cantidad_click)
actualizar_cantidad_button.grid(row=6, column=0)

# Creamos las etiquetas y los cuadros de texto para eliminar un producto
id_eliminar_label = tk.Label(mi_frame, text="ID del producto a eliminar")
id_eliminar_label.grid(row=7, column=0, sticky="w")
id_eliminar_entry = tk.Entry(mi_frame)
id_eliminar_entry.grid(row=7, column=1)

# Creamos el botón para eliminar un producto
def eliminar_producto_click():
    eliminar_producto(int(id_eliminar_entry.get()))
    id_eliminar_entry.delete(0, tk.END)

eliminar_producto_button = tk.Button(mi_frame, text="Eliminar producto", command=eliminar_producto_click)
eliminar_producto_button.grid(row=8, column=0)

# Creamos el botón para mostrar todos los productos
mostrar_productos_button = tk.Button(mi_frame, text="Mostrar productos", command=mostrar_productos)
mostrar_productos_button.grid(row=9, column=0)
"""

root.mainloop()