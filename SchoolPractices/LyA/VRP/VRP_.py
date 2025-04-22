import math
from operator import itemgetter

# Coordenadas de los clientes
coord = {
    'EDO.MEX': (19.2938258568844, -99.65366252023884),
    'QRO': (20.593537489366717, -100.39004057702225),
    'CDMX': (19.432854452264177, -99.13330004822943),
    'SLP': (22.151725492903953, -100.97657666103268),
    'MTY': (25.673156272083876, -100.2974200019319),
    'PUE': (19.063532268065185, -98.30729139446866),
    'GDL': (20.67714565083998, -103.34696388920293),
    'MICH': (19.702614895389996, -101.19228631929688),
    'SON': (29.075273188617818, -110.95962477655333)
}

# Pedidos por cliente
pedidos_dict = {
    'EDO.MEX': 10,
    'QRO': 13,
    'CDMX': 7,
    'SLP': 11,
    'MTY': 15,
    'PUE': 8,
    'GDL': 6,
    'MICH': 7,
    'SON': 8
}

# Parámetros
almacen = (19.432854452264177, -99.13330004822943)  # Coordenadas del almacén
max_carga = 40

# Función para obtener la distancia euclidiana
def distancia(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Función para obtener el pedido de un cliente
def pedidos(cliente):
    return pedidos_dict[cliente]

# Función para verificar si un cliente ya está en una ruta
def en_ruta(rutas, cliente):
    for ruta in rutas:
        if cliente in ruta:
            return ruta
    return None

# Calcula el peso total de una ruta
def peso_ruta(ruta):
    return sum(pedidos(c) for c in ruta)

# Función principal de la heurística voraz
def vrp_voraz():
    # Calcular ahorros
    s = {}
    for c1 in coord:
        for c2 in coord:
            if c1 != c2 and (c2, c1) not in s:
                d_c1_c2 = distancia(coord[c1], coord[c2])
                d_c1_almacen = distancia(coord[c1], almacen)
                d_c2_almacen = distancia(coord[c2], almacen)
                s[(c1, c2)] = d_c1_almacen + d_c2_almacen - d_c1_c2

    # Ordenar los ahorros de mayor a menor
    s_ordenado = sorted(s.items(), key=itemgetter(1), reverse=True)

    rutas = []
    for (c1, c2), _ in s_ordenado:
        rc1 = en_ruta(rutas, c1)
        rc2 = en_ruta(rutas, c2)

        if rc1 is None and rc2 is None:
            if peso_ruta([c1, c2]) <= max_carga:
                rutas.append([c1, c2])
        elif rc1 is not None and rc2 is None:
            if rc1[0] == c1:
                if peso_ruta(rc1 + [c2]) <= max_carga:
                    rc1.insert(0, c2)
            elif rc1[-1] == c1:
                if peso_ruta(rc1 + [c2]) <= max_carga:
                    rc1.append(c2)
        elif rc1 is None and rc2 is not None:
            if rc2[0] == c2:
                if peso_ruta(rc2 + [c1]) <= max_carga:
                    rc2.insert(0, c1)
            elif rc2[-1] == c2:
                if peso_ruta(rc2 + [c1]) <= max_carga:
                    rc2.append(c1)
        elif rc1 != rc2:
            if rc1[-1] == c1 and rc2[0] == c2:
                if peso_ruta(rc1 + rc2) <= max_carga:
                    rc1.extend(rc2)
                    rutas.remove(rc2)
            elif rc1[0] == c1 and rc2[-1] == c2:
                if peso_ruta(rc2 + rc1) <= max_carga:
                    rc2.extend(rc1)
                    rutas.remove(rc1)

    return rutas

# Ejecutar si se llama como script
if __name__ == "__main__":
    rutas = vrp_voraz()
    for i, ruta in enumerate(rutas):
        print(f"Ruta {i+1}: {ruta} - Carga total: {peso_ruta(ruta)}")