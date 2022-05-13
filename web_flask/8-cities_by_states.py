#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """The method lists all State"""
    list_state = []
    my_dict = storage.all(State)
    for key, value in my_dict.items():
        list_state.append(my_dict[key])
    return render_template('7-states_list.html', list_state=list_state)


@app.teardown_appcontext
def tear_down(exception):
    """The method remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """The method list all cities of a State"""
    list_state = storage.all(State)
    list_city = storage.all(City)
    return render_template('8-cities_by_states.html',
                           states=list_state, cities=list_city)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
