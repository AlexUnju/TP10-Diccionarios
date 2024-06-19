import os

def limpiar_consola():
    """Función para limpiar la consola según el sistema operativo."""
    if os.name == 'posix':  # Para sistemas Unix (Linux y macOS)
        _ = os.system('clear')
    else:  # Para sistemas Windows
        _ = os.system('cls')

def menu():
    """Función que muestra el menú y retorna la opción seleccionada por el usuario."""
    print("1. Prestar un libro")
    print("2. Devolver un libro")
    print("3. Mostrar préstamos actuales")
    print("4. Salir")
    opcion = input("Ingrese la opción deseada: ")
    return opcion

def prestar_libro(biblioteca, libro, usuario):
    """Función para prestar un libro a un usuario."""
    if libro in biblioteca:
        print(f"El libro '{libro}' ya está prestado a '{biblioteca[libro]}'")
    else:
        biblioteca[libro] = usuario
        print(f"Se ha prestado el libro '{libro}' a '{usuario}'")
    print()

def devolver_libro(biblioteca, libro):
    """Función para devolver un libro (eliminar la entrada del diccionario)."""
    if libro in biblioteca:
        usuario = biblioteca.pop(libro)
        print(f"El libro '{libro}' ha sido devuelto por '{usuario}'")
    else:
        print(f"El libro '{libro}' no está actualmente prestado.")
    print()

def mostrar_prestamos(biblioteca):
    """Función para mostrar todos los préstamos actuales."""
    if not biblioteca:
        print("No hay libros actualmente prestados.")
    else:
        print("Préstamos actuales:")
        for libro, usuario in biblioteca.items():
            print(f"Libro: '{libro}' - Usuario: '{usuario}'")
    print()

def main():
    """Función principal que controla la ejecución del programa."""
    biblioteca = {
        "Orgullo y prejuicio": "Alicia",
        "Cumbres Borrascosas": "Alicia",
        "Grandes esperanzas": "Juan"
    }
    opcion = None

    while opcion != '4':
        limpiar_consola()
        opcion = menu()

        if opcion == '1':
            libro = input("Ingrese el nombre del libro que desea prestar: ")
            usuario = input("Ingrese el nombre del usuario que lo va a sacar: ")
            prestar_libro(biblioteca, libro, usuario)
        elif opcion == '2':
            libro = input("Ingrese el nombre del libro que desea devolver: ")
            devolver_libro(biblioteca, libro)
        elif opcion == '3':
            mostrar_prestamos(biblioteca)
        elif opcion == '4':
            print("\n¡Hasta luego!")
        else:
            print("\nOpción inválida. Intente nuevamente.\n")
        
        input("Presione Enter para continuar...")
    
main()
