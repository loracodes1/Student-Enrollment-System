from db.models import Base, db, Session, Course, Student, Enrolment
from helpers import get_input

# Migrate DB
print("Migration started....")
Base.metadata.create_all(db)
print("Migration complete")

def list_courses():
    session = Session()
    courses = session.query(Course).all()

    if len(courses) == 0:
        print("No courses found")
        return
    
    print("-" * 100)
    print("ID | CODE | NAME")
    print("-" * 50)
    for course in courses:
        print(course)

    print("-" * 100)

def list_students():
    session = Session()
    students = session.query(Student).all()

    if len(students) == 0:
        print("No students found")
        return
    
    print("-" * 100)
    print("ID | EMAIL | FIRST_NAME | LAST_NAME")
    print("-" * 50)
    for student in students:
        print(student)

    print("-" * 100)

def add_new_course():
    session = Session()
    students = session.query(Student).all()

    if len(students) == 0:
        print("No students found")
        return
    
    print("-" * 100)
    print("ID | EMAIL | FIRST_NAME | LAST_NAME")
    print("-" * 50)
    for student in students:
        print(student)

    print("-" * 100)

def add_new_student():
    session = Session()
    students = session.query(Student).all()

    if len(students) == 0:
        print("No students found")
        return
    
    print("-" * 100)
    print("ID | EMAIL | FIRST_NAME | LAST_NAME")
    print("-" * 50)
    for student in students:
        print(student)

    print("-" * 100)


# Main entry point to our app
def main():
    print("/" * 50)
    print("Welcome to student enrollment system".upper())
    print("/" * 50)

    while True:
        # What does the  user want to do
        print("/" * 50)
        print("What do you want to do?")
        print("1. List all courses")
        print("2. List all students")
        print("3. Add new course")
        print("4. Add new student")
        print("5. Enrol student to course")
        print("6. Un-enrol student from course")
        print("7. Print student report")
        print("8. Print course report")
        print("0. Exit")
        print("/" * 50)
        
        choice = get_input("Choice: ", "int")
        
        if choice == 0:
            break

        if choice is None:
            print("Invalid choice try again")
            continue

        if choice == 1:
            list_courses()
            continue

        if choice == 2:
            list_students()
            continue

        if choice == 3:
            add_new_course()
            continue

        if choice == 4:
            add_new_student()
            continue
        
        # Enf of prompts
        if choice is None:
            print("Invalid choice try again")


if __name__ == "__main__":
    main()