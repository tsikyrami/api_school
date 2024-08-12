# services/student_service.py
from app import db
from app.models import Student, Enrollment, Course
from app.repositories.student_repository import fetch_students_by_department,fetch_student_credits,fetch_students_above_grade_threshold,fetch_min_max_credits_by_department,fetch_students_with_advisor_check

def get_students_by_department(department_id):
    return fetch_students_by_department(department_id)

def get_student_credits():
    return fetch_student_credits()

def get_students_above_grade_threshold(threshold):
    return fetch_students_above_grade_threshold(threshold)

def get_min_max_credits_by_department(department_id):
    return fetch_min_max_credits_by_department(department_id)

def get_students_with_advisor_check(department_id):
    return fetch_students_with_advisor_check(department_id)