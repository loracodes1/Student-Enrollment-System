from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# Set base
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)

class Courses(Base):
    __tablename__ = "courses"

    id=Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    
class Enrolment(Base):
    __tablename__ = "enrolments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    enrolled_on = Column(DateTime, server_default = func.now())
    unenrolled_on = Column(DateTime, nullable=True)
    student = relationship("Student", back_populates="enrolments")
    course = relationship("Course", back_populates="enrolments")

Student.enrolment = relationship("Enrolment", order_by = Enrolment.enrolled_on, back_populates = "student")
Courses.enrolment = relationship("Enrolment", order_by = Enrolment.enrolled_on, back_populates = "course")

