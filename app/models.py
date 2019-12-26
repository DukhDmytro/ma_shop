from datetime import datetime
from sqlalchemy.orm import relationship
from . import db


class OrderArchive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_order = db.Column(db.Integer, db.ForeignKey('orders.id'))
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    price = db.Column(db.Float)
    date_archive = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.id)


class ProductCategories(db.Model):
    __tablename__ = "product_categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    products = relationship("products")


class Cart(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    addition_date = db.Column(db.Date, default=datetime.today().date())


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(350))
    post = db.Column(db.String(2000))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    news_date = db.Column(db.Date, default=datetime.utcnow())


class Mark (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    mark_date = db.Column(db.Date, default=datetime.today().date())
    rating = db.Column(db.Integer)
    users_who_marked = db.relationship("Users")
    products_marked = db.relationship("Product")


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_date = db.Column(db.Date, default=datetime.today().date())
    body = db.Column(db.String(255))


class Users(db.Model):
    """
    Class to create table "users" in database.
    Variables
    ----------
    id
    first_name
    second_name
    email
    password

    Methods
    -------
    __repr__
    __str__
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(500), nullable=False)
    second_name = db.Column(db.String(500))
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<User id: {self.id}>"

    def __str__(self):
        return f"<User id: {self.id}>"