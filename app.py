from flask import Flask, request, jsonify
from flask_cors import CORS

# Ikkada _name_ (double underscore) undali
app = Flask(_name_)
CORS(app)

@app.route("/")
def home():
    return "Backend is working! Portfolio live ki ready."

@app.route("/contact", methods=["POST"])
def contact():
    try:
        data = request.get_json()
        print(f"New Contact Request: {data}")
        return jsonify({"status": "success", "message": "Data received successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Ikkada kuda _name_ mariyu _main_ undali
if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)