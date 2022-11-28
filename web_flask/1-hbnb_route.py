#!/usr/bin/python3
""" task 1

    Write a script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition
"""
from flask import Flask, request
from markupsafe import escape


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def task_0():
    return "Hello HBNB!"


@app.route('/hbnb')
def task_1():
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True)
