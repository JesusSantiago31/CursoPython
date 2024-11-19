# Importación de los módulos necesarios para la aplicación
from flask import Flask, jsonify, request, send_from_directory, render_template  # Importa las funciones y clases de Flask para crear la app y manejar rutas y respuestas
import os  # Importa el módulo os para interactuar con el sistema de archivos
import nbformat  # Importa el módulo nbformat para leer y manejar archivos .ipynb (notebooks de Jupyter)

# Creación de la instancia de la aplicación Flask
app = Flask(__name__, static_folder='static')  # Crea la aplicación Flask con la carpeta estática 'static'

# Definición de la ruta donde se encuentran los documentos .ipynb
DOCUMENTS_FOLDER = 'documentos'  # La carpeta donde se almacenan los documentos .ipynb
app.config['DOCUMENTS_FOLDER'] = DOCUMENTS_FOLDER  # Configura la ruta de los documentos en la aplicación Flask

# Ruta principal que sirve el archivo index.html
@app.route('/')
def home():
    return send_from_directory('static', 'index.html')  # Retorna el archivo 'index.html' desde la carpeta 'static'

# Ruta para servir la página 'regresionLogistica.html'
@app.route("/regresionLogistica", methods=["GET", "POST"])
def logistic_regresion():
    return send_from_directory('static', 'regresionLogistica.html')  # Retorna la página 'regresionLogistica.html'

# Ruta para servir la página 'dataVisualization.html'
@app.route("/dataVisualization", methods=["GET", "POST"])
def data_visualization():
    return send_from_directory('static', 'dataVisualization.html')  # Retorna la página 'dataVisualization.html'

# Ruta para servir la página 'datasetPreparation.html'
@app.route("/datasetPreparations", methods=["GET", "POST"])
def data_prep():
    return send_from_directory('static', 'datasetPreparation.html')  # Retorna la página 'datasetPreparation.html'

# Ruta para servir la página 'pipelineCreation.html'
@app.route("/pipelineCreation", methods=["GET", "POST"])
def pipeline_creation():
    return send_from_directory('static', 'pipelineCreation.html')  # Retorna la página 'pipelineCreation.html'

# Ruta para servir la página 'resultsEvaluation1.html'
@app.route("/resultsEvaluation1", methods=["GET", "POST"])
def results_evaluation_1():
    return send_from_directory('static', 'resultsEvaluation1.html')  # Retorna la página 'resultsEvaluation1.html'

# Ruta para servir la página 'resultsEvaluation2.html'
@app.route("/resultsEvaluation2", methods=["GET", "POST"])
def results_evaluation_2():
    return send_from_directory('static', 'resultsEvaluation2.html')  # Retorna la página 'resultsEvaluation2.html'

# Ruta para leer el contenido de un archivo .ipynb (notebook de Jupyter) y enviarlo como JSON
@app.route('/documentos/contenido/<nombre>', methods=['GET'])
def ver_contenido_documento(nombre):
    try:
        # Construye la ruta completa del archivo .ipynb
        notebook_path = os.path.join(DOCUMENTS_FOLDER, nombre)  # Se une la carpeta de documentos con el nombre del archivo
        
        # Verifica si el archivo existe y si tiene la extensión .ipynb
        if os.path.exists(notebook_path) and nombre.endswith('.ipynb'):
            with open(notebook_path, 'r', encoding='utf-8') as f:
                # Lee el contenido del archivo .ipynb
                notebook_content = nbformat.read(f, as_version=4)  # Usa nbformat para leer el notebook y convertirlo a un formato estructurado

            contenido = []  # Inicializa la lista para almacenar las celdas del notebook

            # Recorre cada celda del notebook
            for cell in notebook_content.cells:
                if cell.cell_type == 'code':  # Si la celda es de tipo 'code' (código)
                    cell_data = {  # Crea un diccionario para almacenar los detalles de la celda de código
                        'tipo': 'código',
                        'contenido': cell.source,  # El código de la celda
                        'salidas': []  # Lista para almacenar las salidas de la celda
                    }

                    # Procesa las salidas de la celda de código
                    for output in cell.outputs:
                        if 'text' in output:  # Si la salida es texto
                            cell_data['salidas'].append({
                                'tipo': 'texto',
                                'contenido': output['text']  # Agrega el texto de la salida
                            })
                        elif 'data' in output:  # Si la salida tiene datos
                            # Procesa las diferentes posibles salidas de datos
                            if 'image/png' in output['data']:  # Si la salida es una imagen PNG
                                cell_data['salidas'].append({
                                    'tipo': 'imagen',
                                    'contenido': output['data']['image/png']  # Agrega la imagen
                                })
                            elif 'application/json' in output['data']:  # Si la salida es JSON
                                cell_data['salidas'].append({
                                    'tipo': 'json',
                                    'contenido': output['data']['application/json']  # Agrega el JSON
                                })
                            elif 'text/html' in output['data']:  # Si la salida es HTML
                                cell_data['salidas'].append({
                                    'tipo': 'html',
                                    'contenido': output['data']['text/html']  # Agrega el HTML
                                })
                    contenido.append(cell_data)  # Agrega la celda de código procesada a la lista de contenido
                
                elif cell.cell_type == 'markdown':  # Si la celda es de tipo 'markdown' (texto)
                    contenido.append({
                        'tipo': 'texto',
                        'contenido': cell.source  # Agrega el contenido markdown
                    })
            
            return jsonify(contenido), 200  # Devuelve el contenido del notebook en formato JSON con un código de éxito 200
        else:
            return jsonify({'mensaje': 'Archivo no encontrado o formato incorrecto'}), 404  # Si el archivo no existe o no tiene el formato correcto, devuelve un error 404
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500  # Si ocurre un error en el proceso, devuelve un mensaje de error con código 500

# Iniciar la aplicación en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo depuración para facilitar el desarrollo y la detección de errores
