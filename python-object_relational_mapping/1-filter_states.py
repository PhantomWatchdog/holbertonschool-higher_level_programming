#!/usr/bin/python3

import MySQLdb
import sys

def main():
    """
    Lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
    """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
