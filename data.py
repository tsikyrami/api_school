from datetime import datetime
from app import create_app
from app.extensions import db
from app.models import Department, Instructor, Course, Student, Enrollment

app = create_app()

with app.app_context():
    # Créer des départements
    dept_cs = Department(name="Computer Science", location="Building A")
    dept_math = Department(name="Mathematics", location="Building B")
    db.session.add(dept_cs)
    db.session.add(dept_math)
    db.session.commit()

    # Créer des instructeurs
    instructor_1 = Instructor(name="Dr. Alice Smith", email="alice.smith@university.edu", department=dept_cs)
    instructor_2 = Instructor(name="Dr. Bob Johnson", email="bob.johnson@university.edu", department=dept_cs)
    instructor_3 = Instructor(name="Dr. Carol White", email="carol.white@university.edu", department=dept_math)
    db.session.add(instructor_1)    
    db.session.add(instructor_2)
    db.session.add(instructor_3)
    db.session.commit()

    # Créer des cours
    course_1 = Course(name="Data Structures", credits=3, department=dept_cs)
    course_2 = Course(name="Algorithms", credits=4, department=dept_cs)
    course_3 = Course(name="Calculus", credits=3, department=dept_math)
    db.session.add(course_1)
    db.session.add(course_2)
    db.session.add(course_3)
    db.session.commit()

    # Associer les instructeurs aux cours
    course_1.instructors.append(instructor_1)
    course_2.instructors.append(instructor_2)
    course_3.instructors.append(instructor_3)
    db.session.commit()

    # Créer des étudiants
    student_1 = Student(name="John Doe", email="john.doe@student.edu", advisor=instructor_1)
    student_2 = Student(name="Jane Smith", email="jane.smith@student.edu", advisor=instructor_1)
    student_3 = Student(name="Tom Brown", email="tom.brown@student.edu", advisor=instructor_2)
    student_4 = Student(name="Emily Davis", email="emily.davis@student.edu", advisor=instructor_3)
    db.session.add(student_1)
    db.session.add(student_2)
    db.session.add(student_3)
    db.session.add(student_4)
    db.session.commit()

    # Associer les étudiants aux instructeurs
    instructor_1.advisees.append(student_1)
    instructor_1.advisees.append(student_2)
    instructor_2.advisees.append(student_3)
    instructor_3.advisees.append(student_4)
    db.session.commit()

    # Créer des inscriptions
    enrollment_1 = Enrollment(student=student_1, course=course_1, grade=85)
    enrollment_2 = Enrollment(student=student_1, course=course_2, grade=90)
    enrollment_3 = Enrollment(student=student_2, course=course_1, grade=70)
    enrollment_4 = Enrollment(student=student_3, course=course_2, grade=95)
    enrollment_5 = Enrollment(student=student_4, course=course_3, grade=88)
    db.session.add(enrollment_1)
    db.session.add(enrollment_2)
    db.session.add(enrollment_3)
    db.session.add(enrollment_4)
    db.session.add(enrollment_5)
    db.session.commit()

    print("Données insérées avec succès!")