#!/usr/bin/python3 
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

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

@app.route("/add_user", methods=["POST"])
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

if __name__ == "__main__":
    app.run()