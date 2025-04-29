from flask import Flask, request, render_template
import math
import random

app = Flask(__name__)

# ---- Código base ----

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i+1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])
    return total

def hill_climbing(coord):
    ruta = list(coord.keys())
    random.shuffle(ruta)

    mejora = True
    while mejora:
        mejora = False
        dist_actual = evalua_ruta(ruta, coord)

        for i in range(len(ruta)):
            if mejora:
                break
            for j in range(len(ruta)):
                if i != j:
                    ruta_tmp = ruta[:]
                    ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                    dist = evalua_ruta(ruta_tmp, coord)
                    if dist < dist_actual:
                        mejora = True
                        ruta = ruta_tmp[:]
                        break
    return ruta, evalua_ruta(ruta, coord)

# ---- Datos iniciales ----

coord_fijo = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754472859146, -103.34625354877137),
    'Monterrey': (25.69161110159454, -100.321838480256),
    'QuintanaRoo': (21.163111924844458, -86.80231502121464),
    'Michohacan': (19.701400113725654, -101.20829680213464),
    'Aguascalientes': (21.87641043660486, -102.26438663286967),
    'CDMX': (19.432713075976878, -99.13318344772986),
    #'QRO': (20.59719437542255, -100.38667040246602)
}

# ---- Rutas de la API ----

@app.route("/", methods=["GET", "POST"])
def index():
    resultado_fijo = None
    resultado_personalizado = None
    ciudades_guardadas = []  # <--- Agregamos esto

    if request.method == "POST":
        if "ejecutar_fijo" in request.form:
            ruta, distancia_total = hill_climbing(coord_fijo)
            resultado_fijo = {"ruta": ruta, "distancia": distancia_total}

        if "ejecutar_personalizado" in request.form:
            try:
                coord_personalizado = {}
                ciudades = request.form.getlist("ciudades")
                ciudades_guardadas = ciudades  # <--- Guardamos las ciudades
                for ciudad in ciudades:
                    partes = ciudad.split(",")
                    nombre = partes[0].strip()
                    lat = float(partes[1].strip())
                    lon = float(partes[2].strip())
                    coord_personalizado[nombre] = (lat, lon)

                ruta, distancia_total = hill_climbing(coord_personalizado)
                resultado_personalizado = {"ruta": ruta, "distancia": distancia_total}
            except Exception as e:
                resultado_personalizado = {"error": str(e)}

    return render_template(
        "index.html",
        resultado_fijo=resultado_fijo,
        resultado_personalizado=resultado_personalizado,
        ciudades_guardadas=ciudades_guardadas  # <--- Enviamos a HTML
    )

# ---- Main ----

if __name__ == "__main__":
    app.run(debug=True)
