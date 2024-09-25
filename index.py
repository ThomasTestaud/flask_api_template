from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)




@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "pong"})





@app.route('/post', methods=['POST'])
def get_new_settings():
    return jsonify({"status": "pong"})



if __name__ == '__main__':
    app.run(debug=True)
