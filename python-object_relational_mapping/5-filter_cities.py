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
    cur.execute("SELECT cities.name FROM cities JOIN states ON states.id\
            = cities.state_id WHERE states.name = '{}'\
            ORDER BY cities.id ASC".format(argv[4]))
    rows = cur.fetchall()
    str_concat = ""
    number_states = 0
    for i in range(int(len(rows))):
        str_concat = str_concat + str(rows[i][0])
        number_states += 1
        if number_states <= len(rows):
            str_concat = str_concat + ", "
        number_states += 1
    print(str_concat)
    db.close()


if __name__ == "__main__":
    select_states()
