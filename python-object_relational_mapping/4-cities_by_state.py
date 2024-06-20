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

    # Connect to MySQL server
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database
    )

cursor = db.cursor()
cursor.execute("SELECT cities.id, cities.name, states.name\
                FROM `cities`\
                JOIN `states`\
                ON cities.state_id = states.id\
                ORDER BY cities.id;")

cities = cursor.fetchall()
for city in cities:
    print(city)

cursor.close()
db.close()
