#!/usr/bin/python3
"""
A script that starts a web flask application
"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Render states and their cities in order of their names"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the database connection when the app context is torn down"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
