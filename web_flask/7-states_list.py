#!/usr/bin/python3
"""
A script that starts a Flask web application to display a list of states.
This application connects to a database to retrieve state information,
sorts the states alphabetically, and renders them in an HTML template.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Handles the route for /states_list.
    
    This function retrieves all State objects from the database, sorts them
    by their name, and renders them in an HTML template.
    
    Returns:
        str: The rendered HTML template displaying the states in alphabetical order.
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the database storage when the app context is torn down.
    
    This function ensures that the storage is properly closed after the 
    application context ends, helping to manage resources efficiently.
    
    Args:
        exception (Exception): The exception that caused the teardown, if any.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
