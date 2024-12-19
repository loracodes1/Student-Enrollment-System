from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)


class Courses
