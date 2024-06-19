
import os

def continuar():
    print()
    input('presione una tecla para continuar ...')
    os.system('cls')

def menu():
    print('1) Cargar alumnos')
    print('2) Mostrar el listado de alumnos.')
    print('3) Buscar un alumno')
    print('4) Modificar los datos de un Alumno')
    print('5) Eliminar un Alumno. ')
    print('6) Mostrar Mayores a una Nota')
    print('7) Salir')
    eleccion = int(input('Elija una opción: '))
    while not((eleccion >= 1) and (eleccion <= 7)):
        eleccion = int(input('Elija una opción: '))
    os.system('cls')
    return eleccion

def leerNota():
    nota = float(input('Nota: '))
    while not((nota >= 0) and (nota <= 10)):
        nota = float(input('Nota: '))
    return nota

def mostrar(diccionario):
    print('Listado de Alumnos')
    for clave, valor in diccionario.items():
        print(clave,valor)

def leerEstudiantes():
    print('Cargar Lista de Alumnos')
    estudiantes = { 88:['Mary', 10.0],
                    29:['Anna', 2.0],
                    53:['Juan', 7.5],
                    67:['Pedro',6.5]}
    dni = -1
    while (dni != 0):
        dni = int(input('DNI (cero para finalizar): '))
        if dni != 0: 
            #datoDNI = estudiantes.get(dni,-1)
            #if (datoDNI == -1):
            if dni in estudiantes:
                print('el estudiante ya existe')
            else:
                nombre = input('Nombre: ')
                nota = leerNota()
                estudiantes[dni] = [nombre,nota]
                print('agregado correctamente')

    return estudiantes

def buscarPorDni(estudiantes):
    dni = int(input('DNI: '))
    datos = estudiantes.get(dni,-1)
    return dni,datos

def buscar(estudiantes):
    print('Buscar un alumno por su DNI ')
    dni, datos = buscarPorDni(estudiantes)
    if(datos != -1): 
        print(dni, datos)
    else:
        print('No existe el DNI ingresado')
    

def modificar(estudiantes):
    print('Modificar datos de un Alumno')
    dni, dato = buscarPorDni(estudiantes)    
    if (dato != -1):
        nombre = input('Nombre: ')
        nota = leerNota()
        estudiantes[dni] = [nombre,nota]
        print('Modificado correctamente')
    else:
        print('el Estudiante NO existe')

def eliminar(estudiantes):
    print('Eliminar un Alumno')
    dni, dato = buscarPorDni(estudiantes)    
    if (dato != -1):
        print('Se va a eliminar: ', estudiantes[dni])
        confirmacion = input('Confirma eliminarlo s/n: ')
        if (confirmacion == 's'):
            del estudiantes[dni]
            print ('Eliminado ...')
    else:
        print('El DNI no existe') 

def mayoresAUnaNota(estudiantes):
    print('Lista de estudiantes mayores a una nota: ')
    nota = leerNota()
    suma = 0.
    cantidad = 0
    for dni, datos in estudiantes.items():
        if datos[1] >= nota: 
            print(dni, datos)
            suma += datos[1]
            cantidad += 1
    print ('Promedio: ', suma / cantidad)        

def salir():
    print('Fin del programa...')

#principal
opcion = 0

os.system('cls')
while (opcion != 7):
    opcion = menu()
    if opcion == 1:
        estudiantes = leerEstudiantes()
    elif opcion == 2:
        mostrar(estudiantes)
    elif opcion == 3:
        buscar(estudiantes)
    elif opcion == 4:
        modificar(estudiantes)
    elif opcion == 5:
        eliminar(estudiantes)
    elif opcion == 6:
        mayoresAUnaNota(estudiantes)
    elif (opcion == 7):        
        salir()
    continuar()
