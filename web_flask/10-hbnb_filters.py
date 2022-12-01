#!/usr/bin/python3
"""Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage
        and storage.all(...)
To load all cities of a State:
If your storage engine is DBStorage, you must use cities relationship
Otherwise, use the public getter method cities
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()

Routes:
/hbnb_filters: display a HTML page like 6-index.html,
    which was done during the project 0x01. AirBnB clone - Web static
"""
from flask import Flask, render_template
from models import storage
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_function(exit):
    storage.close()


@app.route('/hbnb_filters')
def task_10():
    cities_list = []
    for state in storage.all('State').values():
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            for city_db in state.cities:
                cities_list.append(city_db)
        else:
            for city_fs in state.cities():
                cities_list.append(city_fs)
    return render_template("10-hbnb_filters.html",
                           state_list=storage.all('State').values(),
                           cities_list=cities_list,
                           amenities_list=storage.all('Amenity').values())


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
