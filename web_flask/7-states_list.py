#!/usr/bin/python3
"""Module"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """State list"""
    sstate = storage.all(State)
    return render_template("7-states_list.html", states=sstate)


@app.teardown_appcontext
def teardown(self):
    """Method teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True, strict_slashes=False)
