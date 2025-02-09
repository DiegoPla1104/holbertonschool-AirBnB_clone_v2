#!/usr/bin/python3
"""Module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_states():
    """Display a HTML page with a list of states"""
    storage_states = storage.all(State)

    return render_template('8-cities_by_states.html', states=storage_states)


@app.teardown_appcontext
def teardown(exception):
    """Method to remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
