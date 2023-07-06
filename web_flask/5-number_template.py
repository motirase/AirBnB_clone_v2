#!/usr/bin/python3
"""
<<<<<<< HEAD
Script that starts a Flask web application
"""
from flask import Flask, render_template


=======
starts a Flask web application
"""

from flask import Flask, render_template
>>>>>>> 8c5dbeed60929e24fc56e598218afe8c5214768b
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello():
=======
def index():
    """returns Hello HBNB!"""
>>>>>>> 8c5dbeed60929e24fc56e598218afe8c5214768b
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
<<<<<<< HEAD
def holberon():
=======
def hbnb():
    """returns HBNB"""
>>>>>>> 8c5dbeed60929e24fc56e598218afe8c5214768b
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
<<<<<<< HEAD
def c_text(text):
    return "C {}" .format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Function called with /python/<text> route """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """ display a HTML page only if n is an integer """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
=======
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 8c5dbeed60929e24fc56e598218afe8c5214768b
