from mymoneydiary import db
from flask_restful import fields


class Transaction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.String(100), nullable=False)
	transaction_type = db.Column(db.Boolean, nullable=False)
	amount = db.Column(db.Float, nullable=False)
	description = db.Column(db.String(255), nullable=False, default="")
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


	def __repr__(self):
		return f"Transaction(description = {self.description}, \
			amount = {self.amount}, date = {self.date}, \
				type = {'Deposit' if type else 'Withdrawal'})"



transaction_fields = {
	"id": fields.Integer,
	"date": fields.DateTime,
	"transaction_type": fields.Boolean,
	"amount": fields.Float,
	"description": fields.String,
}


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), nullable=False, unique=True)
	password = db.Column(db.String(128), nullable = False)
	transactions = db.relationship('Transaction', backref='user', lazy=True)


	def __repr__(self):
		return f"User(name = {self.username}"
	

user_fields = {
	"id": fields.Integer,
	"username": fields.String,
}	