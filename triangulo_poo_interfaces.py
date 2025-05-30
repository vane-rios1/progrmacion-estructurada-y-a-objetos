import tkinter as tk
from tkinter import messagebox

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Área de un Triángulo")

        self.label_base = tk.Label(ventana, text="Base:")
        self.label_base.pack()
        self.entry_base = tk.Entry(ventana)
        self.entry_base.pack()

        self.label_altura = tk.Label(ventana, text="Altura:")
        self.label_altura.pack()
        self.entry_altura = tk.Entry(ventana)
        self.entry_altura.pack()

        self.boton_calcular = tk.Button(ventana, text="Calcular Área", command=self.calcular_area)
        self.boton_calcular.pack()

        self.resultado = tk.Label(ventana, text="")
        self.resultado.pack()

    def calcular_area(self):
        try:
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            triangulo = Triangulo(base, altura)
            area = triangulo.calcular_area()
            self.resultado.config(text=f"Área: {area}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos.")

def main():
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()