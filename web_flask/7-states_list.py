#!/usr/bin/python3
"""Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage and storage.all
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
/states_list: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask, request, render_template
from markupsafe import escape
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_fun():
    storage.close()


@app.route('/states_list')
def task_7():
    list_states = []
    for coor in storage.all('State').values():
        list_states = list_states.append(coor)
    return render_template("7-states_list.html", list_states=list_states)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
