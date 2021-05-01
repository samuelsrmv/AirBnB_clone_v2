#!/usr/bin/python3
"""1-hbnb"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def function():
    """function"""
    return "¡Hola HBNB!"


@app.route("/hbnb")
def function2():
    """function2"""
    return ("HBNB")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
