from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

# Set base
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True)
    email = Column(String, unique = True)
    first_name = Column(String)
    last_name = Column(String)
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"{self.id} | {self.email} | {self.first_name} | {self.last_name}"


class Course(Base):
    __tablename__ = "courses"

    id=Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"{self.id} | {self.code} | {self.name}"
    
class Enrolment(Base):
    __tablename__ = "enrolments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    enrolled_on = Column(DateTime, server_default = func.now())
    unenrolled_on = Column(DateTime, nullable=True)
    student = relationship("Student", back_populates="enrolments")
    course = relationship("Course", back_populates="enrolments")

    def __repr__(self):
        return f"{self.id} | {self.enrolled_on} | {self.unenrolled_on} |  ({self.student}) | ({self.course})"

# Relationship
Student.enrolments = relationship("Enrolment", order_by = Enrolment.enrolled_on, back_populates = "student")
Course.enrolments = relationship("Enrolment", order_by = Enrolment.enrolled_on, back_populates = "course")

# DB related
db = create_engine('sqlite:///db/system.db', echo = True)
Session = sessionmaker(bind = db)
