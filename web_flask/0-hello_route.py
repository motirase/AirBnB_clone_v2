#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return "10-hbnb_filters.html"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
