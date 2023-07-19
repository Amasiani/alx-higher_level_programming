#!/usr/bin/python3
"""
*Script that lists all State objects that contain the
 letter a from the database hbtn_0e_6_usa.
*Script should take 3 arguments: mysql username,
 mysql password and database name
*Must use the module SQLAlchemy
*Must import State and Base from model_state -
 from model_state import Base, State
*Mcript should connect to a MySQL server running on localhost at port 3306
*Results must be sorted in ascending order by states.id
*Results must be displayed as they are in the example below
*Code should not be executed when imported
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
