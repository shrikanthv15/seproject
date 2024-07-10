from flask import Blueprint, request, jsonify
from func.models import db, User, Profile, SupportRequest

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    profile = Profile.query.filter_by(UserID=user_id).first()
    if profile:
        return jsonify({
            "FullName": profile.FullName,
            "DateOfBirth": profile.DateOfBirth,
            "Address": profile.Address,
            "PhoneNumber": profile.PhoneNumber,
            "SocialProfileLinks": profile.SocialProfileLinks
        }), 200
    return jsonify({"message": "Profile not found"}), 404

@user_bp.route('/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    data = request.get_json()
    profile = Profile.query.filter_by(UserID=user_id).first()
    if profile:
        profile.FullName = data.get('FullName', profile.FullName)
        profile.DateOfBirth = data.get('DateOfBirth', profile.DateOfBirth)
        profile.Address = data.get('Address', profile.Address)
        profile.PhoneNumber = data.get('PhoneNumber', profile.PhoneNumber)
        profile.SocialProfileLinks = data.get('SocialProfileLinks', profile.SocialProfileLinks)
        db.session.commit()
        return jsonify({"message": "Profile updated successfully"}), 200
    return jsonify({"message": "Profile not found"}), 404

@user_bp.route('/support', methods=['POST'])
def create_support_request():
    data = request.get_json()
    new_request = SupportRequest(
        UserID=data['UserID'],
        RequestDetails=data['RequestDetails'],
        RequestStatus='Pending'
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({"message": "Support request created successfully"}), 201
