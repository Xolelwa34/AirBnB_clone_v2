#!/usr/bin/python3
"""
A script that starts a flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def handle_teardow(self):
    """ It removes the current session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_of_state():
    """ Func that displays list of all states"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
