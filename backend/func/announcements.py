from flask import Blueprint, request, jsonify
from func.models import db, Announcement

announcements_bp = Blueprint('announcements', __name__)

@announcements_bp.route('/announcements', methods=['GET'])
def get_announcements():
    announcements = Announcement.query.all()
    return jsonify([{
        "AnnouncementID": ann.AnnouncementID,
        "CourseID": ann.CourseID,
        "Title": ann.Title,
        "Content": ann.Content,
        "CreatedAt": ann.CreatedAt
    } for ann in announcements]), 200

@announcements_bp.route('/announcements', methods=['POST'])
def create_announcement():
    data = request.get_json()
    new_announcement = Announcement(
        CourseID=data['CourseID'],
        Title=data['Title'],
        Content=data['Content']
    )
    db.session.add(new_announcement)
    db.session.commit()
    return jsonify({"message": "Announcement created successfully"}), 201
