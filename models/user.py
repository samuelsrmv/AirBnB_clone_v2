#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
<<<<<<< HEAD
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    reviews = relationship('Review', cascade='all, delete', backref='user'))
=======
    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128), nullable=True)
    last_name = Column('last_name', String(128), nullable=True)
>>>>>>> 4033205a7fd1dbd8e06b7c446bc3899a8f4cc48a
