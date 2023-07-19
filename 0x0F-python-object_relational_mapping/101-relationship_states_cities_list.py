#!/usr/bin/python3
"""
*Script that lists all State objects, and corresponding
 City objects, contained in the database hbtn_0e_101_usa
*Script should take 3 arguments: mysql username,
 mysql password and database name
*Must use the module SQLAlchemy
*Connection to your MySQL server must be to localhost on port 3306
*Must only use one query to the database
*Must use the cities relationship for all State objects
*Must be sorted in ascending order by states.id and cities.id
*Must be displayed as they are in the example below
*Code should not be executed when imported
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
