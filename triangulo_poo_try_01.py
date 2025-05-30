class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

def main():
    try:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        triangulo = Triangulo(base, altura)
        print(f"El área del triángulo es: {triangulo.calcular_area()}")
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")

if __name__ == "__main__":
    main()