#!/usr/bin/python3
"""Fetch the columns of the states table"""

from sys import argv
from sqlalchemy import create_engine, text
from model_state import Base, State


def list_states():
    """Fetch the table and prints it"""
    eng = create_engine("mysql+mysqldb://{}:{}@localhost:3306\
                        /{}".format(argv[1], argv[2], argv[3]))
    connect = eng.connect()
    rows = connect.execute(text('SELECT id, name FROM states')
                           ).first()
    if rows is None:
        print("Nothing")
    else:
        print(f"{rows[0]}: {rows[1]}")


if __name__ == "__main__":
    list_states()
