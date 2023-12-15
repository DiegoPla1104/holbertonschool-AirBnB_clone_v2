#!/usr/bin/python3
"""
module script that starts Flask
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states')
def display_states():
    """
    display a HTML page
    list of all states and related cities
    """
    storage_states = storage.all(State)
    return render_template('8-cities_by_states.html', states=storage_states)


@app.teardown_appcontext
def teardown(self):
    """Method teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, strict_slashes=False)
