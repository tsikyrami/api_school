# data_insertion.py
from app import db, Department, Instructor, Course, Student, Enrollment

def insert_data():
    dept_cs = Department(name="Computer Science", location="Building A")
    dept_math = Department(name="Mathematics", location="Building B")
    db.session.add_all([dept_cs, dept_math])
    db.session.commit()

    instructor_1 = Instructor(name="Dr. Alice Smith", email="alice.smith@university.edu", department=dept_cs)
    instructor_2 = Instructor(name="Dr. Bob Johnson", email="bob.johnson@university.edu", department=dept_cs)
    instructor_3 = Instructor(name="Dr. Carol White", email="carol.white@university.edu", department=dept_math)
    db.session.add_all([instructor_1, instructor_2, instructor_3])
    db.session.commit()

    course_1 = Course(name="Data Structures", credits=3, department=dept_cs)
    course_2 = Course(name="Algorithms", credits=4, department=dept_cs)
    course_3 = Course(name="Calculus", credits=3, department=dept_math)
    db.session.add_all([course_1, course_2, course_3])
    db.session.commit()

    student_1 = Student(name="John Doe", email="john.doe@student.edu", advisor=instructor_1)
    student_2 = Student(name="Jane Smith", email="jane.smith@student.edu", advisor=instructor_1)
    student_3 = Student(name="Tom Brown", email="tom.brown@student.edu", advisor=instructor_2)
    student_4 = Student(name="Emily Davis", email="emily.davis@student.edu", advisor=instructor_3)
    db.session.add_all([student_1, student_2, student_3, student_4])
    db.session.commit()

    enrollment_1 = Enrollment(student=student_1, course=course_1, grade=85)
    enrollment_2 = Enrollment(student=student_1, course=course_2, grade=90)
    enrollment_3 = Enrollment(student=student_2, course=course_1, grade=70)
    enrollment_4 = Enrollment(student=student_3, course=course_2, grade=95)
    enrollment_5 = Enrollment(student=student_4, course=course_3, grade=88)
    db.session.add_all([enrollment_1, enrollment_2, enrollment_3, enrollment_4, enrollment_5])
    db.session.commit()

if __name__ == '__main__':
    insert_data()
