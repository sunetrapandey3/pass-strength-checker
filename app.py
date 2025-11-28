from flask_cors import CORS

from flask import Flask, request, jsonify
from analyzer import analyze_password

app = Flask(__name__)

CORS(app)

@app.route("/check", methods=["POST"])
def check():
    data = request.json

    if not data or "password" not in data:
        return jsonify({"error": "Password missing"}), 400

    pwd = data["password"]
    result = analyze_password(pwd)
    return jsonify(result)

@app.route("/", methods=["GET"])
def home():
    return {"message": "Password Strength API is running!"}

if __name__ == "__main__":
    app.run(debug=True)
