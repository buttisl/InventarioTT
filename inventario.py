import sqlite3

def crear_base_de_datos():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()

crear_base_de_datos()


def registrar_producto(nombre, categoria, cantidad, precio):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO productos (nombre, categoria, cantidad, precio)
    VALUES (?, ?, ?, ?)
''', (nombre, categoria, cantidad, precio))

    conn.commit()
    conn.close()

def consultar_producto(id_producto):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM productos WHERE id = ?
    ''', (id_producto,))

    producto = cursor.fetchone()
    conn.close()

    if producto:
        return producto
    else:
        return None

def actualizar_producto(id_producto, nombre=None, categoria=None, cantidad=None, precio=None):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    if nombre:
        cursor.execute('''
            UPDATE productos SET nombre = ? WHERE id = ?
                ''', (nombre, id_producto))
    if categoria:
        cursor.execute('''
            UPDATE productos SET categoria = ? WHERE id = ?
                ''', (categoria, id_producto))
    if cantidad is not None:
        cursor.execute('''
            UPDATE productos SET cantidad = ? WHERE id = ?
                ''', (cantidad, id_producto))
    if precio is not None:
        cursor.execute('''
            UPDATE productos SET precio = ? WHERE id = ?
                ''', (precio, id_producto))

    conn.commit()
    conn.close()

def eliminar_producto(id_producto):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM productos WHERE id = ?
            ''', (id_producto,))

    conn.commit()
    conn.close()

def listar_productos():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM productos
            ''')

    productos = cursor.fetchall()
    conn.close()

    return productos

def reporte_bajo_stock(cantidad_minima):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM productos WHERE cantidad < ?
            ''', (cantidad_minima,))

    productos_bajo_stock = cursor.fetchall()
    conn.close()

    return productos_bajo_stock


def menu():
    print("Gestión de Inventario")
    print("1. Registrar Producto")
    print("2. Consultar Producto")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Listar Productos")
    print("6. Reporte de Bajo Stock")
    print("7. Salir")

def ejecutar_accion():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría del producto: ")
            cantidad = int(input("Cantidad en stock: "))
            precio = float(input("Precio del producto: "))
            registrar_producto(nombre, categoria, cantidad, precio)
            print("Producto registrado exitosamente.")

        elif opcion == '2':
            id_producto = int(input("ID del producto a consultar: "))
            producto = consultar_producto(id_producto)
            if producto:
                print(f"Producto: {producto}")
            else:
                print("Producto no encontrado.")

        elif opcion == '3':
            id_producto = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre (dejar vacío si no cambia): ")
            categoria = input("Nueva categoría (dejar vacío si no cambia): ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            actualizar_producto(id_producto, nombre, categoria, cantidad, precio)
            print("Producto actualizado exitosamente.")

        elif opcion == '4':
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)
            print("Producto eliminado exitosamente.")

        elif opcion == '5':
            productos = listar_productos()
            if productos:
                for producto in productos:
                    print(producto)
            else:
                print("No hay productos en el inventario.")

        elif opcion == '6':
            cantidad_minima = int(input("Cantidad mínima para bajo stock: "))
            productos_bajo_stock = reporte_bajo_stock(cantidad_minima)
            if productos_bajo_stock:
                for producto in productos_bajo_stock:
                    print(producto)
            else:
                print("No hay productos con bajo stock.")

        elif opcion == '7':
            print("Saliendo...")
            break

if __name__ == '__main__':
    ejecutar_accion()
1