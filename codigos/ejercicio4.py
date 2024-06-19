import os

def limpiar_consola():
    """Función para limpiar la consola según el sistema operativo."""
    if os.name == 'posix':  # Para sistemas Unix (Linux y macOS)
        _ = os.system('clear')
    else:  # Para sistemas Windows
        _ = os.system('cls')

def menu():
    """Función que muestra el menú y retorna la opción seleccionada por el usuario."""
    print("1. Añadir estudiante")
    print("2. Eliminar estudiante")
    print("3. Mostrar estudiante")
    print("4. Listar todos los estudiantes")
    print("5. Listar estudiantes activos o pasivos")
    print("6. Cambiar estado de estudiante")
    print("7. Salir")
    opcion = input("Ingrese la opción deseada: ")
    return opcion

def agregar_estudiante(estudiantes):
    """Función para agregar un estudiante a la base de datos."""
    lu = input("Ingrese la Libreta Universitaria (LU) del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    direccion = input("Ingrese la dirección del estudiante: ")
    telefono = input("Ingrese el teléfono del estudiante: ")
    correo = input("Ingrese el correo electrónico del estudiante: ")
    estado = True  # Por defecto, el estado es True (activo)
    estudiantes[lu] = {
        'nombre': nombre,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'estado': estado
    }
    print(f"\nEstudiante con LU {lu} agregado correctamente.\n")

def eliminar_estudiante(estudiantes):
    """Función para eliminar un estudiante de la base de datos."""
    lu = input("Ingrese la LU del estudiante a eliminar: ")
    if lu in estudiantes:
        del estudiantes[lu]
        print(f"\nEstudiante con LU {lu} eliminado correctamente.\n")
    else:
        print(f"\nNo se encontró ningún estudiante con LU {lu}.\n")

def mostrar_estudiante(estudiantes):
    """Función para mostrar los datos de un estudiante específico."""
    lu = input("Ingrese la LU del estudiante a mostrar: ")
    if lu in estudiantes:
        estudiante = estudiantes[lu]
        print("\nDatos del estudiante:")
        print(f"LU: {lu}")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Dirección: {estudiante['direccion']}")
        print(f"Teléfono: {estudiante['telefono']}")
        print(f"Correo: {estudiante['correo']}")
        estado = "Activo" if estudiante['estado'] else "Inactivo"
        print(f"Estado: {estado}\n")
    else:
        print(f"\nNo se encontró ningún estudiante con LU {lu}.\n")

def listar_estudiantes(estudiantes):
    """Función para listar todos los estudiantes en la base de datos."""
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados en la base de datos.\n")
    else:
        print("\nListado de todos los estudiantes:")
        for lu, estudiante in estudiantes.items():
            print(f"LU: {lu}, Nombre: {estudiante['nombre']}, Estado: {'Activo' if estudiante['estado'] else 'Inactivo'}")
        print()

def listar_activos_pasivos(estudiantes):
    """Función para listar estudiantes activos o pasivos según la opción seleccionada."""
    activo = input("¿Quiere listar estudiantes activos (s/n)? ").lower() == 's'
    estado_buscar = True if activo else False
    estudiantes_filtrados = [lu for lu, estudiante in estudiantes.items() if estudiante['estado'] == estado_buscar]
    if len(estudiantes_filtrados) == 0:
        if activo:
            print("\nNo hay estudiantes activos en la base de datos.\n")
        else:
            print("\nNo hay estudiantes pasivos (inactivos) en la base de datos.\n")
    else:
        print("\nListado de estudiantes:")
        for lu in estudiantes_filtrados:
            print(f"LU: {lu}, Nombre: {estudiantes[lu]['nombre']}")
        print()

def cambiar_estado(estudiantes):
    """Función para cambiar el estado de un estudiante de activo a pasivo o viceversa."""
    lu = input("Ingrese la LU del estudiante cuyo estado desea cambiar: ")
    if lu in estudiantes:
        estudiantes[lu]['estado'] = not estudiantes[lu]['estado']  # Cambiar estado
        estado_actual = "Activo" if estudiantes[lu]['estado'] else "Inactivo"
        print(f"\nEstado del estudiante con LU {lu} cambiado a {estado_actual}.\n")
    else:
        print(f"\nNo se encontró ningún estudiante con LU {lu}.\n")

def main():
    """Función principal que controla la ejecución del programa."""
    estudiantes = {}
    opcion = None
    
    while opcion != '7':
        limpiar_consola()
        opcion = menu()

        if opcion == '1':
            agregar_estudiante(estudiantes)
        elif opcion == '2':
            eliminar_estudiante(estudiantes)
        elif opcion == '3':
            mostrar_estudiante(estudiantes)
        elif opcion == '4':
            listar_estudiantes(estudiantes)
        elif opcion == '5':
            listar_activos_pasivos(estudiantes)
        elif opcion == '6':
            cambiar_estado(estudiantes)
        elif opcion == '7':
            print("\n¡Hasta luego!\n")
        else:
            print("\nOpción inválida. Intente nuevamente.\n")
        
        input("Presione Enter para continuar...")
    
main()
