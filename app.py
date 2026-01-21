from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify({'status': 'PythonBC API ready', 'endpoints': '/run (POST), /health'})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/run', methods=['POST'])
def run():
    data = request.json.get('input', {})
    # TODO: votre script (INSEE, Zoho, pandas...)
    result = f"Script exécuté: input={data}"
    return jsonify({'status': 'success', 'result': result})
