#!/usr/bin/python3
"""
Lists all values in the states tables of database hbtn_0e_0_usa
where name matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    control = db.cursor()
    control.execute("SELECT * \
                    FROM states \
                    WHERE CONVERT(`name` USING Latin1) \
                    COLLATE Latin1_General_CS = '{}' \
                    ORDER BY states.id;".format(sys.argv[4]))
    states = control.fetchall()
    for state in states:
        print(state)
    control.close()
    db.close()
