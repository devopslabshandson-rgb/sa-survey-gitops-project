from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = []

@app.route("/save", methods=["POST"])
def save():
    data_store.append(request.json)
    return jsonify({"status": "saved"})

@app.route("/data", methods=["GET"])
def data():
    return jsonify(data_store)

app.run(host="0.0.0.0", port=5000)
