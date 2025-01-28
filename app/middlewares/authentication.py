from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import JWTDecodeError, NoAuthorizationError

def jwt_error_handler(app):
    @app.before_request
    def validate_jwt_token():
        
        if request.endpoint == 'auth_routes.login':
            return
        
        try:
            verify_jwt_in_request()

        except JWTDecodeError:
            return jsonify({"message": "Invalid token"}), 401

        except NoAuthorizationError:
            return jsonify({"message": "Token is missing or invalid"}), 401

        except Exception as e:
            return jsonify({"message": "An error occurred"}), 500
