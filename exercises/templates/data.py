from model import Base, Vote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///votes.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_survey_info(person_name, person_animal):
    vote_object = Vote(name=person_name, animal=person_animal)
    session.add(vote_object)
    session.commit()

def get_all_survey_info():
    all_info = session.query(Vote).all()
    return all_info