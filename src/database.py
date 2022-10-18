from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Cat(db.Model):
    id = db.column(db.Integer, primary_key = True)
    catname = db.column(db.String(40), unique = True, nullable = False)
    email = db.column(db.String(40), unique = True, nullable = False)
    password = db.column(db.String(40), nullable = False)
    created_at= db.column(db.DateTime, default = datetime.now())
    created_at= db.column(db.DateTime, default = datetime.now())

