#  CLASE que realiza la operación de suma
class Suma:
    #🔧 CONSTRUCTOR: recibe dos números al crear el objeto
    def __init__(self, num1, num2):
        self.num1 = num1  #  OBJETO: atributo que guarda el primer número
        self.num2 = num2  #  OBJETO: atributo que guarda el segundo número

    #  MÉTODO que realiza la suma
    def calcular(self):
        return self.num1 + self.num2  #  operación de suma

#  FUNCIÓN PRINCIPAL del programa
def main():
    try:
        #  OBJETOS: entradas del usuario convertidas a float
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        #  OBJETO: se crea una instancia (objeto) de la clase Suma
        suma = Suma(num1, num2)

        #  LLAMADO al método calcular de la clase
        print("La suma es:", suma.calcular())
    
    #  SINTAXIS de manejo de errores
    except ValueError:
        print("Error: Ingrese solo números válidos.")

#  LLAMADO directo a la función principal (sin if __name__)
main()