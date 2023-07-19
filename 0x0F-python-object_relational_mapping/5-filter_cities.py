#!/usr/bin/python3
"""
*Script that takes in the name of a state as an argument and lists all
 cities of that state, using the database hbtn_0e_4_usa.
*Script take 4 arguments: mysql username, mysql password,
 database name and state name (SQL injection free!).
*Use the module MySQLdb (import MySQLdb).
*Script connect to a MySQL server running on localhost at port 3306
*Results  sorted in ascending order by cities.id
*Use execute() once.
*Results displayed as they are in the example below
*Ccode should not be executed when imported
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `city` \
                INNER JOIN `states` as `state` \
                   ON `city`.`state_id` = `state`.`id` \
                ORDER BY `city`.`id`")
    print(", ".join([cy[2] for cy in c.fetchall() if cy[4] == sys.argv[4]]))
