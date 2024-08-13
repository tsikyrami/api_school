from flask import Blueprint, jsonify
from app.services.student_service import get_students_by_department

bp = Blueprint('students', __name__, url_prefix='/students')

@bp.route('/<int:department_id>/<float:grade_threshold>', methods=['GET'])
def students_by_department(department_id, grade_threshold):
    try:
        students = get_students_by_department(department_id, grade_threshold)
        return jsonify(students)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({"error": error_message}), 500