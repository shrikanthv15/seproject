from flask import Blueprint, request, jsonify
from func.models import db, User

auth_bp = Blueprint('auth', __name__)

def configure_auth(app):
    pass

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(Username=data['Username']).first()
    if user and user.Password == data['Password']:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = User(
        Username=data['Username'],
        Password=data['Password'],
        Email=data['Email'],
        Role=data['Role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201
