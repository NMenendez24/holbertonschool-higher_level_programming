#!/usr/bin/python3
"""Define a Base class """


import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Define a State class"""
    id = sqla.Column(sqla.Integer, primary_key=True, nullable=False)
    name = sqla.Column(sqla.String(128), nullable=False)


if __name__ == "__main__":
    pass
