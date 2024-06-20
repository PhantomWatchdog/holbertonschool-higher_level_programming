#!/usr/bin/python3
"""
Protect from SQL Injection
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name\
                   LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)
