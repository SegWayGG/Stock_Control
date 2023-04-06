import sqlite3

conn = sqlite3.connect('stock.sqlite3')

def create_table():
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, precio REAL, cantidad INTEGER)")

    conn.commit()

create_table()

def agregar_producto(nombre, precio, cantidad):
    conn.execute('''INSERT INTO stock (nombre, precio, cantidad)
                    VALUES (?, ?, ?)''', (nombre, precio, cantidad))
    conn.commit()
    print('Producto agregado al stock')

def actualizar_cantidad(id, n_cantidad):
    cursor = conn.execute('''SELECT * FROM stock WHERE id = ?''', (id,))
    result = cursor.fetchone()

    if not result:
        print("El producto no existe.")
    else:
        conn.execute('''UPDATE stock SET cantidad = ?
                        WHERE id = ?''', (n_cantidad, id))
        conn.commit()
        print('Cantidad actualizada')

def mostrar_productos():
    cursor = conn.execute('''SELECT id, nombre, precio, cantidad FROM stock''')
    rows = cursor.fetchall()

    if not rows:
        print("No hay productos registrados en el stock.")
    else:
        print("Lista de productos en el stock:")

        for row in rows:
            print(f'ID: {row[0]}, Producto: {row[1]}, Precio: {row[2]}, Cantidad: {row[3]}')

def eliminar_producto(id):
    cursor = conn.execute('''SELECT id, nombre, precio, cantidad FROM stock WHERE id = ?''', (id,))
    producto = cursor.fetchone()
    if producto:
        conn.execute('''DELETE FROM stock WHERE id = ?''', (id,))
        conn.commit()
        print(f'Producto "{producto[1]}" eliminado del stock')
    else:
        print(f'No se encontró ningún producto con el ID "{id}"')

def check_table():
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock'")
    result = c.fetchone()

    if result:
        print("La tabla 'stock' existe.")
    else:
        print("La tabla 'stock' no existe.")

check_table()

print("Bienvenidx al stock")
print(f"(1) Agregar producto \n(2) Actualizar cantidad \n(3) Ver stock \n(4) Eliminar producto")
opcion=int(input("¿Que desea hacer?: "))

if (opcion == 1):
    agregar_producto(input("Nombre del producto: "), input("Precio del producto: "), input("Cantidad de productos: "))

elif (opcion == 2):
    mostrar_productos()
    actualizar_cantidad(input("\nID del producto que quiere actualizar: "), input("Cantidad de productos: "))

elif (opcion == 3):
    mostrar_productos()

elif (opcion == 4):
    mostrar_productos()
    eliminar_producto(input("ID del producto a eliminar: "))

conn.close()





"""
import sqlite3

conn = sqlite3.connect('stock.sqlite3')

def create_table():
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, precio REAL, cantidad INTEGER)")

    conn.commit()

create_table()

def agregar_producto(nombre, precio, cantidad):
    conn.execute('''INSERT INTO stock (nombre, precio, cantidad)
                    VALUES (?, ?, ?)''', (nombre, precio, cantidad))
    conn.commit()
    print('Producto agregado al stock')

def actualizar_cantidad(id, n_cantidad):
    conn.execute('''UPDATE stock SET cantidad = ?
                    WHERE id = ?''', (n_cantidad, id))
    conn.commit()
    print('Cantidad actualizada')

def mostrar_productos():
    cursor = conn.execute('''SELECT id, nombre, precio, cantidad FROM stock''')

    if len(cursor) == 0:
        print("No hay productos registrados en el stock.")
    else:
        print("Lista de productos en el stock:")

        for row in cursor:
            print(f'ID: {row[0]}, Producto: {row[1]}, Precio: {row[2]}, Cantidad: {row[3]}')

def check_table():
    conn = sqlite3.connect('stock.sqlite3')
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock'")
    result = c.fetchone()

    if result:
        print("La tabla 'stock' existe.")
    else:
        print("La tabla 'stock' no existe.")

    conn.close()

check_table()

print("Bienvenidx al stock")
print(f"(1) Agregar producto \n(2) Actualizar cantidad \n(3) Ver stock")
opcion=int(input("¿Que desea hacer?: "))

if (opcion == 1):
    agregar_producto(input("Nombre del producto: "), input("Precio del producto: "), input("Cantidad de productos: "))

elif (opcion == 2):
    mostrar_productos()
    actualizar_cantidad(input("ID del producto: "), input("Cantidad de productos: "))

elif (opcion == 3):
    mostrar_productos()
"""

"""
class producto:
    def __init__(self, nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

c = int(input("Ingrese la cantidad de productos: "))
"""
