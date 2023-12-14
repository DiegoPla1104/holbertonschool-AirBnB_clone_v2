#!/usr/bin/python3
"""Module"""
from flask import Flask
"""Create a Flask app instance"""
app = Flask(__name__)

"""Set the option to allow routes without trailing slashes"""
app.url_map.strict_slashes = False


"""Route establishment"""


@app.route("/")
def display_home():
    return "Hello HBNB!"


"""Route establishment"""


@app.route("/hbnb")
def display_hbnb():
    return "HBNB"


"""Route establishment"""


@app.route("/c/<text>")
def display_c(text):
    return f"C {text.replace('_', ' ')}"


"""Route establishment"""


@app.route("/python")
@app.route("/python/<text>")
def display_python(text='is_cool'):
    return f"Python {text.replace('_', ' ')}"


"""Run only if it's the main file"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
