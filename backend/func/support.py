from flask import Blueprint, request, jsonify
from func.models import db, SupportRequest

support_bp = Blueprint('support', __name__)

@support_bp.route('/support', methods=['GET'])
def get_support_requests():
    requests = SupportRequest.query.all()
    return jsonify([{
        "RequestID": req.RequestID,
        "UserID": req.UserID,
        "RequestDetails": req.RequestDetails,
        "RequestStatus": req.RequestStatus,
        "CreatedAt": req.CreatedAt
    } for req in requests]), 200

@support_bp.route('/support/<int:request_id>', methods=['PUT'])
def update_support_request(request_id):
    data = request.get_json()
    support_request = SupportRequest.query.filter_by(RequestID=request_id).first()
    if support_request:
        support_request.RequestStatus = data.get('RequestStatus', support_request.RequestStatus)
        db.session.commit()
        return jsonify({"message": "Support request updated successfully"}), 200
    return jsonify({"message": "Support request not found"}), 404
