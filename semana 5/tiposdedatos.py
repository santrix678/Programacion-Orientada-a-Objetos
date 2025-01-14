# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dado su base y altura.
    :param base: Base del rectángulo (float)
    :param altura: Altura del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    return base * altura

# Función para mostrar el registro de figuras
def mostrar_registro_figuras(registro):
    """
    Muestra el registro de figuras y sus áreas.
    :param registro: Lista de figuras con sus nombres y áreas
    """
    print("\n=== Registro de Figuras ===")
    for figura in registro:
        print(f"Figura: {figura['nombre']}, Área: {figura['area']:.2f} unidades cuadradas")
    print("===========================")

# Programa principal
def main():
    """
    Función principal que permite al usuario calcular áreas y registrar figuras.
    """
    print("=== Calculadora de Áreas ===")
    registro_figuras = []  # Lista para almacenar información de las figuras

    while True:
        print("\nMenú de Opciones:")
        print("1. Calcular área de un rectángulo")
        print("2. Ver registro de figuras")
        print("3. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                nombre_figura = input("Ingrese el nombre de la figura: ")
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                
                area = calcular_area_rectangulo(base, altura)
                print(f"El área del rectángulo '{nombre_figura}' es: {area:.2f} unidades cuadradas")
                
                # Agregar figura al registro
                registro_figuras.append({
                    "nombre": nombre_figura,
                    "area": area
                })
            
            elif opcion == 2:
                if registro_figuras:
                    mostrar_registro_figuras(registro_figuras)
                else:
                    print("El registro está vacío.")
            
            elif opcion == 3:
                print("Gracias por usar la Calculadora de Áreas. ¡Hasta luego!")
                break
            
            else:
                print("Por favor, seleccione una opción válida.")

        except ValueError:
            print("Entrada no válida. Por favor, intente nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
