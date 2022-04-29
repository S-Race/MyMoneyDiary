from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class HelloWorld(Resource):
	def get(self):
		return {"data": "Hello World"}

class Balance(Resource):
	def get(self):
		return {
			"balance": 120
		}

class TransactionModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.String(100), nullable=False)
	type = db.Column(db.Boolean, nullable=False)
	amount = db.Column(db.Float, nullable=False)
	description = db.Column(db.String(255), nullable=False)

	def __repr__(self):
		return f"Transaction(description = {self.description}, \
			amount = {self.amount}, date = {self.date}, \
				type = {'Deposit' if type else 'Withdrawal'})"

api.add_resource(HelloWorld,"/api/helloworld")
api.add_resource(Balance,"/api/balance")

if __name__ == "__main__":
	app.run(debug=True)