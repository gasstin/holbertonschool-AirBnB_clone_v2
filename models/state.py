#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db' or\
       getenv('HBNB_TYPE_STORAGE') == 'test':
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """ For FileStorage """
            from models.__init__ import storage
            cities = []
            for value_city in storage.all('City').values():
                if value_city.state_id == self.id:
                    cities.append(value_city)
            return cities
