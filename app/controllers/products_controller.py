from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.products_services import get_all_products_service, insert_product_service, update_product_service, delete_product_service
from werkzeug.exceptions import BadRequest, NotFound


product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/products', methods=['GET'])
@jwt_required() 
def get_all_products():
    products = get_all_products_service()
    products_list = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price)
        }
        for product in products
    ]
    
    return jsonify({'products': products_list}), 200
    

@product_routes.route('/products', methods=['POST'])
@jwt_required() 
def insert_product():
    data = request.get_json()
    
    if isinstance(data, list):
        if not all('name' in item and 'description' in item and 'price' in item for item in data):
            raise BadRequest('Missing required fields for one or more products')
        products = insert_product_service(data)

    elif isinstance(data, dict):
        if not all(key in data for key in ('name', 'description', 'price')):
            raise BadRequest('Missing required fields')
        products = insert_product_service(data)

    else:
        raise BadRequest('Invalid data format')
    
    return jsonify({
        'message': 'Products created',
        'products': products
    }), 201
        
    
@product_routes.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()  
def update_product(product_id):
    data = request.get_json()
    
    print(product_id)

    if not all(key in data for key in ('name', 'description', 'price')):
        raise BadRequest('Missing required fields')

    product = update_product_service(product_id, data)
    
    return jsonify({
        'message': 'Product updated successfully',
        'product': {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price)
        }
    }), 200
    
    
@product_routes.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required() 
def delete_product(product_id):
    try:
        delete_product_service(product_id)
        
        return jsonify({
            'message': 'Product deleted successfully'
        }), 200

    except NotFound:
        return jsonify({
            'error': 'Product not found',
            'message': f'No product found with ID {product_id}'
        }), 404