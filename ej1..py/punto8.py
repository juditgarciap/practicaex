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

    