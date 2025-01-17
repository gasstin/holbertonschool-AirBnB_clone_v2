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
from models import storage
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_function(exit):
    storage.close()


@app.route('/cities_by_states')
def task_8():
    states_list = []
    cities_list = []
    for state in storage.all('State').values():
        states_list.append(state)
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            for city_db in state.cities:
                cities_list.append(city_db)
        else:
            for city_fs in state.cities():
                cities_list.append(city_fs)
    return render_template("8-cities_by_states.html", states_list=states_list,
                           cities_list=cities_list)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
