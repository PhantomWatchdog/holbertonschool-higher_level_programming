#!/usr/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
            "john": {"name": "John", "age": 30, "city": "New York"}}
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def user(username):
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
            "john": {"name": "John", "age": 30, "city": "New York"}}
    user_data = users.get(username)
    if user_data:
        user_data["username"] = username
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"})


if __name__ == "__main__":
    app.run(port=5000)