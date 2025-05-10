# ¡Pongámonos a prueba!
# Teniendo en cuenta los principios y técnicas de la programación
# estructurada resolver:
# 1. Escribe un programa que tenga un menú para gestionar un
# inventario de productos:
# a. Agregar Producto
# b. Mostrar Inventario
# c. Buscar Producto
# d. Eliminar Producto
# e. Salir
# 2. Escribe un programa que tenga un menú para gestionar una
# lista de contactos.
# a. Agregar Contacto
# b. Eliminar Contacto
# c. Mostrar Contacto
# d. Salir
# 3. Escribe un programa que tenga un menú para gestionar los
# usuarios y password de tus aplicaciones.
# 4. Escribe un programa que tenga un menú para gestionar las
# tareas que permita agregar, marcar como completadas y
# mostrar tareas pendientes.
# 5. Escribe un programa tipo cajero automático que permita:
# a. Iniciar sesión a través de usuario y contraseña
# b. Realizar extracciones.
# c. Realizar depósitos.
# d. Salir

def menu():
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Buscar Producto")
    print("4. Eliminar Producto")
    print("5. Salir")
    return int(input("Seleccione una opción: "))

def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    print(f"Producto {nombre} agregado al inventario.")
    