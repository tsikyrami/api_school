from app.models import Student, Course, Enrollment,Instructor,Department, db
from sqlalchemy.sql import func    

def fetch_students_by_department( department_id):
    return db.session.query(Student).join(Enrollment).join(Course).filter(Course.department_id == department_id).all()

def fetch_student_credits():
    results = db.session.query(
        Student.id,
        Student.name,
        db.func.sum(Course.credits).label('total_credits')
    ).select_from(Student).join(Enrollment, Student.id == Enrollment.student_id).join(Course, Enrollment.course_id == Course.id).group_by(Student.id).all()
    return results

def fetch_students_above_grade_threshold(threshold):
    results = db.session.query(
        Student.id,
        Student.name,
        db.func.avg(Enrollment.grade).label('average_grade')
    ).join(Enrollment).join(Course).group_by(Student.id).having(db.func.avg(Enrollment.grade) >= threshold).all()
    return results

def fetch_min_max_credits_by_department(department_id):
    subquery = (
        db.session.query(
            Student.id.label('student_id'),
            func.sum(Course.credits).label('total_credits')
        )
        .select_from(Student)
        .join(Enrollment, Student.id == Enrollment.student_id)
        .join(Course, Enrollment.course_id == Course.id)
        .join(Department, Course.department_id == Department.id)
        .filter(Department.id == department_id)
        .group_by(Student.id)
        .subquery()
    )
    result = (
        db.session.query(
            func.min(subquery.c.total_credits).label('min_credits'),
            func.max(subquery.c.total_credits).label('max_credits')
        ).first()
    )
    if result:
        min_credits, max_credits = result
    else:
        min_credits = max_credits = None
    return min_credits, max_credits

def fetch_most_experienced_instructor(department_id):
    result = db.session.query(
        Instructor.id,
        Instructor.name,
        db.func.count(Student.id).label('student_count')
    ).join(Student).join(Department).filter(
        Student.advisor_id == Instructor.id,
        Department.id == department_id
    ).group_by(Instructor.id).order_by(db.func.count(Student.id).desc()).first()

    if result:
        return result.id, result.name
    else:
        return None, None

def fetch_students_with_advisor_check(department_id):
    most_experienced_id, _ = fetch_most_experienced_instructor(department_id)
    if most_experienced_id:
        students = db.session.query(Student).filter(
            Student.advisor_id == most_experienced_id
        ).all()
    else:
        students = []

    return students