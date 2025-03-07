from flask import Flask, jsonify
import requests

app4 = Flask(__name__)

# URLs de los otros servicios
SERVICES = {
    "geo": "http://Host.docker.internal:5000/{}",
    "meteo": "http://Host.docker.internal:5001/{}",
    "demo": "http://Host.docker.internal:5002/{}"
}

@app4.route('/<int:municipioid>/<parametro1>/<parametro2>', methods=['GET'])
def get_combined(municipioid, parametro1, parametro2):
    
    response_data = {}
    parametros = [parametro1, parametro2]
    
    for param in parametros:
        if param in SERVICES:
            url = SERVICES[param].format(f"{municipioid}/{param}")
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    response_data[param] = response.json()
                else:
                    response_data[param] = {"error": f"Servicio {param} no disponible"}
            except requests.exceptions.RequestException:
                response_data[param] = {"error": f"Error al conectar con {param}"}
        else:
            response_data[param] = {"error": "Parámetro no reconocido"}
    
    return jsonify(response_data)

if __name__ == '__main__':
    app4.run(host='0.0.0.0', port=5003)
