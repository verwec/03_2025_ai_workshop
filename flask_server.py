from flask import Flask, request, jsonify
from app import chat

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat_route():
    data = request.json
    response = chat(data['query'])
    return jsonify({"message": response})

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')