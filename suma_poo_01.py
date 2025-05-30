#  CLASE que realiza la suma
class Suma:
    #  CONSTRUCTOR: se ejecuta al crear un objeto de esta clase
    def __init__(self, num1, num2):
        self.num1 = num1  #  OBJETO: atributo del objeto creado
        self.num2 = num2  #  OBJETO: atributo del objeto creado

    #  MÉTODO que devuelve la suma de los atributos
    def calcular(self):
        return self.num1 + self.num2  #  operación realizada dentro del método

#  FUNCIÓN PRINCIPAL del programa
def main():
    try:
        #  OBJETOS: se convierten los datos ingresados por el usuario a float
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        #  OBJETO: se crea una instancia de la clase Suma
        operacion = Suma(num1, num2)

        #  LLAMADO al método calcular del objeto operacion
        resultado = operacion.calcular()

        #  MÉTODO print muestra el resultado
        print(f"La suma es: {resultado}")
    
    #  SINTAXIS de manejo de excepciones
    except ValueError:
        print("Error: por favor ingrese solo números válidos.")

#  SINTAXIS para ejecutar el programa directamente (punto de entrada)
if __name__ == "__main__":
    main()