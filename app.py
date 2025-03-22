from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Serve the login page
@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

# Fake Login API (No MySQL, Just Testing Connection)
@app.route("/login", methods=["POST"])
def fake_login():
    data = request.form
    email = data.get("email")
    password = data.get("password")

    # Simulate login logic (No database, just returning a response)
    if email == "test@example.com" and password == "password123":
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
