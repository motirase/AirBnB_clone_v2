#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
=======
"""Defines the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
>>>>>>> 8c5dbeed60929e24fc56e598218afe8c5214768b
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
<<<<<<< HEAD
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

=======
    """Represents a user for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table users.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy relationship): The User-Place relationship.
        reviews (sqlalchemy relationship): The User-Review relationship.
    """
    __tablename__ = "users"
>>>>>>> 8c5dbeed60929e24fc56e598218afe8c5214768b
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
<<<<<<< HEAD
    places = relationship('Place', backref='user', cascade='delete')
    reviews = relationship('Review', backref='user', cascade='delete')

=======
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
>>>>>>> 8c5dbeed60929e24fc56e598218afe8c5214768b
