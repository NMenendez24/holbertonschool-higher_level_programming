#!/usr/bin/python3
"""Lists the values of a table"""


def select_states():
    """List all the states in the states table"""
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute(f"SELECT cities.name FROM cities WHERE state_id = \
                (SELECT states.id FROM states WHERE states.name =\
                '{argv[4]}');")
    rows = cur.fetchall()
    print(rows)
    for i in rows:
        print(i)
    db.close()