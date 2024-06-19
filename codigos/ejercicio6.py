import os

def limpiar_consola():
    """Función para limpiar la consola según el sistema operativo."""
    if os.name == 'posix':  # Para sistemas Unix (Linux y macOS)
        _ = os.system('clear')
    else:  # Para sistemas Windows
        _ = os.system('cls')

def menu():
    """Función que muestra el menú y retorna la opción seleccionada por el usuario."""
    print("1. Cargar lista01 de contactos")
    print("2. Cargar lista02 de contactos")
    print("3. Mostrar listas generadas")
    print("4. Generar lista03 (fusión de lista01 y lista02)")
    print("5. Salir")
    opcion = input("Ingrese la opción deseada: ")
    return opcion

def cargar_lista_contactos():
    """Función para cargar una lista de contactos."""
    lista = []
    continuar = 's'
    while continuar == 's':
        celular = input("Ingrese el número de celular del contacto: ")
        nombre = input("Ingrese el nombre del contacto: ")
        correo = input("Ingrese el correo electrónico del contacto: ")
        lista.append((celular, nombre, correo))
        continuar = input("¿Desea agregar otro contacto? (s/n): ").lower()
    return lista

def mostrar_listas(lista01, lista02):
    """Función para mostrar las listas generadas (lista01 y lista02)."""
    print("\nLista01 de contactos:")
    for contacto in lista01:
        print(f"Número: {contacto[0]}, Nombre: {contacto[1]}, Correo: {contacto[2]}")
    
    print("\nLista02 de contactos:")
    for contacto in lista02:
        print(f"Número: {contacto[0]}, Nombre: {contacto[1]}, Correo: {contacto[2]}")
    print()

def fusionar_listas(lista01, lista02):
    """Función para fusionar lista01 y lista02 en lista03, validando números de celular duplicados."""
    lista03 = lista01[:]
    for contacto in lista02:
        celular, nombre, correo = contacto
        if any(celular == c[0] for c in lista03):
            print(f"\nEl contacto con número de celular {celular} ya existe en lista03:")
            print(f"1. Mantener el contacto actual en lista03")
            print(f"2. Reemplazar con el nuevo contacto")
            opcion = input("Ingrese su opción (1 o 2): ")
            while opcion not in ['1', '2']:
                opcion = input("Opción inválida. Ingrese su opción (1 o 2): ")
            if opcion == '2':
                lista03 = [c for c in lista03 if c[0] != celular]
                lista03.append((celular, nombre, correo))
        else:
            lista03.append((celular, nombre, correo))
    print("\nLista03 generada (fusión de lista01 y lista02):")
    for contacto in lista03:
        print(f"Número: {contacto[0]}, Nombre: {contacto[1]}, Correo: {contacto[2]}")
    print()
    return lista03

def main():
    """Función principal que controla la ejecución del programa."""
    lista01 = []
    lista02 = []
    lista03 = []
    opcion = None
    
    while opcion != '5':
        limpiar_consola()
        opcion = menu()

        if opcion == '1':
            print("\nCargar lista01 de contactos:")
            lista01 = cargar_lista_contactos()
        elif opcion == '2':
            print("\nCargar lista02 de contactos:")
            lista02 = cargar_lista_contactos()
        elif opcion == '3':
            if not lista01 and not lista02:
                print("\nAún no se han cargado las listas.")
            else:
                mostrar_listas(lista01, lista02)
        elif opcion == '4':
            if not lista01 or not lista02:
                print("\nDebe cargar ambas listas (lista01 y lista02) antes de generar lista03.")
            else:
                lista03 = fusionar_listas(lista01, lista02)
        elif opcion == '5':
            print("\n¡Hasta luego!\n")
        else:
            print("\nOpción inválida. Intente nuevamente.\n")
        
        input("Presione Enter para continuar...")
    
main()
