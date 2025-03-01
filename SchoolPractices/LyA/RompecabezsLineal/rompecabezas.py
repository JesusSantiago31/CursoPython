class Nodo:
    def __init__(self, datos, hijos = None):
        self.datos = datos
        self.datos = None
        self.padre = None
        self.costo = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos != None:
            for h in hijos:
                h.padre = self

    def get_hijos(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
    
    def set_costo(self, costo):
        self.costo = costo

    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista

    def _str_(self):
        return str(self.get_datos())


Get_hijos()			# Asigna al nodo la lista de hijos que son pasados por parámetros.
Get_hijos()			# Retorna una lista con los hijos del nodo.
Get_padre()			#Retorna el nodo padre.
Set_padre(padre)	# 	Asigna el nodo padre a este nodo.
Set_datos(dato)		#Asigna un dato al nodo.
Get_datos( )		#	Devuelve el dato almacenado en el nodo.
Set_peso( )			#Asigna un peso al nodo dentro del árbol.
Get_peso( )			#Devuelve el peso del nodo dentro del árbol.
En_lista(lista_nodos)	#	Devuelve True si el dato ontenido en el nodo es igual a alguno de los nodos contenidos en la lista de nodos pasada como parámetros.

# Puzle Lineal con busqueda en amplitud.
from arbol import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado)and len(nodos_frontera) !=0:
        nodo = nodos_frontera.pop(0)
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            # Solucion encontrada
            solucionado = True
            return nodo
        else:
            # Expandir nodos hijo
            dato_nodo = nodo.get_datos()

            # Operador Izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) \
                and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)