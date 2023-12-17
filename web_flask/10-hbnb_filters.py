#!/usr/bin/python3
"""Module"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_lists():
    """State list"""
    sstates = storage.all(State)
    return render_template("7-states_list.html", states=sstates)


@app.route('/cities_by_states', strict_slashes=False)
def display_states():
    """Display a HTML page"""
    storage_states = storage.all(State)
    return render_template('8-cities_by_states.html', states=storage_states)


@app.route('/states/<id>', strict_slashes=False)
def display_cities(id):
    """Display a HTML page"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """Displays the filters in HTML page"""
    sstates = storage.all(State)
    samenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=sstates, amenities=samenities)


@app.teardown_appcontext
def teardown(self):
    """Method to remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
