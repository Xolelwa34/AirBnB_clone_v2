#!/usr/bin/python3
"""starts a web flask application"""
from flask import Flask
"""class Flask"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays text
    Returns:
        text
    """
    return "Hello HBNB!"


@app.route('/airbnb-onepage/', strict_slashes=False)
def airbnb_onepage():
    """
    Displays a welcome message for the Airbnb one page.

    Returns:
        str: The text "Welcome to the Airbnb One Page!".
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
