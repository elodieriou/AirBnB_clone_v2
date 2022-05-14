#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """The method list all cities of a State"""
    list_state = storage.all(State).values()
    return render_template('8-cities_by_states.html',
                           list_states=list_state)


@app.teardown_appcontext
def tear_down(exception):
    """The method remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
