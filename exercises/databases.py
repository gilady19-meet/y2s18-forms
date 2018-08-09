from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_student(name, year):
	student_object = Student(
		name=name,
		year=year)
		#finished_lab=finished_lab)
	session.add(student_object)
	session.commit()

def query_by_name(name):
	student = session.query(Student).filter_by(
		name=name).first()
	return student

def query_all():
	students = session.query(Student).all()
	return students

def delete_student(name):
	session.query(Student).filter_by(
		name=name).delete()
	session.commit()

def update_lab_status(name, finished_lab):
	student_object = session.query(Student).filter_by(
		name=name).first()
	student_object.finished_lab = finished_lab
	session.commit()

def query_by_id(student_id):
    student = session.query(Student).filter_by(
        student_id=student_id).first()
    return student