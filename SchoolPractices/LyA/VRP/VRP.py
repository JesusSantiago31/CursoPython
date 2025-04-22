import math
from operator import itemgetter

def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def en_ruta(rutas, c):
    ruta = None
    for r in rutas:
        if c in r:
            ruta = r
    return ruta

def peso_ruta(ruta):
    total = 0
    for c in ruta:
        total = total + pedidos(c)
    return total

def vrp_voraz():
    # Calcular los ahorros
    s = {}
    for c1 in coord:
        for c2 in coord:
            if c1 != c2:
                if not (c2, c1) in s:
                    d_c1_c2 = distancia(coord[c1], coord[c2])
                    d_c1_almacen = distancia(coord[c1], almacen)
                    d_c2_almacen = distancia(coord[c2], almacen)
                    s[c1, c2] = d_c1_almacen + d_c2_almacen - d_c1_c2
    # Ordenar ahorros
    s = sorted(s.items(), key = itemgetter(1), reverse = True)

    # Construir rutas
    rutas = []
    for k,v in s:
        rc1 = en_ruta(rutas, k[0])
        rc2 = en_ruta(rutas, k[1])
        if rc1 == None and rc2 == None:
            # No estan en ninguna Ruta, La creamos
            if peso_ruta([k[0], k[1]]) <= max_carga:
                rutas.append([k[0], k[1]])
        elif rc1 != None and rc2 == None:
            # Cliente 1 ya cuenta con una ruta, agregamos ruta al cliente 2.
            if rc1[0] == k[0]:
                if peso_ruta(rc1) + peso_ruta([k[1]]) <= max_carga:
                    rutas[rutas.index(rc1)].insert(0, k[1])
            elif rc1[len(rc1) - 1] == k[0]:
                if peso_ruta(rc1) + peso_ruta([k[1]]) <= max_carga:
                    rutas[rutas.index(rc1)].append(k[1])
        elif rc1 == None and rc2 != None:
            # Cliente 2 ya esta en una ruta. Agregamos el Cliente 1
            if rc2[0] == k[1]:
                if peso_ruta(rc2) + peso_ruta([k[0]]) <= max_carga:
                    rutas[rutas.index(rc2)].insert(0, k[0])
            elif rc2[len(rc2) - 1] == k[1]:
                if peso_ruta(rc2) + peso_ruta([k[0]]) <= max_carga:
                    rutas[rutas.index(rc2)].append(k[0])
        elif rc1 != None and rc2 != None and rc1 != rc2:
            # Cliente 1 y 2 ya estan en una ruta. tratamos de unirlas
            if rc1[0] == k[0] and rc2[len(rc2) -1] == k[1]:
                if peso_ruta(rc1) + peso_ruta(rc2) <= max_carga:
                    rutas[rutas.index(rc2)].extend(rc1)
                    rutas.remove(rc1)
            elif rc1[len(rc1) - 1] == k[0] and rc2[0] == k[1]:
                if peso_ruta(rc1) + peso_ruta(rc2) <= max_carga:
                    rutas[rutas.index(rc1)].extend(rc2)

                    rutas.remove(rc2)


coord = {
    'EDO.MEX': (19.2938258568844, -99.65366252023884),
    'QRO': (20.593537489366717, -100.39004057702225),
    'CDMX': (19.432854452264177, -99.13330004822943),
    'SLP': (22.151725492903953, -100.97657666103268),
    'MTY': (25.673156272083876, -100.2974200019319),
    'PUE': (19.063532268065185, -98.30729139446866),
    'GDL':(20.67714565083998, -103.34696388920293),
    'MICH':(19.702614895389996, -101.19228631929688),
    'SON': (29.075273188617818, -110.95962477655333)
}
   
pedidos = {
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


almacen = [19.432854452264177, -99.13330004822943]
max_carga = 40

if __name__ == "__main__":
    rutas = vrp_voraz()
    for ruta in rutas:
        print(ruta)