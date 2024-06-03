#!/usr/bin/python3
"""
A script that starts a Flask web application to display a list of states.
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Renders an HTML page with the states listed in alphabetical order.
    
    Retrieves all State objects from storage, sorts them by name,
    and passes them to the template for rendering.
    
    Returns:
        str: The rendered HTML template for the states list.
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage when the app context tears down.
    
    This function is called automatically when the app context is 
    being torn down. It ensures that the storage is properly closed.
    
    Args:
        exception (Exception): The exception that caused the teardown, if any.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
