#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    state = storage.all(State)
    city = storage.all(City)
    return render_template('9-states.html', states=state, cities=city)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """The method lists all State and all cities by State"""
    list_state = []
    my_dict_state = storage.all(State)
    for key, value in my_dict_state.items():
        if value.id == id:
            list_state.append(my_dict_state[key])
            break
    return render_template('9-states.html', states=list_state)


@app.teardown_appcontext
def tear_down(exception):
    """The method remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
