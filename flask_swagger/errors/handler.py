from flask import Blueprint, request, jsonify

errors = Blueprint('errors', __name__)

@errors.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource not found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response