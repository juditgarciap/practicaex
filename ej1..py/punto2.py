#la clase pedido lleva los atributos necesarios de cada orden que sea solicitada
class Pedido():
    def __init__(self, nombre, multiverso, descripcion):
        self.nombre = nombre
        self.multiverso = multiverso
        self.descripcion = descripcion
        self.prioridad = ""

    def __str__(self):
        return 'Nombre del Khan solicitante: {} - Multiverso: {} - descripcion: {} - prioridad: {}'.format(self.nombre, self.multiverso, self.descripcion, self.prioridad)

#Lleva el historial de los pedidos atendidos, pedidos por prioridad y vitacora de pedidos de alta prioridad
class AtenderPedidos():
    def __init__(self, listapedidos=[]):
        self.vitacora = []
        self.AtencionPrioridad = {"Alta":None,"Media":None,"Baja":None}
        self.HistorialPedidos = []

#De acuerdo a unas condiciones de nombre del Khan, multiverso y descripcion
#se asigna una prioridad particular para cada orden 
def AsignarPrioridad(orden):
    NombresCondicionesPrioridad={"Gran Conquistador":"Alta", "Khan que todo lo sabe":"Media"}
    UniversoCondicionesPrioridad={"616":"Alta", "838":"Media"}
    DescripcionCondicionesPrioridades={"El que permanece":"Alta", "Carnicero de Dioses":"Media"}
    #Se evaluan nombre, multiverso y descripcion para asignar prioridades 
    try:
        PrioridadNombre = NombresCondicionesPrioridad[orden.nombre]
    except:
        PrioridadNombre = "Baja"

    try: 
        PrioridadCondiciones = UniversoCondicionesPrioridad[orden.multiverso]
    except:
        PrioridadCondiciones = "Baja"

    try: 
        PrioridadDescripcion = DescripcionCondicionesPrioridades[orden.descripcion]
    except:
        PrioridadDescripcion = "Baja"


    #En caso de una orden tener ejemplo: nombre de prioridad alta, descripcion de prioridad media/baja
    #Se prima la prioridad de mayor nivel
    if(PrioridadNombre == "Alta" or PrioridadCondiciones == "Alta" or PrioridadDescripcion == "Alta"):
        PrioridadGeneral = "Alta"
    elif(PrioridadNombre == "Media" or PrioridadCondiciones == "Media" or PrioridadDescripcion == "Media"):
        PrioridadGeneral = "Media"
    else:
        PrioridadGeneral = "Baja"
    return PrioridadGeneral

#Actualiza la pila con la vitacora de las ordenes de alta prioridad
def AdministrarVitacora(Pedido,AgregarElminar,Vitacora):
    if(AgregarElminar):
        if(Pedido.prioridad=="Alta"):
            Vitacora.append(Pedido)
    else:
        if(len(Vitacora)>0):
            Vitacora.pop()
    return Vitacora

#Va resolviendo los pedidos de acuerdo a las prioridades de cada orden que recibe
def ResolverPedidos(Pedido, Atenciones):
    RepetirPedido = True
    while(RepetirPedido):
        #Resuelve las ordenes de prioridad alta, luego media y por ultimo baja 
        if(Atenciones.AtencionPrioridad["Alta"] is not None):
            Atenciones.vitacora = AdministrarVitacora(Atenciones.AtencionPrioridad["Alta"], True, Atenciones.vitacora)
            Atenciones.HistorialPedidos.append(Atenciones.AtencionPrioridad["Alta"])
            Atenciones.AtencionPrioridad["Alta"]=None
        elif(Atenciones.AtencionPrioridad["Media"] is not None):
            Atenciones.HistorialPedidos.append(Atenciones.AtencionPrioridad["Media"])
            Atenciones.AtencionPrioridad["Media"]=None
        else:
            Atenciones.HistorialPedidos.append(Atenciones.AtencionPrioridad["Baja"])
            Atenciones.AtencionPrioridad["Baja"]=None
        
        #si el nuevo pedido tiene prioridad Alta, evalua si en ese nivel de prioridad hay alguna
        #orden, en caso de haber no hace nada hasta que la resuelva. Si no hay orden en esa prioridad 
        #entonces asigna una nueva orden
        #En caso de no haber orden la asigna de una vez
        if(Pedido.prioridad == "Alta" and Atenciones.AtencionPrioridad["Alta"] is None ):
            Atenciones.AtencionPrioridad["Alta"] = Pedido
            RepetirPedido = False
        if(Pedido.prioridad == "Media" and Atenciones.AtencionPrioridad["Media"] is None ):
            Atenciones.AtencionPrioridad["Media"] = Pedido
            RepetirPedido = False
        if(Pedido.prioridad == "Baja" and Atenciones.AtencionPrioridad["Baja"] is None ):
            Atenciones.AtencionPrioridad["Baja"] = Pedido
            RepetirPedido = False
    return Atenciones

def VerDatos(Arreglo, Descripcion):
    print("_____________________________")
    print(Descripcion)
    for i in Arreglo:
        print(i)

#Pedido a realizar 
Pedido0 = Pedido(nombre="Khan que todo lo sabe",multiverso="115",descripcion="Descrip1")
Pedido1 = Pedido(nombre="Khan1", multiverso="19841", descripcion="Descrip2")
Pedido2 = Pedido(nombre="Khan2", multiverso="98413", descripcion="Carnicero de Dioses")
Pedido3 = Pedido(nombre="Khan3", multiverso="55198", descripcion="El que permanece")
Pedido4 = Pedido(nombre="Khan4", multiverso="838", descripcion="Descrip3")
Pedido5 = Pedido(nombre="Khan5", multiverso="616", descripcion="Descrip4")
Pedido6 = Pedido(nombre="Khan6", multiverso="89409", descripcion="Descrip5")
Pedido7 = Pedido(nombre="Gran Conquistador", multiverso="", descripcion="Descrip6")
Pedido8 = Pedido(nombre="Khan7", multiverso="36687", descripcion="Descrip7")
Pedido9 = Pedido(nombre="Khan8", multiverso="21967", descripcion="Descrip8")
Pedidos = [Pedido0, Pedido1, Pedido2, Pedido3, Pedido4, Pedido5, Pedido6, Pedido7, Pedido8, Pedido9]

#Se asigna prioridades particulares a cada pedido
for i in Pedidos:
    i.prioridad = AsignarPrioridad(i)

#Se empiezan a resolver los pedidos de acuerdo al orden que se crearon y sus prioridades
AtencionPedidos=AtenderPedidos(Pedidos)
PedidoGuardado=True
for i in Pedidos:
    AtencionesPedidos = ResolverPedidos(i,AtencionPedidos)


VerDatos(AtencionPedidos.HistorialPedidos,"Historial Pedidos")
VerDatos(AtencionPedidos.vitacora,"Historial Vitacora")