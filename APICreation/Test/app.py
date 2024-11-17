from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para ejecutar los scripts
@app.route('/ejecutar/<script_name>')
def ejecutar(script_name):
    script_path = os.path.join('files', script_name)
    if os.path.exists(script_path) and script_path.endswith('.py'):
        try:
            # Ejecutamos el script en el servidor
            result = subprocess.run(['python', script_path], capture_output=True, text=True)
            return jsonify({'output': result.stdout, 'error': result.stderr})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Script no encontrado o inválido'}), 404

if __name__ == '__main__':
    app.run(debug=True)
