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
    value = str(argv[4].split(';')[0])
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'".format
                (value))
    rows = cur.fetchall()
    for i in rows:
        if i[1][0].isupper():
            print(i)
    db.close()


if __name__ == "__main__":
    select_states()
