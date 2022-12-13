#importa el archivo operaciones.py que esta en el mismo directorio
from operaciones import * 

#realiza pruebas de funcionamiento del sistema
a, b, c, d = (10, 5, 0, "Hola")
print( "{} + {} = {}".format(a, b, suma(a, b) ) )
print( "{} - {} = {}".format(b, d, resta(b, d) ) )
print( "{} * {} = {}".format(b, b, producto(b, b) ) )
print( "{} / {} = {}".format(a, c, division(a, c) ) )



#OPERACIONES 

def suma(Numero1, Numero2):
    try:
        return Numero1 + Numero2
    except TypeError:
    # Verifica si el tipo de dato de los atributos de la funciones
    # son tipos de datos para valores numericos
        print("Error: Tipo de dato no valido")

def resta(Numero1, Numero2):
    try:
        return Numero1 - Numero2
    except TypeError:
    # Verifica si el tipo de dato de los atributos de la funciones
    # son tipos de datos para valores numericos
        print("Error: Tipo de dato no valido")

def producto(Numero1, Numero2):
    try:
        return Numero1 * Numero2
    except TypeError:
    # Verifica si el tipo de dato de los atributos de la funciones
    # son tipos de datos para valores numericos
        print("Error: Tipo de dato no valido")

def division(Numero1, Numero2):
    try:
        return Numero1/Numero2
    except ZeroDivisionError:
    # Verifica si se esta haciendo una division entre 0
        print("Error: No es posible dividir entre cero")
    except TypeError:
    # Verifica si el tipo de dato de los atributos de la funciones
    # son tipos de datos para valores numericos
        print("Error: Tipo de dato no valido")