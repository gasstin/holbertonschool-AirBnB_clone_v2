#!/usr/bin/python3
"""
task 6: Write a script that starts a Flask web application
"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>')
def task_4(n):
    """
    /number/<n>: display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def task_5(n):
    """
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def task_6(n):
    """
    /number_template/<n>: display a HTML page only if n is an integer:
        “Number: n is even|odd” inside the tag BODY
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
