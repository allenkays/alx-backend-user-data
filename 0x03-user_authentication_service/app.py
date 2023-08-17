#!/usr/bin/env python3
"""
Simple flask app implementation
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def welcome():
    """defines a root path"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
