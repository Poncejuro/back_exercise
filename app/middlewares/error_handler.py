from flask import jsonify
from werkzeug.exceptions import HTTPException

def error_handler(app):
    @app.errorhandler(Exception)
    def handle_error(e):
        if isinstance(e, HTTPException):
            return jsonify({
                'error': e.name,
                'message': e.description
            }), e.code
        
        return jsonify({
            'error': 'Internal Server Error',
            'message': str(e)
        }), 500
