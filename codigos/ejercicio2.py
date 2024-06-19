import os

def continuar():
    input('\nPresione una tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('\n--- Agenda de Contactos ---')
    print('1. Añadir/modificar contacto')
    print('2. Buscar contacto por nombre')
    print('3. Borrar contacto')
    print('4. Listar todos los contactos')
    print('5. Salir')
    opcion = input('Elija una opción (1-5): ')
    while opcion not in ['1', '2', '3', '4', '5']:
        opcion = input('Opción inválida. Elija una opción del 1 al 5: ')
    return opcion

def agregar_modificar(contactos):
    nombre = input('Ingrese el nombre del contacto: ')
    telefono = input('Ingrese el número de teléfono: ')
    if nombre in contactos:
        print(f"\nEl contacto '{nombre}' ya existe en la agenda.")
        print(f"Número de teléfono actual: {contactos[nombre]}")
        respuesta = input("¿Desea modificar el número de teléfono? (s/n): ")
        if respuesta.lower() == 's':
            contactos[nombre] = telefono
            print(f"Número de teléfono actualizado para '{nombre}': {telefono}")
    else:
        contactos[nombre] = telefono
        print(f"Contacto '{nombre}' agregado a la agenda con número de teléfono: {telefono}")

def buscar_contacto(contactos):
    inicio = input('Ingrese el inicio del nombre a buscar: ')
    encontrados = [(nombre, telefono) for nombre, telefono in contactos.items() if nombre.startswith(inicio)]
    if encontrados:
        print('\nContactos encontrados:')
        for idx, (nombre, telefono) in enumerate(encontrados, start=1):
            print(f"{idx}. Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print(f"No se encontraron contactos que empiecen con '{inicio}'")

def borrar_contacto(contactos):
    nombre = input('Ingrese el nombre del contacto a borrar: ')
    if nombre in contactos:
        confirmacion = input(f"¿Confirma que desea eliminar a '{nombre}'? (s/n): ")
        if confirmacion.lower() == 's':
            del contactos[nombre]
            print(f"Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"No se encontró el contacto '{nombre}' en la agenda.")

def listar_contactos(contactos):
    if contactos:
        print("\nLista de contactos:")
        for nombre, telefono in contactos.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("\nLa agenda está vacía. No hay contactos para mostrar.")

def main():
    contactos = {}
    while True:
        opcion = menu()
        
        if opcion == '1':
            agregar_modificar(contactos)
        elif opcion == '2':
            buscar_contacto(contactos)
        elif opcion == '3':
            borrar_contacto(contactos)
        elif opcion == '4':
            listar_contactos(contactos)
        elif opcion == '5':
            print('\nSaliendo del programa...')
            break
        
        continuar()

# Ejecutar el programa al final del código
os.system('cls' if os.name == 'nt' else 'clear')
main()
