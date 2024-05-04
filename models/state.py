#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """Represents a state for a MySQL database."""
    __tablename__ = "states"

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """
            Returns a list of city instances with state_id that equals
            to the current state.id
            -> it will be the FileStorage relationship between
            State & City
            """
            from models import storage
            from models.city import City
            """ Returns list of City objs in __objects """
            cities_dict = storage.all(City)
            cities_list = []

            """ Copy values from dict to list """
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)

            return cities_list
