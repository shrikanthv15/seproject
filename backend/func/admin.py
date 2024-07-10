from flask import Blueprint, request, jsonify
from func.models import db, Admin, Content

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/content', methods=['POST'])
def upload_content():
    data = request.get_json()
    new_content = Content(
        AdminID=data['AdminID'],
        Title=data['Title'],
        ContentType=data['ContentType'],
        ContentPath=data['ContentPath']
    )
    db.session.add(new_content)
    db.session.commit()
    return jsonify({"message": "Content uploaded successfully"}), 201
