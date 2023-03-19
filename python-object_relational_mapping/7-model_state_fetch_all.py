#!/usr/bin/python3
""""""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State


def list_states():
    eng = create_engine("mysql+mysqldb://{}:{}@localhost:3306\
                        /{}".format(argv[1], argv[2], argv[3]),
                        pool_pre_ping=True)
    connect = eng.connect()
    rows = connect.execute('SELECT * FROM states')
    print(rows)
