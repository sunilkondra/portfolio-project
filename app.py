from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# --- Database Section (Temporary ga disable chesam Render success kosam) ---
# import mysql.connector
# db = mysql.connector.connect(
#    host="localhost",
#    user="root",
#    password="",
#    database="portfolio_db"
# )
# cursor = db.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS contacts (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100),
#     message TEXT
# )
# """)
# -------------------------------------------------------------------------

@app.route("/")
def home():
    return "Backend is working! Portfolio live ki ready."

@app.route("/contact", methods=["POST"])
def contact():
    try:
        data = request.get_json()
        
        # Database ledhu kabatti, just logs lo data chustham
        print(f"New Contact Request: {data}")
        
        # Future lo DB connect chesinappudu ee kindha lines enable cheyali
        # sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
        # values = (data.get("name"), data.get("email"), data.get("message"))
        # cursor.execute(sql, values)
        # db.commit()

        return jsonify({"status": "success", "message": "Data received successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if _name_ == "_main_":
    # Render lo port 10000 standard, adhe unchutunnanu
    app.run(host="0.0.0.0", port=10000)