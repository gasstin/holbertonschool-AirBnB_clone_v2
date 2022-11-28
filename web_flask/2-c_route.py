#!/usr/bin/python3
""" task 2

    Write a script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
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


@app.route('/c/<text>')
def task_2(text):
    text = text.replace("_", " ")
    return f"C {escape(text)}"


if __name__ == '__main__':
    app.run(debug=True)
