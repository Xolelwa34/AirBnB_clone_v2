#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application.
Imports necessary modules, sets up routes,& handles application teardown.
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    This function handles the '/states_list' route.
    It fetches all the states, sorts them in alphabetical order,
    and renders them on a HTML page.
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    This function is called when the application context tears down.
    It closes the storage.
    """
    storage.close()

if __name__ == '__main__':
    """
    This block ensures the Flask application only runs if the script
    is executed directly. When the script is imported, nothing happens.
    """
    app.run(host='0.0.0.0', port='5000')
