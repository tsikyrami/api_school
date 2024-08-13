from datetime import datetime
from sqlalchemy import Table,Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.extensions import db

class Department(db.Model):
    _tablename_ = 'department'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    instructors = db.relationship('Instructor', backref='department', lazy=True)
    courses = db.relationship('Course', backref='department', lazy=True)

    def __repr__(self):
        return f'<Department {self.name}>'

class Instructor(db.Model):
    _tablename_ = 'instructor'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    
    advisees = db.relationship('Student', backref='advisor', lazy=True)
    courses = db.relationship('Course', secondary='instructor_course', backref='instructors')

    def __repr__(self):
        return f'<Instructor {self.name}>'

class Course(db.Model):
    _tablename_ = 'course'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    students = db.relationship('Student', secondary='enrollment', backref='courses')

    def __repr__(self):
        return f'<Course {self.name}>'

class Student(db.Model):
    _tablename_ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    advisor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'), nullable=True)
    enrollments = db.relationship('Enrollment', backref='student', lazy=True)

    def __repr__(self):
        return f'<Student {self.name}>'

class Enrollment(db.Model):
    _tablename_ = 'enrollment'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrolled_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    grade = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Enrollment {self.student.name} in {self.course.name}>'

# Many-to-Many relationship table
instructor_course = db.Table('instructor_course',
    db.Column('instructor_id', db.Integer, db.ForeignKey('instructor.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)