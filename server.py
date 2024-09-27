from flask import Flask, jsonify, request
from src.probabilities import calculateDamage, calculateDrop

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

# Ruta POST para calcular el daño de un héroe
@app.route('/api/calculate/damage', methods=['POST'])
def damage():
    hero = request.get_json()
    return jsonify(calculateDamage(hero)), 201

# Ruta POST para calcular el drop de un producto
@app.route('/api/calculate/drop', methods=['POST'])
def drop():
    products = request.get_json().get('products', [])
    return jsonify(calculateDrop(products)), 201

if __name__ == '__main__':
    # Cambiar la IP y el puerto
    app.run(host='127.0.0.1', port=5000, debug=True)
