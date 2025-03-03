from flask import Flask, request, render_template
from Arbol import Nodo
from Puzzle import buscar_solucion_BFS
from a import buscar_solucion_BFS_rec
from Vuelos_BFS import buscar_solucion_BFS as buscar_solucion_vuelos

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')  # Renderizar el formulario HTML

@app.route('/resultado', methods=['POST'])
def resultado():
    estado_inicial = list(map(int, request.form.get("estado_inicial", "").split(',')))
    solucion = list(map(int, request.form.get("solucion", "").split(',')))
    algoritmo = request.form.get("algoritmo")

    if algoritmo == "BFS":
        nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    elif algoritmo == "BFS_REC":
        nodo_solucion = buscar_solucion_BFS_rec(Nodo(estado_inicial), solucion, [])
    else:
        return "Método de búsqueda no válido"
    
    # Construir la secuencia de pasos hasta la solución
    resultado = []
    if nodo_solucion:  # Comprobar si se encontró una solución
        nodo = nodo_solucion
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
    else:
        resultado = "No se encontró una solución."

    return render_template('resultado.html', resultado=resultado)  # Renderizar el resultado

@app.route('/buscar_vuelos', methods=['POST'])
def buscar_vuelos():
    ciudad_origen = request.form.get("ciudad_origen")
    ciudad_destino = request.form.get("ciudad_destino")
    
    conexiones = {  # Conexiones de las ciudades
        'CDMX': {'SLP', 'MEXICALI', 'CHIHUAHUA'},
        'SAPOPAN': {'ZACATECAS', 'MEXICALI'},
        'GUADALAJARA': {'CHIAPAS'},
        'CHIAPAS': {'CHIHUAHUA'},
        'MEXICALI': {'SLP', 'SAPOPAN', 'CDMX', 'CHIHUAHUA', 'SONORA'},
        'SLP': {'CDMX', 'MEXICALI'},
        'ZACATECAS': {'SAPOPAN', 'SONORA', 'CHIAPAS'},
        'SONORA': {'ZACATECAS', 'MEXICALI'},
        'MICHOACAN': {'CHIHUAHUA'},
        'CHIHUAHUA': {'MICHOACAN', 'ZACATECAS', 'MEXICALI', 'CDMX', 'CHIAPAS'}
    }
    
    nodo_solucion = buscar_solucion_vuelos(conexiones, ciudad_origen, ciudad_destino)  # Llamar la función para vuelos

    # Construir la secuencia de pasos hasta la solución
    resultado = []
    if nodo_solucion:  # Comprobar si se encontró una solución
        nodo = nodo_solucion
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(ciudad_origen)  # Agregar la ciudad de origen al resultado
        resultado.reverse()
    else:
        resultado = "No se encontró una solución."

    return render_template('resultado_vuelos.html', resultado=resultado)  # Renderizar el resultado de vuelos

if __name__ == '__main__':
    app.run(debug=True)
