import random
import math

#Pide un numero que se encuentre en un rango [ini-fin]
#cada vez que pide el numero imprime el atributo mensaje
def leer_numero(ini,fin,mensaje):
    while True:
        print(mensaje,end=" ")
        try:
            dato = int(input())
        except:
            print("Error: Tipo de dato no valido")
        if(dato>=ini and dato<=fin):
            return dato

#Pide los datos para generar los numeros
#primero pregunta cuantos numeros quiere generar y luego como los quiere redondear
def generador():
    numeros = leer_numero(1,20,"¿Cuanto numero quieres generar? [1-20]:")
    modo = leer_numero(1,3,"¿Como quieres redondear los numeros? [1]Al alza [2]A la baja [3]Normal")
    listaAleatorios = []

    #genera los n numeros aleatorios que el usuario indica
    for i in range(numeros):
        NumeroAleatorio = random.uniform(0,100)
        #Segun el tipo de redonde elegido por el usario redondea el nuemro y lo almacena
        if(modo == 1):
            NumeroRedondeado = math.trunc(NumeroAleatorio)+1
            listaAleatorios.append(NumeroRedondeado)
        elif(modo == 2):
            NumeroRedondeado = math.trunc(NumeroAleatorio)
            listaAleatorios.append(NumeroAleatorio)
        else:
            NumeroRedondeado = NumeroAleatorio
            listaAleatorios.append(NumeroAleatorio)
        #Muestra el numero aleatorio generado y el numero con el redonde que eligio el usuario
        print("Numero Aleatorio:",NumeroAleatorio,"Redondeado:",NumeroRedondeado)
    return listaAleatorios
generador()