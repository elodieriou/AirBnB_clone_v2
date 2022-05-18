#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """The method lists States, Cities and Amenities"""
    list_state = storage.all(State).values()
    list_city = storage.all(City).values()
    list_amenity = storage.all(Amenity).values()
    list_place = storage.all(Place).values()
    return render_template('100-hbnb.html',
                           list_state=list_state,
                           list_city=list_city,
                           list_amenity=list_amenity,
                           list_place=list_place)


@app.teardown_appcontext
def tear_down(exception):
    """The method remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
