#!/usr/bin/python3
"""
*Script that lists all City objects from the database hbtn_0e_101_usa
*Script should take 3 arguments: mysql username,
 mysql password and database name
*Must use the module SQLAlchemy
*Script should connect to a MySQL server running on localhost at port 3306
*Must use only one query to the database
*Must use the state relationship to access to the State object
 linked to the City object
*Results must be sorted in ascending order by cities.id
*Results must be displayed as they are in the example below
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

    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
