from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	phone = db.Column(db.String(10), index=True, unique=True)
	campus = db.Column(db.String(64), index=True, unique=False)
	rating = db.Coumn(db.Integer)
	
class Dress(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	color = Column(db.String(64), index=True)
	size = db.Column(db.String(10), index=True)
	brand= db.Column(db.String(64), index=True)
	deposit = db.Column(db.Double, index=True)
	rental = db.Column(db.Double, index=True)
