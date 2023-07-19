#!/usr/bin/python3
"""
*Script that deletes all State objects with a name
 containing the letter a from the database hbtn_0e_6_usa
*Script should take 3 arguments: mysql username,
 mysql password and database name
*Must use the module SQLAlchemy
*Must import State and Base from model_state -
 from model_state import Base, State
*Script should connect to a MySQL server running on localhost at port 3306
*code should not be executed when imported
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    session.commit()
