from flask import Flask, request, jsonify, render_template, send_file
import json
import os
import heapq  # Asegúrate de importar heapq para el algoritmo Dijkstra

app = Flask(__name__)
GRAPH_FILE = 'graph.json'

# Cargar o crear grafo
def load_graph():
    if not os.path.exists(GRAPH_FILE):
        with open(GRAPH_FILE, 'w') as f:
            json.dump({"nodes": [], "edges": {}}, f)
    with open(GRAPH_FILE) as f:
        return json.load(f)

def save_graph(graph):
    with open(GRAPH_FILE, 'w') as f:
        json.dump(graph, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nodes', methods=['POST'])
def add_node():
    data = request.get_json()
    node = data.get('node')
    graph = load_graph()
    if node not in graph["nodes"]:
        graph["nodes"].append(node)
        graph["edges"][node] = {}
        save_graph(graph)
    return jsonify(graph)

@app.route('/edges', methods=['POST'])
def add_edge():
    data = request.get_json()
    src = data.get('src')
    dst = data.get('dst')
    weight = data.get('weight')
    graph = load_graph()

    if src in graph["nodes"] and dst in graph["nodes"]:
        graph["edges"][src][dst] = weight
        save_graph(graph)
        return jsonify(graph)
    else:
        return jsonify({"error": "Uno o ambos nodos no existen"}), 400

@app.route('/dijkstra')
def run_dijkstra():
    start = request.args.get('start')
    end = request.args.get('end')
    graph = load_graph()

    if start not in graph["nodes"]:
        return jsonify({"error": "Nodo inicial no existe"}), 400

    try:
        result = dijkstra(graph, start)  # Ejecutar el algoritmo Dijkstra

        if end:
            if end not in graph["nodes"]:
                return jsonify({"error": "Nodo destino no existe"}), 400
            return jsonify({
                "distance": result["distances"][end],
                "path": result["paths"][end]
            })

        return jsonify({
            "distances": result["distances"],
            "paths": result["paths"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Devolver error como JSON


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph["nodes"]}
    previous = {node: None for node in graph["nodes"]}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph["edges"].get(current_node, {}).items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    paths = {}
    for node in graph["nodes"]:
        if distances[node] < float('inf'):
            path = []
            current = node
            while current is not None:
                path.insert(0, current)
                current = previous[current]
            paths[node] = path

    return {"distances": distances, "paths": paths}

@app.route('/graph.json')
def get_graph_file():
    return send_file(GRAPH_FILE)

@app.route('/graph', methods=['DELETE'])
def delete_graph():
    graph = {"nodes": [], "edges": {}}
    save_graph(graph)
    return jsonify({"message": "Grafo eliminado"})

if __name__ == '__main__':
    app.run(debug=True)
