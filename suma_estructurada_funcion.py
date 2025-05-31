# FUNCIÓN que realiza la suma de dos números 
def sumar(num1, num2):  #  FUNCIÓN definida por el usuario
    return num1 + num2  #  "MÉTODO": operación principal de la lógica

# FUNCIÓN principal del programa
def main():  #  FUNCIÓN principal que organiza el flujo del programa
    # OBJETO: entrada del usuario convertida a número flotante
    num1 = float(input("Ingrese el primer número: "))  #  SINTAXIS de entrada y conversión a float
    num2 = float(input("Ingrese el segundo número: "))  #  SINTAXIS de entrada y conversión a float

    # LLAMADO a la FUNCIÓN sumar
    resultado = sumar(num1, num2)  #  OBJETO resultado de la operación

    # SALIDA del resultado al usuario
    print("La suma es:", resultado)  #  SINTAXIS de salida por pantalla

# LLAMADO a la FUNCIÓN principal (EJECUCIÓN del programa)
main()  #  SINTAXIS que ejecuta la función principal directamente