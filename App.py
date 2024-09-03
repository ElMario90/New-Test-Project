from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_numbers():
    data = request.get_json()
    if not isinstance(data, list) or not all(isinstance(i, int) for i in data):
        return jsonify({"error": "Invalid input"}), 400
    result = sum(data)  # Example processing: summing up the numbers
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)  # Adjust port if needed
