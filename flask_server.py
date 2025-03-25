from flask import Flask, request, jsonify
from app import chat
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat_route():
    data = request.json
    response = chat(data['query'])
    return jsonify({"message": response})

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')