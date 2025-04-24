from flask import Flask, request, jsonify, render_template
from vrp import calcular_rutas_vrp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/vrp', methods=['POST'])
def api_vrp():
    data = request.json

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

    pedidos_dict = {
        'EDO.MEX': 10, 'QRO': 13, 'CDMX': 7, 'SLP': 11,
        'MTY': 15, 'PUE': 8, 'GDL': 6, 'MICH': 7, 'SON': 8
    }

    almacen = (float(data['lat']), float(data['lng']))
    max_carga = int(data['max_carga'])
    precio_combustible = float(data['precio_combustible'])
    velocidad = float(data['velocidad'])
    tiempo_max = float(data['tiempo'])

    resultado = calcular_rutas_vrp(coord, pedidos_dict, almacen, max_carga,
                                   precio_combustible, velocidad, tiempo_max)
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)
