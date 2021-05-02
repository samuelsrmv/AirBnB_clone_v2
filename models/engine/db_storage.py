#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import MySQLdb
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.base_model import BaseModel, Base
import os
from sqlalchemy.engine import create_engine
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """__init__"""
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, password, host, database), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        result = {}
        if cls in classes:
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                result[key] = obj
        elif cls is None:
            for clas in classes:
                query = self.__session.query(classes[clas]).all()
                for obj in query:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """new"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        X = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(X)
        self.__session = Session()

    def close(self):
        """close"""
        self.__session.remove()