#!/usr/bin/python3
"""0-hello_route"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
app.url_map.strict_slashes = False

def function():
    """function"""
    return "¡Hola HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
