import os

def limpiar_consola():
    """Función para limpiar la consola según el sistema operativo."""
    if os.name == 'posix':  # Para sistemas Unix (Linux y macOS)
        _ = os.system('clear')
    else:  # Para sistemas Windows
        _ = os.system('cls')

def menu():
    """Función que muestra el menú y retorna la opción seleccionada por el usuario."""
    print("1. Registrar producto")
    print("2. Mostrar listado de productos")
    print("3. Mostrar productos por rango de stock")
    print("4. Aumentar stock de productos")
    print("5. Eliminar productos con stock cero")
    print("6. Salir")
    opcion = input("Ingrese la opción deseada: ")
    return opcion

def validar_codigo(codigo, productos):
    """Función para validar que el código del producto no esté repetido."""
    if codigo in productos:
        return False
    else:
        return True

def validar_datos(codigo, descripcion, precio, stock):
    """Función para validar que todos los datos sean ingresados y que precio y stock no sean negativos."""
    if codigo == '' or descripcion == '' or precio == '' or stock == '':
        return False
    try:
        precio = float(precio)
        stock = int(stock)
        if precio < 0 or stock < 0:
            return False
        else:
            return True
    except ValueError:
        return False

def registrar_producto(productos):
    """Función para registrar un nuevo producto."""
    print("\nRegistrar producto\n")
    codigo = input("Ingrese el código del producto: ")
    if not validar_codigo(codigo, productos):
        print(f"El código {codigo} ya está registrado.")
        return
    
    descripcion = input("Ingrese la descripción del producto: ")
    precio = input("Ingrese el precio del producto: ")
    stock = input("Ingrese el stock del producto: ")
    
    if not validar_datos(codigo, descripcion, precio, stock):
        print("Datos ingresados incorrectos. Asegúrese de que el precio y el stock sean números no negativos.")
        return
    
    precio = float(precio)
    stock = int(stock)
    
    productos[codigo] = {
        'descripcion': descripcion,
        'precio': precio,
        'stock': stock
    }
    print(f"\nProducto con código {codigo} registrado correctamente.\n")

def mostrar_productos(productos):
    """Función para mostrar el listado de todos los productos."""
    print("\nListado de productos\n")
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for codigo, producto in productos.items():
            print(f"Código: {codigo}, Descripción: {producto['descripcion']}, Precio: ${producto['precio']}, Stock: {producto['stock']}")
    print()

def mostrar_productos_por_rango(productos):
    """Función para mostrar productos cuyo stock se encuentra en el intervalo [desde, hasta]."""
    print("\nMostrar productos por rango de stock\n")
    desde = int(input("Ingrese el límite inferior del rango de stock: "))
    hasta = int(input("Ingrese el límite superior del rango de stock: "))
    print("\nProductos en el rango de stock solicitado:")
    for codigo, producto in productos.items():
        if desde <= producto['stock'] <= hasta:
            print(f"Código: {codigo}, Descripción: {producto['descripcion']}, Precio: ${producto['precio']}, Stock: {producto['stock']}")
    print()

def aumentar_stock(productos):
    """Función para aumentar el stock de productos cuyo stock actual es menor a un valor Y."""
    print("\nAumentar stock de productos\n")
    valor_Y = int(input("Ingrese el valor Y para comparar el stock actual de los productos: "))
    valor_X = int(input("Ingrese el valor X para aumentar el stock de los productos: "))
    cantidad_modificados = 0
    for codigo, producto in productos.items():
        if producto['stock'] < valor_Y:
            producto['stock'] += valor_X
            cantidad_modificados += 1
    print(f"\nSe ha aumentado el stock de {cantidad_modificados} productos correctamente.\n")

def eliminar_productos_stock_cero(productos):
    """Función para eliminar todos los productos cuyo stock es igual a cero."""
    print("\nEliminar productos con stock cero\n")
    productos_a_eliminar = [codigo for codigo, producto in productos.items() if producto['stock'] == 0]
    if len(productos_a_eliminar) == 0:
        print("No hay productos con stock cero para eliminar.")
    else:
        for codigo in productos_a_eliminar:
            del productos[codigo]
        print("Se han eliminado los productos con stock cero correctamente.")
    print()

def main():
    """Función principal que controla la ejecución del programa."""
    productos = {}
    opcion = None
    
    while opcion != '6':
        limpiar_consola()
        opcion = menu()

        if opcion == '1':
            registrar_producto(productos)
        elif opcion == '2':
            mostrar_productos(productos)
        elif opcion == '3':
            mostrar_productos_por_rango(productos)
        elif opcion == '4':
            aumentar_stock(productos)
        elif opcion == '5':
            eliminar_productos_stock_cero(productos)
        elif opcion == '6':
            print("\n¡Hasta luego!\n")
        else:
            print("\nOpción inválida. Intente nuevamente.\n")
        
        input("Presione Enter para continuar...")
    
main()
