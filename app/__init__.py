from flask import Flask
from flask_jwt_extended import JWTManager
from app.extensions import db
from app.models.products import Product
from app.config import Config
from app.controllers.products_controller import product_routes
from app.controllers.auth_controller import auth_routes
from app.middlewares.authentication import jwt_error_handler
from app.middlewares.error_handler import error_handler


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    JWTManager(app)
    jwt_error_handler(app)
    error_handler(app)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    app.register_blueprint(product_routes, url_prefix='/api')
    app.register_blueprint(auth_routes, url_prefix='/api')

    return app
