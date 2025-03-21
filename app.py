from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import mysql.connector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Secret key for session handling
bcrypt = Bcrypt(app)

# Database Connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Faisal@1234",
    "database": "inventory_management"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, password FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and bcrypt.check_password_hash(user[1], password):
            session["user_id"] = user[0]
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401

    return render_template("login.html")

# Logout Route
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
