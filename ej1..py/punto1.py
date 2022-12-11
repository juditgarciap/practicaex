class nodoArbol(object):
    def __init__(self,info):
        self.izq = None
        self.der = None
        self.info = info


#Funcion encargada de asignar un nuevo nodo al arbol
def insertar_nodo(raiz, dato, sentido):
    if(raiz is None):
        raiz = nodoArbol(dato)
    elif(sentido == "Si"):
        raiz.izq = insertar_nodo(raiz.izq,dato,"Si")
    else:
        raiz.der = insertar_nodo(raiz.der, dato,"No")
    return raiz

#Crea el arbol con las diferentes de cada superheroe donde
#cada nodo hoja es un super hereo (siempre a la izquierda de la mision)
#y los nodos intermedio son preguntas sobre la mision (siempre a la derecha)
def CrearEscuadron():
    HabilidadesHeroes=nodoArbol("Mision intergalacticas")

    insertar_nodo(HabilidadesHeroes,"Khan","Si")
    insertar_nodo(HabilidadesHeroes,"Mision de recuperacion","No")

    insertar_nodo(HabilidadesHeroes.der,"Ant-Man","Si")
    insertar_nodo(HabilidadesHeroes.der,"Mision de destruccion","No")

    insertar_nodo(HabilidadesHeroes.der.der,"Hulk","Si")
    insertar_nodo(HabilidadesHeroes.der.der,"Mision de defensa y recuperacion","No")

    insertar_nodo(HabilidadesHeroes.der.der.der,"Capitan America","Si")
    insertar_nodo(HabilidadesHeroes.der.der.der,"Mision de viaje","No")

    insertar_nodo(HabilidadesHeroes.der.der.der.der,"Capitana Marvel","Si")
    insertar_nodo(HabilidadesHeroes.der.der.der.der,"Mision de habilidad","No")

    insertar_nodo(HabilidadesHeroes.der.der.der.der.der,"Khan","Si")
    insertar_nodo(HabilidadesHeroes.der.der.der.der.der,"Mision de recuperacion e infiltracion","No")

    insertar_nodo(HabilidadesHeroes.der.der.der.der.der.der,"The Winter Soldier","Si")
    insertar_nodo(HabilidadesHeroes.der.der.der.der.der.der,"Mision de defensa y tecnologia","No")

    insertar_nodo(HabilidadesHeroes.der.der.der.der.der.der.der,"Iron Man","Si")
    insertar_nodo(HabilidadesHeroes.der.der.der.der.der.der.der,"Mision rapida","No")

    insertar_nodo(HabilidadesHeroes.der.der.der.der.der.der.der.der,"Nick Fury","Si")
    insertar_nodo(HabilidadesHeroes.der.der.der.der.der.der.der.der,"Mision destruir ejercito","No")

    insertar_nodo(HabilidadesHeroes.der.der.der.der.der.der.der.der.der,"Thor","Si")
    insertar_nodo(HabilidadesHeroes.der.der.der.der.der.der.der.der.der,"No se encuentra hereo para ser","No")

    return HabilidadesHeroes

#imprime un listado de la misiones que puedn realizar los superheroes
def VerMisiones(Heroes):
    print("Lista de misiones:")
    for i in Heroes:
        print("--->",Heroes[i])

#Busca el superhereo indicado para cada mision
#haciendo una comparacion entre la mision que se solicita y un recorrido
#en el arbol
def SeleccionarMision(NombreMision,Escuadron):
    if(Escuadron.izq is None):
        return Escuadron.info
    elif(Escuadron.info==NombreMision):
        return SeleccionarMision(NombreMision, Escuadron.izq)
    else:
        return SeleccionarMision(NombreMision, Escuadron.der)


#Superheroes con las misiones que pueden cumplica cada uno
Heroes = { "Khan" : "Mision intergalacticas",
"Ant-Man":"Mision de recuperacion",
"Hulk": "Mision de destruccion",
"Capitan America" : "Mision de defensa y recuperacion",
"Capitana Marvel" : "Mision de viaje",
"Khan" : "Mision de habilidad",
"The Winter Soldier" : "Mision de recuperacion e infiltracion",
"Iron Man" : "Mision de defensa y tecnologia",
"Nick Fury" : "Mision rapida",
"Thor" : "Mision destruir ejercito"
}   

#Crea el arbol de superheroes
EscuadronSHIELD=CrearEscuadron()
VerMisiones(Heroes)

print("Ingrese mision: ")
Mision = input()
print('{} asignado a: {}'.format(SeleccionarMision(Mision,EscuadronSHIELD), Mision))