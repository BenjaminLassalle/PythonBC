from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run():
    data = request.json.get('input', {})
    result = f"Exécuté pour {data}"
    return jsonify({'status': 'success', 'result': result})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})
