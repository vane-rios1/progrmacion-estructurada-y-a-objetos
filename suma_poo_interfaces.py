import tkinter as tk
from tkinter import messagebox

# Clase que realiza la operación de suma
class Suma:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular(self):
        return self.num1 + self.num2

# Clase que gestiona la interfaz gráfica
class InterfazSuma:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Suma de Dos Números")
        ventana.geometry("300x250")

        # Número 1
        tk.Label(ventana, text="Número 1:").pack(pady=5)
        self.entry1 = tk.Entry(ventana)
        self.entry1.pack()

        # Número 2
        tk.Label(ventana, text="Número 2:").pack(pady=5)
        self.entry2 = tk.Entry(ventana)
        self.entry2.pack()

        # Botón de suma
        tk.Button(ventana, text="Sumar", command=self.realizar_suma).pack(pady=10)

        # Resultado
        self.label_resultado = tk.Label(ventana, text="Resultado: ")
        self.label_resultado.pack(pady=5)

    def realizar_suma(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            suma = Suma(num1, num2)
            resultado = suma.calcular()
            self.label_resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese solo números válidos.")

# Función principal
def main():
    ventana = tk.Tk()
    app = InterfazSuma(ventana)
    ventana.mainloop()

# Ejecutar el programa
if __name__ == "__main__":
    main()