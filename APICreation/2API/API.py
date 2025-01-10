from flask import Flask, request, jsonify, send_file
import subprocess
import os
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return app.send_static_file('index.html')

# Ruta para ejecutar el script y mostrar los resultados
@app.route('/execute-script', methods=['POST'])

def execute_script():
    try:
        # Redirigir salidas de print a un archivo temporal
        output_file = "output.txt"
        with open(output_file, "w") as out:
            subprocess.run(["python", "arbol_decision.py"], stdout=out, stderr=out, check=True)

        # Leer las salidas del archivo temporal
        with open(output_file, "r") as out:
            output = out.read()

        # Verifica y muestra las gráficas generadas
        graph1_path = "graph1.png"  # Asume que la primera gráfica se guarda aquí
        graph2_path = "graph2.png"  # Asume que la segunda gráfica se guarda aquí
        graphs = []
        if os.path.exists(graph1_path):
            graphs.append(graph1_path)
        if os.path.exists(graph2_path):
            graphs.append(graph2_path)

        # Devuelve el contenido del print y las URLs de las gráficas
        return jsonify({
            "output": output,
            "graphs": graphs
        })

    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Error al ejecutar el script", "details": str(e)}), 500


# Ruta para ejecutar el script y mostrar los resultados
@app.route('/execute-analysis', methods=['POST'])
def execute_analysis():
    try:
        # Redirigir salidas de print a un archivo temporal
        output_file = "output.txt"
        with open(output_file, "w") as out:
            subprocess.run(["python", "heart_disease.py"], stdout=out, stderr=out, check=True)

        # Leer las salidas del archivo temporal
        with open(output_file, "r") as out:
            output = out.read()

        # Verifica y muestra las gráficas generadas
        graph3_path = "graph3.png"  # Asume que la primera gráfica se guarda aquí
        graph4_path = "graph4.png"  # Asume que la segunda gráfica se guarda aquí
        graph5_path = "graph5.png"  # Asume que la primera gráfica se guarda aquí
        graph6_path = "graph6.png"  # Asume que la segunda gráfica se guarda aquí
        graphs = []
        if os.path.exists(graph3_path):
            graphs.append(graph3_path)
        if os.path.exists(graph4_path):
            graphs.append(graph4_path)
        if os.path.exists(graph5_path):
            graphs.append(graph5_path)
        if os.path.exists(graph6_path):
            graphs.append(graph6_path)

        # Devuelve el contenido del print y las URLs de las gráficas
        return jsonify({
            "output": output,
            "graphs": graphs
        })

    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Error al ejecutar el script", "details": str(e)}), 500


# Ruta para servir las gráficas
@app.route('/get-graph/<filename>', methods=['GET'])
def get_graph(filename):
    try:
        return send_file(filename, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": "No se pudo cargar la gráfica", "details": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
