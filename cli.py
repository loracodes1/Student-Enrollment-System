from db.models import Base, db, Session, Course, Student, execute_sql, time_now
from helpers import get_input
from validator import Validator, validate, rules as R

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
    
    code = get_input("Enter course code: ").upper()
    name = None

    course = session.query(Course).filter_by(code = code).first()

    if course is not None:
        print(f"Course with the code '{code}' already exists, do you want to update it?")
        
        choice = get_input("Y/N: ").upper()

        if choice == "N" or (choice != "Y" and choice != "N"):
            return
        
        name = get_input("Enter course name leave blank to skip: ").capitalize()
    else:
        name = get_input("Enter course name: ").capitalize()

    data = {
        "code": code,
        "name": name
    }

    if course is None:
        rules =  {
            "code": ["required", "min:1", "max:10"],
            "name": ["required", "min:1", "max:50"]
        }
    else:
        rules =  {
            "code": ["required", "min:1", "max:10"],
        }

        if name != "":
            rules["name"] = ["required", "min:1", "max:50"]


    result, _, errors = validate(data, rules, True)

    #  If failed validation 
    if not result:
        print("Error during validation")

        for dict_key in data.keys():
            if dict_key in errors:
                print(f"{dict_key}: ", errors[dict_key].values())

        return
    
    try:
        if course is None:
            # Add
            course = Course(code = data["code"], name = data["name"])
            session.add(course)
        else:
            # Update
            if name != "":
                course.name = data["name"]
                

        session.commit()
        print("Course added/updated successfully")
    except Exception as e:
        print("Error adding/updating course ", e)

def add_new_student():
    session = Session()
    
    code = get_input("Enter course code: ").upper()
    name = None

    course = session.query(Course).filter_by(code = code).first()

    if course is not None:
        print(f"Course with the code '{code}' already exists, do you want to update it?")
        
        choice = get_input("Y/N: ").upper()

        if choice == "N" or (choice != "Y" and choice != "N"):
            return
        
        name = get_input("Enter course name leave blank to skip: ").capitalize()
    else:
        name = get_input("Enter course name: ").capitalize()

    data = {
        "code": code,
        "name": name
    }

    if course is None:
        rules =  {
            "code": ["required", "min:1", "max:10"],
            "name": ["required", "min:1", "max:50"]
        }
    else:
        rules =  {
            "code": ["required", "min:1", "max:10"],
        }

        if name != "":
            rules["name"] = ["required", "min:1", "max:50"]


    result, _, errors = validate(data, rules, True)

    #  If failed validation 
    if not result:
        print("Error during validation")

        for dict_key in data.keys():
            if dict_key in errors:
                print(f"{dict_key}: ", errors[dict_key].values())

        return
    
    try:
        if course is None:
            # Add
            course = Course(code = data["code"], name = data["name"])
            session.add(course)
        else:
            # Update
            if name != "":
                course.name = data["name"]
                

        session.commit()
        print("Course added/updated successfully")
    except Exception as e:
        print("Error adding/updating course ", e)


def delete_course():
    session = Session()
    
    code = get_input("Enter course code: ").upper()
    name = None

    course = session.query(Course).filter_by(code = code).first()

    if course is None:
        print("Course with the code '{code}' not found")
        return
    
    print(f"Are you sure you want to delete course with the code '{code}' all students on this course will be unenrolled")
    choice = get_input("Y/N: ").upper()

    if choice == "N" or (choice != "Y" and choice != "N"):
        return
    
    # Unenrol all students
    try:
        t_now = time_now()

        params = {
            "unenrolled_at": t_now,
            "course_id": course.id
        }
        execute_sql(session, "UPDATE enrolments SET unenrolled_at = :unenrolled_at WHERE course_id = :course_id", params)        

        # Update the course to deleted
        course.code = f"deleted-{course.code}-{t_now.timestamp()}"
        course.deleted_at = t_now()
        
        session.commit()
        print("Course deleted successfully")
    except Exception as e:
        print("Error deleting course ", e)

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
        print("3. Add/Update course (use course code as identifier)")
        print("4. Add/Update student (use student email as identifier)")
        print("5. Enrol student to course")
        print("6. Un-enrol student from course")
        print("7. Print student report")
        print("8. Print course report")
        print("9. Delete course")
        print("10. Delete student")
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

        if choice == 9:
            delete_course()
            continue
        
        # Enf of prompts
        if choice is None:
            print("Invalid choice try again")


if __name__ == "__main__":
    main()