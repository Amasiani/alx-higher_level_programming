#!/usr/bin/python3
"""
Lists all states with a name startin with N
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    
    control = db.cursor()
    control.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    states = control.fetchall()
    for state in states:
        print(state)
    control.close()
    db.close()
