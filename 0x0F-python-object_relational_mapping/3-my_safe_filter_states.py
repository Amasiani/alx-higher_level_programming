#!/usr/bin/python3

"""Script that takes in arguments and displays all values in the states
     table of hbtn_0e_0_usa where name matches the argument. But this time,
     write one that is safe from MySQL injections!

    * Script should take 4 arguments: mysql username, mysql password,
      database name and state name searched (safe from MySQL injection)
    * Must use the module MySQLdb (import MySQLdb)
    * Script should connect to a MySQL server running on localhost at
      port 3306
    * Results must be sorted in ascending order by states.id
    * Results must be displayed as they are in the example below
    * Code should not be executed when imported"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],                                     database=sys.argv[3], port=3306)
    control = db.cursor()
    query = "SELECT * FROM `states` WHERE name = %s"
    arg_value = sys.argv[4]
    control.execute(query, (arg_value, ))
    states = control.fetchall()
    for state in states:
        print(state)

    db_cursor.close()
    db.close()
