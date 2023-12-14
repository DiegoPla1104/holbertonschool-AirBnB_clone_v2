#!/usr/bin/python3
"""Module"""
from flask import Flask
"""Create a Flask app instance"""
app = Flask(__name__)

"""Set the option to allow routes without trailing slashes"""
strict_slashes = False


"""Route establishment"""


@app.route("/")
def display_home():
    return "Hello HBNB!"


"""Route establishment"""


@app.route("/hbnb")
def display_hbnb():
    return "HBNB"


"""Run only if it's the main file"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
