#!/usr/bin/python3
"""
task 3: Write a script that starts a Flask web application
"""
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def task_0():
    """
    Returns Hello HBNB for the '/' url
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def task_1():
    """
    Returns HBNB for the /hbnb route
    """
    return "HBNB"


@app.route('/c/<text>')
def task_2(text):
    """
    display “C ” followed by the value of
    the text variable (replace underscore _ symbols with a space )

    text: is the text to print
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def task_3(text):
    """
    display “Python ”, followed by the value
    of the text variable (replace underscore _ symbols with a space )
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
