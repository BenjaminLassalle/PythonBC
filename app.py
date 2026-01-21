from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'status': 'PythonBC API ready', 
        'endpoints': ['/run (POST)', '/health (GET)']
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/run', methods=['POST'])
def run():
    data = request.json or {}
    input_data = data.get('input', {})
    action = data.get('action', 'unknown')
    
    # TODO: Intégration INSEE/pandas
    result = f"Script exécuté: input={input_data}, action={action}"
    
    return jsonify({
        'status': 'success', 
        'result': result,
        'received': data
    })

if __name__ == '__main__':
    # Pour dev local uniquement
    app.run(host='0.0.0.0', port=5000)
