#!/usr/bin/python3

"""Lists all states with a name starting with N (upper N)
   from database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    control = db.cursor()
    control.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY id")
    states = control.fetchall()
    for state in states:
        print(state)

    control.close()
    db.close()
