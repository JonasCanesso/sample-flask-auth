from app import db

class User(db.Model):
    id = db.Column(db.interger, primary_key=True)
    username = db.Column(db.String(80), nullable=False, Unique=True)
    password = db.Column(db.String(80), nullable=False)