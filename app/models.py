from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    # ...
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), unique=True)
    phone_number = db.Column(db.Integer)
    password_hash = db.Column(db.String(128))
    sold_items = db.relationship('SItems', backref='user')
    bought_items = db.relationship("BItems", backref="user")

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return self.id

class SItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    item = db.Column(db.String(70))
    quantity = db.Column(db.Integer)
    location = db.Column(db.String(70))
    date_start = db.Column(db.DateTime())
    date_end = db.Column(db.DateTime())
    sold = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return '<Post {}>'.format(self.SItems)

class BItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    item = db.Column(db.String(70))
    quantity = db.Column(db.Integer)
    location = db.Column(db.String(70))

    def __repr__(self):
        return '<Post {}>'.format(self.BItems)