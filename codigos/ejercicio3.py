def contar_caracteres(texto):
    # Creamos un diccionario vacío para almacenar las repeticiones
    conteo = {}

    # Recorremos cada caracter en el texto
    for caracter in texto:
        # Si el caracter ya está en el diccionario, incrementamos su contador
        if caracter in conteo:
            conteo[caracter] += 1
        # Si no está, lo agregamos al diccionario con contador inicializado en 1
        else:
            conteo[caracter] = 1

    return conteo

# Función principal para recibir el texto del usuario
def main():
    texto = input("Ingrese un texto: ")
    resultado = contar_caracteres(texto.upper())  # Convertimos a mayúsculas para contar sin distinguir entre mayúsculas y minúsculas
    
    # Mostramos el resultado ordenado alfabéticamente
    print("\nAnálisis de caracteres:")
    for caracter in sorted(resultado):
        print(f"{caracter}: {resultado[caracter]}")

# Ejecutamos el programa principal
main()
