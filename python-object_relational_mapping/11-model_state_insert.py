#!/usr/bin/python3
"""Fetch the columns of the states table"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Get the input arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name='Louisiana'))
    session.commit()
    state = session.query(State).filter(State.name == 'Louisiana').first()
    if state is not None:
        print(state.id)
