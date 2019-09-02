from app import migrate, db, app
from datetime import datetime

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(60), unique=False, nullable=False)
    thumb_urls = db.Column(db.String(256), unique=False, nullable=False)
    items = db.relationship('Item', backref = 'category', lazy = 'dynamic')

    def __init__(self, name, desc, thumb):
        self.name = name
        self.description = desc
        self.thumb_urls = thumb

        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Category %r %r %r %r>' % str(self.id), self.name, self.description, self.thumb_url

#Accosiation table for Cart and Item
class Cart_item (db.Model):
    cart_id = db.Column(db.Integer,  db.ForeignKey('cart.id'), primary_key=True)
    item_id = db.Column(db.Integer,  db.ForeignKey('item.id'), primary_key=True)
    quantity = db.Column(db.Integer, unique = False, nullable = False)

    #back_population for cart_item is set to ensure creating a cart makes an entry here 
    #cart = db.relationship('Cart', back_populates = 'cart_item')
    #item = db.relationship('Item', back_populates = 'carts')

    def __init__(self, cart, item, quantity):
        self.cart_id = cart.id
        self.item_id = item.id
        self.quantity = quantity

        db.session.add(self)
        db.session.commit()

    def remove_item(cart_id, item_id):
        cart_item = Cart_item.query.filter_by(cart_id=cart_id, item_id = item_id).first()
        print(cart_item)
        
        db.session.delete(cart_item)
        db.session.commit()
        


class Item (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable = False)
    price = db.Column(db.Float, unique = False, nullable = False)
    description = db.Column(db.String(60), unique = False, nullable = False)
    cat_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    thumb_urls = db.Column(db.String(256), unique= False, nullable = False)
    
    #carts = db.relationship('Cart_item', back_populates = 'items')

class Cart (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.BIGINT, unique = False, nullable = False, index=True)
    is_empty = db.Column(db.BOOLEAN, nullable = False, default = False, index=True)
    discount = db.Column(db.Float, unique = False, nullable = False, default = 0.0)
    delivery_fee = db.Column(db.Float, unique = False, nullable = False, default = 50.0)

    def __init__(self, user_id, item, quantity):
        cart = Cart.query.filter_by(user_id = user_id).first()
        print (user_id)
        if (cart is not None):
            print ("Adding to old Cart")
            cart_item = Cart_item(cart, item, quantity)
            db.session.add(cart_item)
            db.session.commit()
        else:
            print ("Adding to new Cart")
            self.user_id = user_id
            db.session.add(self)
            db.session.commit()
            cart_item = Cart_item(self, item, quantity)
            db.session.add(cart_item)
            db.session.commit()
    #cart_item = db.relationship('Cart_item', back_populates = 'cart')


class Order (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer,  db.ForeignKey('cart.id'))
    Address = db.Column(db.String(1024), nullable = False)
    geo_lat = db.Column(db.Float, unique = False, nullable = False)
    geo_long = db.Column(db.Float, unique = False, nullable = False)
    phone_no = db.Column(db.String(20), unique = False, nullable = False)
    status = db.Column(db.Integer, unique= False, nullable = False)
    placed_on= db.Column(db.DATETIME, unique= False, nullable = False, default=datetime.utcnow)
