from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

# Definir la ruta absoluta al directorio "files"
MODEL_PATH = os.path.join(os.getcwd(), "files")

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/regresionLogistica", methods=["GET", "POST"])
def logistic_regresion():
    return render_template("regresionLogistica.html")




# Ruta para ejecutar los scripts
@app.route('/ejecutar/<script_name>')
def ejecutar(script_name):
    # Construir la ruta completa al script dentro del directorio "files"
    script_path = os.path.join(MODEL_PATH, script_name)
    
    # Verificar si el script existe y tiene extensión .py
    if os.path.exists(script_path) and script_path.endswith('.py'):
        try:
            # Ejecutar el script usando subprocess
            result = subprocess.run(['python', script_path], capture_output=True, text=True)
            return jsonify({'output': result.stdout, 'error': result.stderr})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Script no encontrado o inválido'}), 404






if __name__ == '__main__':
    app.run(debug=True)

