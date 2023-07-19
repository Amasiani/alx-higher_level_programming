#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Takes three argumrnts of user, password and database.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    control = db.cursor()
    control.execute("SELECT * FROM states order by states.id;")
    states = control.fetchall()
    for state in states:
        print(state)
    control.close()
    db.close()