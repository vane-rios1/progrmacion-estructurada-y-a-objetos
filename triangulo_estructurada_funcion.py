# FUNCIÓN que calcula el área del triángulo
def calcular_area_triangulo(base, altura):
    # MÉTODO: realiza el cálculo del área
    return (base * altura) / 2

# FUNCIÓN principal que organiza el programa
def main():
    # OBJETO: entrada del usuario convertida a número decimal
    base = float(input("Ingrese la base del triángulo: "))  # SINTAXIS de entrada
    altura = float(input("Ingrese la altura del triángulo: "))  # SINTAXIS de entrada

    # LLAMADO al método calcular_area_triangulo
    area = calcular_area_triangulo(base, altura)

    # SINTAXIS: salida del resultado en pantalla
    print(f"El área del triángulo es: {area}")

# EJECUCIÓN del programa llamando la función principal
main()  #  SINTAXIS que ejecuta la función principal directamente