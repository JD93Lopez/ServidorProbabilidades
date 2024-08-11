from flask import Flask, jsonify, request
from probabilities import indiceAleatorio, generarRandom

app = Flask(__name__)

# Ruta de ejemplo para una API GET
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# Ruta de ejemplo para una API POST
@app.route('/api/data', methods=['POST'])
def data():
    data = request.get_json()
    print(data)
    return jsonify({"received": data}), 201

if __name__ == '__main__':
    # Cambiar la IP y el puerto
    app.run(host='127.0.0.1', port=5000, debug=True)
