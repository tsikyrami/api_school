from app.models import Student, Course, Enrollment,Instructor,Department, db
from sqlalchemy.sql import func    

def fetch_students_in_department(department_id, grade_threshold):
    try:
        if not department_id or grade_threshold is None:
            raise ValueError("Invalid parameter: department_id and grade_threshold must be provided and valid.")

        most_experienced_instructor_subquery = db.session.query(
            Instructor.id.label('instructor_id'),
            func.count(Student.id).label('student_count')
        ).join(Student, Student.advisor_id == Instructor.id).filter(
            Instructor.department_id == department_id
        ).group_by(Instructor.id).order_by(func.count(Student.id).desc()).limit(1).subquery()

        results = db.session.query(
            Student.id,
            Student.name,
            func.sum(Course.credits).label('total_credits'),
            func.avg(Enrollment.grade).label('average_grade')
        ).select_from(Student).join(
            Enrollment, Student.id == Enrollment.student_id
        ).join(
            Course, Enrollment.course_id == Course.id
        ).filter(
            Course.department_id == department_id,
            Enrollment.grade >= grade_threshold,
            Student.advisor_id == most_experienced_instructor_subquery.c.instructor_id
        ).group_by(
            Student.id
        ).all()

        if not results:
            return [] 
        
        min_credits = min(student.total_credits for student in results)
        max_credits = max(student.total_credits for student in results)

        students = []
        for student in results:
            students.append({
                'id': student.id,
                'name': student.name,
                'total_credits': student.total_credits,
                'average_grade': student.average_grade,
                'min_credits': min_credits,
                'max_credits': max_credits
            })

        return students
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")
