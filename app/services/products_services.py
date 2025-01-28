from app.extensions import db
from app.models.products import Product
from werkzeug.exceptions import NotFound

def get_all_products_service():
    products = Product.query.all()
    return products

def insert_product_service(data):
    products = []  
    try:
        if isinstance(data, list):  
            for item in data:
                new_product = Product(
                    name=item['name'],
                    description=item['description'],
                    price=item['price']
                )
                db.session.add(new_product)
                products.append(new_product) 

        elif isinstance(data, dict):  
            new_product = Product(
                name=data['name'],
                description=data['description'],
                price=data['price']
            )
            db.session.add(new_product)
            products.append(new_product) 

        db.session.commit()  

        products_list = []
        for product in products:
            products_list.append({
                'id': product.id,  
                'name': product.name,
                'description': product.description,
                'price': str(product.price)
            })

        return products_list

    except Exception as e:
        db.session.rollback()  
        raise Exception(f"Error inserting products: {str(e)}")

def update_product_service(product_id, data):
    product = Product.query.get(product_id)
    
    if not product:
        raise NotFound(f"Product with ID {product_id} not found")
    
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    
    db.session.commit()
    
    return product

def delete_product_service(product_id):
    product = Product.query.get(product_id)
    
    if not product:
        raise NotFound(f"Product with ID {product_id} not found")
    
    db.session.delete(product)
    db.session.commit()