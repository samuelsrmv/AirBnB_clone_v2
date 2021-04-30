#!/usr/bin/python3
"""1-hbnb"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
app.url_map.strict_slashes = False

def function():
    """function"""
    return "¡Hola HBNB!"

@app.route("/hbnb")
app.url_map.strict_slashes = False

def function2():
    """function2"""
    return "HBNB"

@app.route("/c/<text>")
app.url_map.strict_slashes = False

def function3(text):
    """function2"""
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
