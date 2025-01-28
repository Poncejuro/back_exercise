from dotenv import load_dotenv
from flask_jwt_extended import create_access_token
import os

load_dotenv()

def authenticate_user(username, password):
    
    valid_username = os.getenv('USERNAME')
    valid_password = os.getenv('PASSWORD')
    
    if username == valid_username and password == valid_password:
        access_token = create_access_token(identity=username)
        return access_token
    else:
        return None