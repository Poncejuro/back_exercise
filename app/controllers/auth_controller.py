from flask import Blueprint, jsonify, request
from app.services.login_services import authenticate_user

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    access_token = authenticate_user(username, password)

    if access_token:
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
