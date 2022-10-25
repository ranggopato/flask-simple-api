from datetime import datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(40), unique = True, nullable = False)
    email = db.Column(db.String(40), unique = True, nullable = False)
    password = db.Column(db.String(300), nullable = False)
    created_at= db.Column(db.DateTime, default = datetime.now())
    updated_at= db.Column(db.DateTime, default = datetime.now())
    cats = db.relationship('Cats', backref = "user")
    def __repr__(self) -> str:
        return 'User>>>{self.username}'
class Cats(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     jenis = db.Column(db.Text, nullable = True)
     warna = db.Column(db.Text, nullable = False)
     kebiri = db.Column(db.Text, default = 0)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id') )
     created_at= db.Column(db.DateTime, default = datetime.now())
     updated_at= db.Column(db.DateTime, default = datetime.now())
     

     def __repr__(self) -> str:
        return 'Cats>>>{self.id}'

