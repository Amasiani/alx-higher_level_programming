#!/usr/bin/python3

"""
*Improve the files model_city.py and model_state.py, and save
 them as relationship_city.py and relationship_state.py:
*City class:
 No change
*State class:
 In addition to previous requirements, the class attribute cities
 must represent a relationship with the class City.
 If the State object is deleted, all linked City objects must be
 automatically deleted.
 Also, the reference from a City object to his State should be named state
*Must use the module SQLAlchemy
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.
    Attributes:
        id (sqlalchemy.Column): The city's id.
        name (sqlalchemy.Column): The city's name.
        state_id (sqlalchemy.Column): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
