#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, ordered by cities.
*Script should take 3 arguments: mysql username, mysql password and
 database name.
*Must use the module MySQLdb (import MySQLdb).
*Script should connect to a MySQL server running on localhost at port 3306.
*Must be sorted in ascending order by cities.id
*Can use only execute() once
*Results must be displayed as they are in the example below
*Code should not be executed when imported
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    control = db.cursor()
    control.execute("SELECT `city`.`id`, `city`.`name`, `state`.`name` \
                 FROM `cities` as `city` \
                INNER JOIN `states` as `state` \
                   ON `city`.`state_id` = `state`.`id` \
                ORDER BY `city`.`id`")
    [print(city) for city in control.fetchall()]
