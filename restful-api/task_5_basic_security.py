#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
jwt = JWTManager(app)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'super secret key'

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    return None

@app.route("/")
def home():
    """
    This function handles the root route of the Flask API.

    Returns:
        str: A welcome message for the Flask API.
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """
    Retrieves and returns the data from the 'users' dictionary as a JSON response.

    Returns:
        A JSON response containing the list of keys from the 'users' dictionary.
    """
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """
    Returns the status of the API.

    Returns:
        str: The status message "OK".
    """
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """
    Retrieve user information based on the provided username.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        If the user is found, returns a JSON response containing the user information.
        If the user is not found, returns a JSON response with an error message and a 404 status code.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST", "UPDATE", "DELETE"])
def add_user():
    """
    Add a new user to the system.

    Returns:
        A JSON response containing a success message and the user data if the user is added successfully.
        A JSON response containing an error message if the username is missing.
    """
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"error": "Missing username"}), 400
    if not password:
        return jsonify({"error": "Missing password"}), 400
    if verify_password(username, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "This is a protected endpoint"})

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "This is a protected endpoint"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user != 'admin':
        return jsonify({"error": "Unauthorized access"}), 403
    return jsonify({"message": "This is an admin-only endpoint"})

# Error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error():
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error():
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error():
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error():
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error():
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()