#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """The method display an HTML page"""
    list_state = []
    my_dict = storage.all(State)
    for key, value in my_dict.items():
        list_state.append(my_dict[key])
    list_sorted = sorted(list_state, key=lambda s: s.name)
    return render_template('7-states_list.html', list_state=list_sorted)


@app.teardown_appcontext
def tear_down(exception):
    """The method remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
