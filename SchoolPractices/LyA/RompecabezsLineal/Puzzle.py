# Puzle Lineal con busqueda en amplitud.
from Arbol import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while not solucionado and len(nodos_frontera) !=0: ####
        nodo = nodos_frontera.pop(0) # Poner 0 o no
        # Extraer el nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            # Solucion encontrada
            solucionado = True
            return nodo
        
        # Expandir nodos hijo
        dato_nodo = nodo.get_datos()
        
        # Operador Izquierda (intercambiar posición 0 y 1)
        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
        hijo_izquierdo.padre = nodo

        if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_izquierdo)

        # Operador Centro (intercambiar posición 1 y 2)
        hijo_centro = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
        hijo_centro.padre = nodo

        if not hijo_centro.en_lista(nodos_visitados) and not hijo_centro.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_centro)

        # Operador Derecha (intercambiar posición 2 y 3)
        hijo_derecha = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])
        hijo_derecha.padre = nodo

        if not hijo_derecha.en_lista(nodos_visitados) and not hijo_derecha.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_derecha)

           
if __name__ == "__main__":####
    estado_inicial = [4,2,3,1]
    solucion = [1,2,3,4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre()!= None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
        

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)

    ## [[4,2,3,1],[2,4,3,1],[2,1,3,4],[2,1,3,4],[1,2,3,4]]

