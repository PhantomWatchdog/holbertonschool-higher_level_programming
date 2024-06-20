#!/usr/bin/python3
"""
Protect from SQL Injection
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
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
