from app.extensions import db

class Product(db.Model):
    __tablename__ = 'products' 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)  
    description = db.Column(db.Text, nullable=False)  
    price = db.Column(db.Numeric(10, 2), nullable=False)

