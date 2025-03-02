class Nodo:
    def __init__(self, datos, padre=None):
        self.datos = datos
        self.padre = padre

    def get_datos(self):
        return self.datos

    def get_padre(self):
        return self.padre

    def get_hijos(self):
        # Suponiendo que se generan nuevos estados a partir de los datos actuales
        hijos = []
        for i in range(len(self.datos) - 1):
            nuevo_estado = self.datos[:]
            nuevo_estado[i], nuevo_estado[i + 1] = nuevo_estado[i + 1], nuevo_estado[i]
            hijos.append(Nodo(nuevo_estado, self))
        return hijos





def buscar_solucion_BFS_rec(nodo, solucion, visitados):
    if nodo.get_datos() == solucion:
        return nodo

    visitados.append(nodo.get_datos())

    for nodo_hijo in nodo.get_hijos():
        if nodo_hijo.get_datos() not in visitados:
            sol = buscar_solucion_BFS_rec(nodo_hijo, solucion, visitados)
            if sol is not None:
                return sol
    return None


if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    visitados = []
    nodo_inicial = Nodo(estado_inicial)

    nodo_solucion = buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados)

    # Mostrar resultados
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.reverse()
        print(resultado)
    