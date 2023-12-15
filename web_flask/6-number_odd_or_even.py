#!/usr/bin/python3
"""Module"""
from flask import Flask, abort, render_template
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


@app.route("/number/<n>")
def display_number(n):
    if n.isdigit():
        return (f"{n} is a number")
    else:
        abort(404)


@app.route("/number_template/<n>")
def display_number_template(n):
    if n.isdigit():
        return render_template("5-number.html", num=n)
    else:
        abort(404)


@app.route("/number_odd_or_even/<n>")
def display_number_temp_and_type(n):
    if n.isdigit():
        n = int(n)
        typ = 0
        if n % 2 == 0:
            typ = "even"
            return render_template("6-number_odd_or_even.html", num=n, type=typ)
        else:
            typ = "odd"
            return render_template("6-number_odd_or_even.html", num=n, type=typ)
    else:
        abort(404)


"""Run only if it's the main file"""


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
