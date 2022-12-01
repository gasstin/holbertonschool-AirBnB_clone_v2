#!/usr/bin/python3
"""Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage and storage.all
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
/states: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present
        in DBStorage sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
/states/<id>: display a HTML page: (inside the tag BODY)
    If a State object is found with this id:
    H1 tag: “State: ”
    H3 tag: “Cities:”
    UL tag: with the list of City objects linked
        to the State sorted by name (A->Z)
    LI tag: description of one City: <city.id>: <B><city.name></B>
Otherwise:
    H1 tag: “Not found!”
"""
from flask import Flask, request, render_template
from models import storage
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_function(exit):
    storage.close()


@app.route('/states')
def task_9_states():
    list_states = []
    for state in storage.all('State').values():
        list_states.append(state)
    return render_template("9-states.html", states_list=list_states)


@app.route('/states/<id>')
def task_9_cities(id):
    cities_list = []
    state_to_html = None
    for state in storage.all('State').values():
        if state.id == id:
            if getenv('HBNB_TYPE_STORAGE') == 'db':
                for city_db in state.cities:
                    cities_list.append(city_db)
            else:
                for city_fs in state.cities():
                    cities_list.append(city_fs)
            state_to_html = state
    return render_template("9-states.html", state_to_html=state_to_html,
                           cities_list=cities_list, id = id)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
