from flask import Flask, jsonify
import json

app3 = Flask(__name__)

# Cargar los datos desde el archivo JSON
def cargar_datos():
    try:
        with open('datos.json', 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []  # Si el archivo no existe, devolver una lista vacía

@app3.route('/<int:municipioid>/demo', methods=['GET'])
def get_geo(municipioid):
     try:
         # Abrimos el archivo JSON donde están los datos del municipio
         with open('municipio.json') as f:
             data = json.load(f)

         # Buscamos el municipio por su ID
         if data.get('municipioid') == municipioid:
             return jsonify(data), 200  # Municipio encontrado, retornamos 200 OK
         else:
             return jsonify({'error': 'Municipio no encontrado'}), 404  # Municipio no encontrado
     except FileNotFoundError:
         return jsonify({'error': 'Archivo JSON no encontrado'}), 500  # Error si el archivo no existe

if __name__ == '__main__':
    app3.run(port=5002)