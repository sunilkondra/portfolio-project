from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="portfolio_db"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    message TEXT
)
""")

@app.route("/")
def home():
    return "Backend is working!"

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
    values = (name, email, message)

    cursor.execute(sql, values)
    db.commit()

    return jsonify({"message": "Data saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True)