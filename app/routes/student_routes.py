from flask import Blueprint, jsonify
from app.services.student_service import get_students_by_department,get_student_credits,get_students_above_grade_threshold,get_min_max_credits_by_department,get_students_with_advisor_check

bp = Blueprint('students', __name__, url_prefix='/students')

@bp.route('/<int:department_id>', methods=['GET'])
def students_by_department(department_id):
    try:
        students = get_students_by_department(department_id)
        student_list = [{'id': student.id, 'name': student.name, 'email': student.email} for student in students]
        return jsonify(student_list)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": f"Internal server error: {e}"}), 500 
    
@bp.route('/credits', methods=['GET'])
def get_student_credits():
    try:
        results = get_student_credits()
        student_list = [
            {'id': student.id, 'name': student.name, 'total_credits': total_credits}
            for student, total_credits in results
        ]
        return jsonify(student_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@bp.route('/grades/<float:threshold>', methods=['GET'])
def get_students_above_grade_threshold(threshold):
    try:
        results = get_students_above_grade_threshold(threshold)
        student_list = [
            {'id': student_id, 'name': student_name, 'average_grade': average_grade}
            for student_id, student_name, average_grade in results
        ]
        return jsonify(student_list)
    except ValueError:
        return jsonify({'error': 'Invalid threshold value'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@bp.route('/credits/min-max/<int:department_id>', methods=['GET'])
def get_min_max_credits_by_department(department_id):
    try:
        min_credits, max_credits = get_min_max_credits_by_department(department_id)
        return jsonify({
            'min_credits': min_credits,
            'max_credits': max_credits
        })
    except ValueError:
        return jsonify({'error': 'Invalid department ID'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@bp.route('/advisor-check/<int:department_id>', methods=['GET'])
def get_students_with_advisor_check(department_id):
    try:
        students = get_students_with_advisor_check(department_id)
        student_list = [
            {'id': student.id, 'name': student.name, 'advisor_id': student.advisor_id}
            for student in students
        ]
        return jsonify(student_list)
    except ValueError:
        return jsonify({'error': 'Invalid department ID'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500