import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
CORS(app)

# Database Connection using Render Environment Variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Table
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create table
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Backend with Database is LIVE!"

@app.route("/contact", methods=["POST"])
def contact():
    try:
        data = request.get_json()
        new_contact = Contact(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"status": "success", "message": "Message saved to database!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)