def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def main():
    try:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area}")
    except ValueError:
        print("Error: Ingrese solo valores numéricos.")

if __name__ == "__main__":
    main()