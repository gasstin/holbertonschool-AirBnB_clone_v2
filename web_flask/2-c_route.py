#!/usr/bin/python3
""" task 2
"""
from flask import Flask, request
from markupsafe import escape


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def task_0():
    """
        task 0
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def task_1():
    """
        task 1
    """
    return "HBNB"


@app.route('/c/<text>')
def task_2(text):
    """
        /c/<text>: display “C ” followed by the value of
        the text variable (replace underscore _ symbols with a space )
    """
    text = text.replace("_", " ")
    return f"C {escape(text)}"


if __name__ == '__main__':
    app.run(debug=True)
