# services/student_service.py
from app import db
from app.models import Student, Enrollment, Course
from app.repositories.student_repository import fetch_students_in_department

def get_students_by_department(department_id,grade_threshold):
    return fetch_students_in_department(department_id,grade_threshold)