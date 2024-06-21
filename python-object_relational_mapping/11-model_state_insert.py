#!/usr/bin/python3
"""
Adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    # Create a new Engine instance.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables stored in this metadata.
    Base.metadata.create_all(engine)

    # create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new state
    new_state = State(name='Louisiana')

    # Add a new state to the database
    session.add(new_state)

    # Commit the session
    session.commit()

    # Print the new state id
    print(new_state.id)

    # Close the session
    session.close()
