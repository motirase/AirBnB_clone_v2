#!/usr/bin/python3
"""
<<<<<<< HEAD
Script that starts a Flask web application
"""
from flask import Flask


=======
starts a Flask web application
"""

from flask import Flask
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
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
=======
def hbnb():
    """returns HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 8c5dbeed60929e24fc56e598218afe8c5214768b
