from flask import Blueprint, request, jsonify
from func.models import db, Document

documents_bp = Blueprint('documents', __name__)

@documents_bp.route('/documents', methods=['GET'])
def get_documents():
    documents = Document.query.all()
    return jsonify([{
        "DocumentID": doc.DocumentID,
        "CourseID": doc.CourseID,
        "DocumentName": doc.DocumentName,
        "DocumentPath": doc.DocumentPath,
        "UploadedAt": doc.UploadedAt
    } for doc in documents]), 200

@documents_bp.route('/documents', methods=['POST'])
def upload_document():
    data = request.get_json()
    new_document = Document(
        CourseID=data['CourseID'],
        DocumentName=data['DocumentName'],
        DocumentPath=data['DocumentPath']
    )
    db.session.add(new_document)
    db.session.commit()
    return jsonify({"message": "Document uploaded successfully"}), 201
