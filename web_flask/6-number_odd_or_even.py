#!/usr/bin/python3
from flask import Flask, render_template
"""scipt that imports web application flask, render_template method"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays text
    Returns:
        HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """displays text
    Returns:
        HBNB
    """
    return " Hello HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """displays text
    Args:
        text (str): text
    Returns:
        HBNB
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """displays text
    Args:
        text (str): text
    Returns:
        HBNB
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    """displays text
    Args:
        n (int): number
    Returns:
        string
    """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_HTML(n):
    """displays text
    Args:
        n (int): number
    Returns:
        HTML page
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    '''
    /number_odd_or_even/<n> route
    '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
