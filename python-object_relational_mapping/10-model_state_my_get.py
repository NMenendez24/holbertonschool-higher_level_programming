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
    state_name = sys.argv[4]

    # Create a connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password, db_name))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for the state with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # If the state is found, print its id
    if state is not None:
        print(state.id)
    else:
        print("Not found")
