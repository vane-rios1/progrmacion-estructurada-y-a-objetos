import tkinter as tk

# Clase que representa un triángulo
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

# Clase que define la interfaz gráfica
class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Área de un Triángulo")

        # Etiqueta y campo de entrada para la base
        tk.Label(self.ventana, text="Base:").pack()
        self.entry_base = tk.Entry(self.ventana)
        self.entry_base.pack()

        # Etiqueta y campo de entrada para la altura
        tk.Label(self.ventana, text="Altura:").pack()
        self.entry_altura = tk.Entry(self.ventana)
        self.entry_altura.pack()

        # Botón para calcular
        tk.Button(self.ventana, text="Calcular Área", command=self.calcular_area).pack()

        # Etiqueta para mostrar el resultado
        self.label_resultado = tk.Label(self.ventana, text="")
        self.label_resultado.pack()

    # Método que calcula el área y actualiza la interfaz
    def calcular_area(self):
        base = float(self.entry_base.get())
        altura = float(self.entry_altura.get())
        triangulo = Triangulo(base, altura)
        area = triangulo.calcular_area()
        self.label_resultado.config(text=f"Área: {area}")

# Función principal
def main():
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()

# Ejecutar la función principal
if __name__ == "__main__":
    main()