#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="delete")

    @property
    def cities(self):
        """cities"""
        list_cities = []
        ciudades = models.storage.all(City)
        for key, value in ciudades.items():
            if value.state_id == self.id:
                list_cities.append(value)
        return list_cities
        

