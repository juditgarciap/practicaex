import random

#almacena informacion de los nodos de un arbol
class nodoArbol(object):
    def __init__(self,info):
        self.izq = None
        self.der = None
        self.info = info

#agrega un nuevo nodo al arbol
#si el valor del nuevo nos es < raiz pone el nuevo nodo a la izquierda
#si el valor del nuevo nos es > raiz pone el nuevo nodo a la derecha
def insertar_nodo(raiz, dato):
    if(raiz is None):
        raiz = nodoArbol(dato)
    elif(dato < raiz.info):
        raiz.izq = insertar_nodo(raiz.izq,dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

#imprime los nodos del arbol en preorden
def preorden(raiz):
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

#imprime los nodos del arbol en inorden
def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

#imprime los nodos del arbol en postorden
def postorden(raiz):
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

#Busca si el atributo clave se encuentra en el arbol 
#en caso de no encontrarlo retorna None
def buscar(raiz,clave):
    pos = None
    if(raiz is not None):
        if(raiz.info == clave):
            pos = clave
        elif(clave < raiz.info):
            pos = buscar(raiz.izq,clave)
        else:
            pos = buscar(raiz.der,clave)
        return pos

#reemplaza un nodo del arbol cuando ha sido eliminado
def remplazar(raiz):
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

    #elimina un nodo del arbol
def eliminar_nodo(raiz,clave):
    x = None
    if( raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der,clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

#verifica si un numero es par o impar
def EsPar(numero):
    if(numero%2):
        return False
    else:
        return True
#Genera un arbol con 1000 numeros aleatorios enteros en el rango [0-1000]
CantidadNumeros=1000
NumeroAleatorio = random.randint(0,CantidadNumeros)
Arbol = nodoArbol(NumeroAleatorio)
ContadorPares=0
ContadorImpares=0
for i in range(CantidadNumeros-1):
    NumeroAleatorio = random.randint(0,CantidadNumeros)
    #Lleva un conteo de los numeros aleatorios pares o impares
    if(EsPar(NumeroAleatorio)):
        ContadorImpares += 1
    else:
        ContadorPares += 1
    Arbol = insertar_nodo(Arbol, NumeroAleatorio)

#selecciona el tipo de despligue del arbol
print("Despliegue [1]Preorden [2]Inorden [3]Postorden: ")
Despliegue = int(input())
if(Despliegue==1):
    preorden(Arbol)
elif(Despliegue==2):
    inorden(Arbol)
elif(Despliegue==3):
    postorden(Arbol)
else:
    print("Orden no encontrada")

#Busca un numero n si se encuentra en el arbol o no
print("Buscar numero entero en el rango [0-1000]: ")
NumeroBuscar = int(input())
NumeroBuscado = buscar(Arbol,NumeroBuscar)
if(NumeroBuscado is not None):
    print('Numero {} se encuentra en el arbol'.format(NumeroBuscado))
else:
    print('Numero {} no se encuentra en el arbol'.format(NumeroBuscado))

#Elimina 3 valores del arbol
print("\nElimine 3 numeros del arbol")
for i in range(3):
    print('Eliminacion #{}:'.format(i+1))
    NumeroEliminar = int(input())
    eliminar_nodo(Arbol,NumeroEliminar)

print("Numeros pares:",ContadorPares)
print("Numeros impares:",ContadorImpares)
PilaAOrdenar=input()

PilaOrdenada = Ordenar(PilasPalos[PilaAOrdenar])
print('\nPila del palo {} ordenada:\n{}'.format(PilaAOrdenar,PilaOrdenada))