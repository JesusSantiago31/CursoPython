# vrp.py
import math
from operator import itemgetter

def calcular_rutas_vrp(coord, pedidos_dict, almacen, max_carga, precio_combustible, VELOCIDAD_PROMEDIO, TIEMPO_MAXIMO):
    def distancia(coord1, coord2):
        return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2) * 111

    def distancia_total_ruta(ruta):
        total = distancia(almacen, coord[ruta[0]])
        for i in range(len(ruta) - 1):
            total += distancia(coord[ruta[i]], coord[ruta[i+1]])
        total += distancia(coord[ruta[-1]], almacen)
        return total

    def tiempo_ruta(ruta):
        return distancia_total_ruta(ruta) / VELOCIDAD_PROMEDIO

    def es_tiempo_valido(ruta):
        return tiempo_ruta(ruta) <= TIEMPO_MAXIMO

    def pedidos(cliente):
        return pedidos_dict[cliente]

    def en_ruta(rutas, cliente):
        for ruta in rutas:
            if cliente in ruta:
                return ruta
        return None

    def peso_ruta(ruta):
        return sum(pedidos(c) for c in ruta)

    def consumo_por_km_con_carga(carga):
        return 0.3 + 0.01 * carga

    def consumo_combustible_variable(ruta):
        total_consumo = 0
        carga_actual = peso_ruta(ruta)

        dist = distancia(almacen, coord[ruta[0]])
        total_consumo += consumo_por_km_con_carga(carga_actual) * dist
        carga_actual -= pedidos(ruta[0])

        for i in range(len(ruta) - 1):
            dist = distancia(coord[ruta[i]], coord[ruta[i+1]])
            total_consumo += consumo_por_km_con_carga(carga_actual) * dist
            carga_actual -= pedidos(ruta[i+1])

        dist = distancia(coord[ruta[-1]], almacen)
        total_consumo += consumo_por_km_con_carga(0) * dist
        return total_consumo

    def costo_combustible_variable(ruta):
        return consumo_combustible_variable(ruta) * precio_combustible

    def vrp_voraz():
        s = {}
        for c1 in coord:
            for c2 in coord:
                if c1 != c2 and (c2, c1) not in s:
                    d_c1_c2 = distancia(coord[c1], coord[c2])
                    d_c1_almacen = distancia(coord[c1], almacen)
                    d_c2_almacen = distancia(coord[c2], almacen)
                    s[(c1, c2)] = d_c1_almacen + d_c2_almacen - d_c1_c2

        s_ordenado = sorted(s.items(), key=itemgetter(1), reverse=True)
        rutas = []
        for (c1, c2), _ in s_ordenado:
            rc1 = en_ruta(rutas, c1)
            rc2 = en_ruta(rutas, c2)

            if rc1 is None and rc2 is None:
                nueva_ruta = [c1, c2]
                if peso_ruta(nueva_ruta) <= max_carga and es_tiempo_valido(nueva_ruta):
                    rutas.append(nueva_ruta)

            elif rc1 is not None and rc2 is None:
                if rc1[0] == c1:
                    nueva_ruta = [c2] + rc1
                    if peso_ruta(nueva_ruta) <= max_carga and es_tiempo_valido(nueva_ruta):
                        rc1.insert(0, c2)
                elif rc1[-1] == c1:
                    nueva_ruta = rc1 + [c2]
                    if peso_ruta(nueva_ruta) <= max_carga and es_tiempo_valido(nueva_ruta):
                        rc1.append(c2)

            elif rc1 is None and rc2 is not None:
                if rc2[0] == c2:
                    nueva_ruta = [c1] + rc2
                    if peso_ruta(nueva_ruta) <= max_carga and es_tiempo_valido(nueva_ruta):
                        rc2.insert(0, c1)
                elif rc2[-1] == c2:
                    nueva_ruta = rc2 + [c1]
                    if peso_ruta(nueva_ruta) <= max_carga and es_tiempo_valido(nueva_ruta):
                        rc2.append(c1)

            elif rc1 != rc2:
                if rc1[-1] == c1 and rc2[0] == c2:
                    nueva_ruta = rc1 + rc2
                    if peso_ruta(nueva_ruta) <= max_carga and es_tiempo_valido(nueva_ruta):
                        rc1.extend(rc2)
                        rutas.remove(rc2)
                elif rc1[0] == c1 and rc2[-1] == c2:
                    nueva_ruta = rc2 + rc1
                    if peso_ruta(nueva_ruta) <= max_carga and es_tiempo_valido(nueva_ruta):
                        rc2.extend(rc1)
                        rutas.remove(rc1)

        resultados = []
        for ruta in rutas:
            resultados.append({
                "ruta": ruta,
                "carga_total": peso_ruta(ruta),
                "distancia_total": round(distancia_total_ruta(ruta), 2),
                "tiempo_estimado": round(tiempo_ruta(ruta), 2),
                "consumo_litros": round(consumo_combustible_variable(ruta), 2),
                "costo_combustible": round(costo_combustible_variable(ruta), 2)
            })
        
        print(resultados)
        return { "rutas": resultados }

    return vrp_voraz()
