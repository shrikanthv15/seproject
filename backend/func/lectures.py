from flask import Blueprint, request, jsonify
from func.models import db, Lecture

lectures_bp = Blueprint('lectures', __name__)

@lectures_bp.route('/lectures', methods=['GET'])
def get_lectures():
    lectures = Lecture.query.all()
    return jsonify([{
        "LectureID": lec.LectureID,
        "CourseID": lec.CourseID,
        "LectureTitle": lec.LectureTitle,
        "LectureDate": lec.LectureDate,
        "LectureTime": lec.LectureTime,
        "Description": lec.Description,
        "CreatedAt": lec.CreatedAt
    } for lec in lectures]), 200

@lectures_bp.route('/lectures', methods=['POST'])
def create_lecture():
    data = request.get_json()
    new_lecture = Lecture(
        CourseID=data['CourseID'],
        LectureTitle=data['LectureTitle'],
        LectureDate=data['LectureDate'],
        LectureTime=data['LectureTime'],
        Description=data['Description']
    )
    db.session.add(new_lecture)
    db.session.commit()
    return jsonify({"message": "Lecture created successfully"}), 201
