#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("""SELECT cities.name
                    FROM `cities`
                    JOIN `states`
                    ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC;""", (state_name,))

    cities = cursor.fetchall()
    print(", ".join([city[0] for city in cities]))

    cursor.close()
    db.close()
