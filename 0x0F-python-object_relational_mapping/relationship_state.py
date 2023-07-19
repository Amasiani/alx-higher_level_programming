#!/usr/bin/python3
"""
*State class:
 In addition to previous requirements, the class attribute
 cities must represent a relationship with the class City.
 If the State object is deleted, all linked City objects must be
 automatically deleted.
 Also, the reference from a City object to his State should be named state
*Must use the module SQLAlchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """Represents a state for a MySQL database.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state's name.
        cities (sqlalchemy.orm.relationship): The State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
