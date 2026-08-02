#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    session.query(State).filter(
        State.name.like('%a%')).delete(synchronize_session=False)
    session.commit()
    session.close()
