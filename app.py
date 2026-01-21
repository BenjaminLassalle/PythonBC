from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run():
    data = request.json.get('input', {})
    # Votre script Python ici, ex: result = data['siren'] * 2
    return jsonify({'result': 'Exécuté OK'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
