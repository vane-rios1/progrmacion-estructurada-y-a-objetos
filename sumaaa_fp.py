import tkinter as tk                 # Importación de módulo (sintaxis)
from tkinter import messagebox       # Importación de submódulo (sintaxis)

# CLASE que representa la lógica de la suma
class Suma:
    #  CONSTRUCTOR: método especial que se ejecuta al crear el objeto
    def __init__(self, num1, num2):
        self.num1 = num1             # Atributos del objeto
        self.num2 = num2

    # MÉTODO para calcular la suma
    def calcular(self):
        return self.num1 + self.num2

#  CLASE que representa la interfaz gráfica
class InterfazSuma:
    # CONSTRUCTOR: se ejecuta al crear el objeto de la interfaz
    def __init__(self, ventana):
        self.ventna = ventana         # la ventana principal

        # Propiedades de la ventana
        ventana.title("Suma de Dos Números")
        ventana.geometry("300x250")

        # Crear widgets (etiquetas, entradas, botones)
        tk.Label(ventana, text="Número 1:").pack(pady=5)
        self.entry1 = tk.Entry(ventana)       #  OBJETO de tipo Entry (campo de entrada)
        self.entry1.pack()

        tk.Label(ventana, text="Número 2:").pack(pady=5)
        self.entry2 = tk.Entry(ventana)       #  OBJETO de tipo Entry
        self.entry2.pack()

        tk.Button(ventana, text="Sumar", command=self.realizar_suma).pack(pady=10)  #  OBJETO tipo botón

        self.label_resultado = tk.Label(ventana, text="Resultado: ")     #  OBJETO tipo Label
        self.label_resultado.pack(pady=5)

    #  MÉTODO que realiza la suma cuando se presiona el botón
    def realizar_suma(self):
        try:
            num1 = float(self.entry1.get())   # Obtener valores desde los campos
            num2 = float(self.entry2.get())

            suma = Suma(num1, num2)           #  OBJETO: crear instancia de la clase Suma
            resultado = suma.calcular()       # Llamar al método calcular()

            self.label_resultado.config(text=f"Resultado: {resultado}")  # Mostrar el resultado
        except ValueError:
            messagebox.showerror("Error", "Ingrese solo números válidos.")  # Manejo de error

#  FUNCIÓN PRINCIPAL del programa
def main():
    ventana = tk.Tk()                  #  OBJETO: crear la ventana principal
    app = InterfazSuma(ventana)       #  OBJETO: crear una instancia de InterfazSuma
    ventana.mainloop()                # Iniciar la interfaz gráfica

#  SINTAXIS para ejecutar la función principal solo si se corre directamente
if __name__ == "__main__":
    main()