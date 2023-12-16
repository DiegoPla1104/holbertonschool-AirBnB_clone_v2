from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Method to remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    """Display a HTML page with a list of states"""
    storage_states = storage.all(State)
    sorted_states = sorted(storage_states.values(), key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
