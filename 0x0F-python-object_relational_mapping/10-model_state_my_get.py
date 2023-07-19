#!/usr/bin/python3
"""
*Script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
*Script should take 4 arguments: mysql username, mysql password,
 database name and state name to search (SQL injection free)
*Must use the module SQLAlchemy
*Must import State and Base from model_state -
 from model_state import Base, State
*Script should connect to a MySQL server running on localhost at port 3306
*Can assume you have one record with the state name to search
*Results must display the states.id
*If no state has the name you searched for, display Not found
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

    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if found is False:
        print("Not found")